from typing import List
from datetime import date, timedelta

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
        # converts priority to numerical version so that it is easier to compare against other tasks
        return priority_map.get(self.priority, 0)

    def get_info(self) -> str:
        """Return a formatted string with the task's details."""
        return f"{self.due_date} {self.time} - {self.description} ({self.duration} mins) [{self.priority}], {self.completion_status}"

    def mark_complete(self):
        """Mark the task as complete and advance due_date if recurring."""
        self.completion_status = "complete"
        interval = self.FREQUENCY_INTERVALS.get(self.frequency)
        if interval:
            self.due_date += interval
            #print("New due date: " + str(self.due_date))

# The "Brain" that retrieves, organizes, and manages tasks across pets.
class Scheduler:
    def __init__(self, pets: List['Pet']):
        self.pets = pets
        self.tasks: List[Task] = []

    def print_schedule(self, pets: List[Pet], schedule: List['Task']=None, pet_name: str = None):
        for pet in pets:
            print(pet.get_info())
            schedule_to_print = []
            # executes if a sorted/filtered schedule is passed
            if schedule:
                schedule_to_print = schedule
            # executes if no second argument was passed technically
            else:
                schedule_to_print = self.tasks
            for task in schedule_to_print:
                if task in pet.tasks:
                    print(task.get_info())
            if pet_name:
                break

    def sort_by_time(self, pets: List[Pet]) -> List[Task]:
        """Sort tasks from given pets by earliest to latest datetime (date first, then time)."""
        tasks = []
        for pet in pets:
            tasks.extend(pet.tasks)
        # Sort by due_date first, then by time (HH:MM format)
        return sorted(tasks, key=lambda task: (task.due_date, tuple(map(int, task.time.split(':')))))

    def get_pet_by_name(self, pet_name: str) -> Pet:
        """Return a Pet object with the corresponding pet_name."""
        return next((p for p in self.pets if p.name == pet_name), None)

    def filter_tasks(self, completion_status: str = None, pet_name: str = None) -> List[Task]:
        """Filter tasks by completion status or pet name."""
        filtered = self.tasks

        if completion_status:
            filtered = [task for task in filtered if task.completion_status == completion_status]

        if pet_name:
            pet = self.get_pet_by_name(pet_name)
            if pet:
                filtered = [task for task in filtered if task in pet.tasks]

        return filtered

    def check_scheduling_conflicts(self, pet_name: str, task: 'Task') -> bool:
        """Check if a task conflicts with existing tasks. Returns True if conflict exists, False if no conflict."""
        for pet in self.pets:
            for existing_task in pet.tasks:
                # checks if the time and date of an existing task coincides with the new task (same/different pets included)
                if existing_task.due_date == task.due_date and existing_task.time == task.time:
                    print(f"⚠️  CONFLICT DETECTED: Task '{task.description}' conflicts with existing task!")
                    print(f"   Existing: {existing_task.description} at {existing_task.time} on {existing_task.due_date} for {pet.name}")
                    print(f"   New task: {task.description} at {task.time} on {task.due_date} for {pet_name}")
                    # signals that scheduling conflict exists
                    return True
        # signals that there is no scheduling conflict after looping through each pet
        return False
    
    def retrieve_all_tasks(self):
        """Retrieve and aggregate all tasks from all pets."""
        self.tasks.clear()
        for pet in self.pets:
            self.tasks.extend(pet.tasks)

    def add_task(self, pet_name: str, task: 'Task') -> bool:
        """Add a task to a pet after checking for scheduling conflicts. Returns True if added, False if conflict blocked it."""
        pet = self.get_pet_by_name(pet_name)

        if self.check_scheduling_conflicts(pet_name, task):
            print(f"❌ Task not added due to scheduling conflict.")
            return False

        pet.tasks.append(task)
        # updates the scheduler's common list of tasks after every new task is added to a pet
        self.retrieve_all_tasks()
        return True

    def reset_completed_tasks_to_pending(self) -> None:
        """Reset all tasks with completion_status 'complete' back to 'pending'."""
        for task in self.tasks:
            if task.completion_status == "complete":
                task.completion_status = "pending"

# Owner: Manages multiple pets and provides access to all their tasks.
class Owner:
    def __init__(self, name: str):
        self.name: str = name
        self.pets: List[Pet] = []
        self.scheduler: Scheduler = None
    
    def add_pet(self, pet: Pet) -> None:
        """Add a pet to the owner's pet list."""
        self.pets.append(pet)