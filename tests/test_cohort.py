from lib.cohort import Cohort

"""
Cohort constructs with an id, name and genre
"""
def test_cohort_constructs():
    cohort = Cohort(1, "Test Cohort", "Test Genre")
    assert cohort.id == 1
    assert cohort.cohort_name == "Test Cohort"
    assert cohort.start_date == "Test Genre"

"""
We can format cohorts to strings nicely
"""
def test_cohorts_format_nicely():
    cohort = Cohort(1, "Test Cohort", "Test Genre")
    assert str(cohort) == "Cohort(1, Test Cohort, Test Genre)"
    # Try commenting out the `__repr__` method in lib/cohort.py
    # And see what happens when you run this test again.

"""
We can compare two identical cohorts
And have them be equal
"""
def test_cohorts_are_equal():
    cohort1 = Cohort(1, "Test Cohort", "Test Genre")
    cohort2 = Cohort(1, "Test Cohort", "Test Genre")
    assert cohort1 == cohort2
    # Try commenting out the `__eq__` method in lib/cohort.py
    # And see what happens when you run this test again.
