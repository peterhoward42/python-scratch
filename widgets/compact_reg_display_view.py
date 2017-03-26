from PySide.QtCore import Signal, Qt
from PySide.QtGui import QLabel, QHBoxLayout, QVBoxLayout, QApplication, \
    QPushButton, QWidget, QGridLayout


class CompactRegdisplay(QWidget):

    """The user wants to edit the register's value."""
    edit_requested = Signal(int, int)

    def __init__(self, reg_bitwidth):
        super(CompactRegdisplay, self).__init__()
        self._bitwidth = reg_bitwidth

        self._addr_label = None
        self._hex_value_label = None
        self._binary_value_label = None
        self._remove_button = None

        self._build_ui()

    def setValue(self, addr, value, remove_btn_visible):
        self._addr_label.setText(str.format('{:04X}:', addr))
        self._hex_value_label.setText(str.format('0x{:04X}', value))
        # Todo ignoring width
        self._binary_value_label.setText(self._make_binary_value_string(value))
        self._remove_button.setVisible(remove_btn_visible)

    # -------------------------------------------------------------------------
    # Private below
    # -------------------------------------------------------------------------

    def _build_ui(self):
        layout = QVBoxLayout()
        self.setLayout(layout)
        self.setStyleSheet(_COMMON_CSS)

        layout.addLayout(self._make_top_row())
        layout.addLayout(self._make_bottom_row())
        layout.addStretch()

    def _make_top_row(self):
        row = QHBoxLayout()
        row.addStretch()
        self._remove_button = self._make_remove_btn()
        row.addWidget(self._remove_button)
        self._addr_label = self._make_addr_label()
        row.addWidget(self._addr_label)
        self._hex_value_label = self._make_hex_value_label()
        row.addWidget(self._hex_value_label)
        return row

    def _make_bottom_row(self):
        row = QHBoxLayout()
        row.addStretch()
        self._binary_value_label = self._make_binary_value_label()
        row.addWidget(self._binary_value_label)
        return row

    def _make_remove_btn(self):
        lbl = QLabel(u'\u00D7')
        lbl.setStyleSheet(_REMOVE_BTN_CSS)
        return lbl

    def _make_binary_value_label(self):
        lbl = QLabel()
        lbl.setStyleSheet(_BINARY_VALUE_CSS)
        return lbl

    def _make_hex_value_label(self):
        lbl = QLabel()
        lbl.setStyleSheet(_HEX_VALUE_CSS)
        return lbl

    def _make_addr_label(self):
        lbl = QLabel()
        lbl.setStyleSheet(_ADDR_CSS)
        return lbl

    def _make_binary_value_string(self, value):
        # todo take into account bit width
        zeros_and_ones = str.format('{:08b}', value)
        symbols = [_SYMBOL_FOR_BIT[bit] for bit in zeros_and_ones]
        symbols.insert(4, _SLIGHT_SPACE)
        return u''.join(symbols)
        return symbols


# ----------------------------------------------------------------------------
# Module level constants
# ----------------------------------------------------------------------------

_SYMBOL_FOR_BIT = {'0': u'\u25CB', '1': u'\u25CF'}  # Hollow and solid circles.
_SLIGHT_SPACE = u'\u2004'

_COMMON_CSS = """ *
    { font-family: Lucida Sans Unicode;
    } """

_BINARY_VALUE_CSS = """ *
    { font-size: 18px;
    } """

_HEX_VALUE_CSS = """ *
    { font-size: 18px;
      color: blue;
      text-decoration: underline;
    } """

_ADDR_CSS = """ *
    { font-size: 18px;
      color: grey
    } """

_REMOVE_BTN_CSS = """ *
    { font-size: 26px;
      font-weight: bold;
      color: red
    } """

# ----------------------------------------------------------------------------
# __main__ test entry point
# ----------------------------------------------------------------------------

if __name__ == '__main__':
    app = QApplication(())

    widget = CompactRegdisplay(reg_bitwidth=8)
    widget.show()

    widget.setValue(0xFF03, 0xEE, True)

    app.exec_()
