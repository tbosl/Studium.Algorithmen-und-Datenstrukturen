def remove_punctuation(s):
    seq = [c for c in s if c not in [".", ",", "´", "`", "'", ":", ";", "?", "!"]]
    return ''.join(seq)


print(remove_punctuation("Let's try, Mike."))
