from PySide.QtCore import Signal
from PySide.QtGui import QLabel, QApplication

class HexPageNavigator(QWidget):
    """
    A small horizontal widget that lets you select a 'hex-page'. I.e. a hex
    number that is a multiple of 255. It shows you the current page on a
    QPushButton, with big increment / decrement buttons on either side.
    The button also carries a downward arrow to make it look like a pull down
    menu. When you click the button, a big 16 x 16 matrix appears below
    containing all the possibilities. (Think date picker). Clicking on a cell
    in that table selects that value and dismisses the matrix.

    Emits valueChanged(v)
    """

    valueChanged = Signal(object)

    def __init__(self, text, initialValue):
        super(HexPageNavigator, self).__init__()
        self._currentValue = initialValue

        layout = QHBoxLayout()
        self.setLayout(layout)

        layout.addWidget(self._make_page_label())
        layout.addWidget(self._make_dec_arrow())
        layout.addWidget(self._make_push_button())
        layout.addWidget(self._make_inc_arrow())
        layout.addStretch()

    def _make_page_label(self):
        label = QLabel('Page')
        label.setStyleSheet(_PAGE_LABEL_CSS)
        return label

    def _make_dec_arrow(self):
        label = QLabel(u'\u2222')
        label.setStyleSheet(_ARROW_CSS)
        return label


# ----------------------------------------------------------------------------
# __main__ test entry point
# ----------------------------------------------------------------------------

def _print_it(it):
    print it

if __name__ == '__main__':
    app = QApplication(())
    lbl = HexPageNavigator(0xF100)
    lbl.show()
    app.exec_()
