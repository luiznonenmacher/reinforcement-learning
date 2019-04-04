# reinforcement-learning

### introduction

This folder contains the projects I implemented in the reinforcement learning section of Udacity's Machine Learning Engineer Nanodegree. The projects are numbered and each project increases in complexity in terms of the environment and the algorithms applied. Most of the projects are implemented in Jupyter Notebooks, but two of them (temporal_taxi and actor_critic_quadcopter) are implemented using additional .py files to declare parts of the code (like the agent and the tasks).

Except for the last project, all the environments used comes from [openai gym](https://gym.openai.com/).

### Projects

Below there is a quick overview of each project. The first four projects deal with discrete environments, whereas the others deal with continuous spaces.

[1_dynamic_frozenlake](https://github.com/luiznonenmacher/reinforcement-learning/tree/master/1_dynamic_frozenlake): Implementation of dynamic programming to solve the [FrozenLake](https://github.com/openai/gym/blob/master/gym/envs/toy_text/frozen_lake.py) environment.

[2_monte_carlo_blackjack](https://github.com/luiznonenmacher/reinforcement-learning/tree/master/2_monte_carlo_blackjack): Monte Carlo control algorithms to solve the [Blackjack](https://github.com/openai/gym/blob/master/gym/envs/toy_text/blackjack.py) environment.

[3_temporal_cliff_walking](https://github.com/luiznonenmacher/reinforcement-learning/tree/master/3_temporal_cliff_walking): Implementation of many temporal-difference techniques (Sarsa, Q-Learning and Expected Sarsa) to the [CliffWalking](https://github.com/openai/gym/blob/master/gym/envs/toy_text/cliffwalking.py) environment.

[4_temporal_taxi](https://github.com/luiznonenmacher/reinforcement-learning/tree/master/4_temporal_taxi): Use of temporal-difference methods to solve the [Taxi-v2](https://github.com/openai/gym/blob/master/gym/envs/toy_text/taxi.py) environment. Instead of using a Jupyter Notebook, in this implementation I used three .py files, one to declare the agent, another to monitor it's performance and the last one (main.py) to run the environment using the agent.

[5_discretization_and_tile_coding](https://github.com/luiznonenmacher/reinforcement-learning/tree/master/5_discretization_and_tile_coding): Discretization and tile coding are two techniques that can be used to transform continuous-space into discrete ones. Here is a implementation of both methods.

[6_deep_Qlearning_cart](https://github.com/luiznonenmacher/reinforcement-learning/tree/master/6_deep_Qlearning_cart): Implementation of deep Q-learning using Tensorflow to solve the [cartpole](https://github.com/openai/gym/blob/master/gym/envs/classic_control/cartpole.py) task.

[7_actor_critic_quadcopter](https://github.com/luiznonenmacher/reinforcement-learning/tree/master/7_actor_critic_quadcopter): This was the final project of this module and the most challenging one. In that project, I used actor-critic methods (implemented using Keras and Tensorflow) to teach a quadcopter the task of taking off. 

