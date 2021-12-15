class Band:
  def __init__(self, name, members=None):
      self.name = name
      self.members = members

  def __str__(self):
      return f"The band {self.name}"

  def __repr__(self):
      return f"Band instance. name={self.name}, members={self.members}"

  def play_solos(self):
    pass



class Musician:
  def __init__(self, name):
    self.name = name

  def get_instrument(self):
    return 'I got my instrument'

  def play_solo(self):
    return 'doodley doodley doodley doodley'



class Guitarist:
    pass

class Bassist:
    pass

class Drummer:
    pass




if __name__ == '__main__':
  print('Hello Cleavland!')


