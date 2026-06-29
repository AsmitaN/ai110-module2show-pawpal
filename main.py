import pawpal_system
from typing import List

first_owner = pawpal_system.Owner("Lily")
dog = pawpal_system.Pet("Alice", "Husky")
fish = pawpal_system.Pet("Bubble", "Goldfish")

first_owner.add_pet(dog)
first_owner.add_pet(fish)

#for pet in first_owner.pets:
#    print(pet.get_info())

dog_morning_walk = pawpal_system.Task("Morning walk", "08:00", 30, "Daily", "high")
dog_feeding = pawpal_system.Task("Feeding", "09:00", 10, "Twice a day", "high")
dog.add_task(dog_morning_walk)
dog.add_task(dog_feeding)

#for task in dog.tasks:
#    print(task.description, task.duration, task.frequency, task.priority, task.completion_status) 

fish_feeding = pawpal_system.Task("Feeding", "10:00", 5, "Daily", "high")
fish.add_task(fish_feeding)

#for task in fish.tasks:
#    print(task.description, task.duration, task.frequency, task.priority, task.completion_status) 

first_owner.scheduler = pawpal_system.Scheduler(first_owner.pets)
first_owner.scheduler.retrieve_all_tasks()
print("Today's Schedule")
for pet in first_owner.pets:
    print(pet.get_info())
    for task in first_owner.scheduler.tasks:
        if task in pet.tasks:
            print(task.get_info())