# Course: DSC510
# Assignment: 8.1
# Date: 4/27/2020
# Name: Laura Hoffmann
# Description: Program to calculate word totals

import string


def process_line(line, word_count_dict):
    line = line.strip()
    word_list = line.split()
    for word in word_list:
        if word != '--':
            word = word.lower()
            word = word.strip()
            word = word.strip(string.punctuation)
            add_word(word, word_count_dict)


def add_word(word, word_count_dict):
    if word in word_count_dict:
        word_count_dict[word] += 1
    else:
        word_count_dict[word] = 1


def pretty_print(word_count_dict):
    value_key_list = []
    for key, val in word_count_dict.items():
        value_key_list.append((val, key))
    value_key_list.sort(reverse=True)
    print('{:11s}{:11s}'.format("Word", "Count"))
    print('  ' * 21)
    for val, key in value_key_list:
        print('{:12s} {:<3d}'.format(key, val))


def main():
    word_count_dict = {}
    try:
        gba_file = open('gettysburg.txt', 'r')
    except FileNotFoundError as e:
        print(e)
    for line in gba_file:
        process_line(line, word_count_dict)
    print('Length of the dictionary:', len(word_count_dict))
    pretty_print(word_count_dict)


if __name__ == "__main__":
    main()


