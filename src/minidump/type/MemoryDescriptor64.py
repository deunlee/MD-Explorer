class MemoryDescriptor64:
    # https://docs.microsoft.com/en-us/windows/win32/api/minidumpapiset/ns-minidumpapiset-minidump_memory_descriptor64
    # typedef struct _MINIDUMP_MEMORY_DESCRIPTOR64 {
    #     ULONG64 StartOfMemoryRange;
    #     ULONG64 DataSize;
    # } MINIDUMP_MEMORY_DESCRIPTOR64, *PMINIDUMP_MEMORY_DESCRIPTOR64;

    def __init__(self, reader=None):
        self.offset = 0
        self.size   = 0
        if reader:
            self.read(reader)

    def read(self, reader):
        self.offset = reader.read_u8le()
        self.size   = reader.read_u8le()
