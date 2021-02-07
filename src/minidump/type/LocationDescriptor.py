class LocationDescriptor:
    # https://docs.microsoft.com/en-us/windows/win32/api/minidumpapiset/ns-minidumpapiset-minidump_location_descriptor
    # typedef struct _MINIDUMP_LOCATION_DESCRIPTOR {
    #     ULONG32 DataSize;
    #     RVA     Rva;
    # } MINIDUMP_LOCATION_DESCRIPTOR;

    def __init__(self, reader=None):
        self.size   = None # 32-bit
        self.offset = None # 32-bit (=RVA)
        if reader:
            self.read(reader)

    def read(self, reader):
        self.size   = reader.read_u4le()
        self.offset = reader.read_u4le()
