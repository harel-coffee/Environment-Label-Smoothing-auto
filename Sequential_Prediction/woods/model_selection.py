"""Defining the model selection strategies"""

import copy
import numpy as np

from woods import datasets
from woods import utils

def ensure_dict_path(dict, key):
    """Ensure that a path of a nested dictionnary exists. 
    
    If it does, return the nested dictionnary within. If it does not, create a nested dictionnary and return it.

    Args:
        dict (dict): Nested dictionnary to ensure a path
        key (str): Key to ensure has a dictionnary in 

    Returns:
        dict: nested dictionnary
    """
    if key not in dict.keys():
        dict[key] = {}

    return dict[key]

def get_best_hparams(records, selection_method):
    """ Get the best set of hyperparameters for a given a record from a sweep and a selection method

    The way model selection is performed is by computing the validation accuracy of all training checkpoints. 
    The definition of the validation accuracy is given by the selection method. 
    Then using these validation accuracies, we choose the best checkpoint and report the corresponding hyperparameters.

    Args:
        records (dict): Dictionary of records from a sweep
        selection_method (str): Selection method to use

    Returns:
        dict: flags of the chosen model training run for the all trial seeds
        dict: hyperparameters of the chosen model for all trial seeds
        dict: validation accuracy of the chosen model run for all trial seeds
        dict: test accuracy of the chosen model run for all trial seeds
    """

    if selection_method not in globals():
        raise NotImplementedError("Dataset not found: {}".format(selection_method))
    selection_method = globals()[selection_method]

    flags_dict = {}
    hparams_dict = {}
    val_best_acc = {}
    test_best_acc = {}
    for t_seed, t_dict in records.items():
        val_acc_dict = {}
        val_var_dict = {}
        test_acc_dict = {}
        test_var_dict = {}
        for h_seed, h_dict in t_dict.items():
            val_acc, test_acc = selection_method(h_dict)

            val_acc_dict[h_seed] = val_acc
            test_acc_dict[h_seed] = test_acc

        best_seed = [k for k,v in val_acc_dict.items() if v==max(val_acc_dict.values())][0]

        flags_dict[t_seed] = records[t_seed][best_seed]['flags']
        hparams_dict[t_seed] = records[t_seed][best_seed]['hparams']
        val_best_acc[t_seed] = val_acc_dict[best_seed]
        test_best_acc[t_seed] = test_acc_dict[best_seed]
    
    return flags_dict, hparams_dict, val_best_acc, test_best_acc

def get_chosen_test_acc(records, selection_method):
    """ Get the test accuracy that will be chosen through the selection method for a given a record from a sweep 

    The way model selection is performed is by computing the validation accuracy of all training checkpoints. 
    The definition of the validation accuracy is given by the selection method. 
    Then using these validation accuracies, we choose the best checkpoint and report the test accuracy linked to that checkpoint.

    Args:
        records (dict): Dictionary of records from a sweep
        selection_method (str): Selection method to use

    Returns:
        float: validation accuracy of the chosen models averaged over all trial seeds
        float: variance of the validation accuracy of the chosen models accross all trial seeds
        float: test accuracy of the chosen models averaged over all trial seeds
        float: variance of the test accuracy of the chosen models accross all trial seeds
    """

    if selection_method not in globals():
        raise NotImplementedError("Dataset not found: {}".format(selection_method))
    selection_method = globals()[selection_method]

    val_acc_arr = []
    test_acc_arr = []
    for t_seed, t_dict in records.items():
        val_acc_dict = {}
        val_var_dict = {}
        test_acc_dict = {}
        test_var_dict = {}
        for h_seed, h_dict in t_dict.items():
            val_acc, test_acc = selection_method(h_dict)

            val_acc_dict[h_seed] = val_acc
            test_acc_dict[h_seed] = test_acc

        best_seed = [k for k,v in val_acc_dict.items() if v==max(val_acc_dict.values())][0]

        val_acc_arr.append(val_acc_dict[best_seed])
        test_acc_arr.append(test_acc_dict[best_seed])

    return np.mean(val_acc_arr, axis=0), np.std(val_acc_arr, axis=0) / np.sqrt(len(val_acc_arr)), np.mean(test_acc_arr, axis=0), np.std(test_acc_arr, axis=0) / np.sqrt(len(test_acc_arr))

def IID_validation(records):
    """ Perform the IID validation model section on a single training run with NO TEST ENVIRONMENT and returns the results
    
    The model selection is performed by computing the average all domains accuracy of all training checkpoints and choosing the highest one.
        best_step = argmax_{step in checkpoints}( mean(train_envs_acc) )

    Args:
        records (dict): Dictionary of records from a single training run

    Returns:
        float: validation accuracy of the best checkpoint of the training run
        float: validation accuracy of the best checkpoint of the training run

    Note:
        This is for ONLY for sweeps with no test environments.
    """

    # Make copy of record
    records = copy.deepcopy(records)

    flags = records.pop('flags')
    hparams = records.pop('hparams')
    env_name = datasets.get_environments(flags['dataset'])

    val_keys = [str(e)+'_out_acc' for e in env_name]

    val_dict = {}
    val_arr_dict = {}
    for step, step_dict in records.items():

        val_array = [step_dict[k] for k in val_keys]
        val_arr_dict[step] = copy.deepcopy(val_array)
        val_dict[step] = np.mean(val_array)

    ## Picking the max value from a dict
    # Fastest:
    best_step = [k for k,v in val_dict.items() if v==max(val_dict.values())][0]
    # Cleanest:
    # best_step = max(val_dict, key=val_dict.get)
    
    return val_arr_dict[best_step], val_arr_dict[best_step]

def train_domain_validation(records):
    """ Perform the train domain validation model section on a single training run and returns the results
    
    The model selection is performed by computing the average training domains accuracy of all training checkpoints and choosing the highest one.
        best_step = argmax_{step in checkpoints}( mean(train_envs_acc) )

    Args:
        records (dict): Dictionary of records from a single training run

    Returns:
        float: validation accuracy of the best checkpoint of the training run
        float: test accuracy of the best checkpoint (highest validation accuracy) of the training run
    """

    # Make copy of record
    records = copy.deepcopy(records)

    flags = records.pop('flags')
    hparams = records.pop('hparams')
    env_name = datasets.get_environments(flags['dataset'])

    val_keys = [str(e)+'_out_acc' for i,e in enumerate(env_name) if i != flags['test_env']]
    test_key = str(env_name[flags['test_env']]) + '_in_acc'

    val_dict = {}
    test_dict = {}
    for step, step_dict in records.items():

        val_array = [step_dict[k] for k in val_keys]
        val_dict[step] = np.mean(val_array)

        test_dict[step] = step_dict[test_key]

    ## Picking the max value from a dict
    # Fastest:
    best_step = [k for k,v in val_dict.items() if v==max(val_dict.values())][0]
    # Cleanest:
    # best_step = max(val_dict, key=val_dict.get)
    
    return val_dict[best_step], test_dict[best_step]

def test_domain_validation(records):
    """  Perform the test domain validation model section on a single training run and returns the results

    The model selection is performed with the test accuracy of ONLY THE LAST CHECKPOINT OF A TRAINING RUN, so this function simply returns the test accuracy of the last checkpoint.
        best_step = test_acc[-1]

    Args:
        records (dict): Dictionary of records from a single training run

    Returns:
        float: validation accuracy of the training run, which is also the test accuracyof the last checkpoint
        float: test accuracy of the last checkpoint
    """

    # Make a copy 
    records = copy.deepcopy(records)

    flags = records.pop('flags')
    hparams = records.pop('hparams')
    env_name = datasets.get_environments(flags['dataset'])

    val_keys = str(env_name[flags['test_env']])+'_out_acc'
    test_keys = str(env_name[flags['test_env']])+'_in_acc'

    last_step = max([int(step) for step in records.keys()])

    return records[str(last_step)][val_keys], records[str(last_step)][test_keys]