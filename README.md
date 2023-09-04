# SNIaAnalysis

Codes to run a few checks on the available SNIa templates that work for redshifts higher than 1.7 in lsst-i and r rest frame bands. The SNANA simulated data is used for comparison. The header and photometric files are downloaded from https://portal.nersc.gov/cfs/lsst/DESC_TD_PUBLIC/ELASTICC/ELASTICC2_TRAINING_SAMPLE/ELASTICC2_TRAIN_01_SNIa-SALT3/ for ELAsTiCC2 data. The same codes have been and can be tested on ELAsTiCC data, the predecessor of ELAsTiCC2. That data can be downloaded from https://portal.nersc.gov/cfs/lsst/DESC_TD_PUBLIC/ELASTICC/TRAINING_SAMPLES/ELASTICC_TRAIN_SNIa-SALT2/. 

Using these codes would require you to untar the phot and head files and place all four files in the same directory. SNcosmo package required to run can be installed by pip install sncosmo. If you wish to test the code of more data size, then rest of 39 sets of head and phot files can be downloaded from the above two links.
