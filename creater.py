import sqlite3 as db
from random import choice, randrange

with open("base.db", "w") as base:
	pass

male_names = ["Алексей", "Александр", "Дмитрий", "Петр", "Сергей", "Виктор", "Евгений", "Ипостасий"]
female_names = ["Алена", "Анастасия", "Татьяна", "Ольга", "Елена"]
surnames = ["Тимофеенко", "Антоненко", "Петренко", "Максименко", "Столенко", "Кесенко", "Виленко", "Сыско", "Пельменей", "Верьеменко", "Порфенко", "Фоменко", "Баненко", "Чехленко", "Коммисенко", "Тарелко", "Гитаренко", "Фуфленко"]
male_last = ["Алексеевич", "Александрович", "Дмитриевич", "Петрович", "Сергеевич", "Викторович", "Евгеньевич", "Ипостасьевич"]
female_last = ["Алексеевна", "Александровна", "Дмитриевна", "Петровна", "Сергеевна", "Викторовна", "Евгеньевна", "Ипостасьевна"]
subjs = ["Математика", "Информатика", "Английский"]

groups = [
	"Прикладная Математика и Информатика",
	"Математика и Компъютерные Науки",
	"Математическое Обеспечение и Администрирование Информационных Систем",
	"Прикладная Информатика",
	"Прикладная Инженерия",
	"Прикладная Математика"
]

def generate_random_name():
	
	gender = choice(["male", "female"])
	
	names = male_names if gender == "male" else female_names
	lasts = male_last if gender == "male" else female_last

	return choice(surnames)+" "+choice(names)+" "+choice(lasts)

database = db.connect("base.db")
cursor = database.cursor()
cursor.execute("CREATE TABLE Students (ID Integer PRIMARY KEY NOT NULL, Name Text, Born DATETIME, Group_ID Integer);")
cursor.execute("CREATE TABLE Groups (ID Integer, Name Text);")
cursor.execute("CREATE TABLE Subjects (ID Integer, Name Text, Group_ID Integer);")
cursor.execute("CREATE TABLE Marks (Student_ID Integer, Subject_ID Integer, Mark Integer);")
#cursor.execute("CREATE TABLE Gen (GenID SERIAL PRIMARY KEY);")

studcount = 100

for i in range(len(groups)):
	cursor.execute("INSERT INTO Groups VALUES (%i, '%s');"%(i+1, groups[i]))

for i in range(len(subjs)):
	cursor.execute("INSERT INTO Subjects VALUES (%i, '%s', %i);"%(i+1, subjs[i], randrange(len(subjs))+1))

for i in range(1, studcount+1):
	fullname = generate_random_name()
	cursor.execute("INSERT INTO Students VALUES (%i, '%s', '%.4i-%.2i-%.2i', %i);"%( i, fullname, randrange(1995, 2000), randrange(1, 12+1), randrange(1, 30), randrange(len(groups))+1) )

for i in range(1, 100001):
	st_id = randrange(i%100 + 1, studcount+1)
	sub_id = randrange(len(subjs))+1
	mark = randrange(2, 6)
	cursor.execute("INSERT INTO Marks VALUES (%i, %i, %i);"%(st_id, sub_id, mark))


database.commit()
database.close()