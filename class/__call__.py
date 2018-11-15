class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.rate_sum = 0
        self.rate_count = 0

    def __call__(self, rate):
        self.rate_sum += rate
        self.rate_count += 1

        print('title: {}'.format(self.title))
        print('author: {}'.format(self.author))
        print('rate: {}'.format(rate))
        print('rate average: {}'.format(self.rate_sum / self.rate_count))
        print('rate occur {} times'.format(self.rate_count))


if __name__ == '__main__':

    book = Book('healthy food', 'by Better')

    book(5)
    print()

    book(10)