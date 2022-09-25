from abc import ABC, abstractmethod


class InterfaceFrame(ABC):
    @abstractmethod
    def load_widgets(self):
        return

    @abstractmethod
    def frame(self):
        return
