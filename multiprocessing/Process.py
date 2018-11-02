from multiprocessing import Process
import time


def f1(x, y):

    s = 0

    for v in range(x + y):
        s += v

    return s


def f2(x, y, z):

    s = 0

    for v in x:
        s += v

    for v in y:
        s += v

    for v in z:
        s += v

    return s


f1x = 10000000
f1y = 20000000

f2x = range(10000000, 20000000)
f2y = range(10000000, 30000000)
f2z = range(30000000, 40000000)


if __name__ == '__main__':

    s = time.time()
    f1(f1x, f1y)
    f2(f2x, f2y, f2z)

    time_spend = round(time.time() - s, 3)
    print("One thread:", time_spend)

    s = time.time()
    f1_process = Process(target = f1, args = (f1x, f1y))
    f2_process = Process(target = f2, args = (f2x, f2y, f2z))

    f1_process.start()
    f2_process.start()

    f1_process.join()
    f2_process.join()

    time_spend = round(time.time() - s, 3)
    print("Multi thread:", time_spend)