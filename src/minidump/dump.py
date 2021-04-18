import os
from sortedcontainers import SortedList

if __name__ == '__main__':
    import sys
    sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))

from minidump.type   import *
from minidump.reader import Reader
from minidump.memory import MemoryInfo
from minidump.module import ModuleInfo

class MiniDump:

    def __init__(self, path, debug=True):
        self.debug       = debug
        self.header      = None
        self.directories = []
        self.memories    = SortedList()
        self.modules     = SortedList()

        self.reader = Reader()
        self.reader.open_file(path)
        self.read(self.reader)


    def read(self, reader):
        self.header      = Header(reader)
        self.directories = []
        self.memories.clear()
        self.modules.clear()

        reader.backup_pos()
        reader.seek(self.header.stream_offset)
        for i in range(self.header.stream_count):
            self.directories.append(Directory(reader))
            if self.debug:
                print(self.directories[-1])
        reader.restore_pos()

        STREAM_TYPE_TO_PROCESS_FUNCTION = {
            StreamType.Memory64ListStream   : self.__process_mem64_list,
            StreamType.MemoryInfoListStream : self.__process_mem_info_list,
            StreamType.ModuleListStream     : self.__process_module_list,
        }

        for directory in self.directories:
            process_func = STREAM_TYPE_TO_PROCESS_FUNCTION.get(directory.stream_type)
            if process_func:
                process_func(directory.stream)

        self.__fill_memory_use()


    def __process_mem64_list(self, stream): # Memory64ListStream
        file_offset = stream.offset
        for descriptor in stream.descriptors:
            info = MemoryInfo(
                base_address = descriptor.offset,
                size         = descriptor.size,
                file_offset  = file_offset,
            )
            try:
                old_index = self.memories.index(info)
                self.memories[old_index].fill(info)
            except ValueError:
                self.memories.add(info)
            file_offset += descriptor.size

    def __process_mem_info_list(self, stream): # MemoryInfoListStream
        for entry in stream.entries:
            info = MemoryInfo(
                base_address = entry.base_address, 
                size         = entry.size, 
                typ          = entry.type.name,
                state        = entry.state.name,
                protection   = entry.protection,
            )
            try:
                old_index = self.memories.index(info)
                self.memories[old_index].fill(info)
            except ValueError:
                self.memories.add(info)

    def __process_module_list(self, stream): # ModuleListStream
        for module in stream.modules:
            self.modules.add(ModuleInfo(
                base_address = module.base_address,
                size         = module.size,
                path         = module.path,
            ))

    def __fill_memory_use(self):
        if not len(self.modules):
            return

        module_index = 0
        for memory in self.memories:
            module = self.modules[module_index]
            if memory.base_address < module.base_address:
                continue
            while module.base_address + module.size < memory.base_address:
                module_index += 1
                if module_index == len(self.modules):
                    return
                module = self.modules[module_index]
            memory.use = module.path



