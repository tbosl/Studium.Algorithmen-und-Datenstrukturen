def count_duplicates(text):
    words = text.replace('.', '').replace(',', '').split(' ')
    counters = {}
    for word in words:
        word = word.lower()
        if word in counters:
            counters[word] += 1
        else:
            counters[word] = 1
    return counters


print(count_duplicates(
    "The quick brown fox jumps over the lazy dog. "
    "The lazy dog then jumps over the sleeping cat. "
    "The cat wakes up and chases the fox. "
    "The fox escapes and runs into the forest. "
    "In the forest, it finds berries and eats them. "
    "After eating, the fox rests under a tree. "
    "The tree provides shade from the hot sun. "
    "Suddenly, it starts raining. The fox looks for shelter. "
    "It finds a cave and hides inside. "
    "Inside the cave, it discovers a family of bats. "
    "The bats are sleeping peacefully. "
    "The fox decides to wait out the rain with the bats."))
