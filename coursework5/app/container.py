from coursework5.app.classes.arena import Arena
from coursework5.app.classes.equipment import Equipment
from coursework5.app.classes.heroes import BaseUnit, unit_classes

arena = Arena()  # Создаём экземпляр  класса арены

# Словарь игроков
heroes = {
    "player": BaseUnit,
    "enemy": BaseUnit
}

# Создаём экземляр экипировки
equipment = Equipment()
# Получаем список оружия
weapons = equipment.get_weapons_names()
# Получаем список брони
armors = equipment.get_armors_names()

# Форма создания персонажей
forms_create_units = {
    "classes": unit_classes,
    "weapons": weapons,
    "armors": armors
}
