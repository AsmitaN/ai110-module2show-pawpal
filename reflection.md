# PawPal+ Project Reflection

## 1. System Design

**a. Initial design**

class ClassName {
        +type attribute
        +method() returnType
    }

    class AnotherClass {
        +type attribute
        +method() returnType
    }

    ClassName --> AnotherClass : relationship


Design a UML class diagram for a pet care app with Owner, Pet, Task, and Schedule classes. Explain the relationships. Provide the the UML diagram as Mermaid.js code

- Briefly describe your initial UML design.
Three core actions:
    1) Add a pet
    2) Add a task
    3) View the daily schedule of tasks
- What classes did you include, and what responsibilities did you assign to each?
    I included the classes Owner, Pet, Task, and Schedule. The Owner class can add pets and create schedules. The Pet class can return pet-speific information. The Task class can be used to determine the priority level of the given task. The Schedule class can organize tasks by priority and add new tasks.

**b. Design changes**

- Did your design change during implementation?
- If yes, describe at least one change and why you made it.

---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
- How did you decide which constraints mattered most?

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
- Why is that tradeoff reasonable for this scenario?

---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?

---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?

**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?
