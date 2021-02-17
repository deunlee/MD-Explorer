from enum import Enum

class MemoryInfo:
    # https://docs.microsoft.com/en-us/windows/win32/api/minidumpapiset/ns-minidumpapiset-minidump_memory_info
    # typedef struct _MINIDUMP_MEMORY_INFO {
    #     ULONG64 BaseAddress;
    #     ULONG64 AllocationBase;
    #     ULONG32 AllocationProtect;
    #     ULONG32 __alignment1;
    #     ULONG64 RegionSize;
    #     ULONG32 State;
    #     ULONG32 Protect;
    #     ULONG32 Type;
    #     ULONG32 __alignment2;
    # } MINIDUMP_MEMORY_INFO, *PMINIDUMP_MEMORY_INFO;

    class StateType(Enum):
        Unknown  = 0x0
        Commit   = 0x1000  # MEM_COMMIT
        Reserved = 0x2000  # MEM_RESERVE
        Free     = 0x10000 # MEM_FREE

    class MemoryType(Enum):
        Unknown = 0x0
        Private = 0x20000   # MEM_PRIVATE
        Mapped  = 0x40000   # MEM_MAPPED
        Image   = 0x1000000 # MEM_IMAGE

    def __init__(self, reader=None):
        self.base_address       = None
        self.allocation_base    = None
        self.allocation_protect = None
        self.size               = None
        self.state              = None
        self.protection         = None
        self.type               = None
        if reader:
            self.read(reader)

    def read(self, reader):
        self.base_address       = reader.read_u8le()
        self.allocation_base    = reader.read_u8le()
        self.allocation_protect = reader.read_u4le()
        self.__alignment1       = reader.read_u4le()
        self.size               = reader.read_u8le()
        self.state              = reader.read_u4le()
        self.protection         = reader.read_u4le()
        self.type               = reader.read_u4le()
        self.__alignment2       = reader.read_u4le()

        try:
            self.state = self.StateType(self.state)
        except ValueError:
            self.state = self.StateType(0)

        try:
            self.type = self.MemoryType(self.type)
        except ValueError:
            self.type = self.MemoryType(0)

