from typing    import Optional
from functools import total_ordering

@total_ordering
class ModuleInfo:

    def __init__(self, base_address: int, size: int, path: str):
        self.base_address = base_address
        self.size         = size
        self.path         = path

    def __lt__(self, other):
        if not isinstance(other, self.__class__):
            raise NotImplemented
        if self.base_address == other.base_address:
            return self.size < other.size
        else:
            return self.base_address < other.base_address

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            raise NotImplemented
        return (self.base_address == other.base_address
            and self.size         == other.size)

    def __repr__(self):
        return f'<ModuleInfo: base=0x{self.base_address:08x} size=0x{self.size:04x}>'
