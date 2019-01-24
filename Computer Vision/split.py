import cv2
import os
import numpy as np
import matplotlib.pyplot as plt 

classes = ['bullmastiff', 'chowchow', 'pug', 'maltese', 'huskysibir', 'dachshund', 'dalmatian', 'corgi', 'chihuahua', 'yorkshire']
class2idx = {
	'bullmastiff': 0,
	'chowchow': 1,
	'pug': 2,
	'maltese': 3,
	'huskysibir': 4,
	'dachshund': 5,
	'dalmatian': 6,
	'corgi': 7,
	'chihuahua': 8,
	'yorkshire': 9 
}


def split():
	config = {}

	for idx, class_name in enumerate(classes):
		np.random.seed(idx + 1)

		folder = "data/" + class_name

		names = os.listdir(folder)	
		size = len(names)
		indices = np.arange(size)
		np.random.shuffle(indices)

		train = indices[:int(size * 0.6)]
		valid = indices[int(size * 0.6):int(size * 0.8)]
		test = indices[int(size * 0.8):]

		config[class_name] = {
			'train': [names[i] for i in train],
			'valid': [names[i] for i in valid]
		}

		for i in test:
			os.rename(folder + '/' + names[i], "private/all/" + str(class2idx[class_name]) + "_" + names[i])

	import json
	with open('public.json', 'w') as outfile:
	    json.dump(config, outfile)

def prepare_test():
	holder = {}
	folder = "private/all"
	names = os.listdir(folder)
	order = np.arange(len(names))
	np.random.shuffle(order)

	for new_idx, idx in enumerate(order):
		name = names[idx]
		label = int(name.split("_")[0])

		ext = name.split('.')[-1]
		new_name = "{}.{}".format(new_idx, ext)
		os.rename(folder + "/" + name, folder + "/" + new_name)

		holder[new_name] = label

	import json
	with open('private.json', 'w') as outfile:
	    json.dump(holder, outfile)

if __name__ == '__main__':
	prepare_test()
	# split()
	


