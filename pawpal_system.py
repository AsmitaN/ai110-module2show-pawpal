from dataclasses import dataclass
from typing import List

@dataclass
class Pet:
    def __init__(self, name: str, species: str):
        self.name: str = name
        self.species: str = species
    
    def get_info(self) -> str:
        pass

@dataclass
class Task:
    def __init__(self, title: str, duration_minutes: int, priority: str):
        self.title: str = title
        self.duration_minutes: int = duration_minutes
        self.priority: str = priority
    
    def get_priority_level(self) -> int:
        pass

class Schedule:
    def __init__(self):
        self.tasks: List[Task] = []
    
    def add_task(self, task: Task) -> None:
        pass
    
    def get_tasks_by_priority(self) -> List[Task]:
        pass

class Owner:
    def __init__(self, name: str):
        self.name: str = name
        self.pets: List[Pet] = []
        self.schedule: Schedule = None
    
    def add_pet(self, pet: Pet) -> None:
        pass
    
    def create_schedule(self, tasks: List[Task]) -> Schedule:
        pass