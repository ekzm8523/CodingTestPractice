from typing import *

class my_object:
    name: str
    age: int

T = TypeVar('T')
TT = TypeVar('TT', str, int)
TTT = TypeVar('TTT', bound=my_object)


def func(x: Sequence[TTT]) -> T:
    print(type(x))
    return x


KT = TypeVar('KT')
VT = TypeVar('VT')

class Mapping(Generic[KT, VT]):
    def __getitem__(self, key: KT) -> VT:
        print(type(key))
        return VT(key)

X = TypeVar('X')
Y = TypeVar('Y')

def lookup_name(mapping: Mapping[X, Y], key: X, default: Y) -> Y:
    try:
        print(type(mapping))
        return mapping[key]
    except KeyError:
        return default

class A:
    def __init__(self):
        print("A")


class B(A):
    def __init__(self):
        print("B")

if __name__ == '__main__':
    # print(func([1, 2, 3, 4]))
    # print(func([1.1, 2.2, 3.3, 4.4]))
    # print(func("12345"))

    # print(lookup_name({'k1': 1, 'k2': 2}, 'k1', 2))
    # print(type(Mapping))
    # print(isinstance(Mapping, KT))
    # print(type(KT))
    # print(type(TTT))

    print(type(B()))
    print(type(A()))
    print(A.__class__)
    print(B.__class__)
