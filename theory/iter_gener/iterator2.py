# Реализация собственного интератора

class InfiniteSquaring:

  def __init__(self, initial_number):
    self.number_to_square = initial_number

  def __next__(self):
    self.number_to_square = self.number_to_square**2
    return self.number_to_square

  def __iter__(self):
    return self

squaring_of_six = InfiniteSquaring(6)
print(next(squaring_of_six)) # 36
