class VacuumAgent:
    def __init__(self, initial_location='A'):
        self.location = initial_location

    def move(self):
        """Switches the agent's location between room A and room B."""
        self.location = 'B' if self.location == 'A' else 'A'

    def perceive_and_act(self, environment):
        """
        Executes rule-based logic:
        Rule 1: If the current room is dirty, clean it.
        Rule 2: If the current room is clean, move to the other room.
        """
        current_status = environment[self.location]
        
        if is_dirty(environment, self.location):
            clean_room(environment, self.location)
            print(f"Room {self.location} has been cleaned.")
        else:
            other_room = 'B' if self.location == 'A' else 'A'
            print(f"Moving to room {other_room}")
            self.move()


def is_dirty(environment, room):
    """Checks if a given room is dirty."""
    return environment[room].strip().capitalize() == 'Dirty'


def clean_room(environment, room):
    """Cleans a given room in the environment."""
    environment[room] = 'Clean'


def main():
    # Task 1: Set Up the Environment
    room_a = input("Is room A Dirty or Clean? ").strip().capitalize()
    room_b = input("Is room B Dirty or Clean? ").strip().capitalize()

    environment = {
        'A': room_a,
        'B': room_b
    }

    # Task 2 & 3: Initialize Agent and Run Simulation
    agent = VacuumAgent(initial_location='A')

    steps = int(input("\nHow many steps should the agent run? "))
    print()

    for step in range(1, steps + 1):
        print(f"Step {step}: Agent is in room {agent.location}")
        agent.perceive_and_act(environment)
        print(f"Environment state: {environment}\n")


if __name__ == "__main__":
    main()
