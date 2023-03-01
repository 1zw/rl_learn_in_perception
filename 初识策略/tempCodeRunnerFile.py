    # 伯努利定常环境演示
    agent_names = ("EpsilonGreedy", "UCB", "ThompsonSampling")
    agents = (eval(agent_names[0])(opt.k_arm,opt.const_flag,0.01),\
            eval(agent_names[1])(opt.k_arm,opt.const_flag,0.1),\
            eval(agent_names[2])(opt.k_arm,opt.const_flag))
