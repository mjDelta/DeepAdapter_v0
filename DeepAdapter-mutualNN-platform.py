import os, sys
import pandas as pd
import numpy as np

from utils import data_utils as DT
from utils import utils as UT
import utils.triplet as TRP
from models.trainer import Trainer
from models.data_loader import TransData, DataLoader
from models.dl_utils import AE, FBatch

### load data
dat1_name = "rna"
dat2_name = "arr"
db_name = f"{dat1_name}_{dat2_name}"
loadTransData = DT.LoadTransData()
dat1_raw, ids1 = loadTransData.load_data_platform(dat1_name)
dat2_raw, ids2 = loadTransData.load_data_platform(dat2_name)

### preprocessing
prepTransData = DT.PrepTransData()
dat1_raw = prepTransData.sample_norm(dat1_raw)
dat2_raw = prepTransData.sample_norm(dat2_raw)
data1, data2, sorted_cols = prepTransData.sort_genes(dat1_raw, dat2_raw)
data1 = prepTransData.sample_log(data1)
data2 = prepTransData.sample_log(data2)

### assemble data1 & data2
data = np.vstack((data1, data2))
unw_variations = np.array([0]*len(data1) + [1]*len(data2))
dis_labels, diseases, disease2label, label2disease = loadTransData.load_bioLabel_platform(ids1, ids2)
unw2label, label2unw, labels, labels_onehot = prepTransData.label2onehot(unw_variations)

### out paths
out_dir = os.path.join("../model_testcodes/platform_data", "deepAligner_DML/ln_pre_MNNRaw/")
os.makedirs(out_dir, exist_ok = True)

### train & val & test for platform
#### train = unpaired data, test = paired data
train_data, train_labels, train_labels_hot, \
    val_data, val_labels, val_labels_hot, \
    test_data, test_labels, test_labels_hot, \
    train_ids, val_ids, test_ids, \
    train_dis_labels, val_dis_labels, test_dis_labels, \
    tot_train_val_idxs, tot_train_idxs, tot_val_idxs, tot_test_idxs = DT.data_split_platform(data, labels, labels_onehot, dis_labels, ids1, ids2)
train_bios, val_bios, test_bios = dis_labels[tot_train_idxs], dis_labels[tot_val_idxs], dis_labels[tot_test_idxs]


### network parameters setting
from params import dl_params as DLPARAM
net_args = DLPARAM.load_dl_params()

## initialize models
in_dim = data.shape[1]
num_unw_vars = len(unw2label)
ae = AE(in_dim, net_args.hidden_dim, num_unw_vars, net_args.z_dim, net_args.drop).cuda()
fbatch = FBatch(net_args.hidden_dim, num_unw_vars, net_args.z_dim, net_args.drop).cuda()

## initialize dataloader
train_trans = TransData(train_data, train_labels, train_bios, train_ids, train_labels_hot)
train_loader = DataLoader(train_trans, batch_size = net_args.batch_size, collate_fn = train_trans.collate_fn, shuffle = True, drop_last = False)
val_trans = TransData(val_data, val_labels, val_bios, val_ids, val_labels_hot)
val_loader = DataLoader(val_trans, batch_size = net_args.batch_size, collate_fn = val_trans.collate_fn, shuffle = False, drop_last = False)
test_trans = TransData(test_data, test_labels, test_bios, test_ids, test_labels_hot)
test_loader = DataLoader(test_trans, batch_size = net_args.batch_size, collate_fn = test_trans.collate_fn, shuffle = False, drop_last = False)

## initialize trainer
trainer = Trainer(train_loader, val_loader, test_loader, ae, fbatch, label2disease, label2unw, net_args, out_dir)

## initialize mutual neighbors
train_mutuals = TRP.find_MNN_cosine_kSources(train_data, train_labels, train_ids)
val_mutuals = TRP.find_MNN_cosine_kSources(val_data, val_labels, val_ids)
print(len(train_bios), len(set(train_bios)), len(train_ids), len(set(train_ids)))

## training
# trainer.fit(train_mutuals, val_mutuals)

### load trained model & test
trainer.load_trained_ae(os.path.join(out_dir, "ae.tar"))

record_path = os.path.join(out_dir, "res.csv")
trainer.evaluate(record_path, db_name)