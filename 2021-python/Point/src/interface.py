

from abc import ABC, abstractmethod

class IPointXY(ABC):
    """Point interface using X, y variables.
    """
    @property
    @abstractmethod
    def X(self):
        pass

    @X.setter
    @abstractmethod
    def X(self, value):
        pass

    @property
    @abstractmethod
    def y(self):
        pass

    @y.setter
    @abstractmethod
    def y(self, value):
        pass    

class IPointRC(ABC):
    """Point interface using r, c variables.
    """    
    @property
    @abstractmethod
    def r(self):
        pass

    @r.setter
    @abstractmethod
    def r(self, value):
        pass

    @property
    @abstractmethod
    def c(self):
        pass

    @c.setter
    @abstractmethod
    def c(self, value):
        pass        

class IPointNavigation(ABC):
    """Point navigation interface.

    Methods to Implement
    --------------------
    up(self, amount): pass
    down(self, amount): pass
    left(self, amount): pass
    right(self, amount): pass
    move(self, other): pass
    """    
    @abstractmethod
    def up(self, amount: int = 1):
        pass
    
    @abstractmethod
    def down(self, amount: int = 1):
        pass

    @abstractmethod
    def left(self, amount: int = 1):
        pass

    @abstractmethod
    def right(self, amount: int = 1):
        pass

    @abstractmethod
    def move(self, other):
        pass