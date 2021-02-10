from minidump.type.FixedFileInfo      import FixedFileInfo
from minidump.type.LocationDescriptor import LocationDescriptor
from minidump.type.String             import String

class Module:
    # https://docs.microsoft.com/en-us/windows/win32/api/minidumpapiset/ns-minidumpapiset-minidump_module
    # typedef struct _MINIDUMP_MODULE {
    #     ULONG64                      BaseOfImage;
    #     ULONG32                      SizeOfImage;
    #     ULONG32                      CheckSum;
    #     ULONG32                      TimeDateStamp;
    #     RVA                          ModuleNameRva;
    #     VS_FIXEDFILEINFO             VersionInfo;
    #     MINIDUMP_LOCATION_DESCRIPTOR CvRecord;
    #     MINIDUMP_LOCATION_DESCRIPTOR MiscRecord;
    #     ULONG64                      Reserved0;
    #     ULONG64                      Reserved1;
    # } MINIDUMP_MODULE, *PMINIDUMP_MODULE;

    def __init__(self, reader=None):
        self.base_address = None
        self.size         = None
        self.checksum     = None
        self.timestamp    = None
        self.path_offset  = None
        self.path         = None
        self.version_info = None
        self.cv_record    = None
        self.misc_record  = None
        if reader:
            self.read(reader)

    def read(self, reader):
        self.base_address = reader.read_u8le()
        self.size         = reader.read_u4le()
        self.checksum     = reader.read_u4le()
        self.timestamp    = reader.read_u4le()
        self.path_offset  = reader.read_u4le()
        self.version_info = FixedFileInfo(reader)
        self.cv_record    = LocationDescriptor(reader)
        self.misc_record  = LocationDescriptor(reader)
        self.__reserved0  = reader.read_u8le()
        self.__Reserved1  = reader.read_u8le()

        reader.backup_pos()
        reader.seek(self.path_offset)
        module_path = String(reader)
        self.path = module_path.text
        reader.restore_pos()
