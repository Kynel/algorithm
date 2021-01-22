import collections


def groupAnagram(input):
    anagrams = collections.defaultdict(list)

    for word in input:
        anagrams[''.join(sorted(word))].append(word)

    print(list(anagrams.values()))


if __name__ == "__main__":
    input = ["eat", "tea", "tan", "ate", "nat", "bat"]
    groupAnagram(input)
