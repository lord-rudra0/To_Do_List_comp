import google.generativeai as genai
import streamlit as st
import json

genai.configure(api_key="AIzaSyCWk_oh0ZN7UdwUdl7ww8k0BAlgYee_ugU")


def extract_days(user_input):
    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday',
            'today', 'tomorrow', 'yesterday']

    found_days = []
    input_lower = user_input.lower()

    for day in days:
        if day in input_lower:
            found_days.append(day.capitalize())

    return found_days if found_days else ["Unspecified Day"]


def generate_structured_todo(user_input: str):
    days = extract_days(user_input)

    prompt = f"""
    Generate a structured TODO list based on the following user input: "{user_input}"
    The output should be a JSON object with a 'days' array. Each item in the 'days' array should be an object with 'title' and 'tasks' fields.
    The 'title' should be one of the following days: {', '.join(days)}
    The 'tasks' should be an array of objects, each with 'action' and 'completed' fields.
    Example format:
    {{
        "days": [
            {{
                "title": "Monday",
                "tasks": [
                    {{"action": "Clean desk", "completed": false}},
                    {{"action": "Wash clothes", "completed": false}}
                ]
            }},
            {{
                "title": "Tuesday",
                "tasks": [
                    {{"action": "Apply for internships", "completed": false}}
                ]
            }}
        ]
    }}
    Ensure that tasks are assigned to the correct day based on the user input.
    """

    model = genai.GenerativeModel("gemini-1.5-flash")

    result = model.generate_content(
        prompt,
        generation_config=genai.GenerationConfig(
            response_mime_type="application/json"
        )
    )

    try:
        return json.loads(result.text)
    except json.JSONDecodeError:
        st.error("Failed to parse the generated content as JSON. Please try again.")
        return None

def generate_structured_todo(user_input: str):
    days = extract_days(user_input)

    prompt = f"""
    Generate a structured TODO list based on the following user input: "{user_input}"
    The output should be a JSON object with a 'days' array. Each item in the 'days' array should be an object with 'title' and 'tasks' fields.
    The 'title' should be one of the following days: {', '.join(days)}
    The 'tasks' should be an array of objects, each with 'action' and 'completed' fields.
    Example format:
    {{
        "days": [
            {{
                "title": "Monday",
                "tasks": [
                    {{"action": "Clean desk", "completed": false}},
                    {{"action": "Wash clothes", "completed": false}}
                ]
            }},
            {{
                "title": "Tuesday",
                "tasks": [
                    {{"action": "Apply for internships", "completed": false}}
                ]
            }}
        ]
    }}
    Ensure that tasks are assigned to the correct day based on the user input.
    """

    model = genai.GenerativeModel("gemini-1.5-flash")

    result = model.generate_content(
        prompt,
        generation_config=genai.GenerationConfig(
            response_mime_type="application/json"
        )
    )

    try:
        return json.loads(result.text)
    except json.JSONDecodeError:
        st.error("Failed to parse the generated content as JSON. Please try again.")
        return None

# Initialize session state
if 'todo_lists' not in st.session_state:
    st.session_state.todo_lists = None

# Streamlit app interface
st.title("TO-DO App using Gemini API")

# Input for user's natural language TODO list
user_input = st.text_area("Enter your tasks in natural language (include the days):", "")


if st.button("Generate TO-DO Lists"):
    if user_input:
        st.session_state.todo_lists = generate_structured_todo(user_input)
        if st.session_state.todo_lists is None:
            st.error("Failed to generate TODO lists. Please try again.")
    else:
        st.warning("Please enter some tasks before generating the TODO lists.")


# Display tasks as checkboxes for each day
if st.session_state.todo_lists:
    for day_list in st.session_state.todo_lists['days']:
        st.subheader(f"Your TO-DO List for {day_list['title']}:")
        for i, task in enumerate(day_list['tasks']):
            task_key = f"{day_list['title']}_{i}"
            task['completed'] = st.checkbox(task['action'], value=task['completed'], key=task_key)

if st.button("Save Progress"):
    st.success("Progress saved!")
    st.json(st.session_state.todo_lists)

if st.session_state.todo_lists and st.button("Clear All Lists"):
    st.session_state.todo_lists = None
    st.rerun()

if st.session_state.get("clear_message"):
    # st.session_state.clear_message = False
    # st.session_state.todo_lists = None
    st.success("All lists have been cleared!")