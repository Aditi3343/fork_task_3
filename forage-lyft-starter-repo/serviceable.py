from abc import ABC, abstractmethod
class Sericeable(ABC):
    @abstractmethod
    def needs_service(self):
        pass