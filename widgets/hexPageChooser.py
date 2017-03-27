from PySide.QtGui import QDialog, QApplication, QGridLayout

from clickableLabel import ClickableLabel

class HexPageChooser(QDialog):
    """
    A dialog box that shows a 16x16 grid of hex values, starting at
    zero and stepping in increments of FF. When the user clicks one of the
    cells, the corresponding value is noted internally and can be retreived
    using the getPageChosen() method. The click is also passed to the dialog's
    accept() method, and will therefore close the dialog when it used modally.
    """

    def __init__(self, currentValue):
        super(HexPageChooser, self).__init__()
        self._result = None

        self.setWindowTitle('Choose Page')
        grid = QGridLayout()
        self.setLayout(grid)
        for column in range(16):
            for row in range(16):
                value = row * 0x1000 + column * 0x0100
                label = ClickableLabel('0x%04X' % value, value)
                label.clicked.connect(self._click_handler)
                grid.addWidget(label, row, column)
                if value == currentValue:
                    self._style_as_current(label)

    def getPageChosen(self):
        return self._result

    def _style_as_current(self, label):
        label.setStyleSheet(_CURRENT_CSS)

    def _click_handler(self, userData):
        self._result = userData
        self.accept()

# ----------------------------------------------------------------------------
# CSS
# ----------------------------------------------------------------------------

_CURRENT_CSS = """ QLabel
    {
      background-color: lightgrey;
      border: 1px solid blue;
    } """

# ----------------------------------------------------------------------------
# __main__ test entry point
# ----------------------------------------------------------------------------

if __name__ == '__main__':
    app = QApplication(())
    dlg = HexPageChooser(0x2100)
    dlg.exec_()
    result = dlg.getPageChosen()
    print 'page chosen: %04X' % result
    app.exec_()
