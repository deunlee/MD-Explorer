from minidump.type.MemoryInfo import MemoryInfo

class MemoryInfoList:
    # https://docs.microsoft.com/en-us/windows/win32/api/minidumpapiset/ns-minidumpapiset-minidump_memory_info_list
    # typedef struct _MINIDUMP_MEMORY_INFO_LIST {
    #     ULONG   SizeOfHeader;
    #     ULONG   SizeOfEntry;
    #     ULONG64 NumberOfEntries;
    # } MINIDUMP_MEMORY_INFO_LIST, *PMINIDUMP_MEMORY_INFO_LIST;

    def __init__(self, reader=None):
        self.header_size = 0
        self.entry_size  = 0
        self.count       = 0
        self.entries     = []
        if reader:
            self.read(reader)

    def read(self, reader):
        self.header_size = reader.read_u4le()
        self.entry_size  = reader.read_u4le()
        self.count       = reader.read_u8le()
        if self.header_size != 16: # sizeof(MemoryInfoList)
            print(f'MemoryInfoList: Unknown header size {self.header_size}')
        if self.entry_size  != 48: # sizeof(MemoryInfo)
            print(f'MemoryInfoList: Unknown entry size {self.entry_size}')

        self.entries = []
        for i in range(self.count):
            self.entries.append(MemoryInfo(reader))
