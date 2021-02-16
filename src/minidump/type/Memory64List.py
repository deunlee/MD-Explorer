from minidump.type.MemoryDescriptor64 import MemoryDescriptor64

class Memory64List:
    # https://docs.microsoft.com/en-us/windows/win32/api/minidumpapiset/ns-minidumpapiset-minidump_memory64_list
    # typedef struct _MINIDUMP_MEMORY64_LIST {
    #     ULONG64                      NumberOfMemoryRanges;
    #     RVA64                        BaseRva;
    #     MINIDUMP_MEMORY_DESCRIPTOR64 MemoryRanges[0];
    # } MINIDUMP_MEMORY64_LIST, *PMINIDUMP_MEMORY64_LIST;

    def __init__(self, reader=None):
        self.count       = None
        self.offset      = None
        self.descriptors = None
        if reader:
            self.read(reader)

    def read(self, reader):
        self.count       = reader.read_u8le()
        self.offset      = reader.read_u8le()
        self.descriptors = []

        for i in range(self.count):
            self.descriptors.append(MemoryDescriptor64(reader))
