from art import logo


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'] #'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

text = input("Select whether you want to encrypt or decrypt\n 1 --> Encode \n 2 --> Decode \n")
message = input("Enter a message\n")
shift = input("Shift the text by Number \n")

if text == "2":
  shift = int(shift) * -1

res = ''
for c in message:
    if c.isalpha():
      new_ord = ord(c) + int(shift) 
      if new_ord > ord('z'):    # Encode
        new_ord = (new_ord - ord('a')) % 26 + ord('a')
      
      if new_ord < ord('a'):    #Decode
        new_ord = (new_ord - ord('a')) % 26 + ord('a')
        
      res += chr(new_ord)
    if c == " ":
       res += c
print(res)