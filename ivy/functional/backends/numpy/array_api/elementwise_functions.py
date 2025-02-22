# global
import numpy as np
import numpy.array_api as npa


def bitwise_and(x1: np.ndarray,
                x2: np.ndarray)\
        -> np.ndarray:
    return np.bitwise_and(x1, x2)


def equal(x1: np.ndarray, x2: np.ndarray)\
        -> np.ndarray:
    return x1 == x2


def less_equal(x1: np.ndarray, x2: np.ndarray)\
        -> np.ndarray:
    return x1 <= x2


def ceil(x: np.ndarray)\
        -> np.ndarray:
    return np.asarray(npa.ceil(npa.asarray(x)))


def sqrt(x: np.ndarray)\
        -> np.ndarray:
    return np.sqrt(x)


def isfinite(x: np.ndarray) \
        -> np.ndarray:
    return np.asarray(npa.isfinite(npa.asarray(x)))


def asinh(x: np.ndarray)\
        -> np.ndarray:
    return np.arcsinh(x)


def cosh(x: np.ndarray)\
        -> np.ndarray:
    return np.asarray(npa.cosh(npa.asarray(x)))


def log10(x: np.ndarray)\
        -> np.ndarray:
    return np.log10(x)


def log2(x: np.ndarray)\
        -> np.ndarray:
    return np.log2(x)


def log1p(x: np.ndarray)\
        -> np.ndarray:
    return np.log1p(x)


def isnan(x: np.ndarray)\
        -> np.ndarray:
    return np.isnan(x)


def less(x1: np.ndarray,x2: np.ndarray)\
        -> np.ndarray:
    return np.less(x1,x2)


def cos(x: np.ndarray)\
        -> np.ndarray:
    return np.asarray(npa.cos(npa.asarray(x)))


def logical_not(x: np.ndarray)\
        -> np.ndarray:
    return np.logical_not(x)


def logical_or(x1: np.ndarray, x2: np.ndarray)\
        -> np.ndarray:
    return np.logical_or(x1, x2)


def acosh(x: np.ndarray)\
        -> np.ndarray:
    return np.asarray(npa.acosh(npa.asarray(x)))
  

def sin(x: np.ndarray)\
        -> np.ndarray:
    return np.asarray(npa.sin(npa.asarray(x)))

  
def negative(x: np.ndarray) -> np.ndarray:
    return np.negative(x)


def tanh(x: np.ndarray)\
        -> np.ndarray:
    return np.asarray(npa.tanh(npa.asarray(x)))

