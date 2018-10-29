from multiprocessing import Pool
import os
import time

iter_list = zip(range(10000000), range(10000000, 20000000), range(20000000, 30000000))

def f(x, y, z):
    return x + y + z +x*y*z

def time_checker(func):
    def real_time_cheker(process_num, iter_list):
        start = time.time()
        func(process_num, iter_list)
        secs = time.time() - start
        print("Process num", process_num, "spend:", round(secs, 4))
        return
    return real_time_cheker

@time_checker
def pool_calc(process_num, iter_list):
    with Pool(processes = process_num) as pool:
        pool.starmap_async(f, iter_list).get()
        pool.close()
        pool.join()

print("cpu num:", os.cpu_count())
for n in range(1, 9):
    pool_calc(n, iter_list)