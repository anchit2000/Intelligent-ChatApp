CREATE database if not exists chat_application;

use chat_application;

create table if not exists user_table (
	id int auto_increment NOT NULL UNIQUE,
 	name_ char(255) NOT null,
    username char(16) NOT null UNIQUE,
    profile_picture blob,
    date_created datetime NOT null,
    password_ char(255) NOT null,
    primary key (id)
);

create index idx_uname on user_table(username);

create table if not exists messages_table(
	message_id int NOT NULL UNIQUE,
    text_message text,
    attachment blob,
    primary key (message_id)
);

create index idx_msg_id on messages_table(message_id);

create table if not exists conversation_table(
	from_ int NOT NULL,
    to_ int NOT NULL,
    message_id int NOT NULL,
    date_sent datetime NOT NULL,
    FOREIGN KEY (message_id) REFERENCES messages_table(message_id),
    FOREIGN KEY (from_) REFERENCES user_table(id),
    FOREIGN KEY (to_) REFERENCES user_table(id)
);

create index msg_idx on conversation_table(message_id);


create table if not exists sentiment_table(
	sentiment int,
    message_id int NOT NULL,
    FOREIGN KEY (message_id) REFERENCES messages_table(message_id)
);

create index msg_idx_sent on sentiment_table(message_id);

create table if not exists user_sentiment(
	negatives int,
    positives int,
    most_recent int,
    user_id int NOT NULL,
    FOREIGN KEY (user_id) REFERENCES user_table(id)
);

create index user_sent on user_sentiment(user_id);

create table if not exists user_likes_dislikes(
	user_id int NOT NULL UNIQUE,
    likes text,
    dislikes text,
    NER text,
    message_id int NOT NULL UNIQUE,
    FOREIGN KEY (user_id) REFERENCES user_table(id),
    FOREIGN KEY (message_id) REFERENCES messages_table(message_id)
);

create index user_like_dislike on user_likes_dislikes(user_id,message_id);