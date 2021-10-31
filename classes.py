from enum import Enum

class Classes(Enum):
  artificer = "Artificer"
  barbarian = "Barbarian"
  bard = "Bard"
  blood_hunter = "Blood Hunter"
  cleric = "Cleric"
  druid = "Druid"
  fighter = "Fighter"
  monk = "Monk"
  paladin = "Paladin"
  ranger = "Ranger"
  rogue = "Rogue"
  sorcerer = "Sorcerer"
  warlock = "Warlock"
  warrior = "Warrior"
  wizard = "Wizard"

class_list = [x.value for x in Classes]