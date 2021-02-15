from minidump.type.Module import Module

class ModuleList:
    # https://docs.microsoft.com/en-us/windows/win32/api/minidumpapiset/ns-minidumpapiset-minidump_module_list
    # typedef struct _MINIDUMP_MODULE_LIST {
    #     ULONG32         NumberOfModules;
    #     MINIDUMP_MODULE Modules[0];
    # } MINIDUMP_MODULE_LIST, *PMINIDUMP_MODULE_LIST;

    def __init__(self, reader=None):
        self.count   = 0
        self.modules = []
        if reader:
            self.read(reader)

    def read(self, reader):
        self.count   = reader.read_u4le()
        self.modules = []
        for i in range(self.count):
            self.modules.append(Module(reader))
