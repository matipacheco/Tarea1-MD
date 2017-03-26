import csv

def read(reviews):
	with open('beer_reviews.csv', 'rb') as csvfile:
		reader = csv.reader(csvfile, delimiter=',')
		for review in reader:
			reviews.append(list(review))

	return reviews

def empty(string):
	return not string

def set_reviews(reviews):
	labels 	= reviews.pop(0)

	for review in reviews:
		if empty(review[0]):
			review[0]  = 0
		else:
			review[0]  = int(review[0])

		if empty(review[2]):
			review[2]  = 0
		else:
			review[2]  = int(review[2])

		if empty(review[3]):
			review[3]  = 0.0
		else:
			review[3]  = float(review[3])

		if empty(review[4]):
			review[4]  = 0.0
		else:
			review[4]  = float(review[4])

		if empty(review[5]):
			review[5]  = 0.0
		else:
			review[5]  = float(review[5])

		if empty(review[8]):
			review[8]  = 0.0
		else:
			review[8]  = float(review[8])

		if empty(review[9]):
			review[9]  = 0.0
		else:
			review[9]  = float(review[9])

		if empty(review[11]):
			review[11]  = 0.0
		else:
			review[11]  = float(review[11])

		if empty(review[12]):
			review[12]  = 0
		else:
			review[12]  = int(review[12])
	
	return labels, reviews
