# 🎮 DAY 15 — MINI PROJECT

# Game Character Management System

## 📌 Project Overview

Create a simple **Game Character Management System** using Python OOP.

The program will allow the user to create different types of game characters such as:

- Warrior ⚔️
- Mage 🔥
- Archer 🏹

Each character will have common properties, but every character will have a different attack style.

This project is designed to practice advanced Python OOP concepts.

---

# 🎯 Project Objective

Build a Python program that demonstrates how OOP can be used to create different types of game characters.

The program should allow users to:

- Create characters
- Display character information
- Attack
- Heal
- Level up
- Update health
- Demonstrate different attack behaviors

---

# 🧠 OOP Concepts Required

This project must use:

```text
Class & Object
        ↓
Constructor
        ↓
Inheritance
        ↓
Method Overriding
        ↓
Polymorphism
        ↓
Encapsulation
        ↓
Getter & Setter
```

---

# 🧱 Base Class — Character

Create a class named:

```text
Character
```

It should contain:

```text
name
health
level
attack_power
```

Example:

```python
class Character:

    def __init__(self, name, health, level, attack_power):
        self.name = name
        self.__health = health
        self.level = level
        self.attack_power = attack_power
```

---

# ⚔️ Character Methods

The `Character` class should contain the following methods:

```text
display_stats()
attack()
heal()
level_up()
get_health()
set_health()
```

---

# 🔐 Encapsulation

Health should be stored as a private-style attribute.

Example:

```python
self.__health
```

Create a getter:

```text
get_health()
```

and a setter:

```text
set_health()
```

The setter should make sure health does not become negative.

---

# ⚔️ Warrior Class

Create a class:

```text
Warrior
```

It should inherit from:

```text
Character
```

The Warrior should override the:

```text
attack()
```

method.

Example attack:

```text
⚔️ Warrior attacks with a powerful sword!
```

---

# 🔥 Mage Class

Create a class:

```text
Mage
```

It should inherit from:

```text
Character
```

The Mage should override:

```text
attack()
```

Example:

```text
🔥 Mage attacks using a powerful fire spell!
```

---

# 🏹 Archer Class

Create a class:

```text
Archer
```

It should inherit from:

```text
Character
```

The Archer should override:

```text
attack()
```

Example:

```text
🏹 Archer attacks using a powerful arrow!
```

---

# 🔄 Polymorphism

Create objects of:

```text
Warrior
Mage
Archer
```

Then call the same:

```text
attack()
```

method on each object.

Each object should produce different output.

Example:

```text
Warrior → Sword Attack
Mage    → Fire Attack
Archer  → Arrow Attack
```

This demonstrates **polymorphism**.

---

# ❤️ Heal Feature

Create a method:

```text
heal()
```

The method should increase the character's health.

Example:

```text
Amir used Heal!
Health increased to 100.
```

Health should not exceed the maximum health limit.

---

# ⬆️ Level Up Feature

Create a method:

```text
level_up()
```

When the character levels up:

```text
Level + 1
Attack Power + 10
```

Example:

```text
Amir leveled up!

New Level: 6
Attack Power: 60
```

---

# 📊 Display Stats

Create a method:

```text
display_stats()
```

It should display:

```text
================================
        CHARACTER STATS
================================

Name          : Amir
Character     : Warrior
Health        : 100
Level         : 5
Attack Power  : 50

================================
```

---

# 🎮 Sample Output

```text
========================================
       GAME CHARACTER MANAGEMENT
========================================

1. Create Warrior
2. Create Mage
3. Create Archer
4. Display Stats
5. Attack
6. Heal
7. Level Up
8. Exit

Enter your choice: 1

Enter Character Name: Amir
Enter Health: 100
Enter Level: 5
Enter Attack Power: 50

Warrior created successfully! ⚔️
```

---

# ⚔️ Attack Example

```text
Enter your choice: 5

⚔️ Amir attacks with a powerful sword!

Damage: 50
```

---

# 🔥 Mage Example

```text
🔥 Alex attacks using a powerful fire spell!

Damage: 60
```

---

# 🏹 Archer Example

```text
🏹 Rahul attacks using a powerful arrow!

Damage: 55
```

---

# ❤️ Heal Example

```text
Enter your choice: 6

❤️ Amir used Heal!

Health increased to 100.
```

---

# ⬆️ Level Up Example

```text
Enter your choice: 7

🎉 Level Up!

Character : Amir
Old Level : 5
New Level : 6

Attack Power increased!
```

---

# ⭐ BONUS FEATURES

After completing the basic project, add these features:

## 1. Battle Mode

Allow two characters to fight.

```text
Warrior ⚔️
   VS
Mage 🔥
```

---

## 2. Damage System

Each attack should reduce the opponent's health.

Example:

```text
Warrior attacks Mage!

Mage Health:
100 → 50
```

---

## 3. Character Selection

Allow the user to select:

```text
1. Warrior
2. Mage
3. Archer
```

---

## 4. Critical Attack

Add a small chance of critical damage.

Example:

```text
🔥 CRITICAL ATTACK!

Damage: 100
```

---

## 5. Game Over

If health reaches zero:

```text
💀 Character defeated!

Game Over!
```

---

# 📂 Recommended Project Structure

```text
Day15/
│
├── project.md
│
└── mini_project/
    │
    └── game_character.py
```

---

# 🧪 Development Steps

Follow these steps:

### Step 1

Create the `Character` class.

### Step 2

Add constructor.

### Step 3

Add health encapsulation.

### Step 4

Create getter and setter.

### Step 5

Create `Warrior`.

### Step 6

Create `Mage`.

### Step 7

Create `Archer`.

### Step 8

Override the `attack()` method.

### Step 9

Add polymorphism.

### Step 10

Add heal and level-up features.

### Step 11

Create a menu system.

### Step 12

Test the complete program.

---

# 🎯 Project Requirements

Your final program should contain:

- [ ] Character class
- [ ] Warrior class
- [ ] Mage class
- [ ] Archer class
- [ ] Constructor
- [ ] Inheritance
- [ ] Method overriding
- [ ] Polymorphism
- [ ] Encapsulation
- [ ] Getter
- [ ] Setter
- [ ] Attack system
- [ ] Heal system
- [ ] Level-up system
- [ ] Display stats
- [ ] Menu system

---

# 🚀 Learning Goal

By completing this project, I will understand how multiple OOP concepts can work together inside one real-world style application.

The main concept flow is:

```text
Character
    ↓
Inheritance
    ↓
Warrior / Mage / Archer
    ↓
Method Overriding
    ↓
Polymorphism
    ↓
Encapsulation
    ↓
Game System
```

---

# 🏆 Project Difficulty

```text
Difficulty: ⭐⭐⭐⭐
```

### Concepts:

```text
Python OOP
Inheritance
Polymorphism
Encapsulation
Method Overriding
```

---

# 📈 DAY 15 PROJECT STATUS

```text
Project: Game Character Management System

Planning       ✅
Requirements   ✅
OOP Concepts   ✅

Coding         ⬜
Testing        ⬜
GitHub Push    ⬜
```

---

# 🔥 FINAL CHALLENGE

Try to build the complete project **without copying a ready-made solution**.

First create the basic version.

Then add:

```text
⚔️ Battle Mode
❤️ Healing
⬆️ Level Up
🔥 Critical Attack
💀 Game Over
```

## 🚀 Build → Test → Improve → Push to GitHub

**Day 15 / 365 — Project Challenge**