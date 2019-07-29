# np-pred
Prediction of common natural product families from 13C NMR data.
This is a predictive model based on the XGBoost classifer that outputs the probability of a certain natural product structure presence. The input data is the 13C NMR shifts. The families included are:
  ## sesquiterpenoids
  ## diterpenoids
  ## triterpenoids
  ## steroids
  ## flavonoids
  ## lignans
  ## alkaloids
  ## glycosides
Here are included the data sets for each family and python scripts for the training and model generation.
### Requeriments:
### Python >= 3.5
### sklearn == 0.20.1
### imblearn == 0.4.3
### xgboost == 0.82
### pickle
### numpy 
