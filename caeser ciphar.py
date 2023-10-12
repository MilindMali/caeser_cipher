alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caeser(start_text,shift_amount,direction):
  end_text = ''
  
  for letter in start_text:
    if letter in alphabet:
      position=alphabet.index(letter)
      if direction == 'encode':
        new_position=position+shift_amount
      elif direction == 'decode':
        new_position = position-shift_amount
      new_letter=alphabet[new_position]
      end_text+=new_letter
    else:
      end_text+=letter
  
  print(end_text)

should_continue=True
while should_continue:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  
  shift=shift%26
  # organized code
  caeser(start_text=text, shift_amount=shift, direction=direction)

  result=input("Type 'yes' if you want to go again or 'No'")
  if result=='No':
    should_continue=False
    print('Good Bye')
