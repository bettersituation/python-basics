from multiprocessing import Event, Process
import time

def f(event):
    time.sleep(3)
    event.set()


if __name__ == '__main__':

    event = Event()
    print('is set?', event.is_set())

    s = time.time()
    process = Process(target = f, args = (event, ))
    process.start()

    time.sleep(2)
    event.wait()

    time_sleep = round(time.time() - s, 3)

    print('time sleep', time_sleep)

    event.clear()
    print('is set?', event.is_set())
