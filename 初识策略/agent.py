import torch
import torch.distributions as D
import numpy as np

class agent:
    def __init__(self, K, const_flag):
        self.K = K
        self.const_flag = const_flag
        self.counts = torch.zeros(K)
        # metrics
        self.reward = torch.zeros(1)
        self.ba_count = 0
        self.rewards = []
        self.best_act = []
        self.timesteps = 0

    def get_action(self):
        raise NotImplementedError
    
    def update(self, a, r):
        raise NotImplementedError

    def update_metric(self):
        self.rewards.append(np.array(self.reward))
        self.best_act.append(np.array(self.ba_count/self.timesteps))
class EpsilonGreedy(agent):
    def __init__(self, K, const_flag,epsilon):
        super().__init__(K,const_flag)
        self.epsilon = epsilon
        # 期望奖励的估计值，用Qa表示
        self.Q = torch.zeros(K)
        # 计数，每根杆拉过多少次
        self.counts = torch.zeros(self.K)
    # a = tensor(0-9)
    def get_action(self):
        # rand生成在0-1之间的概率,模拟采样概率
        if torch.rand(1) <= self.epsilon:
            return torch.randint(0,self.K,(1,))[0]
        else:
            return torch.max(self.Q,0)[1]
    def update(self,action,reward):
        self.timesteps += 1
        self.reward += reward
        self.counts[action] += 1
        self.epsilon = self.epsilon/self.timesteps
        self.Q[action] += (reward - self.Q[action])/self.counts[action]
class UCB (agent):
    def __init__(self, K, const_flag,weight):
        super().__init__(K,const_flag)
        # weight作为控制不确定度的权
        self.weight = weight
        self.Q = torch.zeros(K)
        # 开始的不确定度应该很大
        self.u = torch.full((K,),1)
        self.couts = torch.zeros(self.K)
    def get_action(self):        
        return torch.max(self.Q+self.weight*self.u,0)[1]
    def update(self,action,reward):
        self.timesteps = torch.sum(self.couts) + 1
        # 不确定度u
        self.u[action] = torch.sqrt(torch.log(torch.Tensor(self.timesteps))/(2*self.counts[action]+1))
        self.reward += reward
        self.counts[action] += 1
        self.Q[action] += (reward - self.Q[action])/self.couts[action]
class ThompsonSampling(agent):
    def __init__(self,K,const_flag):
        super().__init__(K,const_flag)
        # 认为每根拉杆服从一个Beta分布,并初始化形状参数为1
        # contribution1提高系统可利用率
        # contribution2提高系统可探索率
        self.contribution1 = torch.ones(self.K)
        self.contribution2 = torch.ones(self.K)
    def get_action(self):
        self.d = D.Beta(self.contribution1,self.contribution2)
        a = torch.max(self.d.sample(),0)[1]
        return a
        pass
    def update(self,action,reward):
        self.timesteps += 1
        self.reward += reward
        if reward > 1:
            self.contribution1[action] += torch.abs(reward)
        else:
            self.contribution2[action] += torch.abs(reward)
        