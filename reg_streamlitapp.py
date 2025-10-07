# student_registration_app

import streamlit as st
from datetime import date
import pandas as pd
import os
import time

# -------------------------
# Create uploads folder
# -------------------------
UPLOAD_FOLDER = "reg.txt"
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# -------------------------
# Page Setup & Branding
# -------------------------
st.set_page_config(page_title="Student Registration Portal", page_icon="👨‍🎓", layout="centered")

st.title("👨‍🎓 Qbyte Student Registration Portal")
st.markdown("""
Welcome to our **Student Registration & Feedback Portal**.  
Complete each section to register successfully.
""")


# -------------------------
# Tabs for Multi-Step Flow
# -------------------------
tabs = st.tabs(["📝 Registration", "📚 Program Selection", "💬 Feedback", "✅ Submit"])

# -------------------------
# 1. Registration Tab
# -------------------------
with tabs[0]:
    st.header("Student Details")
    name = st.text_input("Full Name")
    
    dob = st.date_input(
    "Date of Birth",
    min_value=date(1900, 1, 1),
    max_value=date.today(),
    help="Select your birth date from the calendar"
)

# Recalculate age whenever DOB changes
    today = date.today()
    age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))

    st.write(f"Your age: {age} years")
    
    email = st.text_input("Email Address")
    
    # Country code + phone input
    country_codes = {
        "Nigeria (+234)": "+234",
        "United Kingdom (+44)": "+44",
        "United States (+1)": "+1",
        "India (+91)": "+91"
    }
    selected_code = st.selectbox("Select Country Code", list(country_codes.keys()))
    phone_number = st.text_input("Phone Number")
    full_phone_number = f"{country_codes[selected_code]} {phone_number}" if phone_number else ""
    
    transcript = st.file_uploader("Upload Transcript / ID", type=["pdf", "docx", "jpg", "png"])
    photo = st.camera_input("Take Photo")
    
    if st.button("Check Registration"):
        if not name:
            st.error("⚠ Please enter your full name")
        if not email:
            st.error("⚠ Please enter your email address")
        if not phone_number:
            st.error("⚠ Please enter your phone number")
        if not transcript:
            st.error("⚠ Please upload your transcript or ID")
        if not photo:
            st.error("⚠ Please take/upload your photo")

# -------------------------
# 2. Program Selection Tab
# -------------------------
with tabs[1]:
    st.header("Choose Your Program")
    program = st.radio(
        "Select your preferred program",
        ("Artificial Intelligence", "Data Science", "Software Engineering", "Cybersecurity")
    )
    terms = st.checkbox("I agree to the terms and conditions")
    
    if st.button("Check Program Selection"):
        if not program:
            st.error("⚠ Please select a program")
        if not terms:
            st.error("⚠ You must agree to the terms and conditions")

# -------------------------
# 3. Feedback Tab
# -------------------------
with tabs[2]:
    st.header("Provide Feedback")
    feedback_comments = st.text_area("Any comments or suggestions?")
    feedback_rating = st.radio("Rate this registration process", ("👍", "👎"))
    
    if st.button("Check Feedback"):
        if not feedback_comments:
            st.error("⚠ Please add your comments")
        if not feedback_rating:
            st.error("⚠ Please select a rating")

# -------------------------
# 4. Submission Tab
# -------------------------
with tabs[3]:
    st.header("Submit Your Registration")
    
    if st.button("Submit Registration"):
        # Validate required fields
        missing_fields = []
        if not name: missing_fields.append("Name")
        if not dob: missing_fields.append("Date of Birth")
        if not email: missing_fields.append("Email")
        if not phone_number: missing_fields.append("Phone Number")
        if not transcript: missing_fields.append("Transcript / ID")
        if not photo: missing_fields.append("Photo")
        if not program: missing_fields.append("Program Selection")
        if not terms: missing_fields.append("Agreement to Terms")
        if not feedback_comments: missing_fields.append("Feedback Comments")
        if not feedback_rating: missing_fields.append("Feedback Rating")
        
        if missing_fields:
            st.warning(f"Please complete the following fields before submitting: {', '.join(missing_fields)}")
        else:
            # Save uploaded files
            transcript_path = ""
            if transcript:
                transcript_path = os.path.join(UPLOAD_FOLDER, transcript.name)
                with open(transcript_path, "wb") as f:
                    f.write(transcript.getbuffer())
            
            photo_path = ""
            if photo:
                photo_path = os.path.join(UPLOAD_FOLDER, f"{name.replace(' ', '_')}_photo.png")
                with open(photo_path, "wb") as f:
                    f.write(photo.getbuffer())
            
            # Show progress bar
            progress_text = "Submitting your registration..."
            my_bar = st.progress(0, text=progress_text)
            for percent_complete in range(100):
                time.sleep(0.01)
                my_bar.progress(percent_complete + 1, text=progress_text)
            
            st.success("🎉 Registration submitted successfully!")
            
            # Display submitted info
            st.header("Your Submitted Details")
            st.write(f"**Name:** {name}")
            st.write(f"**Date of Birth:** {dob}")
            st.write(f"**Age:** {age} years")
            st.write(f"**Email:** {email}")
            st.write(f"**Phone Number:** {full_phone_number}")
            st.write(f"**Selected Program:** {program}")
            st.write(f"**Agreed to Terms:** {'Yes' if terms else 'No'}")
            st.write(f"**Feedback Comments:** {feedback_comments}")
            st.write(f"**Feedback Rating:** {feedback_rating}")
            
            if transcript_path:
                st.write("Uploaded Transcript / ID:", transcript_path)
            if photo_path:
                st.image(photo_path, caption="Your Photo", use_container_width=True)
            
            # -------------------------
            # Save to CSV
            # -------------------------
            submission_data = {
                "Name": name,
                "DOB": dob,
                "Age": age,
                "Email": email,
                "Phone": full_phone_number,
                "Program": program,
                "Agreed_Terms": terms,
                "Feedback_Comments": feedback_comments,
                "Feedback_Rating": feedback_rating,
                "Transcript_Path": transcript_path,
                "Photo_Path": photo_path
            }
            
            csv_file = "student_submissions.csv"
            if os.path.exists(csv_file):
                df = pd.read_csv(csv_file)
                df = pd.concat([df, pd.DataFrame([submission_data])], ignore_index=True)
            else:
                df = pd.DataFrame([submission_data])
            
            df.to_csv(csv_file, index=False)
            st.info(f"Your have been successfully Registered`")
