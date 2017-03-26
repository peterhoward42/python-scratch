from PySide.QtCore import Signal
from PySide.QtGui import QLabel, QHBoxLayout, QVBoxLayout, QApplication, \
    QPushButton, QWidget, QGridLayout

# A Unicode font that supports 'geometric shapes' Unicode block, is installed
# by default on all versions of Windows, and has an equivalent (yet to be tested)
# installed on all versions of MacOS by default.
_LUCIDA_CSS = '* {font-family: Lucida Sans Unicode}'

_SYMBOL_FOR_BIT = {'0': u'\u25CB', '1': u'\u25CF'} # Hollow and solid circles.

class CompactRegdisplay(QVBoxLayout):

    edit_requested = Signal(int, int)

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
        row.addWidget(self._value_as_binary_label)
        row.addStretch()
        return row

    def _make_remove_btn(self):
        remove_btn = QLabel(u'\u25CB\u25CF')
        return remove_btn

    def _make_binary_value_string(self, value):
        # todo take into account bit width
        trad = str.format('{:08b}', value)
        symbols = [_SYMBOL_FOR_BIT[bit] for bit in trad]
        return u''.join(symbols)
        return symbols

if __name__ == '__main__':
    app = QApplication(())

    reg = CompactRegdisplay(reg_bitwidth = 8)
    w = QWidget()
    w.setLayout(reg)
    w.show()

    reg.setValue(0xFF03, 0xEE, True)

    app.exec_()
