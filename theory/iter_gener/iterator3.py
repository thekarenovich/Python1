# Реализация собственного интератора

class StringByLetter:

  def __init__(self, string):
    self.string = string
    self.str_len = len(string)
    self.position = 0

  def __next__(self):
    if self.position < self.str_len:
      letter = self.string[self.position]
      self.position += 1
      return letter.upper()
    raise StopIteration 

  def __iter__(self):
    return self

for letter in StringByLetter("hello"):
  print(letter)
