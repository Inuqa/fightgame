from director import Director


class Main:
    director = None

    def __init__(self):
        self.director = Director()
        self.director.start()


if __name__ == '__main__':
    Main()
