from minidump.type.Thread import Thread

class ThreadList:
    # https://docs.microsoft.com/en-us/windows/win32/api/minidumpapiset/ns-minidumpapiset-minidump_thread_list
    # typedef struct _MINIDUMP_THREAD_LIST {
    #     ULONG32         NumberOfThreads;
    #     MINIDUMP_THREAD Threads[0];
    # } MINIDUMP_THREAD_LIST, *PMINIDUMP_THREAD_LIST;

    def __init__(self, reader=None):
        self.count   = 0
        self.threads = []
        if reader:
            self.read(reader)

    def read(self, reader):
        self.count   = reader.read_u4le()
        self.threads = []
        for i in range(self.count):
            self.threads.append(Thread(reader))
