import numpy as np
from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier
from sklearn.metrics import classification_report, confusion_matrix
from imblearn.under_sampling import RandomUnderSampler
import pickle


# get experimental data
feat = 79 # 79 features corresponding to the max number of carbon atoms in the triterpenoids samples
f = open('triterpenoids.csv', 'r')
m = [] # matrix n samples x m features
l = [] # label vector
for line in f:
        comp = line.split(', ')[:feat] 
        v = line.split(', ')[feat] # last column: label, 0 or 1
        fl = [float(x) for x in comp]
        m.append(fl)
        l.append(float(v.strip()))
data = np.array(m)
tar = np.array(l)

# data balance with the SMOTE algorithm 
ss = {0:3731,1:3731} # sampling strategy 3731 samples for each category
xx = RandomUnderSampler(sampling_strategy=ss,replacement=True,random_state=22).fit_sample(data,tar.squeeze())
data2 = xx[0]
tar2 = xx[1]


test_size = 0.1
X_train, X_test, y_train, y_test = train_test_split(data2, tar2, test_size=test_size, stratify=tar2,random_state=22)
# fit model to training data
model = XGBClassifier(learning_rate=0.25,max_depth=4,n_estimators=200,random_state=42) # these parameters were obtained after the Cross Validation 10-fold grid search.
model.fit(X_train, y_train)
# save model to file .pickle.dat
pickle.dump(model, open("triterpenoids.pickle.dat", "wb")) 
# prediction on the test set
y_pred = model.predict(X_test)

print("Test set results: ", classification_report(y_test, y_pred))
print("Confusion matrix: ")
print(confusion_matrix(y_test,y_pred))

