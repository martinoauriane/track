alphabet_dict = {
  "A": 1, 
  "B": 2, 
  "C": 3, 
  "D": 4, 
  "E": 5, 
  "F": 6, 
  "G": 7, 
  "H": 8, 
  "I": 9, 
  "J": 10, 
  "K": 11, 
  "L": 12, 
  "M": 13, 
  "N": 14, 
  "O": 15, 
  "P": 16, 
  "Q": 17, 
  "R": 18, 
  "S": 19, 
  "T": 20, 
  "U": 21, 
  "V": 22, 
  "W": 23,   
  "X": 24, 
  "Y": 25, 
  "Z": 26, 
  }

def decaler(letter: str, decalage_value):
  letter = letter.upper()
  initial_position = alphabet_dict[letter]
  new_position = initial_position + decalage_value

  if new_position > 26:
    rest = new_position - 26
    for key, value in alphabet_dict.items():
      if value == rest:
        new_letter =  key
        return new_letter
  else : 
    for key, value in alphabet_dict.items():
      if value == new_position:
        new_letter = key
        return new_letter

def exec(message, decalage_value):
  ## make sure that the message is to upper strings
  message = message.upper()
  decalage_value= int(decalage_value)
  answer = []
  for i in range(len(message)):
    new_letter = message[i]
    if new_letter in [",", "!", ".", "?", " ", "'"]:
      answer.append(new_letter)
      continue
    response = decaler(new_letter, decalage_value)
    answer.append(response)
  print(''.join(answer))
  return ''.join(answer)

exec("Cesar, c'est moi", 9)