from abc import ABC, abstractmethod

class Device(ABC):
    def __init__(self, hostname) -> None:
        self.hostname = hostname

    @abstractmethod
    def save_config(self): #Define abstract method with a decorator
        pass

class Router(Device):
    def save_config(self): #Parent abstract method must be overridden 
        return super().save_config() 