def caesar(text, shift, direction):
  message = ""

  if direction == "decode":
    shift *= -1
  for char in text:
    if char.isalpha():
      if char.isupper():
        shift_start = 65
      else:
        shift_start = 97
      shifted_char = chr((ord(char)-shift_start + shift) % 26 + shift_start)
      message += shifted_char
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
  
  caesar(text, shift, direction)

  print("Would you like to restart the cipher program?")
  restart = input("Type 'yes' to restart, type 'no' to quit.\n")
  print("\n**********************************\n")
  if restart == "yes":
    yes = True
  else:
    yes = False

print("Goodbye.")
