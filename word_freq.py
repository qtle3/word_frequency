""" A program to count frequencies of all words in a file. """


def byFreq(pair):
    """A function that returns the second item of a pair."""
    return pair[1]


def main():
    """The main function."""
    filename = input("Give the name of the file: ").strip()
    try:
        with open(filename, "r") as infile:
            text = infile.read()  # read the entire file in a string
    except FileNotFoundError:
        print(f"File not found for  '{filename}'")
        return
    except OSError as e:
        print(f"Error reading file '{filename}': {e}")
        return
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
    for w in uniqueWords:
        print(w, counts[w])


main()
