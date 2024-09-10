#!/usr/bin/env python3

class MyString:
  def __init__(self, value = ''):
    if not isinstance(value, str):
      print("The value must be a string")
    else:
      self.value = value
  
  @property
  def value(self):
      return self._value

  @value.setter
  def value(self, value):
      if not isinstance(value, str):
        print("The value must be a string.")
      else:
        self._value  = value

  def is_sentence(self):
    if self._value.endswith('.'): 
      return True
    else:
      return False
  
  def is_question(self):
    if self._value.endswith('?'): 
      return True
    else:
      return False

  def is_exclamation(self):
    if self._value.endswith('!'): 
      return True
    else:
      return False

  def count_sentences(self):
    sentence_count = 0
    previous_char = None
    for character in self._value:
        if character in '.!?':
            if previous_char != character:
                sentence_count += 1
        previous_char = character
    return sentence_count