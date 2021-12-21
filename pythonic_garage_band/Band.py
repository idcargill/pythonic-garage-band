class Band:
  instances = []

  def __init__(self, name, members=[]):
      self.name = name
      self.members = members
      Band.instances.append(self.name)
      
  def __str__(self):
      return f"The band {self.name}"

  def __repr__(self):
      return f"Band instance. name={self.name}, members={self.members}"

  def play_solos(self):
    solos = []
    for player in self.members:
      solos.append(player.play_solo())
    return solos

  def add_band_member(self, musician):
    self.members.append(musician)

  @staticmethod
  def to_list():
    return Band.instances



class Musician:
  def __init__(self, name):
    self.name = name

  def get_instrument(self):
    return f'{self.instrument}'

  def play_solo(self):
    return f'{self.solo}'
      
  def __str__(self):
    return f'My name is {self.name} and I play {self.instrument}'

  def __repr__(self):
    return f'{self.__class__.__name__} instance. Name = {self.name}'


class Guitarist(Musician):
  def __init__(self, name):
    super().__init__(name)
    self.instrument = 'guitar'
    self.solo = 'face melting guitar solo'

class Bassist(Musician):
    def __init__(self, name):
      super().__init__(name)
      self.instrument = 'bass'
      self.solo = 'bom bom buh bom'

class Drummer(Musician):
    def __init__(self, name):
      super().__init__(name)
      self.instrument = 'drums'
      self.solo = 'rattle boom crash'


def from_file(file_path):
  with open(file_path) as f:
    bands = json.loads(f.read())
    print(bands)

