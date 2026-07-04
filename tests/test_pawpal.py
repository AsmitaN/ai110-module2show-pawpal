import pawpal_system
from datetime import date, timedelta

# ============================================================================
# RECURRENCE LOGIC TESTS
# ============================================================================

def test_daily_task_recurs_with_advanced_due_date():
    """Verify marking a Daily task complete advances its due_date to the next day for recurrence."""
    today = date.today()
    task = pawpal_system.Task("Morning feeding", 10, "Daily", "high", "09:00", due_date=today)

    print(f"\n📋 TEST: Daily Task Recurrence")
    print(f"   Initial due_date: {task.due_date}")
    print(f"   Initial status: {task.completion_status}")

    task.mark_complete()

    print(f"   After mark_complete():")
    print(f"     - due_date: {task.due_date} (advanced by 1 day)")
    print(f"     - status: {task.completion_status}")

    assert task.due_date == today + timedelta(days=1)
    assert task.completion_status == "complete"
    print(f"   ✅ Test passed!\n")


# ============================================================================
# CONFLICT DETECTION TESTS
# ============================================================================

def test_add_task_drops_conflicting_same_time_task():
    """Verify add_task silently drops a second task with the same due_date and time instead of appending it."""
    pet = pawpal_system.Pet("Buddy", "Dog")
    scheduler = pawpal_system.Scheduler([pet])
    today = date.today()
    task1 = pawpal_system.Task("Feeding", 10, "Daily", "high", "09:00", due_date=today)
    task2 = pawpal_system.Task("Vet visit", 60, "Daily", "high", "09:00", due_date=today)

    print(f"\n🚫 TEST: Conflict Detection")
    print(f"   Pet: {pet.name}")
    print(f"   Adding Task 1: '{task1.description}' at {task1.time} on {task1.due_date}")
    result1 = scheduler.add_task(pet.name, task1)
    print(f"     → Result: {'Added' if result1 else 'Blocked'}")

    print(f"   Adding Task 2: '{task2.description}' at {task2.time} on {task2.due_date}")
    result2 = scheduler.add_task(pet.name, task2)
    print(f"     → Result: {'Added' if result2 else 'Blocked (conflict!)'}")
    print(f"   Final pet task count: {len(pet.tasks)}")

    assert len(pet.tasks) == 1
    assert pet.tasks[0].description == "Feeding"
    print(f"   ✅ Test passed!\n")


# ============================================================================
# SORTING TESTS
# ============================================================================

def test_sort_by_time_orders_across_pets():
    """Verify sort_by_time orders tasks from multiple pets earliest to latest by datetime, regardless of which pet owns them."""
    today = date.today()
    dog = pawpal_system.Pet("Rex", "Dog")
    cat = pawpal_system.Pet("Momo", "Cat")
    scheduler = pawpal_system.Scheduler([dog, cat])
    scheduler.add_task(dog.name, pawpal_system.Task("Walk", 30, "Daily", "high", "14:00", due_date=today))
    scheduler.add_task(cat.name, pawpal_system.Task("Feed", 10, "Daily", "high", "08:00", due_date=today+timedelta(days=2)))
    scheduler.add_task(dog.name, pawpal_system.Task("Groom", 20, "Weekly", "low", "10:00", due_date=today))

    print(f"\n⏰ TEST: Sort By DateTime (Across Multiple Pets)")
    print(f"   Pets: {dog.name}, {cat.name}")
    print(f"   Date: {today}")
    print(f"   Tasks added (unordered):")
    for pet in [dog, cat]:
        for task in pet.tasks:
            print(f"     - {task.description} ({task.time}) - {pet.name}")

    scheduler = pawpal_system.Scheduler([dog, cat])
    ordered = scheduler.sort_by_time([dog, cat])

    print(f"   After sorting by datetime:")
    for i, task in enumerate(ordered):
        print(f"     {i+1}. {task.description} at {task.time} on {task.due_date}")

    # Assert the tasks are sorted by earliest to latest datetime (date first, then time)
    assert len(ordered) == 3, f"Expected 3 tasks, got {len(ordered)}"

    # Check each task in order
    assert ordered[0].description == "Groom" and ordered[0].due_date == today and ordered[0].time == "10:00"
    assert ordered[1].description == "Walk" and ordered[1].due_date == today and ordered[1].time == "14:00"
    assert ordered[2].description == "Feed" and ordered[2].due_date == today + timedelta(days=2) and ordered[2].time == "08:00"

    # Verify the datetimes are in ascending order
    datetimes = [(task.due_date, task.time) for task in ordered]
    assert datetimes == [(today, "10:00"), (today, "14:00"), (today + timedelta(days=2), "08:00")]

    print(f"   ✅ Test passed!\n")


# ============================================================================
# WORKFLOW TESTS (Complete + Reset)
# ============================================================================

def test_mark_complete_and_reset_workflow():
    """Verify mark_complete sets status to complete, due_date advances for recurring tasks, and reset_completed_tasks_to_pending resets the status."""
    today = date.today()
    dog = pawpal_system.Pet("Rex", "Dog")
    scheduler = pawpal_system.Scheduler([dog])
    task = pawpal_system.Task("Feeding", 10, "Daily", "high", "09:00", due_date=today)
    scheduler.add_task(dog.name, task)

    print(f"\n🔄 TEST: Complete & Reset Workflow")
    print(f"   Pet: {dog.name}, Task: '{task.description}'")
    print(f"   Initial state:")
    print(f"     - status: {task.completion_status}")
    print(f"     - due_date: {task.due_date}")

    # Mark the task complete: status becomes "complete", due_date advances
    task.mark_complete()
    print(f"   After mark_complete():")
    print(f"     - status: {task.completion_status}")
    print(f"     - due_date: {task.due_date}")
    assert task.completion_status == "complete"
    assert task.due_date == today + timedelta(days=1)

    # Reset completed tasks: status goes back to "pending" for next cycle
    scheduler.reset_completed_tasks_to_pending()
    print(f"   After reset_completed_tasks_to_pending():")
    print(f"     - status: {task.completion_status}")
    assert task.completion_status == "pending"
    print(f"   ✅ Test passed!\n")


# ============================================================================
# EDGE CASE TESTS
# ============================================================================

def test_filter_tasks_for_pet_with_no_tasks():
    """Verify filtering tasks for a pet with no tasks returns an empty list without error."""
    dog = pawpal_system.Pet("Rex", "Dog")
    empty_cat = pawpal_system.Pet("Momo", "Cat")
    scheduler = pawpal_system.Scheduler([dog, empty_cat])

    scheduler.add_task(dog.name, pawpal_system.Task("Walk", 30, "Daily", "high", "09:00"))

    print(f"\n📭 TEST: Filter Tasks for Pet With No Tasks")
    print(f"   Pets: {dog.name} (1 task), {empty_cat.name} (0 tasks)")
    print(f"   Scheduler total tasks: {len(scheduler.tasks)}")
    print(f"   Filtering for pet '{empty_cat.name}'...")

    filtered = scheduler.filter_tasks(pet_name="Momo")

    print(f"   Filtered results: {len(filtered)} tasks")
    assert filtered == []
    assert len(scheduler.tasks) == 1
    print(f"   ✅ Test passed!\n")
