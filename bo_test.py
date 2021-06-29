"""
====== Test the RL agent on each param and find the worst range ======
"""

import os
import argparse
from rl_heuristic_agents import *


def parse_args():
    parser = argparse.ArgumentParser(
        description="BO testing script.")
    parser.add_argument( "--testing_param" ,type=str,
                         required=True ,help='current testing param' )
    parser.add_argument("--testing_range", type=float,
                        required=True, help='current testing range')
    parser.add_argument("--model_path", type=str, required=True,
                        help='saved model path')

    return parser.parse_args()


def main():
    '''
    model training process,
    save the trained model to nn_model_path
    '''

    args = parse_args()

    rl_agent = RLAgent()
    rl_test_reeward = rl_agent.testing_agent(env_range=args.testing_range, nn_model_path=args.model_path)

    rule_agent = RuleBasedAgent()
    rule_test_reward = rule_agent.rule_based_agent_test(env_range=args.testing_range)

    bo_reward = rule_test_reward - rl_test_reeward
    print(bo_reward)


if __name__ == '__main__':
    main()
