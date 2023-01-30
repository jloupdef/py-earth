import os
from functools import wraps
import pytest
from distutils.version import LooseVersion
import sys

def if_environ_has(var_name):
    # Test decorator that skips test if environment variable is not defined
    def if_environ(func):
        @wraps(func)
        def run_test(*args, **kwargs):
            if var_name in os.environ:
                return func(*args, **kwargs)
            else:
                pytest.skip('Only run if %s environment variable is '
                               'defined.' % var_name)
        return run_test
    return if_environ

def if_platform_not_win_32(func):
    @wraps(func)
    def run_test(*args, **kwargs):
        if sys.platform == 'win32':
            pytest.skip('Skip for 32 bit Windows platforms.')
        else:
            return func(*args, **kwargs)
    return run_test
            
def if_sklearn_version_greater_than_or_equal_to(min_version):
    '''
    Test decorator that skips test unless sklearn version is greater than or
    equal to min_version.
    '''
    def _if_sklearn_version(func):
        @wraps(func)
        def run_test(*args, **kwargs):
            import sklearn
            if LooseVersion(sklearn.__version__) < LooseVersion(min_version):
                pytest.skip('sklearn version less than %s' %
                               str(min_version))
            else:
                return func(*args, **kwargs)
        return run_test
    return _if_sklearn_version


def if_statsmodels(func):
    """Test decorator that skips test if statsmodels not installed. """

    @wraps(func)
    def run_test(*args, **kwargs):
        try:
            import statsmodels
        except ImportError:
            pytest.skip('statsmodels not available.')
        else:
            return func(*args, **kwargs)
    return run_test


def if_pandas(func):
    """Test decorator that skips test if pandas not installed. """

    @wraps(func)
    def run_test(*args, **kwargs):
        try:
            import pandas
        except ImportError:
            pytest.skip('pandas not available.')
        else:
            return func(*args, **kwargs)
    return run_test

def if_sympy(func):
    """ Test decorator that skips test if sympy not installed """ 
    
    @wraps(func)
    def run_test(*args, **kwargs):
        try:
            from sympy import Symbol, Add, Mul, Max, RealNumber, Piecewise, sympify, Pow, And, lambdify
        except ImportError:
            pytest.skip('sympy not available.')
        else:
            return func(*args, **kwargs)
    return run_test
    


def if_patsy(func):
    """Test decorator that skips test if patsy not installed. """

    @wraps(func)
    def run_test(*args, **kwargs):
        try:
            import patsy
        except ImportError:
            pytest.skip('patsy not available.')
        else:
            return func(*args, **kwargs)
    return run_test


def assert_list_almost_equal(list1, list2):
    for el1, el2 in zip(list1, list2):
        assert el1 == pytest.approx(el2, abs=1e-7)


def assert_list_almost_equal_value(list, value):
    for el in list:
        assert el == pytest.approx(value, abs=1e-7)
