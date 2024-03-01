import serial
import time

class Printer:
  def __init__(self):
    self.open_port()
  
  def open_port(self):
    for i in range(1,7):
      try:
        self.ser = serial.Serial(f'COM{i}', 115200, timeout=1)
        print(f'Connected to port: COM{i}.')
        time.sleep(1)
        return
      except serial.serialutil.SerialException:
        pass
    raise Exception('No port opened.')
  
  def send_command(self, command, expected_response='ok'):
    """Send command to serial bus and wait for execution."""
    # send command
    self.ser.write((command + '\n').encode())
    self.ser.flush()
    # wait for response
    while True:
      response = self.ser.readline().decode().strip()
      if response == expected_response:
          break
      elif response.startswith('Error'):
          print(f"Error: {response}")
          break
  
  def execute(self, command: object) -> None:
    """Execute a command.
    :param command: A Command-object with a __str__ property."""
    print(command.__str__())
    return self.send_command(command.__str__())
  
  def initialize(self, settings: list) -> None:
    """Initialize the printer using a list of settings."""
    for command in settings:
      self.execute(command)
  


if __name__ == '__main__':
  Ser()