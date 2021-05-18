from database import BDAuth


def check_count():
    db = BDAuth()
    db.c.execute(
        ''' SELECT * FROM paslog'''
    )
    return len(db.c.fetchall())


def ret_new_user(login):
    db = BDAuth()
    db.c.execute(
        '''SELECT * FROM paslog WHERE login=? ''', (login,)
    )
    return db.c.fetchone()


def ins_data(login, password, spec):
    db = BDAuth()
    db.register(login, password, spec)


a = check_count()

log = input()
pas = input()
spec = input()

ins_data(log, pas, spec)

b = check_count()
if a < b:
    print('Ok')
else:
    print('Error')

print('Новый пользователь:', ret_new_user(log))
