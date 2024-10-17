from lib.student_repository import StudentRepository
from lib.student import Student

"""
When we call StudentRepository#all
We get a list of Student objects reflecting the seed data.
"""
def test_get_all_records(db_connection): # See conftest.py to learn what `db_connection` is.
    db_connection.seed("seeds/student_directory_2.sql") # Seed our database with some test data
    repository = StudentRepository(db_connection) # Create a new StudentRepository

    students = repository.all() # Get all students

    # Assert on the results
    assert students == [
        Student(1, 'Doug', 1),
        Student(2, 'Max', 2),
        Student(3, 'Russ', 3),
        Student(4, 'Frankie', 4),
    ]

"""
When we call StudentRepository#find
We get a single Student object reflecting the seed data.
"""
def test_get_single_record(db_connection):
    db_connection.seed("seeds/student_directory_2.sql")
    repository = StudentRepository(db_connection)

    student = repository.find(3)
    assert student == Student(3, 'Russ', 3)

"""
When we call StudentRepository#create
We get a new record in the database.
"""
def test_create_record(db_connection):
    db_connection.seed("seeds/student_directory_2.sql")
    repository = StudentRepository(db_connection)

    repository.create(Student(None, 'Aaron', '1'))

    result = repository.all()
    assert result == [
        Student(1, 'Doug', 1),
        Student(2, 'Max', 2),
        Student(3, 'Russ', 3),
        Student(4, 'Frankie', 4),
        Student(5, 'Aaron', 1),
    ]

"""
When we call StudentRepository#delete
We remove a record from the database.
"""
def test_delete_record(db_connection):
    db_connection.seed("seeds/student_directory_2.sql")
    repository = StudentRepository(db_connection)
    repository.delete(3) # Apologies to Taylor Swift fans

    result = repository.all()
    assert result == [
        Student(1, 'Doug', 1),
        Student(2, 'Max', 2),
        Student(4, 'Frankie', 4),
    ]
