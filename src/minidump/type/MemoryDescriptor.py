from minidump.type.LocationDescriptor import LocationDescriptor

class MemoryDescriptor:
    # https://docs.microsoft.com/en-us/windows/win32/api/minidumpapiset/ns-minidumpapiset-minidump_memory_descriptor
    # typedef struct _MINIDUMP_MEMORY_DESCRIPTOR {
    #     ULONG64                      StartOfMemoryRange;
    #     MINIDUMP_LOCATION_DESCRIPTOR Memory;
    # } MINIDUMP_MEMORY_DESCRIPTOR, *PMINIDUMP_MEMORY_DESCRIPTOR;

    def __init__(self, reader=None):
        self.offset   = None
        self.location = None
        if reader:
            self.read(reader)

    def read(self, reader):
        self.offset   = reader.read_u8le()
        self.location = LocationDescriptor(reader)
