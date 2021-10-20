from some_functions import *


def function_failing():
    print("should not start")
    assert False


def test_average_working():
    # Make sure we are close to 1/2
    N = 100
    x = np.linspace(0, 1, N)
    error = compute_average(x)-1/2
    assert abs(error) < 1e-15


def test_average_not_working():
    # Make sure we are close to 1/2
    N = 100
    x = np.linspace(0, 0.999, N)
    error = compute_average(x)-1/2
    assert abs(error) > 1e-4
