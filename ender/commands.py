'''
All useful commands for the Creality Ender 3 v2
'''
from dataclasses import dataclass
from abc import ABC

@dataclass
class Command(ABC):
  '''Each command is represented as a Command-instance.'''

  def __str__(self) -> str:
    '''Return the G-code representative of this command.'''
    ...

@dataclass
class Move(Command):
  """Move the printer to an absolute position.
  :param x: x coordinate
  :param y: y coordinate
  :param z: z coordinate
  :param rapid: if true, the printer will move as quickly as possible
  """
  x: int = None
  y: int = None
  z: int = None
  rapid: bool = False
  
  def __str__(self) -> str:
    return f'G1 {f"X{self.x}" if self.x is not None else ""} {f"Y{self.y}" if self.y is not None  else ""} {f"Z{self.z}" if self.z is not None  else ""}'

@dataclass
class Home(Command):
  """Home the printer to its origin"""
  x: bool = True
  y: bool = True
  z: bool = True

  def __str__(self) -> str:
    return f'G28 {"X" if self.x else ""} {"Y" if self.y else ""} {"Z" if self.z else ""}'

@dataclass
class SetBedTemp(Command):
  temp: int = 0

  def __str__(self) -> str:
    return f'M140 S{self.temp}'

@dataclass
class ExtruderTemperature(Command):
  temp: int = 0

  def __str__(self) -> str:
    return f'M104 S{self.temp}'

class FanOff(Command):
  def __str__(self) -> str:
    return 'M107'