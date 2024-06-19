# DeepAdapter
## A self-adaptive and versatile tool for eliminating multiple undesirable variations from transcriptome
Codes and tutorial for [A self-adaptive and versatile tool for eliminating multiple undesirable variations from transcriptome](https://www.biorxiv.org/content/10.1101/2024.02.04.578839v1).
# Getting started
## Downloading the datasets
Please download the datasets in [Zenodo](https://zenodo.org/records/10494751).
These datasets are collected from literatures to demonstrate multiple unwanted variations, including:
* batch vairations: LINCS-DToxS ([van Hasselt et al. Nature Communications, 2020](https://www.nature.com/articles/s41467-020-18396-7)) and Quartet project ([Yu, Y. et al. Nature Biotechnology, 2023](https://www.nature.com/articles/s41587-023-01867-9)).
* platform variations: profiles from microarray ([Iorio, F. et al. Cell, 2016](https://www.cell.com/cell/pdf/S0092-8674(16)30746-2.pdf)) and RNA-seq ([Ghandi, M. et al. Nature, 2019](https://www.nature.com/articles/s41586-019-1186-3)).
* purity variations: profiles from cancer cell lines ([Ghandi, M. et al. Nature, 2019](https://www.nature.com/articles/s41586-019-1186-3)) and tissues ([Weinstein, J.N. et al. Nature genetics, 2013](https://www.nature.com/articles/ng.2764)).
* unknown variations: profiles from cancer tissues ([Weinstein, J.N. et al. Nature genetics, 2013](https://www.nature.com/articles/ng.2764)) and Quartet ([Yu, Y. et al. Nature Biotechnology, 2023](https://www.nature.com/articles/s41587-023-01867-9)).
## Re-train the models with provided datasets or your own datasets
* Step 1: please enter the following commands to run DeepAdapter with datasets 
```sh
$ # Clone this repository to your local computer
$ git clone https://github.com/mjDelta/DeepAdapter.git
$ cd DeepAdapter
$ # Install dependencies
$ pip install -r requirements.txt
$ # Launch jupyter notebook
$ jupyter notebook
```
* Step 2: double-click to open `$DeepAdapter-Tutorial.ipynb$`. Please press Shift-Enter to execute a "cell" in `$DeepAdapter-Tutorial.ipynb$`.


**Note: please follow the instructions to put the downloaded files in the right directories.**

