# Alexander Curtin CS7641 assignment 1

Basically the whole implementation is taken from https://github.com/cmaron/CS-7641-assignments.

I made tweaks to get it to work with  https://archive.ics.uci.edu/ml/datasets/Online+Shoppers’+Purchasing+Intention+Dataset#

# Setup

first get the shopping dataset. or don't as it's already in the repository

``` wget https://archive.ics.uci.edu/ml/machine-learning-databases/00468/online_shoppers_intention.csv -O data/online_shoppers_original/online_shoppers_intention.csv ```


## Then install the requirements.txt file in a python3 virtual environment

``` pip install -r requirements.txt ```

## Then install jython

Here's the command if you're on an ubuntu instance

``` sudo apt-get install jython ```

## Prepare the data

``` python run_experiment.py --dump_data```

# Run the toy problem sets

Just pick one, or do all as separate lines.
``` jython (continuouspeaks|flipflop|tsp).py ```

# Run the NN problems

``` ls NN-*.py | xargs -I {} jython {} ```

# Generate the plots

``` python plotting.py ```

