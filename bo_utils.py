import os
import numpy as np

## example:

min_value = 0.1
max_value = 10000

def map_lin_to_log(x):
    x_log = (np.log(x) - np.log(min_value)) / (np.log(max_value) - np.log(min_value))
    return x_log

def map_log_to_lin(x):
    x_lin = np.exp((np.log(max_value)-np.log(min_value))*x + np.log(min_value))
    return x_lin

# another log scale
def map_log_to_lin(x):
    x_lin = 2**(10*x)
    return x_lin

def latest_actor_from(path):
    """
    Returns latest tensorflow checkpoint file from a directory.
    Assumes files are named:
    nn_model_ep_<EPOCH#>.ckpt.meta
    """
    mtime = lambda f: os.stat( os.path.join( path ,f ) ).st_mtime
    files = list( sorted( os.listdir( path ) ,key=mtime ) )
    actors = [a for a in files if "nn_model_ep_" in a]
    actor_path = str( path + '/' + actors[-1] )
    return os.path.splitext( actor_path )[0]

