# ============================================================
# 🎮 DAY 15 MINI PROJECT
# Game Character Management System
# ============================================================
#
# Concepts Used:
# 1. Class & Object
# 2. Constructor
# 3. Inheritance
# 4. Method Overriding
# 5. Polymorphism
# 6. Encapsulation
# 7. Getter & Setter
# ============================================================


# ============================================================
# 🧱 BASE CLASS
# ============================================================

class Character:

    def __init__(self, name, health, level, attack_power):
        self.name = name
        self.__health = health
        self.level = level
        self.attack_power = attack_power
        self.max_health = health

    # --------------------------------------------------------
    # Display character information
    # --------------------------------------------------------

    def display_stats(self):

        print("\n================================")
        print("       CHARACTER STATS")
        print("================================")
        print("Name         :", self.name)
        print("Character    :", self.__class__.__name__)
        print("Health       :", self.__health)
        print("Level        :", self.level)
        print("Attack Power :", self.attack_power)
        print("================================")

    # --------------------------------------------------------
    # Basic attack
    # --------------------------------------------------------

    def attack(self):

        print(self.name, "performs a basic attack!")

    # --------------------------------------------------------
    # Getter
    # --------------------------------------------------------

    def get_health(self):

        return self.__health

    # --------------------------------------------------------
    # Setter
    # --------------------------------------------------------

    def set_health(self, health):

        if health < 0:
            self.__health = 0

        elif health > self.max_health:
            self.__health = self.max_health

        else:
            self.__health = health

    # --------------------------------------------------------
    # Heal character
    # --------------------------------------------------------

    def heal(self):

        old_health = self.__health

        self.set_health(self.__health + 20)

        print("\n❤️", self.name, "used Heal!")

        print("Health:", old_health, "→", self.__health)

    # --------------------------------------------------------
    # Level up
    # --------------------------------------------------------

    def level_up(self):

        self.level += 1
        self.attack_power += 10

        print("\n🎉 Level Up!")

        print("Character:", self.name)
        print("New Level:", self.level)
        print("Attack Power:", self.attack_power)


# ============================================================
# ⚔️ WARRIOR CLASS
# ============================================================

class Warrior(Character):

    # Method overriding

    def attack(self):

        print("\n⚔️", self.name, "attacks with a powerful sword!")

        print("Damage:", self.attack_power)


# ============================================================
# 🔥 MAGE CLASS
# ============================================================

class Mage(Character):

    # Method overriding

    def attack(self):

        print("\n🔥", self.name, "attacks using a powerful fire spell!")

        print("Damage:", self.attack_power)


# ============================================================
# 🏹 ARCHER CLASS
# ============================================================

class Archer(Character):

    # Method overriding

    def attack(self):

        print("\n🏹", self.name, "attacks using a powerful arrow!")

        print("Damage:", self.attack_power)


# ============================================================
# 🎮 CREATE CHARACTERS
# ============================================================

print("========================================")
print("     GAME CHARACTER MANAGEMENT")
print("========================================")

warrior = Warrior(
    "Amir",
    100,
    5,
    50
)

mage = Mage(
    "Alex",
    80,
    5,
    60
)

archer = Archer(
    "Rahul",
    90,
    5,
    55
)


# ============================================================
# 📊 DISPLAY ALL CHARACTER STATS
# ============================================================

print("\n\n========== ALL CHARACTERS ==========")

warrior.display_stats()

mage.display_stats()

archer.display_stats()


# ============================================================
# ⚔️ POLYMORPHISM
# ============================================================

print("\n\n========== POLYMORPHISM ==========")

characters = [
    warrior,
    mage,
    archer
]

for character in characters:

    character.attack()


# ============================================================
# ❤️ HEAL SYSTEM
# ============================================================

print("\n\n========== HEAL SYSTEM ==========")

warrior.set_health(60)

print("Before Heal:")
print("Health:", warrior.get_health())

warrior.heal()


# ============================================================
# ⬆️ LEVEL UP SYSTEM
# ============================================================

print("\n\n========== LEVEL UP SYSTEM ==========")

warrior.level_up()


# ============================================================
# 📊 UPDATED STATS
# ============================================================

print("\n\n========== UPDATED STATS ==========")

warrior.display_stats()


# ============================================================
# 🎯 FINAL MESSAGE
# ============================================================

print("\n========================================")
print("       GAME SYSTEM COMPLETED 🎮")
print("========================================")

print("\nOOP Concepts Demonstrated:")

print("✅ Class & Object")
print("✅ Constructor")
print("✅ Inheritance")
print("✅ Method Overriding")
print("✅ Polymorphism")
print("✅ Encapsulation")
print("✅ Getter")
print("✅ Setter")