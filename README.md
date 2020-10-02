# np-pred
Prediction of common natural product families from 13C NMR data. Work published at https://pubs.acs.org/doi/abs/10.1021/acs.jcim.0c00293
This is a predictive model based on the XGBoost classifer that outputs the probability of a certain natural product structure presence. The input data are the 13C NMR shifts. The families included are:
  ## sesquiterpenoids
  ## diterpenoids
  ## triterpenoids
  ## steroids
  ## flavonoids
  ## lignans
  ## alkaloids
  ## glycosides
  

To perform the predictions use the 'prediction_fams.py' script located in the 'models' dir.
### Requeriments for prediction_fams.py:
### pickle

An example of training and prediction is inluded for the triterpenoids family. The triterpenoids dir contains a script for training and saving the model 'save_model.py', as well as a script 'predict.py' to predict real cases
### Requirements for save_model.py and predict.py:
### Python >= 3.5
### sklearn == 0.20.1
### imblearn == 0.4.3
### xgboost == 0.82
### pickle
### numpy 
