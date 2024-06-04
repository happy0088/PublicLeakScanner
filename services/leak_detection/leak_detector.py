from abc import ABC, abstractmethod

class LeakDetector(ABC):
    @abstractmethod
    def detect_leaks(self):
        pass
