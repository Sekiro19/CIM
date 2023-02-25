import time

from PySide6.QtCore import QObject, Signal, QRunnable, Slot


class WorkerSignals(QObject):
    finished = Signal()
    started = Signal()
    results = Signal(object)  # this signal will return any python objects
    error = Signal(str)

class Worker(QRunnable):
    """
    :param func: pass a function object to run it in separate thread
    :param sleepTime: sleepTime after the function was called
    :param args: pass function args if any
    :param kwargs: pass function kwargs if any
    """

    def __init__(self, func, sleepTime: int = 0, *args, **kwargs):
        super().__init__()
        self.func = func
        self.args = args
        self.kwargs = kwargs
        self.sleepTime = sleepTime
        self.signals = WorkerSignals()

    @Slot()
    def run(self):
        try:
            self.signals.started.emit()  # fire a signal when the worker started working
            result = self.func(*self.args, **self.kwargs)  # unpack the params to the function and run it
        except Exception as err:
            self.signals.error.emit(err)
        else:
            self.signals.results.emit(result)  # fire a signal with the returned objects from the function
        finally:
            if self.sleepTime:
                time.sleep(self.sleepTime)
            try:
                self.signals.finished.emit()  # fire a signal when the worker stopped working
            except RuntimeError:
                return
