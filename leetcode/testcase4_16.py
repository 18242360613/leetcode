import collections

def count_words(s):
    lst = collections.Counter(s.split()).most_common()
    lst.sort(key=lambda t: (-t[1], t[0]))
    return lst

print(count_words("betty bought a bit of butter but the butter was bitter"))