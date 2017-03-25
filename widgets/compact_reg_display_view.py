from PySide.QtCore import Signal
from PySide.QtGui import QLabel, QHBoxLayout, QVBoxLayout, QApplication, \
    QPushButton, QWidget

class CompactRegdisplay(QVBoxLayout):

    edit_requested = Signal(int, int)

    _SYMBOL_FOR_BIT = {'0': '0', '1': '1'} # font troubles - move on
    def __init__(self, reg_bitwidth):
        super(CompactRegdisplay, self).__init__()
        self._reg_bitwidth = reg_bitwidth

        self._addr_label = None
        self._value_as_hex_label = None
        self._value_as_binary_label = None
        self._remove_button = None

        self._build_ui()

    def setValue(self, addr, value, remove_btn_visible):
        self._addr_label.setText(str.format('{:04x}:', addr))
        self._value_as_hex_label.setText(str.format('0x{:04x}', value))
        # Todo ignoring width
        self._value_as_binary_label.setText(self._make_binary_value_string(value))
        self._remove_button.setVisible(remove_btn_visible)

    #-------------------------------------------------------------------------
    # Private below

    def _build_ui(self):
        self.addLayout(self._make_top_row())
        self.addLayout(self._make_bottom_row())
        self.addStretch()

    def _make_top_row(self):
        row = QHBoxLayout()
        self._remove_button = self._make_remove_btn()
        row.addWidget(self._remove_button)
        self._addr_label = QLabel()
        row.addWidget(self._addr_label)
        self._value_as_hex_label = QLabel()
        row.addWidget(self._value_as_hex_label)
        self.addStretch()
        return row

    def _make_bottom_row(self):
        row = QHBoxLayout()
        self._value_as_binary_label = QLabel()
        self._value_as_binary_label.setStyleSheet(
            'font-family: "monspaced"')
        row.addWidget(self._value_as_binary_label)
        row.addStretch()
        return row

    def _make_remove_btn(self):
        btn = QPushButton('rm')
        return btn

    def _make_binary_value_string(self, value):
        # todo take into account bit width
        trad = str.format('{:08b}', value)
        symbols = [self._SYMBOL_FOR_BIT[bit] for bit in trad]
        return u''.join(symbols)
        return symbols

if __name__ == '__main__':
    app = QApplication(())
    reg = CompactRegdisplay(8)
    w = QWidget()
    w.setLayout(reg)
    w.show()

    reg.setValue(0xFF03, 0xEE, True)

    app.exec_()
