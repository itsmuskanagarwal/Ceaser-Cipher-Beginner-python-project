import art
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
    shift_amount *= -1
  for char in start_text:
    if char in alphabet:    
      position = alphabet.index(char)
      new_position = position + shift_amount
      end_text += alphabet[new_position]
    else:
      end_text += alphabet[new_position]
  print(f"Here's the {cipher_direction}d result: {end_text}")

#print ASCII art
print(art.logo)

#if you want to continue the process
flag=1
while(flag==1):
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  
  #if shift is a large no
  shift = shift % 26
  caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
  result = input("Do you want to continue? 'Y'/'N'")
  if result == 'Y':
    flag==1
  if result == 'N':
    flag==0