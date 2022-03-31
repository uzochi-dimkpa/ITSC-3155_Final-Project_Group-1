DROP DATABASE IF EXISTS DuoLing;
CREATE DATABASE IF NOT EXISTS DuoLing;
USE DuoLing;

-- TEMPORARY; WILL EDIT/UPDATE LATER
CREATE TABLE IF NOT EXISTS t_profile  (
	profile_id INT AUTO_INCREMENT NOT NULL,
	first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    profile_role VARCHAR(255) NOT NULL,
	/*
    instructor_id INT AUTO_INCREMENT NOT NULL,
    tenured BOOL NULL DEFAULT 0,
    /**/
    PRIMARY KEY (profile_id)
);

CREATE TABLE IF NOT EXISTS t_question (
	/*
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    class_rank ENUM('freshman', 'sophomore', 'junior', 'senior'),
    year_admitted INT NOT NULL,
    advisor_id INT NULL,
    /**/
    question_id INT AUTO_INCREMENT NOT NULL,
    question_text TEXT NOT NULL,
    PRIMARY KEY (question_id) -- ,
    -- FOREIGN KEY (advisor_id) REFERENCES instructor(instructor_id) ON UPDATE CASCADE ON DELETE SET NULL
);

CREATE TABLE IF NOT EXISTS t_comment (
	/*
    course_id INT AUTO_INCREMENT NOT NULL,
    course_code VARCHAR(255) NOT NULL,
    course_name VARCHAR(255) NOT NULL,
    num_credits INT NOT NULL,
    instructor_id INT NOT NULL,
    /**/
    comment_id INT AUTO_INCREMENT NOT NULL,
    comment_text TEXT NOT NULL,
    PRIMARY KEY (comment_id) -- ,
    -- FOREIGN KEY (instructor_id) REFERENCES instructor(instructor_id) ON UPDATE CASCADE ON DELETE CASCADE
);

/*
CREATE TABLE IF NOT EXISTS student_schedule (
    student_id INT NOT NULL,
    course_id INT NOT NULL,
    PRIMARY KEY (student_id, course_id),
    FOREIGN KEY (student_id) REFERENCES student(student_id) ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (course_id) REFERENCES course(course_id) ON UPDATE CASCADE ON DELETE CASCADE
);
/**/

/*
INSERT INTO instructor (first_name, last_name, tenured)
VALUES
    ('Lauren', 'Garner', 1),
    ('Herman', 'Watts', 0),
    ('Carl', 'Mccarthy', 0),
    ('Sylvia', 'Sanchez', 1)
;
/**/

/*
INSERT INTO student (first_name, last_name, class_rank, year_admitted, advisor_id)
VALUES
    ('Hugh', 'Nichols', 'freshman', 2021, 1),
    ('Carl', 'Mccarthy', 'freshman', 2021, NULL),
    ('Marvin ', 'Sharp', 'sophomore', 2022, 3),
    ('Joyce', 'Harmon', 'junior', 2019, 3),
    ('Doreen', 'Cruz', 'senior', 2018, 1)
;
/**/

/*
INSERT INTO course (course_code, course_name, num_credits, instructor_id)
VALUES
    ('LBST 1102', 'Arts & Society: Film', 3, 2),
    ('ITSC 1213', 'Intro to Computer Science II', 4, 1),
    ('ITSC 1600', 'Computing Professionals', 2, 1),
    ('FILM 3220', 'Intro to Screenwriting', 3, 2),
    ('FILM 3120', 'Fund of Video/Film Prod', 3, 4),
    ('ITSC 3181', 'Intro to Comp Architecture', 4, 3),
    ('ITSC 4155', 'Software Development Projects', 4, 3)
;
/**/

/*
INSERT INTO student_schedule (student_id, course_id)
VALUES
    (1, 1),
    (1, 2),
    (1, 3),
    (2, 2),
    (2, 3),
    (3, 3),
    (3, 4),
    (4, 3),
    (4, 4),
    (4, 5),
    (5, 6)
;
/**/