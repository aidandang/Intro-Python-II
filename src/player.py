# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
  def __init__(self, name, current_room):
    self.name = name
    self.current_room = current_room

  def __str__(self):
    output = "\n"
    output += f"{self.name}\n"
    output += "Now in: " 
    output += f"{self.current_room}"

    return output