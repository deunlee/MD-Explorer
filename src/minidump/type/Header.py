class Header:
    # https://docs.microsoft.com/en-us/windows/win32/api/minidumpapiset/ns-minidumpapiset-minidump_header
    # typedef struct _MINIDUMP_HEADER {
    #     ULONG32 Signature;
    #     ULONG32 Version;
    #     ULONG32 NumberOfStreams;
    #     RVA     StreamDirectoryRva;
    #     ULONG32 CheckSum;
    #     union {
    #         ULONG32 Reserved;
    #         ULONG32 TimeDateStamp;
    #     };
    #     ULONG64 Flags;
    # } MINIDUMP_HEADER, *PMINIDUMP_HEADER;

    def __init__(self, reader=None):
        self.signature     = None
        self.version       = None
        self.stream_count  = None
        self.stream_offset = None
        self.checksum      = None
        self.timestamp     = None
        self.flags         = None
        if reader:
            self.read(reader)

    def read(self, reader):
        self.signature     = reader.read_bytes(4)
        self.version       = reader.read_u4le()
        self.stream_count  = reader.read_u4le()
        self.stream_offset = reader.read_u4le()
        self.checksum      = reader.read_u4le()
        self.timestamp     = reader.read_u4le()
        self.flags         = reader.read_u8le()

        if self.signature != b'MDMP':
            raise Exception('Wrong Signature')
