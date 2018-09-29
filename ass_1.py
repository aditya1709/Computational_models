import os
import numpy as np
import time

def speed_cal(data,t_w_array):
	tcorpus = 0
	ncorpus = 0
	for ct in range(len(data)):
		tcorpus += float(data[ct][0])*(t_w_array[ct] + 140)
		ncorpus += float(data[ct][0])*len(data[ct][1])
	v_cps = ncorpus/tcorpus
	v_wpm = (v_cps*60)/5
	print('Final speed is {}'.format(v_wpm))

def distance(a,b):
	return np.linalg.norm(np.asarray(a)-np.array(b))

def main():
	start_time = time.time()
	key_dict = {}
	key_dict['q'] = [0.0,0.0]
	key_dict['w'] = [0.2,0.0]
	key_dict['e'] = [0.4,0.0]
	key_dict['r'] = [0.6,0.0]
	key_dict['t'] = [0.8,0.0]
	key_dict['y'] = [1.0,0.0]
	key_dict['u'] = [1.2,0.0]
	key_dict['i'] = [1.4,0.0]
	key_dict['o'] = [1.6,0.0]
	key_dict['p'] = [1.8,0.0]
	key_dict['a'] = [0.1,0.3]
	key_dict['s'] = [0.3,0.3]
	key_dict['d'] = [0.5,0.3]
	key_dict['f'] = [0.7,0.3]
	key_dict['g'] = [0.9,0.3]
	key_dict['h'] = [1.1,0.3]
	key_dict['j'] = [1.3,0.3]
	key_dict['k'] = [1.5,0.3]
	key_dict['l'] = [1.7,0.3]
	key_dict['z'] = [0.3,0.6]
	key_dict['x'] = [0.5,0.6]
	key_dict['c'] = [0.7,0.6]
	key_dict['v'] = [0.9,0.6]
	key_dict['b'] = [1.1,0.6]
	key_dict['n'] = [1.3,0.6]
	key_dict['m'] = [1.5,0.6]

	# Extract frequency and word from the corpus.
	with open('./corpus.txt') as f:
		content = f.readlines()
	filtered_data = []
	for i in content:
		filtered_data.append([i.split('	')[0],i.split('	')[1]])
	
	# Filter words to remove symbols as they are not part of keyboard. 
	for count1 in range(len(filtered_data)):
		word = ''
		for count2 in range(len(filtered_data[count1][1])):
			if filtered_data[count1][1][count2] in key_dict:
				word = word + filtered_data[count1][1][count2]
		filtered_data[count1][1] = word		

	# Calculate distances moved for each word 
	# Assumption : User types with both hands (thumbs) and uses each finger alternatively. 
	A = []
	for count1 in range(len(filtered_data)):
		temp = []
		left_data = []
		right_data = []
		for count2 in range(len(filtered_data[count1][1])):
			if count2%2 == 0:
				right_data.append(filtered_data[count1][1][count2])
			else:
				left_data.append(filtered_data[count1][1][count2])
		for skl in range(len(left_data)-1):
			temp.append(distance(key_dict[filtered_data[count1][1][skl]],key_dict[filtered_data[count1][1][skl+1]]))	
		for skr in range(len(right_data)-1):
			temp.append(distance(key_dict[filtered_data[count1][1][skr]],key_dict[filtered_data[count1][1][skr+1]]))		
		# for count2 in range(len(filtered_data[count1][1])-1):
		# 	temp.append(distance(key_dict[filtered_data[count1][1][count2]],key_dict[filtered_data[count1][1][count2+1]]))
		A.append(temp)
	
	W = 0.2
	word_time = []

	# Use fitt's law to model movement time 
	for dist1 in A : 
		temp_sum = []
		for As in dist1:
			temp_sum.append(156.5568 + 26.1044*np.log2((As/W)+1))
		word_time.append(np.sum(temp_sum))

	# Calculate speed for the entire corpus in words/minute
	speed_cal(filtered_data,word_time)
	print(time.time()-start_time)

if __name__ == '__main__':
	main()
