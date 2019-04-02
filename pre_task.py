# Author: Nick Ioannidis
# Date: Tuesday, April 2, 2019
# Purpose: iGEM Software Pre-Task


# Question 1
# Finds most frequent k-mer in text
# Returns empty string if there is larger or if pattern is greater than the length of text
def count(text, pattern):
    k_mers = []
    pattern_dict = dict()
    if pattern > len(text):
        return k_mers
    for i in range(len(text)-pattern+1):
        k_mer = text[i:i+pattern]
        if k_mer in pattern_dict:
            pattern_dict[k_mer] += 1
        else:
            pattern_dict[k_mer] = 1
    return get_max_elements(pattern_dict)


# Question 2
# Finds all shared k-mers given two texts
# Returns empty string if there is no pattern or if pattern is larger than the length of any of two texts
def find_genome_pair(pattern, k_mer, complement):
    coordinates = []
    if pattern > len(k_mer) | pattern > len(complement):
        return coordinates
    for i in range(len(k_mer)-pattern+1):
        slice1 = k_mer[i:i+pattern]
        for j in range(len(complement)-pattern+1):
            slice2 = complement[j:j+pattern]
            translated_slice2 = translate(slice2)
            if (slice1 == slice2) | (slice1 == translated_slice2):
                pair = (i, j)
                coordinates.append(pair)
    return coordinates


# Helper method to get keys with max value and return them as a list
def get_max_elements(pattern_dict):
    k_mers = []
    highest = max(pattern_dict.values())
    for k, v in pattern_dict.items():
        if v == highest:
            k_mers.append(k)
    return k_mers


# Helper method return complement of given k-mer
def translate(k_mer):
    monomer_map = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
    s = ''
    for v in k_mer:
        s += monomer_map[v]
    return s
