from database1 import BDAuth


def ret_new_user(login):
    db = BDAuth()
    db.c.execute(
        '''SELECT * FROM paslog WHERE login=? ''', (login,)
    )
    return db.c.fetchone()


def ins_data(login, password, spec):
    db = BDAuth()
    db.register(login, password, spec)


log = 'pat2'
pas = 'patpass2'
spec = 'Д'

ins_data(log, pas, spec)

print('New user:', ret_new_user(log))
