class String:
    # https://docs.microsoft.com/en-us/windows/win32/api/minidumpapiset/ns-minidumpapiset-minidump_string
    # typedef struct _MINIDUMP_STRING {
    #     ULONG32 Length;
    #     WCHAR   Buffer[0];
    # } MINIDUMP_STRING, *PMINIDUMP_STRING;

    def __init__(self, reader=None):
        self.length = 0
        self.text   = ''
        if reader:
            self.read(reader)

    def read(self, reader):
        self.length = reader.read_u4le()
        try:
            self.text = reader.read_bytes(self.length).decode('utf-16le')
        except:
            self.length = 0
            self.text   = ''
            print('decode error')
