from multiprocessing import Process, Lock
import time


def print_slow_at_1(val):

    if val == 1:
        time.sleep(1)

    print(val)


def print_slow_at_1_lock(val, lock):

    lock.acquire()

    if val == 1:
        time.sleep(1)

    print(val)

    lock.release()


if __name__ == '__main__':

    val_range = range(0, 5)


    # No Lock
    print('Without Lock')
    p_list = []
    for val in val_range:
        p_list.append(Process(target = print_slow_at_1, args = (val, )))

    for p in p_list:
        p.start()

    for p in p_list:
        p.join()


    # Lock
    print('\nWith Lock')
    lock = Lock()
    p_list = []
    for val in val_range:
        p_list.append(Process(target = print_slow_at_1_lock, args = (val, lock)))

    for p in p_list:
        p.start()

    for p in p_list:
        p.join()