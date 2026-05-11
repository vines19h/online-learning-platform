def pangrams(s):
    s = s.lower()
    letters = set()

    for ch in s:
        if 'a' <= ch <= 'z':
            letters.add(ch)

    return "pangram" if len(letters) == 26 else "not pangram"
