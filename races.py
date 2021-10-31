from enum import Enum

class Races(Enum):
  dragonborn = "Dragonborn"
  dwarf = "Dwarf"
  elf = "Elf"
  gnome = "Gnome"
  half_elf = "Half-Elf"
  half_orc = "Half-Orc"
  halfling = "Halfling"
  human = "Human"
  tiefling = "Tiefling"

race_list = [x.value for x in Races]