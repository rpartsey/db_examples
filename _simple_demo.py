def create_college_table(cur):
    cur.execute(
        """
        create table college(
            college_id serial primary key,
            cname varchar(50) unique not null,
            enrollment int check (enrollment > 0)
        );
        """
    )


def populate_collage_table(cur):
    cur.execute(
        """
        insert into college(college_id, cname, enrollment) 
        values
            (1, 'Stanford', 50000),
            (2, 'Lisotechnichny University', 20000),
            (3, 'Harvard', 100000),
            (4, 'Ukrainian Catholic University', 10000);
        """
    )


def create_student_table(cur):
    cur.execute(
        """
        create table student(
            student_id serial primary key,
            full_name varchar(100),
            email varchar(100),
            gpa numeric(3,2) not null,
            size_hs int not null
        );
        """
    )


def populate_student_table(cur):
    cur.execute(
        """
        insert into student(student_id, full_name, email, gpa, size_hs)
        values 
            (1, 'Derek Dennis', 'dennis@example.com', 4, 1000),
            (2, 'Katherine Goodwin', 'goodwin@example.com', 5, 1000),
            (3, 'Madeline Waters', 'waters@example.com', 3.25, 7500),
            (4, 'Robin Morris', 'morris@example.com', 4.8, 4500),
            (5, 'Jeffrey Davis', 'davis@example.com', 5, 2000);
        """
    )


def create_apply_table(cur):
    cur.execute(
        """
        create table apply(
            apply_id serial primary key,
            student_id int references student(student_id),
            college_id int references college(college_id),
            decision bool,
            major char(3)
        );
        """
    )


def populate_apply_table(cur):
    cur.execute(
        """
        insert into apply(apply_id, student_id, college_id, major, decision)
        values
            (1, 1, 1, 'cs', true),
            (2, 2, 2, 'cs', true),
            (3, 3, 3, 'bio', true),
            (4, 4, 4, 'ba', true),
            (5, 5, 4, 'ba', true);
        """
    )


def init_database(cur):
    # college_table
    create_college_table(cur)
    populate_collage_table(cur)

    # student_table
    create_student_table(cur)
    populate_student_table(cur)

    # apply_table
    create_apply_table(cur)
    populate_apply_table(cur)


# import psycopg2
# from simple_demo import init_database
#
# params = {
#     "user": "postgres",
#     "password": "postgres",
#     "host": "127.0.0.1",
#     "port": "5432",
#     "database": "postgres"
# }

# conn = psycopg2.connect(**params)
# try:
#     cur = conn.cursor()
#     init_database(cur)
# except psycopg2.Error as e:
#     # log error
#     conn.rollback()
# else:
#     conn.commit()
# finally:
#     cur.close()
#     conn.close()

# select * from student;

# select count(*) from apply;

# select student_id, full_name, email, gpa from student s
# inner join apply a on s.student_id = a.student_id

# update college set enrollment = enrollment + 1000
# where cname = 'Stanford'

# select round(avg(gpa), 3) from student;
# select max(gpa) from student;

import psycopg2
params = {
    "user": "postgres",
    "password": "postgres",
    "host": "127.0.0.1",
    "port": "5432",
    "database": "postgres"
}

conn = psycopg2.connect(**params)
try:
    cur = conn.cursor()
    init_database(cur)
except psycopg2.Error as e:
    print(e)
    conn.rollback()
else:
    conn.commit()
finally:
    cur.close()
    conn.close()
