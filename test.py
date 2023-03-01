import torch
import numpy as np
import torch.nn as nn
import torch.nn.functional as F
import itertools
device = 'cuda' if torch.cuda.is_available() else 'cpu'
class same_net(nn.Module):
    def __init__(self) -> None:
        super().__init__()
        self.same = nn.Linear(15,4)
    def give_net(self,x):
        return self.same(x)
class net1(nn.Module):
    def __init__(self,same_net) -> None:
        super().__init__()
        self.same_net = same_net
        # self.same = nn.Linear(15,4)
        self.diff1 = nn.Linear(4,2)
    def forward(self,x):
        x = F.relu(self.same_net.give_net(x))
        return self.diff1(x)
class net2(nn.Module):
    def __init__(self,same_net) -> None:
        super().__init__()
        self.same_net = same_net
        # self.same = nn.Linear(15,4)
        self.diff2 = nn.Linear(4,2)
    def forward(self,x):
        x = F.relu(self.same_netsame.give_net(x))
        print(self.diff2(x))
        return self.diff2(x)
np.random.seed(0)
x = torch.Tensor(np.random.randn(15)).to(device)
y1 = torch.Tensor(np.random.randn(2))
y2 = torch.Tensor(np.random.randn(2))
samenet = same_net()
net_1 = net1(samenet)
net_2 = net1(samenet)
opt1 = torch.optim.Adam(itertools.chain(samenet.parameters(),net_1.parameters()),lr = 1e-1)
opt2 = torch.optim.Adam(itertools.chain(samenet.parameters(),net_2.parameters()),lr = 1e-1)
# 输出参数
def print_params(net):                        
    for param_tensor in net.state_dict():
        print(param_tensor, "\t", net.state_dict()[param_tensor])

# print(net_2(x),y2)
for i in range(1):
    loss_1 = torch.mean(F.mse_loss(net_1(x),y1))
    
    loss_2 = torch.mean(F.mse_loss(net_2(x),y2))
    opt1.zero_grad()
    opt2.zero_grad()
    
    print("****************传播前*****************")
    print_params(samenet)
    
    loss_1.backward()
    opt1.step()
    
    print("**************net1传播后***************")
    print_params(samenet)
    
    loss_2.backward()
    opt2.step()
    print("**************net2传播后***************")
    print_params(samenet)

