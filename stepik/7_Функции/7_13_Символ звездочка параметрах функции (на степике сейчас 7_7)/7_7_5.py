words = input().split()


def are_anagrams(s1, s2, *, start=0, end=-1, ignore_case=True):
    if end == -1:
        part1 = s1[start:]
        part2 = s2[start:]
    else:
        part1 = s1[start:end]
        part2 = s2[start:end]

    if ignore_case:
        part1 = part1.lower()
        part2 = part2.lower()

    return sorted(part1) == sorted(part2)

result = are_anagrams(*words, ignore_case=False)