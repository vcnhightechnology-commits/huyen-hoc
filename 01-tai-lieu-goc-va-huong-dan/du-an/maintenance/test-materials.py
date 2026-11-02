"""Exercise material restore integrity and non-overwrite behavior without network."""
from pathlib import Path
from hashlib import sha256
import json, subprocess, sys, tempfile, unittest, zipfile

SCRIPT = Path(__file__).with_name('materials.py')

class RestoreTests(unittest.TestCase):
    def setUp(self):
        test_root = SCRIPT.parent.parent/'tmp/materials-tests'
        test_root.mkdir(parents=True, exist_ok=True)
        self.temp = tempfile.TemporaryDirectory(dir=test_root)
        self.root = Path(self.temp.name)
        self.cache = self.root/'cache'; self.cache.mkdir()
        self.dest = self.root/'destination'
        self.data = '原文\r\nKeep exact bytes.\x00\n'.encode('utf-8')
        self.sha = sha256(self.data).hexdigest()
        self.bundle = self.cache/'hhc-materials-001.zip'
        with zipfile.ZipFile(self.bundle, 'w') as z: z.writestr('objects/'+self.sha, self.data)
        self.m = {'schema': 'hhc-materials-v1', 'repository': 'example/example', 'releaseTag': 'materials-v53', 'files': [{'file': p, 'bytes': len(self.data), 'sha256': self.sha} for p in ['v53/source.txt', 'tmp/duplicate.txt']], 'objects': {self.sha: {'bytes': len(self.data), 'bundle': self.bundle.name, 'member': 'objects/'+self.sha}}, 'bundles': [{'file': self.bundle.name, 'bytes': self.bundle.stat().st_size, 'sha256': sha256(self.bundle.read_bytes()).hexdigest()}]}
        self.manifest = self.root/'manifest.json'
        self.save()
    def tearDown(self):
        assert self.root.resolve().is_relative_to((SCRIPT.parent.parent/'tmp/materials-tests').resolve())
        self.temp.cleanup()
    def save(self): self.manifest.write_text(json.dumps(self.m), encoding='utf-8')
    def run_restore(self, *args):
        return subprocess.run([sys.executable, str(SCRIPT), '--manifest', str(self.manifest), '--cache', str(self.cache), '--destination', str(self.dest), *args], capture_output=True, text=True)
    def test_shared_object_preserves_both_paths_and_bytes(self):
        r = self.run_restore('--all'); self.assertEqual(r.returncode, 0, r.stderr)
        self.assertEqual((self.dest/'v53/source.txt').read_bytes(), self.data)
        self.assertEqual((self.dest/'tmp/duplicate.txt').read_bytes(), self.data)
        r = self.run_restore('--all'); self.assertEqual(r.returncode, 0, r.stderr)
        self.assertIn('"restored": 0', r.stdout)
    def test_conflict_refuses_before_other_writes(self):
        p = self.dest/'tmp/duplicate.txt'; p.parent.mkdir(parents=True); p.write_bytes(b'newer research')
        r = self.run_restore('--all'); self.assertNotEqual(r.returncode, 0)
        self.assertEqual(p.read_bytes(), b'newer research')
        self.assertFalse((self.dest/'v53/source.txt').exists())
    def test_tampered_bundle_and_object_are_rejected(self):
        self.bundle.write_bytes(b'corrupt')
        self.assertNotEqual(self.run_restore('--all').returncode, 0)
        with zipfile.ZipFile(self.bundle, 'w') as z: z.writestr('objects/'+self.sha, b'wrong bytes')
        self.m['bundles'][0].update(bytes=self.bundle.stat().st_size, sha256=sha256(self.bundle.read_bytes()).hexdigest()); self.save()
        self.assertNotEqual(self.run_restore('--all').returncode, 0)
        self.assertFalse((self.dest/'v53/source.txt').exists())
    def test_selection_and_unsafe_paths(self):
        self.assertEqual(self.run_restore('--prefix', 'v53/').returncode, 0)
        self.assertFalse((self.dest/'tmp/duplicate.txt').exists())
        self.assertNotEqual(self.run_restore('--path', 'missing.txt').returncode, 0)
        for path in ['../escape', '/absolute', 'C:/escape', '.git/config', 'v53/../../escape']:
            self.m['files'][0]['file'] = path; self.save()
            self.assertNotEqual(self.run_restore('--all').returncode, 0)

if __name__ == '__main__': unittest.main()
