import tkinter as tk
from tkinter import ttk


students = []


def load_student_information():
    global students
    try:
        with open("Assessment 1\Exercise 3\studentMarks.txt", "r",  encoding='utf-8') as file:
            lines = file.readlines()
            for line in lines[1:]:
                parts = line.strip().split(", ")
                student_id, name, *marks = parts
                coursework = sum(map(int, marks[:3]))
                exam = int(marks[3])
                total = coursework + exam
                percentage = (total / 160) * 100
                grade = (
                    'A' if percentage >= 70 else
                    'B' if percentage >= 60 else
                    'C' if percentage >= 50 else
                    'D' if percentage >= 40 else 'F'
                )
                students.append({
                    "id": student_id,
                    "name": name,
                    "coursework": coursework,
                    "exam": exam,
                    "percentage": percentage,
                    "grade": grade
                })
    except FileNotFoundError:
        print("Error: 'Assessment 1\Exercise 3\studentMarks.txt' file not found!")


def inspect_all_students():
    output_text.delete(1.0, tk.END)
    total_percentage = 0
    for student in students:
        total_percentage += student["percentage"]
        output_text.insert(tk.END, f"ID: {student['id']}, Name: {student['name']}, "
                                   f"Coursework: {student['coursework']}, Exam: {student['exam']}, "
                                   f"Percentage: {student['percentage']:.2f}%, Grade: {student['grade']}\n")
    average_percentage = total_percentage / len(students) if students else 0
    output_text.insert(tk.END, f"\nNumber of Students: {len(students)}")
    output_text.insert(tk.END, f"\nAverage Percentage: {average_percentage:.2f}%\n")

def inspect_individual_student():
    student_input = entry_student.get().strip()
    output_text.delete(1.0, tk.END)
    for student in students:
        if student_input == student["id"] or student_input.lower() in student["name"].lower():
            output_text.insert(tk.END, f"ID: {student['id']}, Name: {student['name']}, "
                                       f"Coursework: {student['coursework']}, Exam: {student['exam']}, "
                                       f"Percentage: {student['percentage']:.2f}%, Grade: {student['grade']}\n")
            return
    output_text.insert(tk.END, "Student not found.\n")

def display_the_highest_score():
    if not students:
        output_text.insert(tk.END, "No student data available.\n")
        return

    highest_student = None
    for student in students:
        if highest_student is None or student["percentage"] > highest_student["percentage"]:
            highest_student = student

    
    output_text.delete(1.0, tk.END)
    output_text.insert(tk.END, f"ID: {highest_student['id']}, Name: {highest_student['name']}, "
                               f"Coursework: {highest_student['coursework']}, Exam: {highest_student['exam']}, "
                               f"Percentage: {highest_student['percentage']:.2f}%, Grade: {highest_student['grade']}\n")

def display_the_lowest_score():
    if not students:
        output_text.insert(tk.END, "No student data available.\n")
        return

    lowest_student = None
    for student in students:
        if lowest_student is None or student["percentage"] < lowest_student["percentage"]:
            lowest_student = student


    output_text.delete(1.0, tk.END)
    output_text.insert(tk.END, f"ID: {lowest_student['id']}, Name: {lowest_student['name']}, "
                               f"Coursework: {lowest_student['coursework']}, Exam: {lowest_student['exam']}, "
                               f"Percentage: {lowest_student['percentage']:.2f}%, Grade: {lowest_student['grade']}\n")
root = tk.Tk()
root.title("Student Manager")
root.geometry("600x400")

btn_view_all = tk.Button(root, text="View All Student Records", command=inspect_all_students)
btn_view_all.pack(pady=5)

btn_view_individual = tk.Button(root, text="Search Student Record", command=inspect_individual_student)
btn_view_individual.pack(pady=5)

btn_highest_score = tk.Button(root, text="Display the Highest Score", command=display_the_highest_score)
btn_highest_score.pack(pady=5)

btn_lowest_score = tk.Button(root, text="Display the Lowest Score", command=display_the_lowest_score)
btn_lowest_score.pack(pady=5)

lbl_prompt = tk.Label(root, text="Please Enter Student ID or Name:")
lbl_prompt.pack(pady=5)
entry_student = tk.Entry(root)
entry_student.pack(pady=5)

output_text = tk.Text(root, height=15, width=70)
output_text.pack(pady=10)

load_student_information()
root.mainloop()
