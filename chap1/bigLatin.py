from collections import defaultdict
import pprint


def make_big_latin(word):
    """Make word latinized

    Args:
        word (Str): [description]

    Returns:
        Str: latinized word
    """
    latin = ""
    if word[0] in ['a', 'i', ' u', 'e', 'o']:
        latin = word + "way"
    else:
        latin = word[1:] + word[0] + "ay"
    return latin.capitalize() if word.istitle() else latin


def bar_graph(text):
    d = defaultdict(list)
    text = text.replace(' ', '')
    for character in text:
        print(character)
        d[character].append(character)
    pprint.pprint(d)
    sortedDict = sorted(d.items(), key=lambda x: len(x[1]))
    pprint.pprint(sortedDict)


def main():
    word = input('Input a word.\n')
    # print(make_big_latin(word))
    bar_graph(word)

    print((lambda x1, x2: x1**2+x2**2)(5, 3))


if __name__ == '__main__':
    main()
