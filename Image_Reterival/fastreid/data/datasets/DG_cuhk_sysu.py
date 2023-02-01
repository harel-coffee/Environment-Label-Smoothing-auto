# encoding: utf-8
"""
@author:  xingyu liao
@contact: sherlockliao01@gmail.com
"""

import os
from glob import glob

from fastreid.data.datasets import DATASET_REGISTRY
from fastreid.data.datasets.bases import ImageDataset

__all__ = ['DG_CUHK_SYSU', ]


@DATASET_REGISTRY.register()
class DG_CUHK_SYSU(ImageDataset):
    dataset_dir = "CUHK-SYSU"
    dataset_name = "CUHK-SYSU"

    def __init__(self, root='datasets', **kwargs):
        self.root = root
        self.train_path = os.path.join(self.root, self.dataset_dir, 'cropped_image')

        required_files = [self.train_path]
        self.check_before_run(required_files)

        train = self.process_train(self.train_path)

        super().__init__(train, [], [], **kwargs)

    def process_train(self, train_path):
        data = []
        img_paths = glob(os.path.join(train_path, "*.jpg"))
        for img_path in img_paths:
            split_path = img_path.split('/')[-1].split('_') # p00001_n01_s00001_hard0.png
            pid = self.dataset_name + "_" + split_path[0]
            camid = int(split_path[1][1:-4])
            # camid = self.dataset_name + "_" + split_path[2][1:]
            data.append([img_path, pid, camid])
        return data