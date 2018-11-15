class Water:

    @staticmethod
    def get_volume(x, y, z):
        return x * y * z


if __name__ == '__main__':
    volume = Water.get_volume(3, 4, 5)
    print(volume)