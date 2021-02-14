from enum import Enum

class StreamType(Enum):
    # https://docs.microsoft.com/en-us/windows/win32/api/minidumpapiset/ne-minidumpapiset-minidump_stream_type

    UnusedStream                =  0 # Reserved. Do not use this enumeration value.
    ReservedStream0             =  1 # Reserved. Do not use this enumeration value.
    ReservedStream1             =  2 # Reserved. Do not use this enumeration value.
    ThreadListStream            =  3 # MINIDUMP_THREAD_LIST
    ModuleListStream            =  4 # MINIDUMP_MODULE_LIST
    MemoryListStream            =  5 # MINIDUMP_MEMORY_LIST
    ExceptionStream             =  6 # MINIDUMP_EXCEPTION_STREAM
    SystemInfoStream            =  7 # MINIDUMP_SYSTEM_INFO
    ThreadExListStream          =  8 # MINIDUMP_THREAD_EX_LIST
    Memory64ListStream          =  9 # MINIDUMP_MEMORY64_LIST
    CommentStreamA              = 10 # The stream contains an ANSI string used for documentation purposes.
    CommentStreamW              = 11 # The stream contains a Unicode string used for documentation purposes.
    HandleDataStream            = 12 # MINIDUMP_HANDLE_DATA_STREAM
    FunctionTableStream         = 13 # MINIDUMP_FUNCTION_TABLE_STREAM
    UnloadedModuleListStream    = 14 # MINIDUMP_UNLOADED_MODULE_LIST
    MiscInfoStream              = 15 # MINIDUMP_MISC_INFO or MINIDUMP_MISC_INFO_2
    MemoryInfoListStream        = 16 # MINIDUMP_MEMORY_INFO_LIST
    ThreadInfoListStream        = 17 # MINIDUMP_THREAD_INFO_LIST
    HandleOperationListStream   = 18 # MINIDUMP_HANDLE_OPERATION_LIST
    TokenStream                 = 19 # 
    JavaScriptDataStream        = 20 # 
    SystemMemoryInfoStream      = 21 # 
    ProcessVmCountersStream     = 22 # 
    IptTraceStream              = 23 # 
    ThreadNamesStream           = 24 # 
    ceStreamNull                = 25 # 
    ceStreamSystemInfo          = 26 # 
    ceStreamException           = 27 # 
    ceStreamModuleList          = 28 # 
    ceStreamProcessList         = 29 # 
    ceStreamThreadList          = 30 # 
    ceStreamThreadContextList   = 31 # 
    ceStreamThreadCallStackList = 32 # 
    ceStreamMemoryVirtualList   = 33 # 
    ceStreamMemoryPhysicalList  = 34 # 
    ceStreamBucketParameters    = 35 # 
    ceStreamProcessModuleMap    = 36 # 
    ceStreamDiagnosisList       = 37 # 
    LastReservedStream          = 38 # MINIDUMP_USER_STREAM
