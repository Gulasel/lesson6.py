import sqlite3

connect = sqlite3.connect("courses.db")
cursor = connect.cursor()

cursor.execute("""
                CREATE TABLE IF NOT EXISTS courses(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    full_name VARCHAR(40) NOT NULL,
                    username VARCHAR(30),
                    age INT DEFAULT NULL, 
                    birth_date DATE,
                    student_id INT NOT NULL,
                    has_laptop BOOLEAN DEFAULT NULL
                )""")

def register():
    full_name = input("Введите ФИО: ")
    username = input("Введите свой username: ")
    age = int(input("Введите возраст: "))
    birth_date = input("Введите дату рождения: ")
    student_id = int(input("Введите свой ID: "))
    has_laptop = input("Есть ли у вас ноутбук? (Да/Нет): ").lower() == 'да'
    
    print("Успешно зарегистрированы!")

    cursor.execute(f"""INSERT INTO courses 
                      (full_name, username, age, birth_date, student_id, has_laptop)
                      VALUES ('{full_name}', '{username}', {age}, '{birth_date}', {student_id}, {has_laptop})""")
    
    connect.commit()

def all_students():
    cursor.execute("SELECT * FROM courses")
    students = cursor.fetchall()
    for student in students:
        print(student)

register()
