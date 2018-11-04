from multiprocessing.managers import BaseManager
from multiprocessing import Process
from queue import LifoQueue


class LifoQueueManager(BaseManager):

    def __init__(self):
        super().__init__()
        self.register("LifoQueue", LifoQueue)


def get_data(queue):
    while not queue.empty():
        print(queue.get())


if __name__ == "__main__":

    manager = LifoQueueManager()
    manager.start()
    queue = manager.LifoQueue()

    queue.put("1")
    queue.put("2")
    queue.put("3")

    p = Process(target=get_data, args=(queue, ))
    p.start()
    p.join()