class Jackson():
    _exist = None

    def __new__(cls):

        if Jackson._exist:
            print ('Hi, Jackson! I know you')
            print ('you are {}'.format(Jackson._exist))
            return Jackson._exist

        else:
            print ('First time to see you, Jackson!')
            return super(Jackson, cls).__new__(cls)

    def __init__(self):
        Jackson._exist = self


if __name__ == '__main__':

    first = Jackson()
    second = Jackson()
    third = Jackson()