import re
import collections


def mostCommon(paragraph, banned):
    words = [word for word in re.sub(r'[^\w]', ' ', paragraph)
             .lower().split()
             if word not in banned]

    counts = collections.Counter(words)
    print(counts)
    return counts.most_common(1)[0][0]


if __name__ == "__main__":
    paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
    banned = ["hit"]
    print(mostCommon(paragraph, banned))
