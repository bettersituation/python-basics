from multiprocessing import Queue
import time

queue = Queue()

queue.put("message 1")
queue.put(["message", 2])

print(queue.get())
print(queue.get())
print('size:', queue.qsize())
print('is empty?', queue.empty())

queue.put(3)
queue.put(4)
queue.put('5')

print(queue.get())
print('size:', queue.qsize())

print(queue.get())
print('is empty?', queue.empty())