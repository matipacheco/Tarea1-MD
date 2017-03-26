import csv

def drink(reviews):
	with open('beer_reviews.csv', 'rb') as csvfile:
		reader = csv.reader(csvfile, delimiter=',')
		for review in reader:
			review.pop(6)
			reviews.append(list(review))

	return reviews

def empty(string):
	return not string

def format_reviews(reviews):
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

		if empty(review[7]):
			review[7]  = 0.0
		else:
			review[7]  = float(review[7])

		if empty(review[8]):
			review[8]  = 0.0
		else:
			review[8]  = float(review[8])

		if empty(review[10]):
			review[10]  = 0.0
		else:
			review[10]  = float(review[10])

		if empty(review[11]):
			review[11]  = 0
		else:
			review[11]  = int(review[11])
	
		review.pop(9)
		review.pop(6)
		review.pop(1)

	labels.pop(9)
	labels.pop(6)
	labels.pop(1)

	return labels, reviews
