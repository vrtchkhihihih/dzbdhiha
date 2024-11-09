import sqlite3

def init_db():
        conn = sqlite3.connect('pethome.db')
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS pethome (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT UNIQUE NOT NULL,
               poroda TEXT NOT NULL
            )
        ''')
        conn.commit()
        conn.close()


def Insert_user(name, poroda):
        conn = sqlite3.connect('pethome.db')
        cursor = conn.cursor()
        cursor.execute ('''INSERT INTO pethome (name, poroda) 
                        VALUES (?,?)''',(name, poroda))

        conn.commit()
        conn.close()

def update_user(id, name, poroda):
    conn = sqlite3.connect('pethome.db')
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE pethome SET name = ?, poroda = ?
        WHERE id = ?
    ''', (name, poroda, id))
    conn.commit()
    conn.close() 
        
def delete_user(id):
    conn = sqlite3.connect('pethome.db')
    cursor = conn.cursor() 
    cursor.execute('DELETE FROM pethome WHERE id = ?', (id,))
    conn.commit()
    conn.close()

def get_user_by_id(id):
    conn = sqlite3.connect('pethome.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM pethome WHERE id = ?', (id,))
    user = cursor.fetchone()  
    conn.close()
    return user

if __name__ == '__main__':
    init_db()
    
    while True:
        choice = input("Введите название функции (update,delete,insert,get,end): ")

        if choice == "update":

            id = int(input("Введите id для обновления: "))
            name = input("Введите новое кличку: ")
            poroda = input("Введите новую порода: ")
            update_user(id, name, poroda)

        elif choice == "delete":

            id = int(input("Введите id для удаления: "))
            delete_user(id)

        elif choice == "insert":

            name = input("Введите кличку: ")
            poroda = input("Введите порода: ")
            Insert_user(name, poroda)

        elif choice == "get":

            id = int(input("Введите id пользователя: "))
            user_data = get_user_by_id(id)
            if user_data:
                print("Данные пользователя:")
                print(f"ID: {user_data[0]}")
                print(f"Кличка: {user_data[1]}")
                print(f"Порода: {user_data[2]}")
            else:
                print(f"Пет с ID {id} не найден.")
        elif choice == "end":
            print("Программа завершена.")
            break

        else:
            print("Некорректный выбор функции. Попробуйте еще раз.")