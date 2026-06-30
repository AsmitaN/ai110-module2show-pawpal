import pawpal_system

def test_mark_complete_changes_status():
    """Verify that calling mark_complete() changes the task's completion_status from pending to complete."""
    task = pawpal_system.Task("Morning walk", 30, "Daily", "high", "08:00")
    assert task.completion_status == "pending"
    task.mark_complete()
    assert task.completion_status == "complete"

def test_add_task_increases_pet_task_count():
    """Verify that adding a task to a Pet increases that pet's task count."""
    pet = pawpal_system.Pet("Buddy", "Dog")
    assert len(pet.tasks) == 0

    task1 = pawpal_system.Task("Feeding", 10, "Twice a day", "high", "09:00")
    pet.add_task(task1)
    assert len(pet.tasks) == 1

    task2 = pawpal_system.Task("Walk", 30, "Daily", "high", "10:00")
    pet.add_task(task2)
    assert len(pet.tasks) == 2
