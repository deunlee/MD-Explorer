from typing    import Optional
from functools import total_ordering

@total_ordering
class MemoryInfo:

    def __init__(self,
        base_address : int,
        size         : int,
        file_offset  : Optional[int] = None,
        typ          : Optional[str] = None,
        state        : Optional[str] = None,
        protection   : Optional[str] = None,
        use          : Optional[str] = None,
    ):
        self.base_address = base_address
        self.size         = size
        self.file_offset  = file_offset
        self.typ          = typ
        self.state        = state
        self.protection   = protection
        self.use          = use

    def fill(self, other):
        if not isinstance(other, self.__class__):
            raise NotImplemented
        if other.file_offset : self.file_offset = other.file_offset
        if other.typ         : self.typ         = other.typ
        if other.state       : self.state       = other.state
        if other.protection  : self.protection  = other.protection
        if other.use         : self.use         = other.use

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
        return f'<MemoryInfo: base=0x{self.base_address:08x} size=0x{self.size:04x}>'
