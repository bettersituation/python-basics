from multiprocessing import Manager, Process


def plus_set(d):
    d["1"] = 1
    d["2"] = 2
    d["3"] = 3
    d["4"] = 4


def minus_set(d):
    d["1"] = -1
    d["2"] = -2
    d["3"] = -3
    d["4"] = -4


def char_set(d):
    d["1"] = "a"
    d["2"] = "b"
    d["3"] = "c"
    d["4"] = "d"


def list_set(d):
    d["1"] = [1]
    d["2"] = [2]
    d["3"] = [3]
    d["4"] = [4]


def print_dict(d):
    for k, v in d.items():
        print("{}: {}".format(k, v))


if __name__ == "__main__":

    shared_dict_manager = Manager()
    shared_dict = shared_dict_manager.dict()

    p_list = []
    for _ in range(10):
        p_list.append(Process(target = plus_set, args = (shared_dict, )))
        p_list.append(Process(target = minus_set, args = (shared_dict, )))
        p_list.append(Process(target = char_set, args = (shared_dict, )))
        p_list.append(Process(target = list_set, args = (shared_dict, )))

    for p in p_list:
        p.start()

    for p in p_list:
        p.join()

    print_dict(shared_dict)