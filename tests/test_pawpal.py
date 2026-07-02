import pawpal_system
from datetime import date, timedelta

def test_mark_complete_changes_status():
    """Verify that calling mark_complete() on a recognized frequency task advances due_date and resets to pending."""
    today = date.today()
    task = pawpal_system.Task("Morning walk", 30, "Daily", "high", "08:00", due_date=today)
    assert task.completion_status == "pending"
    assert task.due_date == today
    task.mark_complete()
    assert task.completion_status == "pending"  # Daily task auto-recurs
    assert task.due_date == today + timedelta(days=1)

def test_add_task_increases_pet_task_count():
    """Verify that adding a task to a Pet increases that pet's task count."""
    pet = pawpal_system.Pet("Buddy", "Dog")
    assert len(pet.tasks) == 0

    task1 = pawpal_system.Task("Feeding", 10, "Daily", "high", "09:00")
    pet.add_task(task1)
    assert len(pet.tasks) == 1

    task2 = pawpal_system.Task("Walk", 30, "Daily", "high", "10:00")
    pet.add_task(task2)
    assert len(pet.tasks) == 2
