from collections.abc import Iterator, Sequence
import time


__all__ = ("randint", "randrange", "choices")


MULTIPLIER = 1103515245
INCREMENTOR = 12345
MODULUS = 2 ** 31


class LCGHandler: 
    """LCG type"""
    def __init__(self, times: int | None = None) -> None: 
        self.seed = int(time.time_ns())
        self.times = times
        self._count = 0

    @staticmethod
    def formula(seed: int) -> int:
        """The LCG Formula"""
        return (MULTIPLIER * seed + INCREMENTOR) % MODULUS
    
    def rand_min_max(self, min_: int, max_: int) -> int: 
        self.seed = LCGHandler.formula(self.seed)
        return min_ + (self.seed % (max_ - min_))
    
    def __iter__(self) -> Iterator[int]: 
        self._count = 0 

        return self 

    def __next__(self) -> int: 
        if self._count == self.times: 
            raise StopIteration
        
        self.seed = LCGHandler.formula(self.seed)
        self._count += 1 
        return self.seed
    
_lcg = LCGHandler()

def randint(a: int, b: int) -> int:
    """random.randint-like function
    Basically calls randrange(a, b + 1)
    """
    return randrange(a, b + 1)

def randrange(a: int, b: int) -> int:
    """Gets a pseudo-random number given the range"""
    return _lcg.rand_min_max(a, b)

def choices[T](iterable: Sequence[T]) -> T:
    """Not Implemented"""
    return NotImplemented
