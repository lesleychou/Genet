"""
====== Main logic ======
"""

import subprocess
import os
from bayes_opt import BayesianOptimization
from bo_utils import *

# Default
TOTAL_EPOCHS = 100000
BAYESIAN_OPTIMIZER_INTERVAL = 5000
NUM_BO_UPDATE = int(TOTAL_EPOCHS / BAYESIAN_OPTIMIZER_INTERVAL)
MODEL_SAVED_PATH = ''


def black_box_function(x):
    '''
    :param x: input is the param that need to be test
    :return:  (heuristic_agent - rl_agent) reward
    '''
    latest_model_path = latest_actor_from(MODEL_SAVED_PATH)
    x_map = map_log_to_lin(x)

    testing_command = " python bo_test.py  \
                --testing_param={current_param} \
                --testing_range={current_range} \
                --model_path='{model_path}' \
                ".format(current_param='', current_range=x_map, model_path=latest_model_path)

    r = float(subprocess.check_output(testing_command, shell=True, text=True).strip())
    return r


# BO guided training flow:
for i in range(1, NUM_BO_UPDATE):
    pbounds = {'x': (0, 1)}
    optimizer = BayesianOptimization(
        f=black_box_function,
        pbounds=pbounds
    )

    optimizer.maximize(
        init_points=13,
        n_iter=2,
        kappa=20,
        xi=0.1
    )
    next = optimizer.max
    param = next.get( 'params' ).get( 'x' )

    bo_best_param = map_log_to_lin(param)
    print( "BO chose this best param........", param, bo_best_param )

    latest_model_path = latest_actor_from(MODEL_SAVED_PATH)

    command = "python bo_train.py \
                    --nn_model='{model_path}' \
                    --training_range={bo_chosen_param}"  \
                    .format( model_path=latest_model_path, bo_chosen_param=bo_best_param)
    os.system(command)

    print("Running training:", i)
    i += 1

print("Hooray!")
