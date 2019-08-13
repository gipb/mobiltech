from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import _init_paths

import os

import torch
import torch.utils.data
from opts import opts
from models.model import create_model, load_model, save_model
from models.data_parallel import DataParallel
from logger import Logger
from datasets.dataset_factory import get_dataset
from trains.train_factory import train_factory

opt = opts().parse()

torch.manual_seed(opt.seed)
torch.backends.cudnn.benchmark = not opt.not_cuda_benchmark and not opt.test
Dataset = get_dataset(opt.dataset, opt.task)
opt = opts().update_dataset_info_and_set_heads(opt, Dataset)
print(opt)

model = create_model(opt.arch, opt.heads, opt.head_conv)

from torch.autograd import Variable
import torch.onnx

optimizer = torch.optim.Adam(model.parameters(), opt.lr)
model = load_model(model, opt.load_model).cuda()
dummy_input = Variable(torch.randn(16, 3, 512, 512)).cuda()

torch.onnx.export(model, dummy_input, "centernet.onnx")
