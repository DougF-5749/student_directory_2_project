class Cohort:
    # We initialise with all of our attributes
    # Each column in the table should have an attribute here
    def __init__(self, id, cohort_name, start_date):
        self.id = id
        self.cohort_name = cohort_name
        self.start_date = start_date

    # This method allows our tests to assert that the objects it expects
    # are the objects we made based on the database records.
    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    # This method makes it look nicer when we print an Cohort
    def __repr__(self):
        return f"Cohort({self.id}, {self.cohort_name}, {self.start_date})"
