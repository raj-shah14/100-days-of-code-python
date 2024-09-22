import random
from hangman_words import word_list
from hangman_art import stages, logo2, logo3

print(logo3)
chosen_word = word_list[random.randint(0, len(word_list))]

def find_all_indexes(input_string, char):
    return [index for index, current_char in enumerate(input_string) if current_char == char]

lives = len(stages) - 1
word = ["__"] * len(chosen_word)
print(stages[lives])

while lives >= 0:
  print(" ".join(word))
  
  char = input("Give the input letter\n")
  if char not in chosen_word:
      lives -= 1
      print(stages[lives])
  else:
    idx = find_all_indexes(chosen_word, char)
    for i in idx:
      word[i] = char

  if ''.join(word) == chosen_word:
    print("You Win")
    print(logo2)
    lives = len(stages) - 1
    chosen_word = word_list[random.randint(0, len(word_list))]
    word = ["__"] * len(chosen_word)

print(chosen_word)
print("You lose")
    
