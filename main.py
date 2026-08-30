# main.py - The View Layer
from app.schedule import ScheduleManager

def front_desk_daily_roster(manager, day):
    """Displays a pretty table of all lessons on a given day."""
    print(f"\n--- Daily Roster for {day} ---")
    # Notice: This code does not need to change. It doesn't care where the Course class lives.
    # It only talks to the manager.
    # TODO: Call a method on the manager to get the day's lessons and print them.

    lessons = manager.get_lessons_by_day(day)
    
    if not lessons:
        print(f"No lessons found for {day}.")
        return

    for course_name, time, room in lessons:
        print(f"Course: {course_name} | Time: {time} | Room: {room}")
   
def switch_course(manager, student_id, from_course_id, to_course_id):
    # TODO: Implement the logic to switch a student by calling methods on the manager.
    
    success = manager.switch_student_course(student_id, from_course_id, to_course_id)
    if success:
        print("Course switched successfully.")
    else:
        print("Error: Switch failed.")
    

def main():
    """Main function to run the MSMS application."""
    manager = ScheduleManager() # Create ONE instance of the application brain.
    
    while True:
        print("\n===== MSMS v3 (Object-Oriented) =====")
        print("1. View Daily Roster")
        print("2. Student Check-in")
        print("3. Switch Course")
        print("q. Quit")
        
        choice = input("Enter choice: ")
        if choice == '1':
            day = input("Enter day (e.g., Monday): ")
            front_desk_daily_roster(manager, day)
        elif choice == '2':
            try:
                s_id = int(input("Enter Student ID: "))
                c_id = int(input("Enter Course ID: "))
                manager.check_in(s_id, c_id)
            except ValueError:
                print("Error: IDs must be numbers.")
        elif choice == '3':
            try:
                s_id = int(input("Enter Student ID: "))
                from_c = int(input("Enter Current Course ID: "))
                to_c = int(input("Enter New Course ID: "))
                switch_course(manager, s_id, from_c, to_c)
            except ValueError:
                print("Error: IDs must be numbers.")
        elif choice.lower() == 'q':
            break
        
if __name__ == "__main__":
    main()