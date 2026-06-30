from typing import List

# Stores pet details and a list of tasks.
class Pet:
    def __init__(self, name: str, species: str):
        self.name: str = name
        self.species: str = species
        self.tasks: List[Task] = []
    
    def get_info(self) -> str:
        """Return a formatted string with the pet's name and species."""
        return f"{self.name} ({self.species})"

    def add_task(self, task: 'Task') -> None:
        """Add a task to the pet's task list."""
        self.tasks.append(task)

# Represents a single activity (description, time, frequency, priority, completion status).
class Task:
    def __init__(self, description: str, duration: int, frequency: str, priority: str, time: str = "00:00", completion_status: str = "pending"):
        self.description = description
        self.duration = duration
        self.frequency = frequency
        self.priority = priority
        self.time = time
        self.completion_status = completion_status
    
    def get_priority_level(self) -> int:
        """Return the numeric priority level (1=low, 2=medium, 3=high)."""
        priority_map = {"low": 1, "medium": 2, "high": 3}
        return priority_map.get(self.priority.lower(), 0)
    
    def get_info(self) -> str:
        """Return a formatted string with the task's details."""
        return f"{self.time} - {self.description} ({self.duration} mins) [{self.priority}], {self.completion_status}"
    
    def mark_complete(self):
        """Mark the task as complete."""
        self.completion_status = "complete"

# The "Brain" that retrieves, organizes, and manages tasks across pets.
class Scheduler:
    def __init__(self, pets: List['Pet']):
        self.pets = pets
        self.tasks: List[Task] = []

    def retrieve_all_tasks(self) -> List[Task]:
        """Retrieve and aggregate all tasks from all pets."""
        self.tasks.clear()
        for pet in self.pets:
            self.tasks.extend(pet.tasks)

    def get_tasks_by_priority(self) -> List[Task]:
        """Return tasks sorted by priority in descending order (highest first)."""
        return sorted(self.tasks, key=lambda task: task.get_priority_level(), reverse=True)

# Owner: Manages multiple pets and provides access to all their tasks.
class Owner:
    def __init__(self, name: str):
        self.name: str = name
        self.pets: List[Pet] = []
        self.scheduler: Scheduler = None
    
    def add_pet(self, pet: Pet) -> None:
        """Add a pet to the owner's pet list."""
        self.pets.append(pet)
    
    def create_schedule(self) -> Scheduler:
        """Create and return a scheduler for managing the owner's pets' tasks."""
        self.scheduler = Scheduler(self.pets)
        return self.scheduler