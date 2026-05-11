from typing import Callable


def dataclass(cls):
    """Vereinfacht Klassen."""

    fields = list(cls.__annotations__.keys())

    def __init__(self, *args):
        for name, value in zip(fields, args):
            setattr(self, name, value)

    cls.__init__ = __init__

    def __repr__(self):
        args = ", ".join(f"{f}={getattr(self, f)!r}" for f in fields)
        return f"{cls.__name__}({args})"

    cls.__repr__ = __repr__

    def __eq__(self, other):
        if not isinstance(other, cls):
            return NotImplemented
        return all(getattr(self, f) == getattr(other, f) for f in fields)

    cls.__eq__ = __eq__

    return cls


@dataclass
class Person:
    """Vereinfachte Personen Klasse."""

    id: int
    name: str
    age: int


# p1 = Person(1, "Hans", 25)
# p2 = Person(2, "Hansi", 26)
# print(p1)
# print(p1 == p2)

# Funktionen: First-Class Citizen


def gruss() -> str:
    """Grüßt mit: "Hallo"."""

    return "Hallo"


x = gruss
print(x())

befehle = [print, len]
befehle[0]("12345678")
print(befehle[1]("12345678"))


def großbuchstaben(function: Callable) -> str:
    """Verändert die Funktion, die gegeben wird in Großbuchstaben."""
    
    result = function()
    return result.upper()


print(großbuchstaben(gruss))


# Dekorator: Funktion


def euro(function):
    def wrapper(*args, **kwargs):
        ergebnis = function(*args, **kwargs)
        return f"{ergebnis} €"

    return wrapper


def kontostand():
    return 5000


# print(kontostand())
