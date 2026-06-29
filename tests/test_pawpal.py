from pawpal_system import Pet, Task, Owner, Scheduler

def test_mark_complete_changes_status():
    """Verify that calling mark_complete() changes the task's completion_status from pending to complete."""
    task = Task("Morning walk", "08:00", 30, "Daily", "high")
    assert task.completion_status == "pending"
    task.mark_complete()
    assert task.completion_status == "complete"


def test_add_task_increases_pet_task_count():
    """Verify that adding a task to a Pet increases that pet's task count."""
    pet = Pet("Buddy", "Dog")
    assert len(pet.tasks) == 0

    task1 = Task("Feeding", "09:00", 10, "Twice a day", "high")
    pet.add_task(task1)
    assert len(pet.tasks) == 1

    task2 = Task("Walk", "10:00", 30, "Daily", "high")
    pet.add_task(task2)
    assert len(pet.tasks) == 2
