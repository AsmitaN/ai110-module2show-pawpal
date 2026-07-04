# PawPal+ Project Reflection

## 1. System Design

**a. Initial design**

- Briefly describe your initial UML design.
Three core actions:
    1) Add a pet
    2) Add a task
    3) View the daily schedule of tasks
- What classes did you include, and what responsibilities did you assign to each?
    I included the classes Owner, Pet, Task, and Schedule. The Owner class can add pets and create schedules. The Pet class can return pet-speific information. The Task class can be used to determine the priority level of the given task. The Schedule class can organize tasks by priority and add new tasks.

**b. Design changes**

- Did your design change during implementation?\
    Yes
- If yes, describe at least one change and why you made it.\
    I moved the add_task() function from the Pet class to the Scheduler task because the Scheduler needs the updated list of tasks including the new ones that are added. This is why the corresponding Pet's list is first changed after a task is added and then the retrieve_all_tasks() functions is called right after.
---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?\
    The scheduler considers time and preferences such as pet and completion_status.
- How did you decide which constraints mattered most?\
    I chose these constraints based on the requirements for the project.

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.\
    This checks only for exact time matches instead of overlapping durations. 
- Why is that tradeoff reasonable for this scenario?\
    Suppose two tasks are scheduled at the same time but have different durations (so one task's duration would be smaller than that of the other).\
    The owner could potentially complete the longer-duration task before the shorter-duration task (or the other way around) but this means that the time for the shorter-duration would have to be changed.\
    This could confuse the owner because the task time can't be adjusted after its instance is created, so the task moved later in the hour would still have the same hour as the other task.
---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?\
    I used AI for brainstorming, applying the outline to the UI, improving efficiency, and for evaluating the methods through customized pytests.
- What kinds of prompts or questions were most helpful?\
    The prompts that referred to the UML to create implementations of the outline were helpful because it provided the AI context to construct logic.

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.\
    This happened in the initial stage that I asked the AI to come up with a UML diagram. It added a different class that I did not specify (ie. ScheduleTask) and different attributes that I thought strayed away from the core responsibilities for each class.
- How did you evaluate or verify what the AI suggested?\
    I evaluated its suggested UML by displaying it on mermaid.live. I was not ready to accept it after looking over the textual outline, and the visual representation further proved my hesitation. I then informed the AI that it was a good start but I wanted no additional classes and to enforce composition where appropriate.
---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?\
    I tested the recurring, conflict detection, sorting, and filtering by pet/completion_status behaviors.
- Why were these tests important?\
    These tests were important because they tested the primary functionalities (including edge cases) of the application I was designing.

**b. Confidence**

- How confident are you that your scheduler works correctly?\
    I am mostly confident that my scheduler works correctly.
- What edge cases would you test next if you had more time?\
    I would test that adding a Pet or Task increases the length of the Pets and Tasks lists, respectively.

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?\
    I really liked how everything comes together to support the UI's backend functionality.
**b. What you would improve**

- If you had another iteration, what would you improve or redesign?\
    I would including include logic to sort tasks by priority.

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?\
    You should improve your UML as you gain a better understanding of the project's main goals.
