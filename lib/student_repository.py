from lib.student import Student

class StudentRepository:

    # We initialise with a database connection
    def __init__(self, connection):
        self._connection = connection

    # Retrieve all students
    def all(self):
        rows = self._connection.execute('SELECT * from students')
        students = []
        for row in rows:
            item = Student(row["id"], row["student_name"], row["cohort_id"])
            students.append(item)
        return students

    # Find a single student by their id
    def find(self, student_id):
        rows = self._connection.execute(
            'SELECT * from students WHERE id = %s', [student_id])
        row = rows[0]
        return Student(row["id"], row["student_name"], row["cohort_id"])

    # Create a new student
    # Do you want to get its id back? Look into RETURNING id;
    def create(self, student):
        self._connection.execute('INSERT INTO students (student_name, cohort_id) VALUES (%s, %s)', [
                                student.student_name, student.cohort_id])
        return None

    # Delete an student by their id
    def delete(self, student_id):
        self._connection.execute(
            'DELETE FROM students WHERE id = %s', [student_id])
        return None
