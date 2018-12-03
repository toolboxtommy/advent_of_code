#!/usr/bin/env python

with open('day1_data.txt', 'r') as puzzle_input:
	all_freqs = [int(freq) for freq in puzzle_input.read().split('\n')]

# problem 1
print('Problem 1: {}'.format(sum(all_freqs)))

# problem 2
current_freq = 0
past_freqs = []
solution_found = False
while not solution_found:
    for freq in all_freqs:
        current_freq += freq
        if current_freq in past_freqs:
            print('Problem 2: {}'.format(current_freq))
            solution_found = True
            break
        else:
            past_freqs.append(current_freq)