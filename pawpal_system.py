from typing import List
from datetime import date, timedelta, datetime

# Stores pet details and a list of tasks.
class Pet:
    def __init__(self, name: str, species: str):
        self.name: str = name
        self.species: str = species
        self.tasks: List[Task] = []
    
    def get_name(self) -> str:
        """Return a string with the pet's name."""
        return f"{self.name}"

    def get_info(self) -> str:
        """Return a formatted string with the pet's name and species."""
        return f"{self.name} ({self.species})"

    def add_task(self, task: 'Task') -> None:
        """Add a task to the pet's task list and check for scheduling conflicts."""
        for existing_task in self.tasks:
            if existing_task.due_date == task.due_date and existing_task.time == task.time:
                print(f"⚠️  WARNING: Scheduling conflict for {self.name}!")
                print(f"   Task 1: {existing_task.description} at {existing_task.time} on {existing_task.due_date}")
                print(f"   Task 2: {task.description} at {task.time} on {task.due_date}")
                return
        self.tasks.append(task)

# Represents a single activity (description, time, frequency, priority, completion status).
class Task:
    FREQUENCY_INTERVALS = {
        "Daily": timedelta(days=1),
        "Weekly": timedelta(weeks=1),
    }

    def __init__(self, description: str, duration: int, frequency: str, priority: str, time: str, completion_status: str = "pending", due_date: date = date.today()):
        self.description = description
        self.duration = duration
        self.frequency = frequency
        self.priority = priority
        self.time = time
        self.due_date = due_date
        self.completion_status = completion_status
    
    def get_priority_level(self) -> int:
        """Return the numeric priority level (1=low, 2=medium, 3=high)."""
        priority_map = {"low": 1, "medium": 2, "high": 3}
        return priority_map.get(self.priority.lower(), 0)

    def get_info(self) -> str:
        """Return a formatted string with the task's details."""
        return f"{self.due_date} {self.time} - {self.description} ({self.duration} mins) [{self.priority}], {self.completion_status}"

    def mark_complete(self):
        """Mark the task as complete and advance due_date."""
        self.completion_status = "complete"
        interval = self.FREQUENCY_INTERVALS.get(self.frequency)
        if interval:
            self.due_date += interval
            self.completion_status = "pending"
            print("New due date: " + str(self.due_date))

# The "Brain" that retrieves, organizes, and manages tasks across pets.
class Scheduler:
    def __init__(self, pets: List['Pet']):
        self.pets = pets
        self.tasks: List[Task] = []

    def sort_by_time(self, pets: List[Pet]) -> List[Task]:
        """Sort tasks from given pets by earliest to latest time (HH:MM format)."""
        tasks = []
        for pet in pets:
            tasks.extend(pet.tasks)
        return sorted(tasks, key=lambda task: tuple(map(int, task.time.split(':'))))

    def get_pet_by_name(self, pet_name: str) -> Pet:
        """Return a Pet object with the corresponding pet_name."""
        return next((p for p in self.pets if p.name == pet_name), None)

    def filter_tasks(self, completion_status: str = None, pet_name: str = None) -> List[Task]:
        """Filter tasks by completion status and/or pet name."""
        filtered = self.tasks

        if completion_status:
            filtered = [task for task in filtered if task.completion_status == completion_status]

        if pet_name:
            pet = self.get_pet_by_name(pet_name)
            if pet:
                filtered = [task for task in filtered if task in pet.tasks]

        return filtered

    def check_scheduling_conflicts(self) -> None:
        """Check for scheduling conflicts across all pets (any number) and print warnings."""
        all_tasks = []
        for pet in self.pets:
            for task in pet.tasks:
                all_tasks.append((pet, task))

        for i, (pet1, task1) in enumerate(all_tasks):
            for pet2, task2 in all_tasks[i+1:]:
                if task1.due_date == task2.due_date and task1.time == task2.time:
                    print(f"⚠️  CROSS-PET CONFLICT: {pet1.name} and {pet2.name} have tasks at the same time! Newest task not added, schedule for different time.")
                    print(f"   {pet1.name}: {task1.description} at {task1.time} on {task1.due_date}")
                    print(f"   {pet2.name}: {task2.description} at {task2.time} on {task2.due_date}")

    def retrieve_all_tasks(self) -> List[Task]:
        """Retrieve and aggregate all tasks from all pets."""
        self.tasks.clear()
        for pet in self.pets:
            self.tasks.extend(pet.tasks)

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