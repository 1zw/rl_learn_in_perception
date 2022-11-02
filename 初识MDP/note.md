# 手撕贝尔曼方程
@Wizard
****
## 思路
由于MDP中的价值函数和Q_value都和动作有关，我们希望把他们和MRP中的价值函数关联起来，便于计算
****
## 前述知识
1. 贝叶斯公式  
$$P(A|B)=\frac{P(AB)}{P(B)}$$
2. 条件期望  
    ① 对于离散型变量  
    $$E(Y|X=x) = \sum_{y}y*p(Y=y|X=x) $$  
    ② 对于连续型变量  
    $$E(Y|X=x) = \int_{-\infty}^{+\infty}y*f_Y(y|X=x)dy$$  
    ③ 条件期望性质  
    $$E(E(Y|X=x)) = E(Y) $$  

    *Prof:*    
    $$\begin{aligned}
    E(E(Y|X=x)) &=\int_{-\infty}^{+\infty}E(Y|X=x)*f_1(x) \\
    &= \iint_{-\infty}^{+\infty}yg_2(y|x)f_1(x)dxdy \\
    &= \iint_{-\infty}^{+\infty}y\frac{f(x,y)}{f_1(x)}f_1(x)dxdy \\
    &= \iint_{-\infty}^{+\infty}yf(x,y)dxdy \\
    &= E(Y) \\
    \end{aligned}$$  
    由上面的证明有  
    $$\begin{aligned}
    E(E(G_{t+1}|s_{t+1})|s_t) &=  E(G_{t+1}|s_{t+1}) \\
    E(V(s_{t+1})|s_t) &= V(s_{t+1})
    \end{aligned}$$  

3. 基本的MP,MRP,MDP概念知识  
 ****
## 马尔可夫奖励过程(MRP)
1. **贝尔曼方程**  
   V是价值函数，也叫值函数，MRP中V是状态的函数，用来表征当前状态下能获得奖励的大小  
   公式中  
   $$p(s'|s)$$ 
   <font color="#dd0" size='3'>表示从状态s转移到s'的概率 </font><br /> 
   
   $$\begin{aligned}
    V(s) &= E(G_t|s_t = s) \\
    &= E(r_{t+1}+\gamma*V(s_{t+1})|s_t=s) \\
    &= R(s) + \gamma\sum_{s'\in S}^{}p(s'|s)V(s')
    \end{aligned}$$  
****
## 马尔可夫决策过程(MDP)
1. **策略**  
   策略是在当前状态下所有动作的<font color="#dd0000" size='5'>概率分布 </font><br /> 
   $$\pi(a|s) = p(a_t=a|s_t=s)$$
2. **MDP状态转移函数**  
   $$P(s'|s,a)$$
   它和MRP中状态转移函数之间的关系为
   $$P(s'|s) = \sum_{a\in A}\pi(a|s)p(s'|s,a)$$
3. **奖励函数**
   $$r_{\pi} = \sum_{a\in A}\pi(a|s)R(s,a)$$  
4. **值函数和Q_value**  
   $$V_{\pi}(s) = \sum_{a\in A}\pi(a|s)Q_{\pi}(a,s) $$   
   $$\begin{aligned}
   Q(s,a) &= E(G_t|s_t=s,a_t=a) \\
   &= E(r_{t+1}+\gamma*V(s_{t+1})|s_t=s,a_t=a) \\
   &= R(s,a)+ \gamma*\sum_{s'\in S}p(s'|s,a)V(s')
   \end{aligned}$$
   上面两个公式互相迭代可以得到：     
    ① 当前价值和未来价值的关联  
   $$\begin{aligned}
   V_{\pi}(s) = \sum_{a\in A}\pi(a|s)(R(s,a)+ \gamma*\sum_{s'\in S}p(s'|s,a)V(s'))
   \end{aligned}$$  
    ②  当前q_value和未来q_value的关联  
   $$\begin{aligned}  
   Q(s,a) = R(s,a)+ \gamma*\sum_{s'\in S}p(s'|s,a)(\sum_{a\in A}\pi(a|s')Q_{\pi}(a,s'))
   \end{aligned}$$  



