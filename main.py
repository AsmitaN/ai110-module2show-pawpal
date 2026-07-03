import pawpal_system
from typing import List

first_owner = pawpal_system.Owner("Lily")
dog = pawpal_system.Pet("Alice", "Husky")
fish = pawpal_system.Pet("Bubble", "Goldfish")

first_owner.add_pet(dog)
first_owner.add_pet(fish)

#for pet in first_owner.pets:
#    print(pet.get_info())
dog_feeding = pawpal_system.Task("Feeding", 10, "Daily", "high", "09:00")
dog.add_task(dog_feeding)

#for task in dog.tasks:
#    print(task.description, task.duration, task.frequency, task.priority, task.completion_status) 

fish_feeding = pawpal_system.Task("Feeding", 5, "Daily", "high", "10:00")
fish.add_task(fish_feeding)
dog_morning_walk = pawpal_system.Task("Morning walk", 30, "Daily", "high", "08:00")
dog.add_task(dog_morning_walk)
clean_tank = pawpal_system.Task("Clean tank", 5, "Weekly", "high", "11:00")
fish.add_task(clean_tank)

#for task in fish.tasks:
#    print(task.description, task.duration, task.frequency, task.priority, task.completion_status) 

first_owner.scheduler = pawpal_system.Scheduler(first_owner.pets)

print("Today's Schedule (sorted by earliest to latest hour)")
sorted_schedule = first_owner.scheduler.sort_by_time(first_owner.pets)
for pet in first_owner.pets:
    print(pet.get_info())
    for task in sorted_schedule:
        if task in pet.tasks:
            print(task.get_info())

first_owner.scheduler.retrieve_all_tasks()

print("Today's Schedule (filtered by pet name)")
filtered_schedule = first_owner.scheduler.filter_tasks(pet_name=first_owner.pets[0].get_name())
print(first_owner.pets[0].get_info())

for i in range(len(filtered_schedule)):
    print(filtered_schedule[i].get_info())

first_owner.scheduler.tasks[3].mark_complete()


print("Today's Schedule (filtered by completion status - after marking a daily task complete)")
filtered_schedule = first_owner.scheduler.filter_tasks("pending")

for pet in first_owner.pets:
    print(pet.get_info())
    for task in filtered_schedule:
        if task in pet.tasks:
            print(task.get_info())

print("Today's Schedule (sorted by earliest to latest hour)")
sorted_schedule = first_owner.scheduler.sort_by_time(first_owner.pets)
for pet in first_owner.pets:
    print(pet.get_info())
    for task in sorted_schedule:
        if task in pet.tasks:
            print(task.get_info())