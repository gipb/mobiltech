from test_argparse import opts

def demo(opt):
    print(opt.number)

if __name__ == '__main__':
    opt = opts().init()
    demo(opt)

