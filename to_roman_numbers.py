""" ROMAN NUMBERS """

numbers_dict = {
  "I": 1, 
  "V": 5,
  "X": 10, 
  "L": 50, 
  "C": 100
}

def convert(roman_numbers: str):
  last = ""
  final_number = 0
  for number in roman_numbers:
    if last == "":
      final_number += numbers_dict[number]
      last = number
    else :
      number_before = numbers_dict[last]
      current_number = numbers_dict[number]
      if number_before < current_number:
        final_number += current_number - number_before * 2
        last = number
      else :
        final_number += current_number
        last = number
  print("number is", final_number)
  return final_number

convert("XII")