def find_anagrams(word, dictionary):
    sorted_word = sorted(word)

    anagrams = [w for w in dictionary if sorted(w) == sorted_word]

    return anagrams

# Example usage:
word_to_find = "listen"
word_dictionary = ["enlist", "silent", "tinsel", "not", "this", "is", "a", "test"]

result = find_anagrams(word_to_find, word_dictionary)
print(f"Anagrams of '{word_to_find}': {result}")
