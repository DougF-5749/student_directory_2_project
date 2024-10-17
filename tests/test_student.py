from lib.student import Student

"""
Student constructs with an id, name and genre
"""
def test_artist_constructs():
    artist = Student(1, "Test Student", 1)
    assert artist.id == 1
    assert artist.student_name == "Test Student"
    assert artist.cohort_id == 1

"""
We can format artists to strings nicely
"""
def test_artists_format_nicely():
    artist = Student(1, "Test Student", "Test Genre")
    assert str(artist) == "Student(1, Test Student, Test Genre)"
    # Try commenting out the `__repr__` method in lib/artist.py
    # And see what happens when you run this test again.

"""
We can compare two identical artists
And have them be equal
"""
def test_artists_are_equal():
    artist1 = Student(1, "Test Student", "Test Genre")
    artist2 = Student(1, "Test Student", "Test Genre")
    assert artist1 == artist2
    # Try commenting out the `__eq__` method in lib/artist.py
    # And see what happens when you run this test again.
