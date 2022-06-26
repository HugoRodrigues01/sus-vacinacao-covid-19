from controller import QtCore, QtGui, QtWidgets

import sys, traceback


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

        except Exception as error:
            traceback.print_exc()
            exctype, value = sys.exc_info()[:2]
            self.signals.error.emit((exctype, value, traceback.format_exc()))

        else:
            self.signals.results.emit(result)  # Return the result of the processing

        finally:
            self.signals.finished.emit()  # Done
