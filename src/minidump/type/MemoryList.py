from minidump.type.MemoryDescriptor import MemoryDescriptor

class MemoryList:
    # https://docs.microsoft.com/en-us/windows/win32/api/minidumpapiset/ns-minidumpapiset-minidump_memory_list
    # typedef struct _MINIDUMP_MEMORY_LIST {
    #     ULONG32                    NumberOfMemoryRanges;
    #     MINIDUMP_MEMORY_DESCRIPTOR MemoryRanges[0];
    # } MINIDUMP_MEMORY_LIST, *PMINIDUMP_MEMORY_LIST;

    def __init__(self, reader=None):
        if reader:
            self.read(reader)

    def read(self, reader):
        self.count       = reader.read_u4le()
        self.descriptors = [None] * (self.count)

        for i in range(self.count):
            self.descriptors[i] = MemoryDescriptor(reader)
