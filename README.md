# Caesar Cipher
This project contains a Python two implementations of the classic Caesar cipher encryption algorithm.

## What is a Caesar Cipher?
The Caesar cipher is one of the simplest and most widely known encryption techniques. Named after Julius Caesar, it is a type of substitution cipher in which each letter in the plaintext is shifted a certain number of places down or up the alphabet. For example, with a shift of 3, A would be replaced by D, B would become E, and so on.

## Features
- **Encryption**: Encrypts plaintext by shifting letters by a specified number of positions. 
- **Decryption**: Decrypts ciphertext by reversing the shift applied during encryption
- **Configurable Shift**: Allows the user to specify the shift value for encryption and decryption.

## Project Structure
- `original`: Contains the original implementation of the Caesar cipher.
- `optimized`: Contains the optimized implementation of the Caesar cipher.

### Original Implementation
The original implementation uses a list of alphabet characters to shift the letters.
```
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
```

### Optimized Implementation
The optimized implementation uses ASCII values for character manipulation, which simplifies the shifting process and makes the code more efficient.
```
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
```
