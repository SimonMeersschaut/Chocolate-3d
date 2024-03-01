from .commands import Command


class Settings(list):
  '''A list of settings to be applied to the printer'''
  # def __init__(self, *args):
  #   self.settings = args
  ...
  


class FastAcceleration(Command):
  def __str__(self):
    return f'M201 X1000 Y1000 Z100 E2000'
