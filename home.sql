drop table if exists Signup;
create table Signup(
	S_id INTEGER PRIMARY KEY AUTOINCREMENT,
	FirstName TEXT NOT NULL,
	LastName TEXT NOT NULL,
	Password TEXT NOT NULL,
	Email TEXT NOT NULL,
	AccessCode INTEGER
);

drop table if exists Admin;
create table Admin(
	ID INTEGER PRIMARY KEY AUTOINCREMENT,
	Username TEXT NOT NULL,
	Password TEXT NOT NULL
);