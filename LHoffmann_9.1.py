# Course: DSC510
# Assignment: 8.1
# Date: 4/27/2020
# Name: Laura Hoffmann
# Description: Program to write new text files

# Generate a text file for the output of the dictionary from the gba_file
# Add a function (process_file) similar to pretty_print
    # This function prompts user for name of new file and then commands to write the dictionary to the new file
    # instead of to the screen in addition to formatting the dictionary

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


def process_file(word_count_dict):
    # User input for the file name
    file = input('What would you like the new file to be called?: ')
    # Create a file to be written from scratch with the user input as the name
    with open(file, 'w') as file:
        wordcount = 'Your total word count is: ' + str(len(word_count_dict))
        # Since file.write can only take one argument I made it into a variable
        file.write(wordcount)
        file.write('\n' * 2)
        # Formatting from pretty_print function
        value_key_list = []
        for key, val in word_count_dict.items():
            value_key_list.append((val, key))
        value_key_list.sort(reverse=True)
        file.write('{:11s}{:11s}'.format("Word", "Count"))
        file.write('\n' * 2)
        for val, key in value_key_list:
            file.write('{:12s} {:<3d}'.format(key, val, ))
            file.write('\n')


def main():
    word_count_dict = {}
    try:
        with open('gettysburg.txt', 'r') as gba_file:
            for line in gba_file:
                process_line(line, word_count_dict)
        process_file(word_count_dict)
    except FileNotFoundError as e:
        print(e)


if __name__ == "__main__":
    main()
