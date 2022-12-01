

__all__ = [
    "PointBaseRC"
    ]


from src.interface import IPointRC

class PointBaseRC(IPointRC):
    """Base point class.  Implements comparison and hash methods.
    
    Attributes
    ----------
    c : int
        Column varable
    r : int
        Row variable

    """

    def __init__(self, c: int, r: int) -> None:
        self.__c = c
        self.__r = r
    
    @property
    def r(self):
        return self.__r
    
    @r.setter
    def r(self, value):
        if not isinstance(value, int):
            raise ValueError("Integer type expected.")
        self.__r = value

    @property
    def c(self):
        return self.__c
    
    @c.setter
    def c(self, value):
        if not isinstance(value, int):
            raise ValueError("Integer type expected.")
        self.__c = value        

    def __hash__(self):
        """Hashing method."""
        return hash(str(self))
    
    def __eq__(self, other):
        """Equal."""
        return self.c == other.c and self.r == other.r
    
    def __ne__(self, other):
        """Not equal."""
        return self.c != other.c or self.r != other.r
    
    def __lt__(self, other):
        """Less than."""
        return (self.c < other.c and self.r <= other.r
            or self.c <= other.c and self.r < other.r)

    def __le__(self, other):
        """Less than or equal."""
        return self.c <= other.c and self.r <= other.r
    
    def __gt__(self, other):
        """Greater than."""
        return (self.c > other.c and self.r >= other.r
            or self.c <= other.c and self.r > other.r)

    def __ge__(self, other):
        """Greater than or equal."""
        return self.c >= other.c and self.r >= other.r

    def __repr__(self):
        return f"<{self.__class__.__name__} ({self.c}, {self.r})>"