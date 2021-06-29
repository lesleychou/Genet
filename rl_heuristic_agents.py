"""
======Provided by user======
class RLAgent: build a RL training and testing agent.
class RuleBasedAgent: build a heuristic-rule agent for specified application.
"""

import os

class RLAgent(object):

    def __init__(self):
        self.summary_dir = ''

    def training_agent(self, env_range):
        '''
        Use the environment defined in Park, build a RL training agent.
        input: the current env_range need to be trained
        return: a NN model
        '''
        nn_model_path = None
        return nn_model_path

    def testing_agent(self, env_range, nn_model_path):
        '''

        input: a NN model
        return: rl_testing reward
        '''
        rl_testing_reward = 0
        return rl_testing_reward


class RuleBasedAgent(object):

    def __init__(self):
        self.summary_dir = ''

    def rule_based_agent_test(self, env_range):
        '''
        Choose a rule-based agent as the baseline.
        return: testing reward
        '''
        rule_based_reward = 0
        return rule_based_reward



