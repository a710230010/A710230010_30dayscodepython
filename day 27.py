class Student:
    def __init__(self, student_id, name, grade):
        self.student_id = student_id
        self.name = name
        self.grade = grade

    def display_info(self):
        print(f"Student ID: {self.student_id}")
        print(f"Name: {self.name}")
        print(f"Grade: {self.grade}")
        print()

class School:
    def __init__(self, name):
        self.name = name
        self.students = []

    def enroll_student(self, student):
        self.students.append(student)
        print(f"{student.name} enrolled in {self.name}.")

    def expel_student(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                self.students.remove(student)
                print(f"{student.name} ({student_id}) expelled from {self.name}.")
                return
        print(f"Student with ID {student_id} not found in {self.name}.")

    def display_students(self):
        if not self.students:
            print(f"No students enrolled in {self.name} yet.")
        else:
            print(f"Students enrolled in {self.name}:")
            for student in self.students:
                student.display_info()

# Contoh penggunaan
if __name__ == "__main__":
    # Membuat sekolah
    my_school = School("International High School")

    # Mendaftarkan beberapa siswa ke sekolah
    s1 = Student("S001", "Alice Brown", 11)
    s2 = Student("S002", "Bob Smith", 10)
    s3 = Student("S003", "Charlie Davis", 12)

    my_school.enroll_student(s1)
    my_school.enroll_student(s2)
    my_school.enroll_student(s3)

    # Menampilkan semua siswa yang terdaftar di sekolah
    my_school.display_students()

    # Mengeluarkan seorang siswa
    my_school.expel_student("S002")
    my_school.expel_student("S004")  # ID siswa yang tidak ada di sekolah
