import sys
import pandas as pd



def imputeByClassMode(data):
	classes = data['00class'].unique()
	classesData = {}

	for c in classes:
		classesData[c] = data[data['00class'] == c]

	final = pd.DataFrame()

	for cdata in classesData.values():
		#print("Imputing for class %d" % cdata['00class'][0])
		for column in cdata.columns:
			try:
				mode = cdata[column].mode()[0]
			except IndexError:
				mode = 0
			cdata[column].fillna(mode, inplace=True)
		final = final.append(cdata)
	return final	

if __name__ == '__main__':
	data = pd.read_csv(sys.argv[1])
	finalFile = sys.argv[2]
	final = imputeByClassMode(data)
	final.to_csv(finalFile, na_rep='NaN')