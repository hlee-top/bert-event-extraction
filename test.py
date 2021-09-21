# import torch
# import os
# os.environ["CUDA_VISIBLE_DEVICES"] = "4"
# print(torch.cuda.is_available())
# ng = torch.cuda.device_count()
# print("Devices:%d" %ng)
# infos = [torch.cuda.get_device_properties(i) for i in range(ng)]
# print("infos",infos)
# print(torch.cuda.current_device())
# nohup python -u train.py >log.txt 2>&1 &
