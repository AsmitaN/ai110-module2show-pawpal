import streamlit as st
from pawpal_system import Owner, Pet, Task

st.set_page_config(page_title="PawPal+", page_icon="🐾", layout="centered")

st.title("🐾 PawPal+")

st.markdown(
    """
Welcome to the PawPal+ starter app.

This file is intentionally thin. It gives you a working Streamlit app so you can start quickly,
but **it does not implement the project logic**. Your job is to design the system and build it.

Use this app as your interactive demo once your backend classes/functions exist.
"""
)

with st.expander("Scenario", expanded=True):
    st.markdown(
        """
**PawPal+** is a pet care planning assistant. It helps a pet owner plan care tasks
for their pet(s) based on constraints like time, priority, and preferences.

You will design and implement the scheduling logic and connect it to this Streamlit UI.
"""
    )

with st.expander("What you need to build", expanded=True):
    st.markdown(
        """
At minimum, your system should:
- Represent pet care tasks (what needs to happen, how long it takes, priority)
- Represent the pet and the owner (basic info and preferences)
- Build a plan/schedule for a day that chooses and orders tasks based on constraints
- Explain the plan (why each task was chosen and when it happens)
"""
    )

st.divider()

# Initialize session state
if "owners" not in st.session_state:
    st.session_state.owners = {}
    st.session_state.owners["Jordan"] = Owner("Jordan")
    new_pet = Pet("Mochi", "Golden Retriever")
    st.session_state.owners["Jordan"].add_pet(new_pet)

if "current_owner" not in st.session_state:
    st.session_state.current_owner = None

st.subheader("👤 Owner & Pet Setup")

owner_name = st.text_input("Owner name", placeholder="Enter owner name")
pet_name = st.text_input("Pet name", placeholder="Enter pet name")
species = st.text_input("Species", placeholder="Enter pet species (i.e. Golden Retriever)")

col1, col2 = st.columns(2)
with col1:
    if st.button("Create Owner"):
        if owner_name == "":
            st.error("Please enter an owner name")
            st.stop()
        elif owner_name in st.session_state.owners:
            st.warning(f"Owner '{owner_name}' already exists")
            st.session_state.current_owner = owner_name
        else:
            st.session_state.owners[owner_name] = Owner(owner_name)
            st.session_state.current_owner = owner_name
            st.success(f"Created owner: {owner_name}")

with col2:
    if st.button("Add Pet"):
        if owner_name == "":
            st.error("Please enter the owner's name of the pet to be added")
            st.stop()
        if pet_name == "" or species == "":
            st.error("Please enter all values needed to add a new pet")
            st.stop()
        current_owner = st.session_state.owners[owner_name]
        pet_exists = any(pet.name == pet_name for pet in current_owner.pets)
        if pet_exists:
            st.warning(f"Pet '{pet_name}' already exists for {current_owner.name}")
        else:
            new_pet = Pet(pet_name, species)
            current_owner.add_pet(new_pet)
            st.success(f"Added {pet_name} ({species})")

# Display created owners and their pets
if st.session_state.owners:
    st.write("**Created Owners:**")
    for owner_key, owner_obj in st.session_state.owners.items():
        st.write(f"\n**{owner_obj.name}**")
        if owner_obj.pets:
            for pet in owner_obj.pets:
                st.write(f"  - {pet.get_info()}")
        else:
            st.write("  *(no pets yet)*")

st.markdown("### Tasks")
st.caption("Add a few tasks. In your final version, these should feed into your scheduler.")

if "tasks" not in st.session_state:
    st.session_state.tasks = []

col1, col2 = st.columns(2)
with col1:
    owner_name = st.selectbox("Owner", options=list(st.session_state.owners.keys()), index=0)
    current_owner = st.session_state.owners[owner_name]
with col2:
    current_owner = st.session_state.owners[owner_name]
    pet = st.selectbox("Pet", options=(pet.name for pet in current_owner.pets), index=0)

col1, col2 = st.columns(2)
with col1:
    task_description = st.text_input("Description", placeholder="Enter a short title for the task")
with col2:
    duration = st.number_input("Duration (minutes)", placeholder="Enter how long the task will take")

col1, col2, col3 = st.columns(3)
with col1:
    frequency = st.selectbox("Frequency", ["Hourly", "Daily", "Weekly"], index=0)
with col2:
    priority = st.selectbox("Priority", ["low", "medium", "high"], index=0)
with col3:
    time = st.text_input("Time to complete by", placeholder="Enter in HH:MM format")

if st.button("Add task"):
    if task_description!="" and duration!="" and frequency!="" and priority!="" and time!="":
        new_task = Task(task_description, duration, frequency, priority, time)
        
    else:
        st.error("Please enter all values needed to add a new task")
        st.stop()

if st.session_state.tasks:
    st.write("Current tasks:")
    st.table(st.session_state.tasks)
else:
    st.info("No tasks yet. Add one above.")

st.divider()

st.subheader("Build Schedule")
st.caption("This button should call your scheduling logic once you implement it.")

if st.button("Generate schedule"):
    st.warning(
        "Not implemented yet. Next step: create your scheduling logic (classes/functions) and call it here."
    )
    st.markdown(
        """
Suggested approach:
1. Design your UML (draft).
2. Create class stubs (no logic).
3. Implement scheduling behavior.
4. Connect your scheduler here and display results.
"""
    )
