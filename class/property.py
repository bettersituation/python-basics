class Name:
    def __init__(self):
        self._name = None

    @property
    def name(self):
        print('name is {}'.format(self._name))
        return self._name

    @name.setter
    def name(self, name):
        print('set name as {}'.format(self._name))
        self._name = name


if __name__ == '__main__':
    Person = Name()
    Person.name = 'Bob'
    Person.name