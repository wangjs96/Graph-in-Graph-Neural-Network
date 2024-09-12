Codes in this repository consist of GIG-GatedGCN and GIG-CTR-GCN. The original GatedGCN can be found from [here](https://github.com/wangjs96/benchmarking-gnns/blob/master/layers/gated_gcn_layer.py) and orginal CTR-GCN can be found from [here](https://github.com/Uason-Chen/CTR-GCN).
If you find this repository useful for your research, please cite:

```
@misc{wang2024graphgraphneuralnetwork,
      title={Graph in Graph Neural Network}, 
      author={Jiongshu Wang and Jing Yang and Jiankang Deng and Hatice Gunes and Siyang Song},
      year={2024},
      eprint={2407.00696},
      archivePrefix={arXiv},
      primaryClass={cs.LG},
      url={https://arxiv.org/abs/2407.00696}, 
}
```

Requirements
=
- Python 3.8
- PyTorch 1.9.0
- CUDA 11.1
- DGL 0.9.0

- Check the required python packages in `ga_dependency.txt` right [here](./GIG-Supplementary-Codes-Anonymous/data/) for graph analysis tasks.
```
pip install -r ga_dependency.txt
```
- Check the required python packages in `sk_dependency.txt` right [here](./GIG-Supplementary-Codes-Anonymous/NTURGB/GIG-CTR-GCN/) for action recognition tasks.
```
pip install -r sk_dependency.txt
```

Training
= 
>For general graph analysis tasks (clicking the link will directly take you to the target folder):

- [MNIST](./GIG/data/superpixels)
1) Execute the code blocks in 'prepare_superpixels_MNIST.ipynb' to download dataset and complete preprocessing
2) Execute the 'MNIST.ipynb' to start training

- [CIFAR10](./GIG/data/superpixels/)
1) Execute the code blocks in 'prepare_superpixels_CIFAR.ipynb' to download dataset and complete preprocessing
2) Execute the 'CIFAR10.ipynb' to start training
  
- [CLUSTER](./GIG/data/SBMs/)
1) Execute the code blocks in 'prepare_SBM_CLUSTER.ipynb' to download dataset and complete preprocessing
2) Execute the 'CLUSTER.ipynb' to start training

- [PATTERN](./GIG/data/SBMs/)
1) Execute the code blocks in 'prepare_SBM_PATTERN.ipynb' to download dataset and complete preprocessing
2) Execute the 'PATTERN.ipynb' to start training

- [ZINC](./GIG/data/molecules/)
1) Execute the code blocks in 'prepare_molecules.ipynb' to download dataset and complete preprocessing
2) Execute the 'ZINC.ipynb' to start training

- [ZINC-full](./GIG/data/molecules/)
1) Execute the code blocks in 'prepare_molecules_ZINC_full.ipynb' to download dataset and complete preprocessing
2) Execute the 'ZINC-full.ipynb' to start training

- [AQSOL](./GIG/data/molecules/)
1) Execute the code blocks in 'prepare_molecules.ipynb' to download dataset and complete preprocessing
2) Execute the 'AQSOL.ipynb' to start training

- [TSP](./GIG/data/TSP/)
1) Execute the code blocks in 'prepare_TSP.ipynb' to download dataset and complete preprocessing
2) Execute the 'TSP.ipynb' to start training

- [TU](./GIG/data/TUs/)
1) Dataset will be automatically downloaded and processed. Nonthing needs to be done right here.
2) Execute the 'TU-GIG-Codes.ipynb' to start training

- [OGBG-PPA](./GIG/data/OGBG-PPA/)
1) Dataset will be automatically downloaded and processed. Nonthing needs to be done right here.
2) Execute the 'OGBG-PPA.ipynb' to start training


>For human-skeleton action recognition tasks, the raw data should be downloaded from CTR-GCN (https://github.com/Uason-Chen/CTR-GCN). Then data preprocessing should be run then as following:

##### Directory Structure

- Put downloaded data into the following directory structure:

```
- data/
  - NW-UCLA/
    - all_sqe
      ... # raw data of NW-UCLA
  - ntu/
  - ntu120/
  - nturgbd_raw/
    - nturgb+d_skeletons/     # from `nturgbd_skeletons_s001_to_s017.zip`
      ...
    - nturgb+d_skeletons120/  # from `nturgbd_skeletons_s018_to_s032.zip`
      ...
```

##### Generating Data

- Generate NTU RGB+D 60 or NTU RGB+D 120 dataset:

```
 cd ./data/ntu # or cd ./data/ntu120
 # Get skeleton of each performer
 python get_raw_skes_data.py
 # Remove the bad skeleton 
 python get_raw_denoised_data.py
 # Transform the skeleton to the center of the first frame
 python seq_transformation.py
```

##### Executing training

* NTURGB+D X-Sub
  * Using command `python main.py --config config/nturgbd-cross-subject/default.yaml --work-dir work_dir/ntu/csub/ctrgcn --device 0`

* NTURGB+D X-View
  * Using command `python main.py --config config/nturgbd-cross-view/default.yaml --work-dir work_dir/ntu/cview/ctrgcn --device 0`
