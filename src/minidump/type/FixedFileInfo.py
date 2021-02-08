class FixedFileInfo:
    # https://docs.microsoft.com/en-us/windows/win32/api/verrsrc/ns-verrsrc-vs_fixedfileinfo
    # typedef struct tagVS_FIXEDFILEINFO {
    #     DWORD dwSignature;
    #     DWORD dwStrucVersion;
    #     DWORD dwFileVersionMS;
    #     DWORD dwFileVersionLS;
    #     DWORD dwProductVersionMS;
    #     DWORD dwProductVersionLS;
    #     DWORD dwFileFlagsMask;
    #     DWORD dwFileFlags;
    #     DWORD dwFileOS;
    #     DWORD dwFileType;
    #     DWORD dwFileSubtype;
    #     DWORD dwFileDateMS;
    #     DWORD dwFileDateLS;
    # } VS_FIXEDFILEINFO;

    def __init__(self, reader=None):
        self.signature          = None
        self.struct_version     = None
        self.file_version_ms    = None
        self.file_version_ls    = None
        self.product_version_ms = None
        self.product_version_ls = None
        self.file_flags_mask    = None
        self.file_flags         = None
        self.file_os            = None
        self.file_type          = None
        self.file_subtype       = None
        self.file_date_ms       = None
        self.file_date_ls       = None
        if reader:
            self.read(reader)

    def read(self, reader):
        self.signature          = reader.read_u4le()
        self.struct_version     = reader.read_u4le()
        self.file_version_ms    = reader.read_u4le()
        self.file_version_ls    = reader.read_u4le()
        self.product_version_ms = reader.read_u4le()
        self.product_version_ls = reader.read_u4le()
        self.file_flags_mask    = reader.read_u4le()
        self.file_flags         = reader.read_u4le()
        self.file_os            = reader.read_u4le()
        self.file_type          = reader.read_u4le()
        self.file_subtype       = reader.read_u4le()
        self.file_date_ms       = reader.read_u4le()
        self.file_date_ls       = reader.read_u4le()
