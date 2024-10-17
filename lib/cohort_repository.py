from lib.cohort import Cohort

class CohortRepository:

    # We initialise with a database connection
    def __init__(self, connection):
        self._connection = connection

    # Retrieve all cohorts
    def all(self):
        rows = self._connection.execute('SELECT * from cohorts')
        cohorts = []
        for row in rows:
            item = Cohort(row["id"], row["cohort_name"], row["start_date"])
            cohorts.append(item)
        return cohorts

    # Find a single cohort by their id
    def find(self, cohort_id):
        rows = self._connection.execute(
            'SELECT * from cohorts WHERE id = %s', [cohort_id])
        row = rows[0]
        return Cohort(row["id"], row["cohort_name"], row["start_date"])

    # Create a new cohort
    # Do you want to get its id back? Look into RETURNING id;
    def create(self, cohort):
        self._connection.execute('INSERT INTO cohorts (cohort_name, start_date) VALUES (%s, %s)', [
                                cohort.cohort_name, cohort.start_date])
        return None

    # Delete an cohort by their id
    def delete(self, cohort_id):
        self._connection.execute(
            'DELETE FROM cohorts WHERE id = %s', [cohort_id])
        return None
