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
In the 'models' dir are included the 'prediction_fams.py' script and the models for each family.
### Requeriments for prediction_fams.py:
### pickle
The triterpenoids dir contains a script for training and saving the model 'save_model.py', as well as a script 'predict.py' to predict real cases
### Requirements for save_model.py and predict.py:
### Python >= 3.5
### sklearn == 0.20.1
### imblearn == 0.4.3
### xgboost == 0.82
### pickle
### numpy 
This triterpenoid example can be repeated for the other families following the readme file instructions
