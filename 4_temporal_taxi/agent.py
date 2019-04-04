import numpy as np
from collections import defaultdict

class Agent:

    def __init__(self, nA=6):
        """ Initialize agent.

        Params
        ======
        - nA: number of actions available to the agent
        """
        self.nA = nA
        self.Q = defaultdict(lambda: np.zeros(self.nA))

    def select_action(self, state, i_episode, epsilon_divisor):
        """ Given the state, select an action.

        Params
        ======
        - state: the current state of the environment

        Returns
        =======
        - action: an integer, compatible with the task's action space
        """

        self.epsilon = 1.0 / ((i_episode/epsilon_divisor) + 1)
        policy= np.ones(self.nA) * self.epsilon / self.nA
        policy[np.argmax(self.Q[state])] = 1 - self.epsilon + (self.epsilon / self.nA)
        action =  np.random.choice(np.arange(self.nA), p=policy)
                         
        return action
    

    def step(self, state, action, reward, next_state, done, i_episode, alpha, gamma, epsilon_divisor):
        """ Update the agent's knowledge, using the most recently sampled tuple.

        Params
        ======
        - state: the previous state of the environment
        - action: the agent's previous choice of action
        - reward: last reward received
        - next_state: the current state of the environment
        - done: whether the episode is complete (True or False)
        """
        next_action = self.select_action(next_state, i_episode, epsilon_divisor)
        self.Q[state][action] += alpha * (reward + (gamma * self.Q[next_state][next_action]) - self.Q[state][action])
