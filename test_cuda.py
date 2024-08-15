import torch
print(torch.__version__)  # 顯示 PyTorch 版本
print(torch.cuda.is_available())  # 檢查 CUDA 是否可用
print(torch.cuda.current_device())