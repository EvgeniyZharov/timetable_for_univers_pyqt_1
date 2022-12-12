import pymysql
from config import host, user, password, db_name

con = pymysql.connect(
    host=host,
    port=3306,
    user=user,
    password=password,
    # database=db_name,
    cursorclass=pymysql.cursors.DictCursor
)

DATABASE_NAME = "project_database_1"
TABLES = ["course", "stud_group", "student", "positions", "department", "worker", "type_table", "corpus",
          "classroom", "academic_plan", "direction", "subjects", "timetable", "count_classroom", "class_type"]

"""

drop function if exists project_database_1.conc;

delimiter $$
create function project_database_1.conc(a char(20), b char(20)) returns char(20)
deterministic
begin
	DECLARE с char(20);
	SET с = concat(a, "  ", b);
	return с;
END;
$$
delimiter ;

select project_database_1.conc("test:", "number"); 

"""


"""

drop procedure if exists project_database_1.proc;

DELIMITER //
CREATE PROCEDURE project_database_1.proc (a char(20))
BEGIN

    select * 
    from project_database_1.timetable
    where title = a;
END //
DELIMITER ;

call project_database_1.proc("one");

"""

# TRIGGERS

"""

-- CREATE TRIGGER project_database_1.up_count_classroom AFTER INSERT ON project_database_1.classroom
-- FOR EACH ROW UPDATE project_database_1.count_classroom SET count = (count + 1) WHERE id_corpus = NEW.id_corpus;

-- CREATE TRIGGER project_database_1.down_count_classroom BEFORE DELETE ON project_database_1.classroom
-- FOR EACH ROW UPDATE project_database_1.count_classroom SET count = (count - 1) WHERE id_corpus = OLD.id_corpus;

"""


def sql_procedure_timetable(title):
    request = f"call project_database_1.proc('{title}');"
    with con.cursor() as cur:
        cur.execute(request)
        return cur.fetchall()[0]

# print(sql_procedure_timetable("one"))


def sql_function_conc(value_one, value_two):
    request = f"select project_database_1.conc('{value_one}', '{value_two}');"
    with con.cursor() as cur:
        cur.execute(request)
        return cur.fetchone()[f"project_database_1.conc('{value_one}', '{value_two}')"]

# print(sql_function_conc("Количество классов:", 45))


def create_main_db():
    try:
        request = f"CREATE DATABASE IF NOT EXISTS project_database_1;"
        with con.cursor() as cur:
            cur.execute(request)
            con.commit()
            return True
    except Exception:
        return False


def create_course_table():
    try:
        request = """CREATE TABLE IF NOT EXISTS project_database_1.course (id_course_code int AUTO_INCREMENT,
								 course_number int UNIQUE,
                                 PRIMARY KEY(id_course_code));"""
        with con.cursor() as cur:
            cur.execute(request)
            con.commit()
            return True
    except Exception:
        return False


def create_stud_group_table():
    try:
        request = """CREATE TABLE IF NOT EXISTS project_database_1.stud_group (id_group_code int AUTO_INCREMENT,
								 id_course_code int,
                                 group_name VARCHAR(20) UNIQUE,
                                 FOREIGN KEY(id_course_code) REFERENCES course(id_course_code) ON DELETE CASCADE ON UPDATE CASCADE,
                                 PRIMARY KEY(id_group_code));"""
        with con.cursor() as cur:
            cur.execute(request)
            con.commit()
            return True
    except Exception:
        return False


def create_student_table():
    try:
        request = """CREATE TABLE IF NOT EXISTS project_database_1.student (id_student_code int AUTO_INCREMENT,
								 id_group_code int,
                                 stud_name VARCHAR(20),
                                 student_ticket_number VARCHAR(20) UNIQUE,
                                 FOREIGN KEY(id_group_code) REFERENCES stud_group(id_group_code) ON DELETE CASCADE ON UPDATE CASCADE,
                                 PRIMARY KEY(id_student_code));"""
        with con.cursor() as cur:
            cur.execute(request)
            con.commit()
            return True
    except Exception:
        return False


def create_positions_table():
    try:
        request = """CREATE TABLE IF NOT EXISTS project_database_1.positions (id_position_code int AUTO_INCREMENT,
								 position_name VARCHAR(20) UNIQUE,
                                 PRIMARY KEY(id_position_code));"""
        with con.cursor() as cur:
            cur.execute(request)
            con.commit()
            return True
    except Exception:
        return False


def create_department_table():
    try:
        request = """CREATE TABLE IF NOT EXISTS project_database_1.department (id_department_code int AUTO_INCREMENT,
                                 department_name VARCHAR(20) UNIQUE,
                                 PRIMARY KEY(id_department_code));"""
        with con.cursor() as cur:
            cur.execute(request)
            con.commit()
            return True
    except Exception:
        return False


def create_worker_table():
    try:
        request = """CREATE TABLE IF NOT EXISTS project_database_1.worker (id_worker_code int AUTO_INCREMENT,
                                 worker_name VARCHAR(20) UNIQUE,
                                 id_department_code int,
                                 id_position_code int,
                                 FOREIGN KEY(id_department_code) REFERENCES department(id_department_code) ON DELETE CASCADE ON UPDATE CASCADE,
                                 FOREIGN KEY(id_position_code) REFERENCES positions(id_position_code) ON DELETE CASCADE ON UPDATE CASCADE,
                                 PRIMARY KEY(id_worker_code));"""
        with con.cursor() as cur:
            cur.execute(request)
            con.commit()
            return True
    except Exception:
        return False


def create_corpus_table():
    try:
        request = """CREATE TABLE IF NOT EXISTS project_database_1.corpus (id_corpus int AUTO_INCREMENT,
                                 corpus_name VARCHAR(20) UNIQUE,
                                 PRIMARY KEY(id_corpus));"""
        with con.cursor() as cur:
            cur.execute(request)
            con.commit()
            return True
    except Exception:
        return False


def create_classroom_table():
    try:
        request = """CREATE TABLE IF NOT EXISTS project_database_1.classroom (id_classroom_code int AUTO_INCREMENT,
                                 id_corpus int,
                                 number VARCHAR(20) UNIQUE,
                                 FOREIGN KEY(id_corpus) REFERENCES corpus(id_corpus) ON DELETE CASCADE ON UPDATE CASCADE,
                                 PRIMARY KEY(id_classroom_code));"""
        with con.cursor() as cur:
            cur.execute(request)
            con.commit()
            return True
    except Exception:
        return False


def create_academic_plan_table():
    try:
        request = """CREATE TABLE IF NOT EXISTS project_database_1.academic_plan (id_academic_plan_code int AUTO_INCREMENT,
                                 hours int UNIQUE,
                                 PRIMARY KEY(id_academic_plan_code));"""
        with con.cursor() as cur:
            cur.execute(request)
            con.commit()
            return True
    except Exception:
        return False


def create_direction_table():
    try:
        request = """CREATE TABLE IF NOT EXISTS project_database_1.direction (id_direction_code int AUTO_INCREMENT,
                                 title VARCHAR(20) UNIQUE UNIQUE,
                                 id_academic_plan_code int,
                                 FOREIGN KEY(id_academic_plan_code) REFERENCES academic_plan(id_academic_plan_code) ON DELETE CASCADE ON UPDATE CASCADE,
                                 PRIMARY KEY(id_direction_code));"""
        with con.cursor() as cur:
            cur.execute(request)
            con.commit()
            return True
    except Exception:
        return False


def create_subjects_table():
    try:
        request = """CREATE TABLE IF NOT EXISTS project_database_1.subjects (id_subjects_code int AUTO_INCREMENT,
                                 subjects_name VARCHAR(20) UNIQUE, 
                                 id_direction_code int,
                                 FOREIGN KEY(id_direction_code) REFERENCES direction(id_direction_code) ON DELETE CASCADE ON UPDATE CASCADE,
                                 PRIMARY KEY(id_subjects_code));"""
        with con.cursor() as cur:
            cur.execute(request)
            con.commit()
            return True
    except Exception:
        return False


def create_class_type_table():
    try:
        request = """CREATE TABLE IF NOT EXISTS project_database_1.class_type (id_class_type_code int AUTO_INCREMENT,
                                 title VARCHAR(20) UNIQUE,
                                 PRIMARY KEY(id_class_type_code));"""
        with con.cursor() as cur:
            cur.execute(request)
            con.commit()
            return True
    except Exception:
        return False


def create_timetable_table():
    try:
        request = """CREATE TABLE IF NOT EXISTS project_database_1.timetable (id_group_code int,
                                 id_classroom_code int,
                                 id_subjects_code int,
                                 id_worker_code int,
                                 id_class_type_code int,
                                 title VARCHAR(20) UNIQUE,
                                 FOREIGN KEY(id_group_code) REFERENCES stud_group(id_group_code) ON DELETE CASCADE ON UPDATE CASCADE,
                                 FOREIGN KEY(id_classroom_code) REFERENCES classroom(id_classroom_code) ON DELETE CASCADE ON UPDATE CASCADE,
                                 FOREIGN KEY(id_subjects_code) REFERENCES subjects(id_subjects_code) ON DELETE CASCADE ON UPDATE CASCADE,
                                 FOREIGN KEY(id_worker_code) REFERENCES worker(id_worker_code) ON DELETE CASCADE ON UPDATE CASCADE,
                                 FOREIGN KEY(id_class_type_code) REFERENCES class_type(id_class_type_code) ON DELETE CASCADE ON UPDATE CASCADE,
                                 PRIMARY KEY(title));"""
        with con.cursor() as cur:
            cur.execute(request)
            con.commit()
            return True
    except Exception:
        return False


def create_count_classroom_table():
    try:
        request = """CREATE TABLE IF NOT EXISTS project_database_1.count_classroom (id_corpus int,
                                 count int,
                                 FOREIGN KEY(id_corpus) REFERENCES corpus(id_corpus) ON DELETE CASCADE ON UPDATE CASCADE,
                                 PRIMARY KEY(id_corpus));"""
        with con.cursor() as cur:
            cur.execute(request)
            con.commit()
            return True
    except Exception:
        return False



print(create_main_db())
print(create_course_table())
print(create_stud_group_table())
print(create_student_table())
print(create_positions_table())
print(create_department_table())
print(create_worker_table())
print(create_corpus_table())
print(create_classroom_table())
print(create_academic_plan_table())
print(create_direction_table())
print(create_subjects_table())
print(create_class_type_table())
print(create_timetable_table())
print(create_count_classroom_table())


def describe_users_table(table):
    if table in TABLES:
        show_table_query = f"DESCRIBE {DATABASE_NAME}.{table}"
        with con.cursor() as cur:
            cur.execute(show_table_query)
            # Fetch rows from last executed query
            result = cur.fetchall()
            for row in result:
                print(row)


# describe_users_table("timetable")


def add_course_in_table(course_number):
    try:
        request = "INSERT INTO project_database_1.course (course_number) VALUES (%s);"
        # request = "INSERT INTO users (name) VALUES (%s)"
        record = [(course_number,)]
        with con.cursor() as cur:
            cur.executemany(request, record)
            con.commit()
        return True
    except Exception:
        return False


def add_stud_group_in_table(id_course_code, group_name):
    try:
        request = "INSERT INTO project_database_1.stud_group (id_course_code, group_name) VALUES (%s, %s);"
        record = [(id_course_code, group_name)]
        with con.cursor() as cur:
            cur.executemany(request, record)
            con.commit()
        return True
    except Exception:
        return False


def add_student_in_table(id_group_code, stud_name, student_ticket_number):
    try:
        request = "INSERT INTO project_database_1.student (id_group_code, stud_name, student_ticket_number) VALUES (%s, %s, %s);"
        # request = "INSERT INTO users (name) VALUES (%s)"
        record = [(id_group_code, stud_name, student_ticket_number)]
        with con.cursor() as cur:
            cur.executemany(request, record)
            con.commit()
        return True
    except Exception:
        return False


def add_positions_in_table(position_name):
    try:
        request = "INSERT INTO project_database_1.positions (position_name) VALUES (%s);"
        # request = "INSERT INTO users (name) VALUES (%s)"
        record = [(position_name,)]
        with con.cursor() as cur:
            cur.executemany(request, record)
            con.commit()
        return True
    except Exception:
        return False


def add_department_in_table(department_name):
    try:
        request = "INSERT INTO project_database_1.department (department_name) VALUES (%s);"
        # request = "INSERT INTO users (name) VALUES (%s)"
        record = [(department_name,)]
        with con.cursor() as cur:
            cur.executemany(request, record)
            con.commit()
        return True
    except Exception:
        return False


def add_worker_in_table(worker_name, id_department_code, id_position_code):
    try:
        request = "INSERT INTO project_database_1.worker (worker_name, id_department_code, id_position_code) VALUES (%s, %s, %s);"
        # request = "INSERT INTO users (name) VALUES (%s)"
        record = [(worker_name, id_department_code, id_position_code)]
        with con.cursor() as cur:
            cur.executemany(request, record)
            con.commit()
        return True
    except Exception:
        return False


def add_count_classroom_in_table(id_corpus):
    try:
        request = "INSERT INTO project_database_1.count_classroom (id_corpus, count) VALUES (%s, %s);"
        # request = "INSERT INTO users (name) VALUES (%s)"
        record = [(id_corpus, 0)]
        with con.cursor() as cur:
            cur.executemany(request, record)
            con.commit()
            return True
    except Exception:
        return False


def add_corpus_in_table(corpus_name):
    try:
        request = "INSERT INTO project_database_1.corpus (corpus_name) VALUES (%s);"
        # request = "INSERT INTO users (corpus_name) VALUES (%s)"
        record = [(corpus_name,)]
        with con.cursor() as cur:
            cur.executemany(request, record)
            con.commit()

            request = "SELECT id_corpus FROM project_database_1.corpus WHERE corpus_name = (%s)"
            cur.execute(request, (corpus_name,))
            corpus_id = cur.fetchall()[0]["id_corpus"]
            print(add_count_classroom_in_table(corpus_id))
        return True
    except Exception:
        return False


def add_classroom_in_table(id_corpus, number):
    try:
        request = "INSERT INTO project_database_1.classroom (id_corpus, number) VALUES (%s, %s);"
        # request = "INSERT INTO users (name) VALUES (%s)"
        record = [(id_corpus, number)]
        with con.cursor() as cur:
            cur.executemany(request, record)
            con.commit()
        return True
    except Exception:
        return False


def add_academic_plan_in_table(hours):
    try:
        request = "INSERT INTO project_database_1.academic_plan (hours) VALUES (%s);"
        # request = "INSERT INTO users (name) VALUES (%s)"
        record = [(hours)]
        with con.cursor() as cur:
            cur.executemany(request, record)
            con.commit()
        return True
    except Exception:
        return False


def add_direction_in_table(title, id_academic_plan_code):
    try:
        request = "INSERT INTO project_database_1.direction (title, id_academic_plan_code) VALUES (%s, %s);"
        # request = "INSERT INTO users (name) VALUES (%s)"
        record = [(title, id_academic_plan_code)]
        with con.cursor() as cur:
            cur.executemany(request, record)
            con.commit()
        return True
    except Exception:
        return False


def add_subjects_in_table(subjects_name, id_direction_code):
    try:
        request = "INSERT INTO project_database_1.subjects (subjects_name, id_direction_code) VALUES (%s, %s);"
        # request = "INSERT INTO users (name) VALUES (%s)"
        record = [(subjects_name, id_direction_code)]
        with con.cursor() as cur:
            cur.executemany(request, record)
            con.commit()

        return True
    except Exception:
        return False


def add_class_type_in_table(title):
    try:
        request = "INSERT INTO project_database_1.class_type (title) VALUES (%s);"
        # request = "INSERT INTO users (name) VALUES (%s)"
        record = [(title,)]
        with con.cursor() as cur:
            cur.executemany(request, record)
            con.commit()

        return True
    except Exception:
        return False


def add_timetable_in_table(id_group_code, id_classroom_code, id_subjects_code, id_worker_code, id_class_type_code, title):
    try:
        request = "INSERT INTO project_database_1.timetable (id_group_code, id_classroom_code, id_subjects_code, id_worker_code, id_class_type_code, title) VALUES (%s, %s, %s, %s, %s, %s);"
        # request = "INSERT INTO users (name) VALUES (%s)"
        record = [(id_group_code, id_classroom_code, id_subjects_code, id_worker_code, id_class_type_code, title)]
        with con.cursor() as cur:
            cur.executemany(request, record)
            con.commit()

        return True
    except Exception:
        return False


course_number = 1
id_course_cod = 1
id_group_cod = 1
id_department = 1
id_position = 1
hours = 40
id_academic_plan = 1
id_direction = 1
id_corpus = 1
id_classroom = 69
id_subject = 1
id_worker = 1
id_class_type = 1

print("#"*100)
print(add_course_in_table(course_number))
print(add_stud_group_in_table(id_course_cod, "SECOND"))
print(add_student_in_table(id_group_cod, "Ivan", "334hdsl3"))
print(add_positions_in_table("buhg"))
print(add_department_in_table("Count money"))
print(add_worker_in_table("Vladimir", id_department, id_position))
print(add_academic_plan_in_table(hours))
print(add_direction_in_table("IT", id_academic_plan))
print(add_subjects_in_table("math", id_direction))
print(add_corpus_in_table("E"))
print(add_classroom_in_table(id_corpus, "13sd312"))
print(add_class_type_in_table("First"))
print(add_timetable_in_table(id_group_cod, id_classroom, id_subject, id_worker, id_class_type, "two"))
print("#"*100)


# UPDATE

def update_student(stud_name, student_ticket_number, id_group_code, id_student_code):
    try:
        request = f"UPDATE project_database_1.student SET stud_name = '{stud_name}' WHERE id_student_code = {id_student_code}"
        with con.cursor() as cur:
            cur.execute(request)
            con.commit()
        request = f"UPDATE project_database_1.student SET student_ticket_number = '{student_ticket_number}' WHERE id_student_code = {id_student_code}"
        with con.cursor() as cur:
            cur.execute(request)
            con.commit()
        request = f"UPDATE project_database_1.student SET id_group_code = '{id_group_code}' WHERE id_student_code = {id_student_code}"
        with con.cursor() as cur:
            cur.execute(request)
            con.commit()

        return True
    except Exception:
        return False


def update_classroom(number, id_corpus, id_classroom_code):
    try:
        request = f"UPDATE project_database_1.classroom SET id_corpus = '{id_corpus}' WHERE id_classroom_code = {id_classroom_code}"
        with con.cursor() as cur:
            cur.execute(request)
            con.commit()
        request = f"UPDATE project_database_1.classroom SET number = '{number}' WHERE id_classroom_code = {id_classroom_code}"
        with con.cursor() as cur:
            cur.execute(request)
            con.commit()

        return True
    except Exception:
        return False



# SELECT


def get_table(table_title):
    if table_title in TABLES:
        request = f"SELECT * FROM {DATABASE_NAME}.{table_title}"
        with con.cursor() as cur:
            cur.execute(request)
        return cur.fetchall()


print("#" * 100)
print(get_table("course"))
print(get_table("stud_group"))
print(get_table("student"))
print(get_table("positions"))
print(get_table("department"))
print(get_table("worker"))
print(get_table("corpus"))
print(get_table("classroom"))
print(get_table("academic_plan"))
print(get_table("direction"))
print(get_table("subjects"))
print(get_table("class_type"))
print(get_table("timetable"))
print(get_table("count_classroom"))
print("#" * 100)


# DELETE


def del_course_from_table(course_number):
    try:
        request = f"DELETE FROM project_database_1.course WHERE course_number = '{course_number}'"
        with con.cursor() as cur:
            cur.execute(request)
            con.commit()
            return True
    except Exception:
        return False


def del_stud_group_from_table(group_name):
    try:
        request = f"DELETE FROM project_database_1.stud_group WHERE group_name = '{group_name}'"
        with con.cursor() as cur:
            cur.execute(request)
            con.commit()
            return True
    except Exception:
        return False


def del_student_from_table(student_ticket_number):
    try:
        request = f"DELETE FROM project_database_1.student WHERE student_ticket_number = '{student_ticket_number}'"
        with con.cursor() as cur:
            cur.execute(request)
            con.commit()
            return True
    except Exception:
        return False


def del_positions_from_table(position_name):
    try:
        request = f"DELETE FROM project_database_1.positions WHERE position_name = '{position_name}'"
        with con.cursor() as cur:
            cur.execute(request)
            con.commit()
            return True
    except Exception:
        return False


def del_department_from_table(department_name):
    try:
        request = f"DELETE FROM project_database_1.department WHERE department_name = '{department_name}'"
        with con.cursor() as cur:
            cur.execute(request)
            con.commit()
            return True
    except Exception:
        return False


def del_worker_from_table(id_worker_code):
    try:
        request = f"DELETE FROM project_database_1.worker WHERE id_worker_code = '{id_worker_code}'"
        with con.cursor() as cur:
            cur.execute(request)
            con.commit()
            return True
    except Exception:
        return False


def del_type_table_from_table(type_name):
    try:
        request = f"DELETE FROM project_database_1.type_table WHERE type_name = '{type_name}'"
        with con.cursor() as cur:
            cur.execute(request)
            con.commit()
            return True
    except Exception:
        return False


def del_corpus_from_table(corpus_name):
    try:
        request = f"DELETE FROM project_database_1.corpus WHERE corpus_name = '{corpus_name}'"
        with con.cursor() as cur:
            cur.execute(request)
            con.commit()
            return True
    except Exception:
        return False


def del_classroom_from_table(number):
    try:
        request = f"DELETE FROM project_database_1.classroom WHERE number = '{number}'"
        with con.cursor() as cur:
            cur.execute(request)
            con.commit()
            return True
    except Exception:
        return False


def del_academic_plan_from_table(hours):
    try:
        request = f"DELETE FROM project_database_1.academic_plan WHERE hours = '{hours}'"
        with con.cursor() as cur:
            cur.execute(request) 
            con.commit()
            return True
    except Exception:
        return False


def del_direction_from_table(title):
    try:
        request = f"DELETE FROM project_database_1.direction WHERE title = '{title}'"
        with con.cursor() as cur:
            cur.execute(request)
            con.commit()
            return True
    except Exception:
        return False


def del_subjects_from_table(subjects_name):
    try:
        request = f"DELETE FROM project_database_1.subjects WHERE subjects_name = '{subjects_name}'"
        with con.cursor() as cur:
            cur.execute(request)
            con.commit()
            return True
    except Exception:
        return False


def del_timetable_from_table(title):
    try:
        request = f"DELETE FROM project_database_1.timetable WHERE title = '{title}'"
        with con.cursor() as cur:
            cur.execute(request)
            con.commit()
            return True
    except Exception:
        return False


