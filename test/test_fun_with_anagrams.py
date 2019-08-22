def funWithAnagrams(s):
    if not 1 <= len(s) <= 1000:
        return s
    ss = {}
    for w in sorted(s):
        srt = "".join(sorted(w))
        if not srt in ss:
            ss[srt] = w
    return sorted(ss.values())

def test_fwa_1():
    s = ["code", "aaagmnrs", "anagrams", "doce"]
    assert funWithAnagrams(s) == ["aaagmnrs", "code"]
