import torch
x = torch.arange(12,dtype=torch.float32)
x = x.reshape(3,4)
y = torch.randn(3,4)

# Adam 优化器