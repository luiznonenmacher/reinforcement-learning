from agent import Agent
from monitor import interact
import gym
import numpy as np

alpha_values = [0.5, 0.1, 0.05, 0.01]
num_episode_values = [20000]
gamma_values = [1, 0.8, 0.5]
epsilon_divisor_values = [4, 40, 400]

env = gym.make('Taxi-v2')
agent = Agent()

for alpha in alpha_values:
    for gamma in gamma_values:
        for epsilon_divisor in epsilon_divisor_values:
            for num_episode in num_episode_values:
                avg_rewards, best_avg_reward = interact(env, agent, num_episode, 100, alpha, gamma, epsilon_divisor)
                print('alpha: {}, gamma: {}, epsilon_divisor: {}, num_episode: {}, reward: {}'.format(alpha, gamma, epsilon_divisor, num_episode, best_avg_reward))
