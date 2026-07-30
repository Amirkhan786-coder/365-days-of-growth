# REVERSE WORDS 

text = input("Enter a sentence: ")

words = text.split()

words.reverse()

print("Reversed Words:")

print(" ".join(words))