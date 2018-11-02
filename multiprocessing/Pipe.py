from multiprocessing import Pipe

head, tail = Pipe()

head.send('message 1')
head.send(['list', 'message', '2'])
print(tail.recv())

tail.send('send to head')
print(head.recv())

print(tail.recv())