# Music School Management System (MSMS) - PST1

## Overview
This is a Music School Management System built as part of the FIT1056 project. It manages students, teachers, and course enrollments using a procedural approach in Python.

## Features / Project Structure
The project is organized into four main parts within `MSMS.py`.

Fragment 1.1: Defines the `Student` and `Teacher` classes, along with memory storage lists (`student_db`, `teacher_db`).

Fragment 1.2: Implements core backend functions for adding teachers, listing records, and searching data.

Fragment 1.3: Adds high-level front desk functions (like registration, enrollment, and ID lookups).

Fragment 1.4: Implements the main interactive menu loop (`while True`) for user interaction.

## How to Run
1. Open your terminal in the project folder.
2. Run the application with Python:
   ```bash
   python MSMS.py


## Design Choices & Assumptions

Storage: As specified for PST1, all data is stored temporarily in global lists. This keeps the prototype lightweight and focuses the design on core logic without needing external database files yet.

Layered structure: The code separates database, core helper functions, frontdesk, and the menu application. This approach makes the code easier to debug and upgrade.

Auto increment IDs: Simple counter variables are used to generate unique IDs automatically for every new student and teacher added to the system.