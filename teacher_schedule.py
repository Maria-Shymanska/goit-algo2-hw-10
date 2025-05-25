# Define the Teacher class
class Teacher:
    def __init__(self, first_name, last_name, age, email, can_teach_subjects):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.can_teach_subjects = set(can_teach_subjects)
        self.assigned_subjects = set()

    def __repr__(self):
        return f"{self.first_name} {self.last_name} ({self.age})"

# Greedy scheduling function
def create_schedule(subjects, teachers):
    uncovered_subjects = set(subjects)
    schedule = []

    while uncovered_subjects:
        # Find candidates who can cover any of the uncovered subjects
        candidates = []
        for teacher in teachers:
            can_teach = teacher.can_teach_subjects & uncovered_subjects
            if can_teach:
                candidates.append((teacher, can_teach))

        if not candidates:
            return None  # Not all subjects can be covered

        # Choose the teacher who covers the most uncovered subjects, break ties by youngest age
        best_teacher, best_subjects = max(
            candidates,
            key=lambda x: (len(x[1]), -x[0].age)
        )

        # Assign subjects and update uncovered subjects
        best_teacher.assigned_subjects = best_subjects
        schedule.append(best_teacher)
        uncovered_subjects -= best_subjects
        teachers.remove(best_teacher)

    return schedule

# Main function to run the program
if __name__ == '__main__':
    subjects = {'Math', 'Physics', 'Chemistry', 'CS', 'Biology'}

    teachers = [
        Teacher("Oleksandr", "Ivanenko", 45, "o.ivanenko@example.com", {"Math", "Physics"}),
        Teacher("Maria", "Petrenko", 38, "m.petrenko@example.com", {"Chemistry"}),
        Teacher("Serhii", "Kovalenko", 50, "s.kovalenko@example.com", {"CS", "Math"}),
        Teacher("Natalia", "Shevchenko", 29, "n.shevchenko@example.com", {"Biology", "Chemistry"}),
        Teacher("Dmytro", "Bondarenko", 35, "d.bondarenko@example.com", {"Physics", "CS"}),
        Teacher("Olena", "Hrytsenko", 42, "o.grytsenko@example.com", {"Biology"}),
    ]

    schedule = create_schedule(subjects, teachers)

    if schedule:
        print("Class Schedule:")
        for teacher in schedule:
            print(f"{teacher.first_name} {teacher.last_name}, {teacher.age} y.o., email: {teacher.email}")
            print(f"   Assigned subjects: {', '.join(teacher.assigned_subjects)}\n")
    else:
        print("It is not possible to cover all subjects with the available teachers.")
