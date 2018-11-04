from multiprocessing import Process, Array
import ctypes


class ArrayStruct(ctypes.Structure):
    _fields_ = [('name', ctypes.c_wchar_p), ('value', ctypes.c_float), ('set', ctypes.c_bool)]


def f(array):
    for e in array:
        print(e.name)
        print(e.value)
        print(e.set)
        print()


def g(array):
    for i in range(len(array)):
        print("{}-th value: {}".format(i, array[i]))


if __name__ == "__main__":

    arr_struct = Array(ArrayStruct, [("sea", 4.5, True), ("star", 1.1, False), ("space", 5, True)])
    f(arr_struct)
    print()

    arr = Array(ctypes.c_int, [4,2,3])
    g(arr)