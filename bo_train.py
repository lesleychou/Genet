"""
====== Train the RL agent with BO guided domain randomization ======
"""
import os
import argparse
from rl_heuristic_agents import *


def parse_args():
    parser = argparse.ArgumentParser(
        description="BO training script.")
    parser.add_argument( "--training_param" ,type=str,
                         required=True ,help='current training param' )
    parser.add_argument("--training_range", type=float,
                        required=True, help='current training range')
    parser.add_argument("--model_path", type=str, required=True,
                        help='saved model path')

    return parser.parse_args()


def main():
    '''
    model training process,
    save the trained model to nn_model_path
    '''

    rl_agent = RLAgent()
    # TODO: update the training_range_input
    rl_agent.training_agent(env_range=1)


if __name__ == '__main__':
    main()