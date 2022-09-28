"""Defining hyper parameters and their distributions for HPO"""

import numpy as np

from woods.objectives import OBJECTIVES

def get_training_hparams(dataset_name, seed, sample=False):
    """ Get training related hyper parameters (class_balance, weight_decay, lr, batch_size)

    Args:
        dataset_name (str): dataset that is gonna be trained on for the run
        seed (int): seed used if hyper parameter is sampled
        sample (bool, optional): If ''True'', hyper parameters are gonna be sampled randomly according to their given distributions. Defaults to ''False'' where the default value is chosen.

    Raises:
        NotImplementedError: Dataset name not found

    Returns:
        dict: Dictionnary with hyper parameters values
    """

    dataset_train = dataset_name + '_train'
    if dataset_train not in globals():
        raise NotImplementedError("dataset not found: {}".format(dataset_name))
    else:
        hyper_function = globals()[dataset_train]

    hparams = hyper_function(sample)
    
    for k in hparams.keys():
        hparams[k] = hparams[k](np.random.RandomState(seed))

    return hparams


def Basic_Fourier_train(sample):
    """ Basic Fourier model hparam definition 
    
    Args:
        sample (bool): If ''True'', hyper parameters are gonna be sampled randomly according to their given distributions. Defaults to ''False'' where the default value is chosen.
    """
    if sample:
        return {
            'class_balance': lambda r: True,
            'weight_decay': lambda r: 0.,
            'lr': lambda r: 10**r.uniform(-4.5, -2.5),
            'batch_size': lambda r: int(2**r.uniform(3, 9))
        }
    else:
        return {
            'class_balance': lambda r: True,
            'weight_decay': lambda r: 0,
            'lr': lambda r: 1e-3,
            'batch_size': lambda r: 64
        }
    
def Spurious_Fourier_train(sample):
    """ Spurious Fourier model hparam definition 
    
    Args:
        sample (bool): If ''True'', hyper parameters are gonna be sampled randomly according to their given distributions. Defaults to ''False'' where the default value is chosen.
    """
    if sample:
        return {
            'class_balance': lambda r: True,
            'weight_decay': lambda r: 0.,
            'lr': lambda r: 10**r.uniform(-4.5, -2.5),
            'batch_size': lambda r: int(2**r.uniform(3, 9))
        }
    else:
        return {
            'class_balance': lambda r: True,
            'weight_decay': lambda r: 0,
            'lr': lambda r: 1e-3,
            'batch_size': lambda r: 64,

        }

def TMNIST_train(sample):
    """ TMNIST model hparam definition 
    
    Args:
        sample (bool): If ''True'', hyper parameters are gonna be sampled randomly according to their given distributions. Defaults to ''False'' where the default value is chosen.
    """
    if sample:
        return {
            'class_balance': lambda r: True,
            'weight_decay': lambda r: 0.,
            'lr': lambda r: 10**r.uniform(-4.5, -2.5),
            'batch_size': lambda r: int(2**r.uniform(3, 9))
        }
    else:
        return {
            'class_balance': lambda r: True,
            'weight_decay': lambda r: 0,
            'lr': lambda r: 1e-3,
            'batch_size': lambda r: 64
        }

def TCMNIST_seq_train(sample):
    """ TCMNIST_seq model hparam definition 
    
    Args:
        sample (bool): If ''True'', hyper parameters are gonna be sampled randomly according to their given distributions. Defaults to ''False'' where the default value is chosen.
    """
    if sample:
        return {
            'class_balance': lambda r: True,
            'weight_decay': lambda r: 0.,
            'lr': lambda r: 10**r.uniform(-4.5, -2.5),
            'batch_size': lambda r: int(2**r.uniform(3, 9))
        }
    else:
        return {
            'class_balance': lambda r: True,
            'weight_decay': lambda r: 0,
            'lr': lambda r: 1e-3,
            'batch_size': lambda r: 64
        }

def TCMNIST_step_train(sample):
    """ TCMNIST_step model hparam definition 
    
    Args:
        sample (bool): If ''True'', hyper parameters are gonna be sampled randomly according to their given distributions. Defaults to ''False'' where the default value is chosen.
    """
    if sample:
        return {
            'class_balance': lambda r: True,
            'weight_decay': lambda r: 0.,
            'lr': lambda r: 10**r.uniform(-4.5, -2.5),
            'batch_size': lambda r: int(2**r.uniform(3, 9))
        }
    else:
        return {
            'class_balance': lambda r: True,
            'weight_decay': lambda r: 0,
            'lr': lambda r: 1e-3,
            'batch_size': lambda r: 64
        }

def CAP_train(sample):
    """ CAP model hparam definition 
    
    Args:
        sample (bool): If ''True'', hyper parameters are gonna be sampled randomly according to their given distributions. Defaults to ''False'' where the default value is chosen.
    """
    if sample:
        return {
            'class_balance': lambda r: True,
            'weight_decay': lambda r: 0.,
            'lr': lambda r: 10**r.uniform(-5, -3),
            'batch_size': lambda r: int(2**r.uniform(3, 4))
        }
    else:
        return {
            'class_balance': lambda r: True,
            'weight_decay': lambda r: 0,
            'lr': lambda r: 10**-4,
            'batch_size': lambda r: 8
        }

def SEDFx_train(sample):
    """ SEDFx model hparam definition 
    
    Args:
        sample (bool): If ''True'', hyper parameters are gonna be sampled randomly according to their given distributions. Defaults to ''False'' where the default value is chosen.
    """
    if sample:
        return {
            'class_balance': lambda r: True,
            'weight_decay': lambda r: 0.,
            'lr': lambda r: 10**r.uniform(-5, -3),
            'batch_size': lambda r: int(2**r.uniform(3, 4))
        }
    else:
        return {
            'class_balance': lambda r: True,
            'weight_decay': lambda r: 0,
            'lr': lambda r: 10**-4,
            'batch_size': lambda r: 8
        }

def PCL_train(sample):
    """ PCL model hparam definition """
    if sample:
        return {
            'class_balance': lambda r: True,
            'weight_decay': lambda r: 0.,
            'lr': lambda r: 10**r.uniform(-5, -3),
            'batch_size': lambda r: int(2**r.uniform(3, 5))
        }
    else:
        return {
            'class_balance': lambda r: True,
            'weight_decay': lambda r: 0.,
            'lr': lambda r: 10**-3,
            'batch_size': lambda r: 32
        }

def HHAR_train(sample):
    """ HHAR model hparam definition 
    
    Args:
        sample (bool): If ''True'', hyper parameters are gonna be sampled randomly according to their given distributions. Defaults to ''False'' where the default value is chosen.
    """
    if sample:
        return {
            'class_balance': lambda r: True,
            'weight_decay': lambda r: 0.,
            'lr': lambda r: 10**r.uniform(-4, -2),
            'batch_size': lambda r: int(2**r.uniform(3, 4))
        }
    else:
        return {
            'class_balance': lambda r: True,
            'weight_decay': lambda r: 0,
            'lr': lambda r: 10**-4,
            'batch_size': lambda r: 8
        }

def LSA64_train(sample):
    """ LSA64 model hparam definition 
    
    Args:
        sample (bool): If ''True'', hyper parameters are gonna be sampled randomly according to their given distributions. Defaults to ''False'' where the default value is chosen.
    """
    if sample:
        return {
            'class_balance': lambda r: True,
            'weight_decay': lambda r: 0.,
            'lr': lambda r: 10**r.uniform(-5, -3),
            'batch_size': lambda r: int(2**r.uniform(3, 4))
        }
    else:
        return {
            'class_balance': lambda r: True,
            'weight_decay': lambda r: 0,
            'lr': lambda r: 10**-4,
            'batch_size': lambda r: 2
        }

def get_model_hparams(dataset_name):
    """ Get the model related hyper parameters

    Each dataset has their own model hyper parameters definition

    Args:
        dataset_name (str): dataset that is gonna be trained on for the run
        seed (int): seed used if hyper parameter is sampled
        sample (bool, optional): If ''True'', hyper parameters are gonna be sampled randomly according to their given distributions. Defaults to ''False'' where the default value is chosen.

    Raises:
        NotImplementedError: Dataset name not found

    Returns:
        dict: Dictionnary with hyper parameters values
    """
    dataset_model = dataset_name + '_model'
    if dataset_model not in globals():
        raise NotImplementedError("dataset not found: {}".format(dataset_name))
    else:
        hyper_function = globals()[dataset_model]

    hparams = hyper_function()
    
    return hparams

def Basic_Fourier_model():
    """ Spurious Fourier model hparam definition """
    return {
        'model': 'LSTM',
        'hidden_depth': 1, 
        'hidden_width': 20,
        'recurrent_layers': 2,
        'state_size': 32
    }

def Spurious_Fourier_model():
    """ Spurious Fourier model hparam definition """
    return {
        'model': 'LSTM',
        'hidden_depth': 1, 
        'hidden_width': 20,
        'recurrent_layers': 2,
        'state_size': 32
    }

def TMNIST_model():
    """ TMNIST model hparam definition """
    return {
        'model': 'MNIST_LSTM',
        'hidden_depth': 3, 
        'hidden_width': 64,
        'recurrent_layers': 1,
        'state_size': 128
    }

def TCMNIST_seq_model():
    """ TCMNIST_seq model hparam definition """
    return {
        'model': 'MNIST_LSTM',
        'hidden_depth': 3, 
        'hidden_width': 64,
        'recurrent_layers': 1,
        'state_size': 128
    }

def TCMNIST_step_model():
    """ TCMNIST_step model hparam definition """
    return {
        'model': 'MNIST_LSTM',
        'hidden_depth': 3, 
        'hidden_width': 64,
        'recurrent_layers': 1,
        'state_size': 128
    }

def CAP_model():
    """ CAP model hparam definition """
    return {
        'model': 'deep4'
    }

def SEDFx_model():
    """ SEDFx model hparam definition """
    return {
        'model': 'deep4'
    }

def PCL_model():
    """ PCL model hparam definition"""
    return {
        'model': 'EEGNet'
    }

def HHAR_model():
    """ HHAR model hparam definition """
    return {
        'model': 'deep4',
    }

def LSA64_model():
    """ LSA64 model hparam definition """
    return {
        'model': 'CRNN',
        # Classifier
        'hidden_depth': 1,
        'hidden_width': 64,
        # LSTM
        'recurrent_layers': 2,
        'state_size': 128,
        # Resnet encoder
        'fc_hidden': (512,512),
        'CNN_embed_dim': 256
    }

def get_objective_hparams(objective_name, seed, sample=False):
    """ Get the objective related hyper parameters

    Each objective has their own model hyper parameters definitions

    Args:
        objective_name (str): objective that is gonna be trained on for the run
        seed (int): seed used if hyper parameter is sampled
        sample (bool, optional): If ''True'', hyper parameters are gonna be sampled randomly according to their given distributions. Defaults to ''False'' where the default value is chosen.

    Raises:
        NotImplementedError: Objective name not found

    Returns:
        dict: Dictionnary with hyper parameters values
    """
    # Return the objective class with the given name
    objective_hyper = objective_name+'_hyper'
    if objective_hyper not in globals():
        raise NotImplementedError("objective not found: {}".format(objective_name))
    else:
        hyper_function = globals()[objective_hyper]

    hparams = hyper_function(sample)

    for k in hparams.keys():
        hparams[k] = hparams[k](np.random.RandomState(seed))
    
    return hparams

def DANN_hyper(sample):
    """ DANN objective hparam definition 
    
    Args:
        sample (bool): If ''True'', hyper parameters are gonna be sampled randomly according to their given distributions. Defaults to ''False'' where the default value is chosen.
    """
    if sample:
        return {
            'lambda': lambda r: 10**r.uniform(-2, 2),
            'weight_decay_d': lambda r: 10**r.uniform(-6, -2),
            'd_steps_per_g_step' : lambda r: int(2**r.uniform(0, 3)),
            'grad_penalty' : lambda r: 10**r.uniform(-1, 1),
            'beta1': lambda r: r.choice([0., 0.5]),
            'mlp_width': lambda r: int(2 ** r.uniform(6, 10)),
            'mlp_depth': lambda r: int(r.choice([3, 4, 5])),
            'mlp_dropout': lambda r: r.choice([0., 0.1]),
            'label_smooth': lambda r: True,
            'eps': lambda r: r.uniform(0, 1),
            'lr_d': lambda r: 10**r.uniform(-4.5, -2.5),
        }
    else:
        return {
            'lambda': lambda r: 0.1,
            'weight_decay_d': lambda r: 0.0,
            'd_steps_per_g_step' : lambda r: 2,
            'grad_penalty' : lambda r: 0.0,
            'beta1': lambda r: 0.5,
            'mlp_width': lambda r: 64,
            'mlp_depth': lambda r: 2,
            'mlp_dropout': lambda r: 0.0,
            'label_smooth': lambda r: False,
            'eps': lambda r: 0.1,
            'lr_d': lambda r: 1e-3,
        }
    
def ERM_hyper(sample):
    """ ERM objective hparam definition 
    
    Args:
        sample (bool): If ''True'', hyper parameters are gonna be sampled randomly according to their given distributions. Defaults to ''False'' where the default value is chosen.
    """
    return {}

def IRM_hyper(sample):
    """ IRM objective hparam definition 
    
    Args:
        sample (bool): If ''True'', hyper parameters are gonna be sampled randomly according to their given distributions. Defaults to ''False'' where the default value is chosen.
    """
    if sample:
        return {
            'penalty_weight': lambda r: 10**r.uniform(-1,5),
            'anneal_iters': lambda r: r.uniform(0,2000)
        }
    else:
        return {
            'penalty_weight': lambda r: 1e2,
            'anneal_iters': lambda r: 500
        }


def VREx_hyper(sample):
    """ VREx objective hparam definition 
    
    Args:
        sample (bool): If ''True'', hyper parameters are gonna be sampled randomly according to their given distributions. Defaults to ''False'' where the default value is chosen.
    """
    if sample:
        return {
            'penalty_weight': lambda r: 10**r.uniform(-1,5),
            'anneal_iters': lambda r: r.uniform(0,2000)
        }
    else:
        return {
            'penalty_weight': lambda r: 1e2,
            'anneal_iters': lambda r: 500
        }

def SD_hyper(sample):
    """ SD objective hparam definition 
    
    Args:
        sample (bool): If ''True'', hyper parameters are gonna be sampled randomly according to their given distributions. Defaults to ''False'' where the default value is chosen.
    """
    if sample:
        return {
            'penalty_weight': lambda r: 10**r.uniform(-5,-1)
        }
    else:
        return {
            'penalty_weight': lambda r: 1
        }
        
def IGA_hyper(sample):
    """ IGA objective hparam definition 
    
    Args:
        sample (bool): If ''True'', hyper parameters are gonna be sampled randomly according to their given distributions. Defaults to ''False'' where the default value is chosen.
    """
    if sample:
        return {
            'penalty_weight': lambda r: 10**r.uniform(-1,5)
        }
    else:
        return {
            'penalty_weight': lambda r: 1e1
        }

def ANDMask_hyper(sample):
    """ ANDMask objective hparam definition 
    
    Args:
        sample (bool): If ''True'', hyper parameters are gonna be sampled randomly according to their given distributions. Defaults to ''False'' where the default value is chosen.
    """
    if sample:
        return {
            'tau': lambda r: r.uniform(0,1)
        }
    else:
        return {
            'tau': lambda r: 1
        }


def Fish_hyper(sample):
    """ Fish objective hparam definition 
    
    Args:
        sample (bool): If ''True'', hyper parameters are gonna be sampled randomly according to their given distributions. Defaults to ''False'' where the default value is chosen.
    """
    if sample:
        return {
            'meta_lr': lambda r: 0.5
        }
    else:
        return {
            'meta_lr': lambda r:r.choice([0.05, 0.1, 0.5])
        }
        
def SANDMask_hyper(sample):
    """ SANDMask objective hparam definition 
    
    Args:
        sample (bool): If ''True'', hyper parameters are gonna be sampled randomly according to their given distributions. Defaults to ''False'' where the default value is chosen.
    """
    if sample:
        return {
            'tau': lambda r: r.uniform(0.0,1.),
            'k': lambda r: 10**r.uniform(-3, 5),
            'betas': lambda r: r.uniform(0.9,0.999)
        }
    else:
        return {
            'tau': lambda r: 0.5,
            'k': lambda r: 1e+1,
            'betas': lambda r: 0.9
        }        
        
def IB_ERM_features_hyper(sample):
    """ IB_ERM objective hparam definition 
    
    Args:
        sample (bool): If ''True'', hyper parameters are gonna be sampled randomly according to their given distributions. Defaults to ''False'' where the default value is chosen.
    """
    if sample:
        return {
            'ib_weight': lambda r: 10**r.uniform(-3,0),
        }
    else:
        return {
            'ib_weight': lambda r: 0.1,
        }
        
def IB_ERM_logits_hyper(sample):
    """ IB_ERM objective hparam definition 
    
    Args:
        sample (bool): If ''True'', hyper parameters are gonna be sampled randomly according to their given distributions. Defaults to ''False'' where the default value is chosen.
    """
    if sample:
        return {
            'ib_weight': lambda r: 10**r.uniform(-3,0),
        }
    else:
        return {
            'ib_weight': lambda r: 0.1,
        }
 
def IB_IRM_hyper(sample):
    """ IB_ERM objective hparam definition 
    
    Args:
        sample (bool): If ''True'', hyper parameters are gonna be sampled randomly according to their given distributions. Defaults to ''False'' where the default value is chosen.
    """
    if sample:
        return {
            'ib_weight': lambda r: 10**r.uniform(-1,5),
            'ib_anneal': lambda r: r.uniform(0,2000),
            'irm_weight': lambda r: 10**r.uniform(-1,5),
            'irm_anneal': lambda r: r.uniform(0,2000)
        }
    else:
        return {
            'ib_weight': lambda r: 1e2,
            'ib_anneal': lambda r: 500,
            'irm_weight': lambda r: 1e2,
            'irm_anneal': lambda r: 500
        }
