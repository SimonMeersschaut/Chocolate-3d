import ender


class Callibration(ender.Printer):
  def __init__(self, plate_size: int = 220):
    self.plate_size = plate_size
    super().__init__()
  
  def start(self):
    """Callibrate the printer, relative to the base plate."""
    # First home the x and y axis
    self.execute(ender.commands.Home(True, True, False))
    # Now callibrate four points
    self.get_point(0, 0)
    self.get_point(self.plate_size, 0)
    self.get_point(0, self.plate_size)
    self.get_point(self.plate_size, self.plate_size)
  
  def get_point(self, x: int, y: int, z_margin: int=20) -> int:
    """ Returns the z-position of the base plate, using user input.
    :param x: the x position of the point on the base plate
    :param y: the y position of the point on the base plate
    """
    self.execute(ender.commands.Move(x, y, z_margin))


def main():
  callibration = Callibration()
  input('[Enter] to start callibration')
  callibration.start()
  
if __name__ == '__main__':
  main()