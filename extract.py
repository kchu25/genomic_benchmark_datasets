import os

from genomic_benchmarks.data_check import list_datasets

list_datasets()

# look at https://github.com/ML-Bioinfo-CEITEC/genomic_benchmarks/blob/main/src/genomic_benchmarks/dataset_getters/pytorch_datasets.py
from genomic_benchmarks.dataset_getters.pytorch_datasets import (
    DemoCodingVsIntergenomicSeqs,
    DemoHumanOrWorm,
    DemoMouseEnhancers,
    DrosophilaEnhancersStark,
    HumanEnhancersCohn,
    HumanEnhancersEnsembl,
    HumanNontataPromoters,
    HumanOcrEnsembl,
)

fcns = [DemoCodingVsIntergenomicSeqs, DemoHumanOrWorm, DemoMouseEnhancers,
    DrosophilaEnhancersStark, HumanEnhancersCohn, HumanEnhancersEnsembl,
    HumanNontataPromoters, HumanNontataPromoters, HumanOcrEnsembl]
names = ["DemoCodingVsIntergenomicSeqs", "DemoHumanOrWorm", "DemoMouseEnhancers",
    "DrosophilaEnhancersStark", "HumanEnhancersCohn", "HumanEnhancersEnsembl",
    "HumanNontataPromoters", "HumanNontataPromoters", "HumanOcrEnsembl"]

folder_name = 'datasets_for_classifications/'
os.mkdir(folder_name)

for fcn, name in zip(fcns, names):
    dataset_folder = folder_name + name + '/'
    os.mkdir(dataset_folder)

    dset = fcn(split='train', version=0)
    with open(dataset_folder + 'train.fa', 'a') as the_file:
        for (dna_str, class_) in dset:
            the_file.write('> ' + str(class_) + '\n')
            the_file.write(dna_str + '\n')

    dset = fcn(split='test', version=0)
    with open(dataset_folder + 'test.fa', 'a') as the_file:
        for (dna_str, class_) in dset:
            the_file.write('> ' + str(class_) + '\n')
            the_file.write(dna_str + '\n')
