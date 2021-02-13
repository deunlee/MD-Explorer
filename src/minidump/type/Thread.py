from minidump.type.LocationDescriptor import LocationDescriptor
from minidump.type.MemoryDescriptor   import MemoryDescriptor

class Thread:
    # https://docs.microsoft.com/en-us/windows/win32/api/minidumpapiset/ns-minidumpapiset-minidump_thread
    # typedef struct _MINIDUMP_THREAD {
    #     ULONG32                      ThreadId;
    #     ULONG32                      SuspendCount;
    #     ULONG32                      PriorityClass;
    #     ULONG32                      Priority;
    #     ULONG64                      Teb;
    #     MINIDUMP_MEMORY_DESCRIPTOR   Stack;
    #     MINIDUMP_LOCATION_DESCRIPTOR ThreadContext;
    # } MINIDUMP_THREAD, *PMINIDUMP_THREAD;

    def __init__(self, reader=None):
        self.thread_id      = None
        self.suspend_count  = None
        self.priority_class = None
        self.priority       = None
        self.teb            = None
        self.stack          = None
        self.thread_context = None
        if reader:
            self.read(reader)

    def read(self, reader):
        self.thread_id      = reader.read_u4le()
        self.suspend_count  = reader.read_u4le()
        self.priority_class = reader.read_u4le()
        self.priority       = reader.read_u4le()
        self.teb            = reader.read_u8le()
        self.stack          = MemoryDescriptor(reader)
        self.thread_context = LocationDescriptor(reader)
