DROP TABLE IF EXISTS students;
DROP SEQUENCE IF EXISTS students_id_seq;

DROP TABLE IF EXISTS cohorts;
DROP SEQUENCE IF EXISTS cohorts_id_seq;

CREATE SEQUENCE IF NOT EXISTS cohorts_id_seq;
CREATE TABLE cohorts (
  id SERIAL PRIMARY KEY,
  cohort_name text,
  start_date text
);

CREATE SEQUENCE IF NOT EXISTS students_id_seq;
CREATE TABLE students (
  id SERIAL PRIMARY KEY,
  student_name text,
  cohort_id int,
  constraint fk_cohort foreign key(cohort_id)
    references students(id)
    on delete cascade
);

INSERT INTO cohorts (cohort_name, start_date) VALUES ('Sept 2024', '2024-09-16');
INSERT INTO cohorts (cohort_name, start_date) VALUES ('Oct 2024', '2024-10-16');
INSERT INTO cohorts (cohort_name, start_date) VALUES ('Nov 2024', '2024-11-16');
INSERT INTO cohorts (cohort_name, start_date) VALUES ('Dec 2024', '2024-12-16');

INSERT INTO students (student_name, cohort_id) VALUES ('Doug', '1');
INSERT INTO students (student_name, cohort_id) VALUES ('Max', '2');
INSERT INTO students (student_name, cohort_id) VALUES ('Russ', '3');
INSERT INTO students (student_name, cohort_id) VALUES ('Frankie', '4');