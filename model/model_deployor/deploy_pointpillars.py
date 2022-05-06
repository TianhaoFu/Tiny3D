# Copyright (c) OpenMMLab. All rights reserved.
import os
os.environ["CUDA_VISIBLE_DEVICES"] = "2"
from argparse import ArgumentParser

from mmdet3d.apis import inference_detector, init_model, show_result_meshlab


def main():
    parser = ArgumentParser()
    parser.add_argument('pcd', help='Point cloud file')
    parser.add_argument('config', help='Config file')
    parser.add_argument('checkpoint', help='Checkpoint file')
    parser.add_argument(
        '--device', default='cuda:0', help='Device used for inference')

    args = parser.parse_args()

    # build the model from a config file and a checkpoint file
    model = init_model(args.config, args.checkpoint, device=args.device)


if __name__ == '__main__':
    main()
