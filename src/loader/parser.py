import argparse


class Parser():
    def __init__(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("--level", type=int, help="level of game", default=1)
        self.args = parser.parse_args()

    def arguments(self):
        return self.args