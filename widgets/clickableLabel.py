from PySide.QtCore import Signal
from PySide.QtGui import QLabel, QApplication

class ClickableLabel(QLabel):
    """
    Tiny wrapper around QLabel that emits 'clicked' when you click on the
    QLabel. (They don't emit mouse events on their own). More strictly -
    responds to the mouse-up event.

    You can provide an arbitrary object to the constructor, which will be
    passed back to you as an argument when the signal is emitted.
    """

    clicked = Signal(object)

    def __init__(self, text, clickUserData):
        super(ClickableLabel, self).__init__(text)
        self._clickUserData = clickUserData

    def mouseReleaseEvent(self, *args, **kwargs):
        super(ClickableLabel, self).mouseReleaseEvent(*args, **kwargs)
        self.clicked.emit(self._clickUserData)

# ----------------------------------------------------------------------------
# __main__ test entry point
# ----------------------------------------------------------------------------

def _print_it(it):
    print it

if __name__ == '__main__':
    app = QApplication(())
    lbl = ClickableLabel('hello', 42)
    lbl.clicked.connect(_print_it)
    lbl.show()
    app.exec_()
