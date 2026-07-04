# PawPal+ (Module 2 Project)

You are building **PawPal+**, a Streamlit app that helps a pet owner plan care tasks for their pet.

## Scenario

A busy pet owner needs help staying consistent with pet care. They want an assistant that can:

- Track pet care tasks (walks, feeding, meds, enrichment, grooming, etc.)
- Consider constraints (time available, priority, owner preferences)
- Produce a daily plan and explain why it chose that plan

Your job is to design the system first (UML), then implement the logic in Python, then connect it to the Streamlit UI.

## What you will build

Your final app should:

- Let a user enter basic owner + pet info
- Let a user add/edit tasks (duration + priority at minimum)
- Generate a daily schedule/plan based on constraints and priorities
- Display the plan clearly (and ideally explain the reasoning)
- Include tests for the most important scheduling behaviors

## Getting started

### Setup

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### Suggested workflow

1. Read the scenario carefully and identify requirements and edge cases.
2. Draft a UML diagram (classes, attributes, methods, relationships).
3. Convert UML into Python class stubs (no logic yet).
4. Implement scheduling logic in small increments.
5. Add tests to verify key behaviors.
6. Connect your logic to the Streamlit UI in `app.py`.
7. Refine UML so it matches what you actually built.

## 🖥️ Sample Output

Paste a sample of your app's CLI or Streamlit output here so a reader can see what a generated plan looks like:

```
Today's Schedule
Alice (Husky)
2026-07-03 09:00 - Feeding (10 mins) [high], pending
2026-07-03 08:00 - Morning walk (30 mins) [high], pending
Bubble (Goldfish)
2026-07-03 10:00 - Feeding (5 mins) [high], pending
2026-07-03 11:00 - Clean tank (5 mins) [high], pending
```

## 🧪 Testing PawPal+

test_daily_task_recurs_with_advanced_due_date() checks that a completed task with daily frequency recurs the next day (by examining the updated due_date)\
test_add_task_drops_conflicting_same_time_task() verifies that a task with the same time and due_date as an existing task will not be added to specified pet's list of tasks.\
test_sort_by_time_orders_across_pets() checks that all tasks in the schedule is sorted by earliest to latest time\
test_mark_complete_and_reset_workflow() tests that the status is set to complete when mark_complete() is invoked and reset to pending after reset_completed_tasks_to_pending() is called\
test_filter_tasks_for_pet_with_no_tasks() checks that when a name filter corresponding to a pet with no tasks is passed, an empty list of tasks would be returned
```bash
# Run the full test suite:
python -m pytest -v -s

# Run with coverage:
pytest --cov
```

Sample test output:

```
tests/test_pawpal.py::test_daily_task_recurs_with_advanced_due_date 
📋 TEST: Daily Task Recurrence
   Initial due_date: 2026-07-03
   Initial status: pending
   After mark_complete():
     - due_date: 2026-07-04 (advanced by 1 day)
     - status: complete
   ✅ Test passed!

PASSED
tests/test_pawpal.py::test_add_task_drops_conflicting_same_time_task 
🚫 TEST: Conflict Detection
   Pet: Buddy
   Adding Task 1: 'Feeding' at 09:00 on 2026-07-03
     → Result: Added
   Adding Task 2: 'Vet visit' at 09:00 on 2026-07-03
⚠️  CONFLICT DETECTED: Task 'Vet visit' conflicts with existing task!
   Existing: Feeding at 09:00 on 2026-07-03 for Buddy
   New task: Vet visit at 09:00 on 2026-07-03 for Buddy
❌ Task not added due to scheduling conflict.
     → Result: Blocked (conflict!)
   Final pet task count: 1
   ✅ Test passed!

PASSED
tests/test_pawpal.py::test_sort_by_time_orders_across_pets 
⏰ TEST: Sort By Time (Across Multiple Pets)
   Pets: Rex, Momo
   Tasks added (unordered):
     - Walk (14:00) - Rex
     - Groom (10:00) - Rex
     - Feed (08:00) - Momo
   After sorting by time:
     1. Feed at 08:00
     2. Groom at 10:00
     3. Walk at 14:00
   ✅ Test passed!

PASSED
tests/test_pawpal.py::test_mark_complete_and_reset_workflow 
🔄 TEST: Complete & Reset Workflow
   Pet: Rex, Task: 'Feeding'
   Initial state:
     - status: pending
     - due_date: 2026-07-03
   After mark_complete():
     - status: complete
     - due_date: 2026-07-04
   After reset_completed_tasks_to_pending():
     - status: pending
   ✅ Test passed!

PASSED
tests/test_pawpal.py::test_filter_tasks_for_pet_with_no_tasks 
📭 TEST: Filter Tasks for Pet With No Tasks
   Pets: Rex (1 task), Momo (0 tasks)
   Scheduler total tasks: 1
   Filtering for pet 'Momo'...
   Filtered results: 0 tasks
   ✅ Test passed!

PASSED

============================================================================== 5 passed in 0.01s ==============================================================================
```
Confidence level: 4 stars
## 📐 Smarter Scheduling

| Feature | Method(s) | Notes |
|---------|-----------|-------|
| Task sorting | Scheduler.sort_by_time() | by time |
| Collecting tasks from all pets | Scheduler.retrieve_all_tasks() | must call this before first Scheduler.filter_tasks() call so that tasks field is non-empty |
| Filtering | Scheduler.filter_tasks() | by pet_name and/or completion_status |
| Conflict handling | Scheduler.check_scheduling_conflicts() | overlapping time slots |
| Recurring tasks | Task.mark_complete() | daily vs. weekly |

## 📸 Demo Walkthrough

Describe your app in numbered steps so a reader can follow along without watching a video:

1. <!-- Describe this step -->
2. <!-- Describe this step -->
3. <!-- Describe this step -->
4. <!-- Describe this step -->
5. <!-- Add more steps as needed -->

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or link to a demo video here -->
