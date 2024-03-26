def count_vowels(s):
    return sum([1 for i in s if str(i).lower() in ["a", "e", "i", "o", "u"]])


print(count_vowels("hallo, mein name ist TObi"))