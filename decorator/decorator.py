# Enter your code here. Read input from STDIN. Print output to STDOUT
import time
from functools import wraps


class TimeChecker:
    _instance_dict = {}

    def __new__(cls, *args, **kwargs):
        if args:
            ref = args[0]
        else:
            ref = kwargs['ref']

        if ref in TimeChecker._instance_dict.keys():
            return TimeChecker._instance_dict[ref]
        else:
            return super(TimeChecker, cls).__new__(cls)

    def __init__(self, ref):
        TimeChecker._instance_dict[ref] = self
        self.ref = ref
        self.timecount_dict = {}

    def __call__(self, func):
        func_ref = func.__repr__()
        if func_ref not in self.timecount_dict.keys():
            self.timecount_dict[func_ref] = {'time': 0., 'count': 0}

        @wraps(func)
        def wrapper(*args, **kwargs):
            start = time.time()
            result = func(*args, **kwargs)
            time_spend = time.time() - start
            self.timecount_dict[func_ref]['time'] += time_spend
            self.timecount_dict[func_ref]['count'] += 1
            return result
        return wrapper

if __name__ == '__main__':
    test_checker = TimeChecker('test')

    @test_checker
    def f():
        time.sleep(0.1)
        return

    class Test:

        def __init__(self):
            self.a = 'a'

        @test_checker
        def f(self, a, b):
            time.sleep(0.2)
            return a + b

        @staticmethod
        @test_checker
        def g():
            time.sleep(0.5)
            return 'a'

        @classmethod
        @test_checker
        def h(cls):
            time.sleep(0.3)
            return 'b'

    test = Test()
    f()
    f()
    test.f(2, 3)
    test.f(2, 3)
    test.f(2, 3)
    Test.g()
    test.h()

    print(test_checker.timecount_dict)