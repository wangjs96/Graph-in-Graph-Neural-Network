"""
    File to load dataset based on user control from main file
"""
from data.superpixels import SuperPixDataset
from data.molecules import MoleculeDataset
from data.SBMs import SBMsDataset
from data.TSP import TSPDataset
from data.TUs import TUsDataset



def LoadData(DATASET_NAME):
    """
        This function is called in the main.py file 
        returns:
        ; dataset object
    """
    # handling for MNIST or CIFAR Superpixels
    if DATASET_NAME == 'MNIST' or DATASET_NAME == 'CIFAR10':
        return SuperPixDataset(DATASET_NAME)
    
    # handling for (ZINC) molecule dataset
    if DATASET_NAME in ['ZINC', 'ZINC-full', 'AQSOL']:
        return MoleculeDataset(DATASET_NAME)


    # handling for SBM datasets
    SBM_DATASETS = ['SBM_CLUSTER', 'SBM_PATTERN']
    if DATASET_NAME in SBM_DATASETS: 
        return SBMsDataset(DATASET_NAME)
    
    # handling for TSP dataset
    if DATASET_NAME == 'TSP':
        return TSPDataset(DATASET_NAME)

    # handling for the TU Datasets
    TU_DATASETS = ['ENZYMES', 'DD', 'PROTEINS_full']
    if DATASET_NAME in TU_DATASETS: 
        return TUsDataset(DATASET_NAME)


    
