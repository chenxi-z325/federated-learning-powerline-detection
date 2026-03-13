import numpy as np

def fedavg(weights_list):
    """
    Perform Federated Averaging (FedAvg) algorithm on a list of weights.
    
    Args:
        weights_list (list of np.ndarray): List containing the weights from each client.
        
    Returns:
        np.ndarray: Averaged weights.
    """
    # Sum the weights across clients
    return np.mean(weights_list, axis=0)