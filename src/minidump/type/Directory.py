from minidump.type.StreamType         import StreamType
from minidump.type.LocationDescriptor import LocationDescriptor
from minidump.type.Memory64List       import Memory64List
from minidump.type.MemoryInfoList     import MemoryInfoList
from minidump.type.ModuleList         import ModuleList
from minidump.type.ThreadList         import ThreadList

class Directory:
    # https://docs.microsoft.com/en-us/windows/win32/api/minidumpapiset/ns-minidumpapiset-minidump_directory
    # typedef struct _MINIDUMP_DIRECTORY {
    #     ULONG32                      StreamType;
    #     MINIDUMP_LOCATION_DESCRIPTOR Location;
    # } MINIDUMP_DIRECTORY, *PMINIDUMP_DIRECTORY;

    STREAM_TYPE_TO_STREAM = {
        # StreamType.MemoryListStream        : MemoryList,
        StreamType.Memory64ListStream        : Memory64List,
        StreamType.MemoryInfoListStream      : MemoryInfoList,
        StreamType.ModuleListStream          : ModuleList,
        StreamType.ThreadListStream          : ThreadList,
        # StreamType.ThreadInfoListStream      : ThreadInfoList,
        # StreamType.ThreadExListStream        : ThreadExList,
        # StreamType.ExceptionStream           : Exception,
        # StreamType.HandleDataStream          : HandleData,
        # StreamType.HandleOperationListStream : HandleOperationList,
        # StreamType.FunctionTableStream       : FunctionTable,
        # StreamType.UnloadedModuleListStream  : UnloadedModuleList,
        # StreamType.SystemInfoStream          : SystemInfo,
        # StreamType.MiscInfoStream            : MiscInfo,
        # StreamType.TokenStream               : TokenStream,
        # StreamType.JavaScriptDataStream      : JavaScriptDataStream,
        # StreamType.SystemMemoryInfoStream    : SystemMemoryInfoStream,
        # StreamType.ProcessVmCountersStream   : ProcessVmCountersStream,
        # StreamType.IptTraceStream            : IptTraceStream,
        # StreamType.ThreadNamesStream         : ThreadNamesStream,
        # StreamType.CommentStreamA            : CommentStreamA,
        # StreamType.CommentStreamW            : CommentStreamW,
    }

    def __init__(self, reader=None):
        self.stream          = None # stream data
        self.stream_type     = None # stream type
        self.stream_size     = None # stream size
        self.stream_file_ofs = None # file offset of stream
        self.dir_file_ofs    = None # file offset of directory
        if reader:
            self.read(reader)

    def __repr__(self):
        file_ofs    = f'0x{self.dir_file_ofs:04x}'    if self.dir_file_ofs    else 'N/A'
        stream_ofs  = f'0x{self.stream_file_ofs:08x}' if self.stream_file_ofs else 'N/A'
        stream_name = self.stream_type.name.ljust(25) if self.stream_type     else 'N/A'
        return f'<Directory: {stream_name} @ DIR:{file_ofs} -> STREAM:{stream_ofs}>'

    def read(self, reader):
        self.dir_file_ofs    = reader.pos()
        self.stream_type     = StreamType(reader.read_u4le()) # read 4   bytes
        stream_location      = LocationDescriptor(reader)     # read 4+4 bytes
        self.stream_file_ofs = stream_location.offset
        self.stream_size     = stream_location.size

        reader.backup_pos()
        reader.seek(self.stream_file_ofs)
        self.stream = self.STREAM_TYPE_TO_STREAM.get(self.stream_type)
        if self.stream:
            self.stream = self.stream(reader)
        reader.restore_pos()
