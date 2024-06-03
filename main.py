alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(text, shift, direction):
  message = ""

  if direction == "decode":
    shift *= -1
  for char in text:
    if char in alphabet:
      message += alphabet[alphabet.index(char) + shift]
    else:
      message += char
    
  print(f"The {direction}d message is {message}\n")


import art
print (art.logo) 

yes = True

while yes:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))

  while shift > 26:
    shift %= 26
  caesar(text, shift, direction)

  print("Would you like to restart the cipher program?")
  restart = input("Type 'yes' to restart, type 'no' to quit.\n")
  print("\n**********************************\n")
  if restart == "yes":
    yes = True
  else:
    yes = False

print("Goodbye.")
