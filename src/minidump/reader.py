class Reader:

    def __init__(self, binary_data=None):
        self._data   = binary_data
        self._pos    = 0
        self._backup = []

    def open_file(self, file_path):
        with open(file_path, 'rb') as f:
            self._data = f.read()
        self._pos = 0

    def pos(self):
        return self._pos
    def seek(self, pos):
        self._pos = pos
    
    def backup_pos(self):
        self._backup.append(self._pos)
    def restore_pos(self):
        self._pos = self._backup.pop()

    def read_bytes(self, size):
        value = self._data[self._pos:self._pos+size]
        self._pos += size
        return value

    def _read_uint(self, size, byteorder):
        return int.from_bytes(self.read_bytes(size), byteorder=byteorder, signed=False)
    def read_u2le(self):
        return self._read_uint(2, 'little')
    def read_u4le(self):
        return self._read_uint(4, 'little')
    def read_u8le(self):
        return self._read_uint(8, 'little')
