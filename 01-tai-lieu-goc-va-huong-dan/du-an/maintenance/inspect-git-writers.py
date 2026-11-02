"""Read only current directories for named Windows Git PIDs, without dumping environment."""
import ctypes as c
from ctypes import wintypes as t
import json,sys
K=c.WinDLL('kernel32',use_last_error=True);N=c.WinDLL('ntdll')
K.OpenProcess.argtypes=[t.DWORD,t.BOOL,t.DWORD];K.OpenProcess.restype=t.HANDLE
K.ReadProcessMemory.argtypes=[t.HANDLE,c.c_void_p,c.c_void_p,c.c_size_t,c.POINTER(c.c_size_t)];K.ReadProcessMemory.restype=t.BOOL
K.CloseHandle.argtypes=[t.HANDLE]
N.NtQueryInformationProcess.argtypes=[t.HANDLE,t.ULONG,c.c_void_p,t.ULONG,c.POINTER(t.ULONG)];N.NtQueryInformationProcess.restype=c.c_long
class PBI(c.Structure):_fields_=[('reserved',c.c_void_p),('peb',c.c_void_p),('reserved2',c.c_void_p*2),('pid',c.c_void_p),('reserved3',c.c_void_p)]
out=[]
for pid in map(int,sys.argv[1:]):
 h=K.OpenProcess(0x410,False,pid)
 if not h:out.append({'pid':pid,'error':c.get_last_error()});continue
 try:
  info=PBI();used=t.ULONG();status=N.NtQueryInformationProcess(h,0,c.byref(info),c.sizeof(info),c.byref(used));assert status==0,status
  def read(addr,size):
   buf=c.create_string_buffer(size);got=c.c_size_t();assert K.ReadProcessMemory(h,addr,buf,size,c.byref(got)),c.get_last_error();assert got.value==size;return buf.raw
  params=int.from_bytes(read(info.peb+0x20,8),'little');raw=read(params+0x38,16);length=int.from_bytes(raw[:2],'little');pointer=int.from_bytes(raw[8:16],'little');assert length<65536
  cwd=read(pointer,length).decode('utf-16-le');out.append({'pid':pid,'cwd':cwd})
 finally:K.CloseHandle(h)
print(json.dumps(out,ensure_ascii=False))
