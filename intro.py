import streamlit as st

st.title("Hello streamlit 👋🏼")
st.header("This is a header")
st.subheader("This is a subheader")
st.write("Hello world")
st.text("Hello world again...")
st.caption("This is a caption")
st.markdown("This is a markdown")
st.code("from streamlit import st", language="python")

# Widgets
my_name = st.text_input("Enter your name")
st.text_area("Enter your address", "123 somewhere")
st.number_input("Enter your age", 0, 100)
st.date_input("Enter your date of birth")
st.time_input("Enter your time of birth")

my_audio = st.audio_input("Recoder a voice message")
if my_audio:
    st.audio(my_audio)

# st.image("https://images.pexels.com/photos/220453/pexels-photo-220453.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2")
# st.video("https://www.youtube.com/watch?v=9bZkp7q19f0")

st.file_uploader("Upload a file", type=["pdf", "txt"])

my_image = st.camera_input("Take a picture")

st.divider()

st.toggle("Show/Hide")
st.checkbox("I agree")
program = st.radio("Select a program", ["AI & Prompt Engineering", "Data Analytics", "Data Science"])
st.segmented_control("Select a program", ["AI & Prompt Engineering", "Data Analytics", "Data Science"])
st.pills("Select a program", ["AI & Prompt Engineering", "Data Analytics", "Data Science"])
st.feedback("thumbs")


prompt = st.chat_input("Ask me anything...")
if prompt:
    st.chat_message("user").write(prompt)
    st.chat_message("ai").write("This will be your AI response...")

st.button("Click me")
st.download_button("Download", "data.csv")
st.link_button("Go to Google", "https://google.com")

st.balloons()
# st.snow()

with st.form("my_form"):
    st.text_input("First name")
    st.text_input("Last name")
    st.form_submit_button("Submit")


st.success("Success message")
st.error("Error message")
st.warning("Warning message")
st.info("Info message")

st.badge("Python")
st.badge("Qubyteflow", color='green', icon="💻")
st.badge("Pandas", color='red')

st.markdown(":blue-badge[Python] :orange-badge[Qubyteflow] :red-badge[Pandas]")


with st.spinner("Waiting..."):
    import time
    time.sleep(5)
    st.success("Done!")

with st. status("Processing..."):
    import time
    time.sleep(5)
    st.success("Done!")

progress_text = "Operation in progress. Please wait."
my_bar = st.progress(0, text=progress_text)
for percent_complete in range(101):
    import time
    time.sleep(0.1)
    my_bar.progress(percent_complete, text=progress_text)
st.success("Done!")


st.toast("Toast message")
st.toast("Another toast", icon="👋🏼")
st.toast("A different toast", icon="👋🏼")
