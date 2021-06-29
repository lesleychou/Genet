# Genet API

## Install
```
bayesian-optimization 
numpy
```

## BO interface (Application independent)
1. `bo_train.py`: train the RL agent based on the range BO picked.
2. `bo_test.py`: test the RL agent on param x, find the current 
worst behaved range of x. 
3. `bo_update.py`: BO guided domain randomization logic.


## Simulator (specified by user)

1. `rl_heuristic_agents.py`: For each application, implement a RL 
training and testing agent, a rule-based agent.
2. `env_params.py`: specify env params with their [min, max] range.

