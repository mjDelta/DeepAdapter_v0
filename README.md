# DeepAdapter
## A self-adaptive and versatile tool for eliminating multiple undesirable variations from transcriptome
Codes and tutorial for [A self-adaptive and versatile tool for eliminating multiple undesirable variations from transcriptome](https://www.biorxiv.org/content/10.1101/2024.02.04.578839v1).

We make an one-line code to utilize DeepAdapter for convenient usage.
```sh
$ from deepAdapter import run as RUN
$ trainer = RUN.train(,
    train_list = train_list,
    val_list = val_list,
    test_list = test_list,
    label2unw = label2bat,
    label2wnt = bio_label2bat,
    net_args = net_args,
    out_dir = out_dir)
```

# Get started
## Download the exmaple datasets
Please download the datasets in [Zenodo](https://zenodo.org/records/10494751).
These datasets are collected from literatures to demonstrate multiple unwanted variations, including:
* batch vairations: LINCS-DToxS ([van Hasselt et al. Nature Communications, 2020](https://www.nature.com/articles/s41467-020-18396-7)) and Quartet project ([Yu, Y. et al. Nature Biotechnology, 2023](https://www.nature.com/articles/s41587-023-01867-9)).
* platform variations: profiles from microarray ([Iorio, F. et al. Cell, 2016](https://www.cell.com/cell/pdf/S0092-8674(16)30746-2.pdf)) and RNA-seq ([Ghandi, M. et al. Nature, 2019](https://www.nature.com/articles/s41586-019-1186-3)).
* purity variations: profiles from cancer cell lines ([Ghandi, M. et al. Nature, 2019](https://www.nature.com/articles/s41586-019-1186-3)) and tissues ([Weinstein, J.N. et al. Nature genetics, 2013](https://www.nature.com/articles/ng.2764)).
* unknown variations: profiles from cancer tissues ([Weinstein, J.N. et al. Nature genetics, 2013](https://www.nature.com/articles/ng.2764)) and Quartet ([Yu, Y. et al. Nature Biotechnology, 2023](https://www.nature.com/articles/s41587-023-01867-9)).

After downloading, place the datasets in the `data/` directory located in the same hierarchy as this tutorial.
* batch datasets: `data/batch_data/`
* platform datasets: `data/platform_data/`
* purity datasets: `data/purity_data/`

**Putting datasets in the right directory is important for loading the example datasets successfully.**

## The file format of your own dataset
The input files include $2$ files: 
* **gene_expression.txt** for gene expression matrix;
* **unwantedVar_biologicalSig.txt** for annotations of unwanted variations and biological signals.

The example of **gene_expression.txt** is as follows (**Note: every row should be split by commas.**):
| SampleId | Gene_1 | Gene_2 | Gene_3 | ... | Gene_n-2 | Gene_n-1 | Gene_n |
|  ----  | ----  | ----  | ----  |  ----  | ----  | ----  | ----  |
| **1** | x<sub>11</sub> | x<sub>12</sub> | x<sub>13</sub> | ... | x<sub>1(n-2)</sub> | x<sub>1(n-1)</sub> | x<sub>1n</sub> |
| **2** | x<sub>21</sub> | x<sub>22</sub> | x<sub>23</sub> | ... | x<sub>2(n-2)</sub> | x<sub>2(n-1)</sub> | x<sub>2n</sub> |
| ... | ... | ... | ... | ... | ... | ... | ... |
| **m** | x<sub>m1</sub> | x<sub>m2</sub> | x<sub>m3</sub> | ... | x<sub>m(n-2)</sub> | x<sub>m(n-1)</sub> | x<sub>mn</sub> |

The example of **unwantedVar_biologicalSig.txt** is as follows (**Note: every row should be split by commas.**):
| SampleId | Unwanted_var | Biological_sig |
|  ----  | ----  | ----  |
| **1** | unwantedVar<sub>1</sub> | biologicalSig<sub>1</sub> |
| **2** | unwantedVar<sub>1</sub> | biologicalSig<sub>1</sub> |
| ... | ... | ... |
| **m** | unwantedVar<sub>p</sub> | biologicalSig<sub>q</sub> |

Examples of **unwantedVar** and **biologicalSig**:
* **unwantedVar**:
    * **batch**: batch1, batch2, ..., batch(n);
    * **platform**: RNA-seq, microarray;
    * **purity**: cell lines, tissue;
    * ...
* **biologicalSig**:
    * **cancer types**: lung cancer, kidney cancer, ..., bone cancer;
    * **lineages**: Lung, kidney, ..., eye;
    * **donor sources**: donor1, donor2, ..., donor(n);
    * ...

## Use the tutorials: re-train the models with provided datasets or your own datasets
* Step 1: please enter the following commands to run DeepAdapter with datasets 
```sh
$ # Clone this repository to your local computer
$ git clone https://github.com/mjDelta/DeepAdapter.git
$ cd DeepAdapter
$ # create a new conda environment
$ conda create -n deepAdapter python=3.9
$ # activate environment
$ conda activate deepAdapter
$ # Install dependencies
$ pip install -r requirements.txt
$ # Launch jupyter notebook
$ jupyter notebook
```
* Step 2: double-click to open tutorials:
    * `DA-Batch-Tutorial.ipynb`: the tutorial of re-training DeepAdapter using the example dataset;
    * `DA-YourOwnData-Tutorial.ipynb`: the tutorial of training DeepAdapter using your own dataset.

**After opening the tutorials, please press Shift-Enter to execute a "cell" in `.ipynb`.**
