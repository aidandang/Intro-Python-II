# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
  def __init__(self, name, description):
    self.name = name
    self.description = description
  
  def __str__(self):
    output = "\n"
    output += f"{self.name}\n"
    output += f"{self.description}\n"
    output += "Exit to the: "
    output += " [North] " if hasattr(self, "n_to") else ""
    output += " [South] " if hasattr(self, "s_to") else ""

    return output