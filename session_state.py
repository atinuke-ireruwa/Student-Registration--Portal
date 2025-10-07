import streamlit as st

st.text_input("Enter your name", key="my_name")
st.text_area("Enter your address", key="my_address")
st.number_input("Enter your age", 0, 100, key="my_age")
st.date_input("Enter your date of birth", key="my_dob")
st.time_input("Enter your time of birth", key="my_time")


st.write(st.session_state)
st.write(st.session_state.my_name)
st.write(st.session_state.my_address)
st.write(st.session_state.my_age)
st.write(st.session_state.my_dob)
st.write(st.session_state.my_time)


#1. On change 
#2. On click

def number_slider():
    st.write(f"Your selected number is {st.session_state.my_slider}")

def terms_and_conditions():
    if st.session_state.my_terms:
        st.write("You have accepted the terms and conditions")
    else:
        st.write("You have not accepted the terms and conditions")

def toggle():
    if st.session_state.my_toggle:
        st.write("Toggle is ON")
    else:
        st.session_state.show_text = True

def feedback():
    if st.session_state.my_feedback == 0:
        st.error("Not satisfied")
    else:
        st.success("Satisfied")


st.slider("Select a number", 0, 100, 20, key="my_slider", on_change=number_slider)
st.checkbox("Accept terms and conditions", key="my_terms", on_change=terms_and_conditions)
st.toggle("Show/Hide", key="my_toggle", on_change=toggle)
st.segmented_control("Select a color", ["Red", "Green", "Blue"], key="my_color")
st.pills("Select a color", ["Red", "Green", "Blue"], key="my_pills")
st.feedback("thumbs", key="my_feedback", on_change=feedback)


def do_something():
    st.write("You have clicked the button")

st.button("Chat with AI", on_click=do_something)

def enroll_student():
    st.write(f"Enrolling {st.session_state.my_first_name} {st.session_state.my_last_name} with age {st.session_state.my_age} and phone number {st.session_state.my_phone}")

with st.form("my_form"):
    st.text_input("First name", key="my_first_name")
    st.text_input("Last name", key="my_last_name")
    st.number_input("Enter your age", 0, 100, key="my_age")
    st.number_input("Enter your phone number", key="my_phone")
    st.form_submit_button("Enroll", on_click=enroll_student)

st.chat_message("user").write("Hello")
st.chat_message("assistant").write("Hi")

st.chat_message("user").markdown("Write me a python code for hello world...")
st.chat_message("ai").code("print('Hello world')", language="python")

prompt = st.chat_input("Ask me anything...")
if prompt:
    st.chat_message("user").write(prompt)
    st.chat_message("ai").write("This will be your AI response...")

st.write(st.session_state)