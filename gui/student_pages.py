# gui/student_pages.py
import streamlit as st

def show_student_management_page(manager):
    """Renders all components for the student management page."""
    st.header("Student Management")

    # --- Search Section (remains the same) ---
    st.subheader("Find a Student")
    search_name = st.text_input("Enter Student Name to Search")
    if st.button("Search Student"):
        if search_name:
            found_students = [s for s in manager.students if search_name.lower() in s.name.lower()]
            if found_students:
                for student in found_students:
                    st.success(f"Found Student: {student.name} (ID: {student.id})")
                    st.write(f"Enrolled Courses: {student.enrolled_course_ids}")
            else:
                st.error("Student not found.")
        else:
            st.warning("Please enter a Student Name.")

    # --- Registration Section (now works correctly) ---
    st.subheader("Register New Student")
    with st.form("registration_form"):
        reg_name = st.text_input("New Student Name")
        reg_instrument = st.text_input("First Instrument")
        submitted = st.form_submit_button("Register Student")
        
        if submitted:
            # This call now works because we implemented the method in PST3.
            if reg_name and reg_instrument:
                new_student = manager.register_new_student(reg_name, reg_instrument)
                if new_student:
                    st.success(f"Successfully registered {reg_name}!")
                    # You can use st.balloons() for extra flair.
                else:
                    st.error(f"Could not register student. A teacher for {reg_instrument} might not be available.")
            else:
                st.warning("Please enter both a name and an instrument.")