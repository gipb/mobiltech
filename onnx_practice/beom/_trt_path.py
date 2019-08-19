import os.path as osp
import sys

def add_path(path):
    if path not in sys.path:
        sys.path.insert(0, path)

this_dir = '/usr/local/TensorRT-5.1.5.0/samples'

# Add lib to PYTHONPATH
lib_path = osp.join(this_dir, 'python')
add_path(lib_path)
