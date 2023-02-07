import argparse



class Parser():
    def __init__(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("--level", type=int, default=1, help="level of game")
        self.args = parser.parse_args()

    def arguments(self):
        return self.args