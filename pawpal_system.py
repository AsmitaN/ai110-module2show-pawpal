from typing import List

# Stores pet details and a list of tasks.
class Pet:
    def __init__(self, name: str, species: str):
        self.name: str = name
        self.species: str = species
        self.tasks: List[Task] = []
    
    def get_info(self) -> str:
        return f"{self.name} ({self.species})"

    def add_task(self, task: 'Task') -> None:
        self.tasks.append(task)

# Represents a single activity (description, time, frequency, priority, completion status).
class Task:
    def __init__(self, description: str, time: str, duration: int, frequency: str, priority: str, completion_status: str = "pending"):
        self.description = description
        self.time = time
        self.duration = duration
        self.frequency = frequency
        self.priority = priority
        self.completion_status = completion_status
    
    def get_priority_level(self) -> int:
        priority_map = {"low": 1, "medium": 2, "high": 3}
        return priority_map.get(self.priority.lower(), 0)
    
    def get_info(self) -> str:
        return f"{self.time} - ({self.description}) ({self.duration} mins) [{self.priority}], {self.completion_status}"

# The "Brain" that retrieves, organizes, and manages tasks across pets.
class Scheduler:
    def __init__(self, pets: List['Pet']):
        self.pets = pets
        self.tasks: List[Task] = []

    #def retrieve_all_tasks(self) -> List[Task]:
        #all_tasks = []
        #for pet in self.pets:
            #all_tasks.extend(pet.tasks)
        #return all_tasks
    def retrieve_all_tasks(self) -> List[Task]:
        for pet in self.pets:
            self.tasks.extend(pet.tasks)

    def add_task(self, task: Task) -> None:
        self.tasks.append(task)

    def get_tasks_by_priority(self) -> List[Task]:
        return sorted(self.tasks, key=lambda task: task.get_priority_level(), reverse=True)

# Owner: Manages multiple pets and provides access to all their tasks.
class Owner:
    def __init__(self, name: str):
        self.name: str = name
        self.pets: List[Pet] = []
        self.scheduler: Scheduler = None
    
    def add_pet(self, pet: Pet) -> None:
        self.pets.append(pet)
    
    def create_schedule(self) -> Scheduler:
        self.scheduler = Scheduler(self.pets)
        return self.scheduler