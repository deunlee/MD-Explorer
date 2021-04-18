import os
import sys
from PyQt5        import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtCore import Qt

if __name__ == '__main__':
    import sys
    sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))

from common   import *
from minidump import *




class TableModel(QtCore.QAbstractTableModel):

    def __init__(self, data, column_text, column_alignment=None):
        super(TableModel, self).__init__()
        self._data             = data
        self._column_text      = column_text
        self._column_alignment = column_alignment or [Qt.AlignLeft] * len(column_text)

    def data(self, index, role):
        if role == Qt.DisplayRole:
            return self._data[index.row()][index.column()]
        elif role == Qt.TextAlignmentRole:
            return self._column_alignment[index.column()] | Qt.AlignVCenter

    def rowCount(self, index):
        return len(self._data)

    def columnCount(self, index):
        return len(self._column_text)

    def headerData(self, section, orientation, role):
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return str(self._column_text[section])
            if orientation == Qt.Vertical:
                return str(section)


class MemoryTableModel(QtCore.QAbstractTableModel):

    def __init__(self, minidump):
        super().__init__()
        self._data         = minidump.memories
        self._column_text  = ['Base Address', 'File Offset', 'Size'       , 'Type'        , 'State'       , 'Protection', 'Use'       ]
        self._column_width = [150           , 120          , 80           , 80            , 80            , 85          , 0           ]
        self._column_align = [Qt.AlignLeft  , Qt.AlignLeft , Qt.AlignRight, Qt.AlignCenter, Qt.AlignCenter, Qt.AlignLeft, Qt.AlignLeft]

    def data(self, index, role):
        if role == Qt.DisplayRole:
            col_func = [
                lambda x: f'0x{x.base_address:X}',
                lambda x: f'0x{x.file_offset:08X}' if x.file_offset      else 'N/A',
                lambda x: size_to_str(x.size)      if x.size             else 'N/A',
                lambda x: x.typ                    if x.typ != 'Unknown' else 'N/A',
                lambda x: x.state                  if x.state            else 'N/A',
                lambda x: x.protection             if x.protection       else 'N/A',
                lambda x: x.use                    if x.use              else '',
            ]
            return col_func[index.column()](self._data[index.row()])
        elif role == Qt.TextAlignmentRole:
            return self._column_align[index.column()] | Qt.AlignVCenter

    def rowCount(self, index=0):
        return len(self._data)

    def columnCount(self, index=0):
        return len(self._column_text)

    def columnWidth(self, index):
        return self._column_width[index]

    def headerData(self, section, orientation, role):
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return str(self._column_text[section])
            if orientation == Qt.Vertical:
                return str(section)


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        uic.loadUi('src/gui/main.ui', self)
        self.show()

        dump = MiniDump('KakaoTalk.DMP')

        # Memory
        memory_model = MemoryTableModel(dump)
        self.tv_memory.setModel(memory_model)
        for i in range(memory_model.columnCount()):
            self.tv_memory.setColumnWidth(i, memory_model.columnWidth(i))
        self.tv_memory.horizontalHeader().setStretchLastSection(True)
        self.tv_memory.verticalHeader().setDefaultSectionSize(12)
        self.tv_memory.setSelectionBehavior(QtWidgets.QTableView.SelectRows)
        self.tv_memory.setWordWrap(False)


if __name__ == '__main__':
    
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()

