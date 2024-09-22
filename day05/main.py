import random


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= (input("How many letters would you like in your password?\n"))
nr_symbols = (input(f"How many symbols would you like?\n"))
nr_numbers = (input(f"How many numbers would you like?\n"))

password = []

def generator(number, vals):
  p = []
  for _ in range(int(number)):
    val = random.randint(0,len(vals) - 1)
    char = vals[val]
    if random.randint(0,1) and char.isalpha():
      char.upper()
    p.append(char)
  return p

password += generator(nr_letters, letters)
password += generator(nr_numbers, numbers)
password += generator(nr_symbols, symbols)

random.shuffle(password)

# Join the shuffled list into a string
random_string = ''.join(password)
print(random_string)


  
