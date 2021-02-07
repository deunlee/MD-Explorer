class LocationDescriptor64:
    # https://docs.microsoft.com/en-us/windows/win32/api/minidumpapiset/ns-minidumpapiset-minidump_location_descriptor64
    # typedef struct _MINIDUMP_LOCATION_DESCRIPTOR64 {
    #     ULONG64 DataSize;
    #     RVA64   Rva;
    # } MINIDUMP_LOCATION_DESCRIPTOR64;

    def __init__(self, reader=None):
        self.size   = None # 64-bit
        self.offset = None # 64-bit (=RVA)
        if reader:
            self.read(reader)

    def read(self, reader):
        self.size   = reader.read_u8le()
        self.offset = reader.read_u8le()
