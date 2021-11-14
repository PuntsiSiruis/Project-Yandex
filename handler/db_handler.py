import sqlite3
import self


from main import Interface, Interface2

#def son(self):
   # self.int4 = Interface()
    #self.int4.setVisible(False)

def run2(self):
    self.int5 = Interface2()
    self.int5.show()


def login(login, passw, signal):
    con = sqlite3.connect('handler/users')
    cur = con.cursor()

    # Проверяем есть ли такой пользователь
    cur.execute(f'SELECT * FROM users WHERE name="{login}";')
    value = cur.fetchall()

    if value != [] and value[0][2] == passw:
        signal.emit('Успешная авторизация!')
        run2(self)
        #son(self)
    else:
        signal.emit('Проверьте правильность ввода данных!')

    cur.close()
    con.close()


def register(login, passw, signal):
    con = sqlite3.connect('handler/users')
    cur = con.cursor()

    cur.execute(f'SELECT * FROM users WHERE name="{login}";')
    value = cur.fetchall()


    if value != []:
        signal.emit('Такой ник уже используется!')

    elif len(value) >= 5:
        signal.emit('В строках Логин и Пароль минимальное количество символов - 5')

    else:
        value == []
        cur.execute(f"INSERT INTO users (name, password) VALUES ('{login}', '{passw}')")
        signal.emit('Вы успешно зарегистрированы!')
        con.commit()

    cur.close()
    con.close()