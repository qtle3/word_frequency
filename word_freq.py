import os

# script to count the frequency of words in a text file


# function to sort by frequency
def byFreq(pair):
    return pair[1]


# main function
def main():

    folder_path = (
        "C:/Users/Q/Documents/Important Stuff/Python Work/Projects/word_counter"
    )
    filename = input("Give the name of the file: ").strip()
    file_path = os.path.join(folder_path, filename)
    try:
        with open(filename, "r") as infile:
            text = infile.read()  # read the entire file in a string
    except FileNotFoundError:
        print(f"File not found for  '{filename}'")
        return
    except OSError as e:
        print(f"Error reading file '{filename}': {e}")
        return

    # remove punctuation characters from the text
    for ch in "!'\"#$%&()*+,-./:;<=>?@[\\]^_`{|}~":
        # loop through all these characters, replacing each by space
        # Note: charcters " and ' are included with a \ before them
        text = text.replace(ch, " ")

    words = text.split()  # get words (tokens separated by whitespaces)
    counts = {}  # dictionary for frequency counts
    for w in words:
        counts[w] = counts.get(w, 0) + 1  # increment counts

    # get list of words that appear in document
    uniqueWords = list(counts.items())

    # sort the list by frequency
    uniqueWords.sort(key=byFreq, reverse=True)

    # print the words and their frequencies
    for w, freq in uniqueWords:
        print(w, freq)


main()
