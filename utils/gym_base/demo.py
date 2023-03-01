# import gym
# env = gym.make("LunarLander-v2", render_mode="human")
# observation, info = env.reset(seed=42)
# for _ in range(1000):
#    # action = policy(observation)  # User-defined policy function
#    # observation, reward, terminated, truncated, info = env.step(action)

#    # if terminated or truncated:
#       observation, info = env.reset()
# env.close()
import time
import flappy_bird_gym
env = flappy_bird_gym.make("FlappyBird-v0")
obs = env.reset()
while True:
    # Next action:
    # (feed the observation to your agent here)
    action = env.action_space.sample()  # env.action_space.sample() for a random action
    action_dim = env.action_space.n
    state_dim = env.observation_space.shape[0]
    # Processing:
    obs, reward, done, info = env.step(action)
    print(obs, reward, done, info)
    # print(action_dim,state_dim)
    # Rendering the game:
    # (remove this two lines during training)
    env.render()
    time.sleep(1 / 30)  # FPS

    # Checking if the player is still alive
    if done:
        break

env.close()