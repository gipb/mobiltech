import argparse

class opts(object):
    def __init__(self):
        self.parser = argparse.ArgumentParser()

        self.parser.add_argument('--number', default = 0,
                                help = 'number')

        print("initializing...")

    def parse(self, args=''):
        if args == '':
            opt = self.parser.parse_args()
        else:
            opt = self.parser.parse_args(args)

        print("parsing...")

        return opt

    def init(self, args=''):
        opt = self.parse(args)

        print("completed!")

        return opt
