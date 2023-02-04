import sys
from traceback import format_exception
from typing import (
    Type,
)
from types import (
    TracebackType,
)
from PyQt5.QtWidgets import QApplication

from window import MainWindow


def except_hook(exception_type: Type[BaseException], exception: BaseException, traceback: TracebackType) -> None:
    traceback_string = "".join(format_exception(exception_type, exception, traceback))
    print(traceback_string, end='', file=sys.stderr)
    QApplication.quit()


sys.excepthook = except_hook
app = QApplication(sys.argv)
main_window = MainWindow()
main_window.show()
exit_code = app.exec()
sys.exit(exit_code)
