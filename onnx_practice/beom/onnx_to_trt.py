from __future__ import print_function

import os, sys, argparse
import tensorrt as trt
import _trt_path
import onnx

import common

TRT_LOGGER = trt.Logger(trt.Logger.WARNING)

class opts(object):
    def __init__(self):
        self.parser = argparse.ArgumentParser()

        self.parser.add_argument('--onnx_file_path', default = '',
                                 help='path of onnx file. ex) /path/to/onnx/file.onnx')
        self.parser.add_argument('--engine_file_path', default = '',
                                 help='path for trt file. ex) /path/to/trt/file.trt')

    def parse(self, args=''):
        if args == '':
            opt = self.parser.parse_args()
        else:
            opt = self.parser.parse_args(args)

        return opt

def get_engine(onnx_file_path, engine_file_path=""):
    def build_engine():
        with trt.Builder(TRT_LOGGER) as builder, builder.create_network() as network, trt.OnnxParser(network, TRT_LOGGER) as parser:
            builder.max_workspace_size = common.GiB(1)
            builder.max_batch_size = 1

            if not os.path.exists(onnx_file_path):
                print('ONNX file {} not found.'.format(onnx_file_path))
                exit(0)
            print('Loading ONNX file from path {}...'.format(onnx_file_path))
            with open(onnx_file_path, 'rb') as model:
                print('Beginning ONNX file parsing')
                parser.parse(model.read())
            print('Completed parsing of ONNX file')
            print('Building an engine from file {}; \
                    this may take a while...'.format(onnx_file_path))
            
            engine = builder.build_cuda_engine(network)
            print('Completed creating Engine')
            with open(engine_file_path, 'wb') as f:
                f.write(engine.serialize())
            return engine

    if os.path.exists(engine_file_path):
        print('Reading engine from file {}'.format(engine_file_path))
        with open(engine_file_path, 'rb') as f, trt.Runtime(TRT_LOGGER) as runtime:
            return runtime.deserialize_cuda_engine(f.read())
    else:
        return build_engine()


def main(opt):
    print(opt)
    engine = get_engine(opt.onnx_file_path, opt.engine_file_path)
    print(engine)

if __name__ == '__main__':
    opt = opts().parse()
    main(opt)
