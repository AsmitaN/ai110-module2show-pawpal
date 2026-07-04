import pawpal_system
from datetime import date, timedelta
#from typing import List

first_owner = pawpal_system.Owner("Lily")
first_owner.scheduler = pawpal_system.Scheduler(first_owner.pets)
dog = pawpal_system.Pet("Alice", "Husky")
fish = pawpal_system.Pet("Bubble", "Goldfish")

first_owner.add_pet(dog)
first_owner.add_pet(fish)

today = date.today()

dog_feeding = pawpal_system.Task("Feeding", 10, "Daily", "high", "09:00", due_date=today)
first_owner.scheduler.add_task(dog.name, dog_feeding)

fish_feeding = pawpal_system.Task("Feeding", 5, "Daily", "high", "10:00", due_date=today+timedelta(days=2))
first_owner.scheduler.add_task(fish.name, fish_feeding)

dog_morning_walk = pawpal_system.Task("Morning walk", 30, "Daily", "high", "08:00", due_date=today)
first_owner.scheduler.add_task(dog.name, dog_morning_walk)

tank_cleaning = pawpal_system.Task("Clean tank", 5, "Weekly", "high", "11:00", due_date=today)
first_owner.scheduler.add_task(fish.name, tank_cleaning)

print("Today's Schedule")
first_owner.scheduler.print_schedule(pets = first_owner.pets)

print("Today's Schedule (sorted by earliest to latest datetime)")
sorted_schedule = first_owner.scheduler.sort_by_time(first_owner.pets)
first_owner.scheduler.print_schedule(first_owner.pets, sorted_schedule)

print("Today's Schedule (filtered by pet name)")
filtered_schedule = first_owner.scheduler.filter_tasks(pet_name=first_owner.pets[0].get_name())
first_owner.scheduler.print_schedule(first_owner.pets, filtered_schedule, pet_name=first_owner.pets[0].get_name())

first_owner.scheduler.tasks[2].mark_complete()

print("Today's Schedule (filtered by completion status - after marking a daily task complete)")
filtered_schedule = first_owner.scheduler.filter_tasks("pending")
first_owner.scheduler.print_schedule(first_owner.pets, filtered_schedule)

first_owner.scheduler.reset_completed_tasks_to_pending()

print("Today's Schedule (sorted by earliest to latest datetime) - after resetting completed daily task to pending")
sorted_schedule = first_owner.scheduler.sort_by_time(first_owner.pets)
first_owner.scheduler.print_schedule(first_owner.pets, sorted_schedule)