import unittest
from database import BDAuth


class MyTestCase(unittest.TestCase):
    def test_auth(self):
        db = BDAuth()
        self.assertEqual(db.check_pass('doc1', 'docpass'), 'doc')
        self.assertEqual(db.check_pass('pat1', 'patpass'), 'patient')
        self.assertEqual(db.check_pass('man1', 'manpass'), 'manager')

    def test_change_password(self):
        db = BDAuth()
        self.assertEqual(db.change_password('doc1', 'docpass', 'docpass1'), 0)

    def test_del_user(self):
        db = BDAuth()
        self.assertEqual(db.del_user('pat2', 'patpass2'), 0)


if __name__ == '__main__':
    unittest.main()
