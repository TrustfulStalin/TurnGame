
# Base Character class
class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.max_health = health  # Store the original health for maximum limit

    def attack(self, opponent):
        opponent.health -= self.attack_power
        print(f"{self.name} attacks {opponent.name} for {self.attack_power} damage!")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")

    def display_stats(self):
        print(f"{self.name}'s Stats - Health: {self.health}/{self.max_health}, Attack Power: {self.attack_power}")

    # Heal method to restore health based on character type
    def heal(self):
        if isinstance(self, Warrior): 
            health_amount = 5
            self.health = min(self.health + health_amount, self.max_health)  # Prevent exceeding max health
            print(f"Your Warrior has been healed for {health_amount} points. Your health is now {self.health}.")
        elif isinstance(self, Mage):
            health_amount = 25
            self.health = min(self.health + health_amount, self.max_health)
            print(f"Your Mage has been healed for {health_amount} points. Your health is now {self.health}.")
        elif isinstance(self, Archer):
            health_amount = 10
            self.health = min(self.health + health_amount, self.max_health)
            print(f"Your Archer has been healed for {health_amount} points. Your health is now {self.health}.")
        elif isinstance(self, Paladin):
            health_amount = 15
            self.health = min(self.health + health_amount, self.max_health)
            print(f"Your Paladin has been healed for {health_amount} points. Your health is now {self.health}.")

    # Upgrade method to increase attack power for any character
    def upgrade(self):
        powerup = 1.5  # Upgrade factor
        self.attack_power *= powerup  # Increase attack power by factor of 1.5
        print(f"{self.name}'s attack power has been increased to {self.attack_power:.2f}!")

    # Special method for each class
    def special(self, opponent):
        pass  # This will be overridden by each specific character class

# Warrior class (inherits from Character)
class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=140, attack_power=25)

    def special(self, opponent):
        Sb = 35
        opponent.health -= Sb
        print(f"{self.name} casts 'Savage Blows'!")
        print(f"Wizard takes {Sb} damage. Wizard's remaining health: {opponent.health}")

# Mage class (inherits from Character)
class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=75, attack_power=35)

    def special(self, opponent):
        blizz = 50
        opponent.health -= blizz
        print(f"{self.name} casts 'Blizzard' and freezes the wizard!")
        print(f"Wizard takes {blizz} damage. Wizard's remaining health: {opponent.health}")

# Archer class (inherits from Character)
class Archer(Character):
    def __init__(self, name):
        super().__init__(name, health=85, attack_power=45)

    def special(self, opponent):
        KS = 55
        opponent.health -= KS
        print(f"{self.name} performs 'Kill Shot'!")
        print(f"Wizard takes {KS} damage. Wizard's remaining health: {opponent.health}")

# Paladin class (inherits from Character)
class Paladin(Character):
    def __init__(self, name):
        super().__init__(name, health=135, attack_power=50)

    def special(self, opponent):
        FL = 75
        opponent.health -= FL
        print(f"{self.name} casts 'Face the Light' and repels all evil forces!")
        print(f"Wizard takes {FL} damage. Wizard's remaining health: {opponent.health}")

# EvilWizard class (inherits from Character)
class EvilWizard(Character):
    def __init__(self, name):
        super().__init__(name, health=150, attack_power=15)  # Lower attack power
    
    # Evil Wizard's special ability: it can regenerate health
    def regenerate(self):
        self.health += 5  # Lower regeneration amount
        print(f"{self.name} regenerates 5 health! Current health: {self.health}")

# Function to create player character based on user input
def create_character():
    print("Choose your character class:")
    print("1. Warrior")
    print("2. Mage")
    print("3. Archer")
    print("4. Paladin")
    
    class_choice = input("Enter the number of your class choice: ")
    name = input("Enter your character's name: ")

    if class_choice == '1':
        return Warrior(name)
    elif class_choice == '2':
        return Mage(name)
    elif class_choice == '3':
        return Archer(name)
    elif class_choice == '4':
        return Paladin(name)
    else:
        print("Invalid choice. Defaulting to Warrior.")
        return Warrior(name)

# Battle function with user menu for actions
def battle(player, wizard):
    while wizard.health > 0 and player.health > 0:
        print("\n--- Your Turn ---")
        print("1. Attack")
        print("2. Use Special Ability")
        print("3. Heal")
        print("4. View Stats")
        print("5. Attack power upgrade")
        
        choice = input("Choose an action: ")

        if choice == '1':
            player.attack(wizard)
        elif choice == '2':
            player.special(wizard)  # Call the special method for any class
        elif choice == '3':
            player.heal()
        elif choice == '4':
            player.display_stats()
        elif choice == '5':
            player.upgrade()  # Upgrade works for all character types
        else:
            print("Invalid choice, try again.")
            continue

        # Evil Wizard's turn to attack and regenerate
        if wizard.health > 0:
            wizard.regenerate()
            wizard.attack(player)

        if player.health <= 0:
            print(f"{player.name} has been defeated!")
            break

    if wizard.health <= 0:
        print(f"The wizard {wizard.name} has been defeated by {player.name}!")

# Main function to handle the flow of the game
def main():
    # Character creation phase
    player = create_character()

    # Evil Wizard is created
    wizard = EvilWizard("The Dark Wizard")

    # Start the battle
    battle(player, wizard)

if __name__ == "__main__":
    main()