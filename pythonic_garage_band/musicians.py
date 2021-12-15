class Band:
  def __init__(self, band_name):
    self.band_name = band_name
    self.members = []  # list of musician instances

  def play_solos(self):
    pass


  def __str__(self):
    return f'Band_Name = {self.name}' 

  def __repr__(self):
    rep = f'Band(self.band_name'
    return rep


class Musicion:
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