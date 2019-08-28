import os.path as osp
import sys

def add_path(path):
    if path not in sys.path:
        sys.path.insert(0, path)

this_dir = '/root/practice/CenterNet_object2D/src'

# Add lib to PYTHONPATH
lib_path = osp.join(this_dir, 'lib')
add_path(lib_path)
add_path('/mnt/nas/data/coco/PythonAPI')
