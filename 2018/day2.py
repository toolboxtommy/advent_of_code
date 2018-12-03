#!/usr/bin/env python

from collections import Counter

with open('day2_data.txt', 'r') as puzzle_input:
	all_box_ids = [box_id for box_id in puzzle_input.read().split('\n')]

# problem 1
doubles = 0
triples = 0
for box_id in all_box_ids:
	double_found = False
	triple_found = False
	for letter in set(box_id):
		count = box_id.count(letter)
		if count == 2 and not double_found:
			doubles += 1
			double_found = True
		elif count == 3 and not triple_found:
			triples += 1
			triple_found = False
print('Problem 1: {}'.format(doubles*triples))

def match(id1, id2):
	strike_one = False
	position = None
	for i, chars in enumerate(zip(id1, id2)):
		if chars[0] != chars[1]:
			if strike_one:
				return False
			else:
				strike_one = True
				position = i
	if strike_one:
		return id1[:position]+id1[position+1:]
	return False

found = False
for first_box_id in all_box_ids:
	for second_box_id in all_box_ids:
		res = match(first_box_id, second_box_id)
		if not res:
			continue
		print('Problem 2: {}'.format(res))
		found = True
		break
	if found:
		break