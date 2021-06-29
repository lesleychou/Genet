"""
====== Train the RL agent with BO guided domain randomization ======
"""

import os
from rl_heuristic_agents import *

def main():
    '''
    model training process,
    save the trained model to nn_model_path
    '''

    rl_agent = RLAgent(summary_dir='')
    # TODO: update the training_range_input
    rl_agent.training_agent(env_range=1)


if __name__ == '__main__':
    main()