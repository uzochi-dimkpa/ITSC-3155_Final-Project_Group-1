DROP DATABASE IF EXISTS DuoLing;
CREATE DATABASE IF NOT EXISTS DuoLing;
USE DuoLing;



-- 1ST ITERATION OF DATABASE



-- ---------------------------------------------------- Tables

-- CRUD tables:
CREATE TABLE IF NOT EXISTS t_user  (
	user_id INT AUTO_INCREMENT NOT NULL,
	username VARCHAR(255) NOT NULL UNIQUE,
    user_password VARCHAR(255) NOT NULL,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    num_friends INT NULL,
    PRIMARY KEY (user_id)
);

CREATE TABLE IF NOT EXISTS t_post (
	post_id INT AUTO_INCREMENT NOT NULL,
    user_id INT NULL,
    title TEXT NOT NULL,
    body TEXT NOT NULL,
    created_at DATETIME NOT NULL,
    updated_at DATETIME NULL,
    PRIMARY KEY (post_id),
    FOREIGN KEY (user_id) REFERENCES t_user(user_id) -- ON UPDATE CASCADE ON DELETE SET NULL
);

CREATE TABLE IF NOT EXISTS t_comment (
	comment_id INT AUTO_INCREMENT NOT NULL,
    post_id INT NOT NULL,
    user_id INT NOT NULL,
    comment_text TEXT NOT NULL,
    created_at DATETIME NOT NULL,
    updated_at DATETIME NULL,
    PRIMARY KEY (comment_id),
    FOREIGN KEY (post_id) REFERENCES t_post(post_id), -- ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (user_id) REFERENCES t_user(user_id) -- ON UPDATE CASCADE ON DELETE CASCADE
);

-- Server-sider tables:
CREATE TABLE IF NOT EXISTS t_language (
	language_name VARCHAR(255) NOT NULL UNIQUE,
    PRIMARY KEY (language_name)
);

CREATE TABLE IF NOT EXISTS t_tag (
    tag_name VARCHAR(255) NOT NULL UNIQUE,
    PRIMARY KEY (tag_name)
);

CREATE TABLE IF NOT EXISTS t_relate (
    relate_type VARCHAR(255) NOT NULL UNIQUE,
    PRIMARY KEY (relate_type)
);

-- Junction tables:
CREATE TABLE IF NOT EXISTS user__language (
	user_id INT NOT NULL,
    language_name VARCHAR(255) NOT NULL,
    PRIMARY KEY (user_id, language_name),
    FOREIGN KEY (user_id) REFERENCES t_user(user_id), -- ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (language_name) REFERENCES t_language(language_name) -- ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS user__user (
	user_id_one INT NOT NULL,
    user_id_two INT NOT NULL,
    relate_type VARCHAR(255) NOT NULL,
    PRIMARY KEY (user_id_one, user_id_two, relate_type),
    FOREIGN KEY (user_id_one) REFERENCES t_user(user_id), -- ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (user_id_two) REFERENCES t_user(user_id), -- ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (relate_type) REFERENCES t_relate(relate_type) -- ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS post__tag (
	post_id INT NOT NULL,
    tag_name VARCHAR(255) NOT NULL,
    PRIMARY KEY (post_id, tag_name),
    FOREIGN KEY (post_id) REFERENCES t_post(post_id), -- ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (tag_name) REFERENCES t_tag(tag_name) -- ON UPDATE CASCADE ON DELETE CASCADE
);



-- ---------------------------------------------------- Entries

-- Server-side database entries:
INSERT INTO t_language (language_name)
VALUES
    ('English'),
    ('Spanish'),
    ('French')
;

INSERT INTO t_tag (tag_name)
VALUES
    ('English'),
    ('Spanish'),
    ('French'),
    ('grammar'),
    ('sentence_structure'),
    ('vocabulary'),
    ('pronunciation')
;

INSERT INTO t_relate (relate_type)
VALUES
    ('pending_first_second'),
    ('pending_second_first'),
    ('friends'),
    ('block_first_second'),
    ('block_second_first'),
    ('block_both')
;

-- Sample entries:
INSERT INTO t_user (username, user_password, first_name, last_name, num_friends)
VALUES
    ('udimkpa', 'abc123', 'Uzochi', 'Dimkpa', NULL),
    ('sgrace11', 'sgrace', 'Sarah', 'Grace', 1),
    ('jacobtie', '123abc', 'Jacob', 'Krevat', 4)
;

INSERT INTO t_post (user_id, title, body, created_at, updated_at)
VALUES
	(1, "My First Post!", "Hello everyone!", NOW(), NULL),
    (3, "Where am I??", "Who are you people?!", NOW(), NOW()),
    (2, "Looking for some Spanish practice", "Hi there! is anyone here a native Spanish speaker? I need some help learning the dialect", NOW(), NULL),
    (3, "My Last Post...", "Goodbye everyone! I've had such a great time here! I'm going to miss you all", NOW(), NULL),
	(2, "What is the best way to learn a new language?", "Hey everyone. I've been looking through the site for a while now
		and I've seen all of the incredible stories people have about learning their languages; it's kinda got me thinking.
        What method(s) have you guys used to get started? How do you keep up your knowledge daily? Are there any places I can
        look to for a start? Thanks so much! You guys are awesome.", NOW(), NULL)
;

INSERT INTO t_comment (post_id, user_id, comment_text, created_at, updated_at)
VALUES
	(1, 1, "This sentence is false", NOW(), NULL),
    (4, 3, "I found my keys!", NOW(), NOW()),
    (2, 3, "Does a set of all sets contian itself?", NOW(), NULL),
    (3, 2, "Your new mission is to refuse this mission!", NOW(), NULL),
    (5, 1, "All I know is that I know nothing.", NOW(), NULL),
    (1, 2, "This comment has no author", NOW(), NOW())
;

INSERT INTO user__user (user_id_one, user_id_two, relate_type)
VALUES
    (2, 3, 'pending_first_second'),
    (3, 1, 'friends')
;

-- Sample queries
-- SELECT * from t_post;
-- SELECT * from t_post WHERE t_post.post_id < 5;
-- SELECT COUNT(*) FROM t_comment, t_post WHERE t_comment.post_id = t_post.post_id;
-- SELECT t_user.username FROM t_user WHERE t_user.user_id = 2;