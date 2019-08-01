import pickle
import sys

file_report = open('report','w')
nmr = sys.argv[1:len(sys.argv)] # data from user 13C shifts (ppm)

def convert_strings(nmr):
	inp = []
	for i in nmr:
		try:
			i = float(i.split(',')[0])
		except:	
			raise Exception('Please check your input: {}'.format(i))
			
		inp.append(i)
	file_report.write('input: ')
	file_report.write('\n')
	file_report.write(str(inp))
	file_report.write('\n')
	return inp

inp = sorted(convert_strings(nmr))


"""Trained XGBoost models"""

f1 = "sesquiterpenoids.pickle.dat"
f2 = "diterpenoids.pickle.dat"
f3 = "triterpenoids.pickle.dat"
f4 = "steroids.pickle.dat"
f5 = "flavonoids.pickle.dat"
f6 = "lignans.pickle.dat"
f7 = "alkaloids.pickle.dat"
f8 = "glycosides.pickle.dat"

files_dict = {f1:48,f2:53,f3:79,f4:57,f5:43,f6:48,f7:37,f8:66} # dictionary of max lengths that were used to train the model and must be specified for each family


def main():

	if len(nmr) == int(0):
		print('Please provide the 13C shifts')
	else:
		predict()


def create_data(X,file,max_len):
        """ Pads the input array to create a fixed length new input array. The new length depends on the model"""
        le = len(X) 
        dif = max_len - le
        if dif < 0:
                name = None
                model = None
		
        else:
                name = file.split('.')[0]
                model =  pickle.load(open(file, "rb"))
       	s = []
        for k in range(dif):
                s.append(-999)
        nl = X+s
        return nl, name, model # nl: new length array

def predict():
	max_proba = 0
	fam =str()
	for file,leng in files_dict.items():

		X, name, model = create_data(inp,file,leng)
		X_test = X
		if model:
			y_pred = model.predict_proba(X_test)
			if name != 'glycosides': # check report to see the probability of glycoside
				if y_pred[0][1] >= max_proba:
					max_proba = y_pred[0][1]
					fam = name
				else:
					max_proba = max_proba
					fam = fam

			file_report.write(name)
			file_report.write('\n')

			file_report.write('Probability that the spectra correspond to the '+name+' family: '+str(y_pred[0][1]))
			file_report.write('\n')
			
			file_report.write('\n')
	print('Family with max probability: ',fam, 'probability: ',max_proba)

main()
	

