from PyQt6 import QtCore, QtGui, QtWidgets
from time import time

import sys
import traceback


class WorkerSignals(QtCore.QObject):

    finished = QtCore.pyqtSignal()
    error = QtCore.pyqtSignal(tuple)
    results = QtCore.pyqtSignal(object)
    progress = QtCore.pyqtSignal(int)


class Worker(QtCore.QRunnable):
    def __init__(self, fn, *args, **kwargs):
        super(Worker, self).__init__()
        self.function = fn
        self.args = args
        self.kwargs = kwargs
        self.signals = WorkerSignals()

    @QtCore.pyqtSlot()
    def run(self):

        try:
            result = self.function(*self.args, **self.kwargs)

        except Exception:
            traceback.print_exc()
            exctype, value = sys.exc_info()[:2]
            self.signals.error.emit((exctype, value, traceback.format_exc()))

        else:
            self.signals.results.emit(result)  # Return the result of the processing

        finally:
            self.signals.finished.emit()  # Done


def start_worker(
    function, thread, result, finished=lambda: "", error=lambda: ""
) -> str:
    time_start: float = time()

    worker: Worker = Worker(function)
    worker.signals.results.connect(result)
    worker.signals.progress.connect(lambda output: print("Output ", output))
    worker.signals.error.connect(error)
    worker.signals.finished.connect(finished)

    #  Start function(process) in thread
    thread.start(worker)

    time_finishe: float = time()

    return f"Worker finished., {(time_finishe - time_start):.3f}s"
