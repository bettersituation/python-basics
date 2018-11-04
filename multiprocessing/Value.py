from multiprocessing import Process, Value
import ctypes

"""
python typecode
# signed vs unsigned - signed: -+ / unsigned: +
'b' - signed char
'B' - unsigned char
'u' - Py_UNICODE
'h' - signed short
'H' - unsigned short
'i' - signed int
'I' - unsigned int
'l' - signed long
'L' - unsigned long
'f' - float
'd' - double


ctypes type
c_bool
c_char
c_wchar
c_byte
c_ubyte
c_short
c_ushort
c_int
c_uint
c_long
c_ulong
c_longlong
c_ulonglong
c_float
c_double
c_longdouble
c_char_p
c_wchar_p
c_void_p
"""


def f(value, i):
    value.value = "hi " + str(i)
    print(value.value)


def g(value, i):
    value.value = "bye " + str(i)
    print(value.value)


def f_in_lock(value, i):
    value.acquire()
    value.value = "hi " + str(i)
    print(value.value)
    value.release()


def g_in_lock(value, i):
    value.acquire()
    value.value = "bye " + str(i)
    print(value.value)
    value.release()


if __name__ == "__main__":

    i_list = range(1, 6)

    # without using value lock
    val = Value(ctypes.c_wchar_p, "")

    f_list = []
    for i in i_list:
        f_list.append(Process(target = f, args = (val, i)))

    for f_p in f_list:
        f_p.start()

    for f_p in f_list:
        f_p.join()


    # using value lock
    val = Value(ctypes.c_wchar_p, "")

    f_list = []
    for i in i_list:
        f_list.append(Process(target = f_in_lock, args = (val, i)))

    for f_p in f_list:
        f_p.start()

    for f_p in f_list:
        f_p.join()