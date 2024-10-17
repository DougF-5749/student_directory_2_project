from lib.cohort_repository import CohortRepository
from lib.cohort import Cohort

"""
When we call CohortRepository#all
We get a list of Cohort objects reflecting the seed data.
"""
def test_get_all_records(db_connection): # See conftest.py to learn what `db_connection` is.
    db_connection.seed("seeds/student_directory_2.sql") # Seed our database with some test data
    repository = CohortRepository(db_connection) # Create a new CohortRepository

    cohorts = repository.all() # Get all cohorts

    # Assert on the results
    assert cohorts == [
        Cohort(1, 'Sept 2024', '2024-09-16'),
        Cohort(2, 'Oct 2024', '2024-10-16'),
        Cohort(3, 'Nov 2024', '2024-11-16'),
        Cohort(4, 'Dec 2024', '2024-12-16'),
    ]

"""
When we call CohortRepository#find
We get a single Cohort object reflecting the seed data.
"""
def test_get_single_record(db_connection):
    db_connection.seed("seeds/student_directory_2.sql")
    repository = CohortRepository(db_connection)

    artist = repository.find(3)
    assert artist == Cohort(3, 'Nov 2024', '2024-11-16')

"""
When we call CohortRepository#create
We get a new record in the database.
"""
def test_create_record(db_connection):
    db_connection.seed("seeds/student_directory_2.sql")
    repository = CohortRepository(db_connection)

    repository.create(Cohort(None, 'Jan 2025', '2025-01-16'))

    result = repository.all()
    assert result == [
        Cohort(1, 'Sept 2024', '2024-09-16'),
        Cohort(2, 'Oct 2024', '2024-10-16'),
        Cohort(3, 'Nov 2024', '2024-11-16'),
        Cohort(4, 'Dec 2024', '2024-12-16'),
        Cohort(5, 'Jan 2025', '2025-01-16'),
    ]

"""
When we call CohortRepository#delete
We remove a record from the database.
"""
def test_delete_record(db_connection):
    db_connection.seed("seeds/student_directory_2.sql")
    repository = CohortRepository(db_connection)
    repository.delete(3) # Apologies to Taylor Swift fans

    result = repository.all()
    assert result == [
        Cohort(1, 'Sept 2024', '2024-09-16'),
        Cohort(2, 'Oct 2024', '2024-10-16'),
        Cohort(4, 'Dec 2024', '2024-12-16'),
    ]
