import unittest
from task_24_3 import MatrixTurn


class MatrixTestCase(unittest.TestCase):
    '''Тестирование'''

    def test_matrix(self):
        '''Проверяем пример по которому выдает ошибку'''
        Matrix = ["123456", "234567", "345678", "456789"]
        MatrixTurn(Matrix, 4, 6, 1)
        self.assertEqual(Matrix, ['212345', '343456', '456767', '567898'])

    def test_matrix_2(self):
        '''Проверяем второй пример по которому выдает ошибку'''
        Matrix = ["123456", "234567", "345678", "456789"]
        MatrixTurn(Matrix, 4, 6, 2)
        self.assertEqual(Matrix, ['321234', '454345', '567656', '678987'])

    def test_matrix_3(self):
        '''Проверяем пример'''
        Matrix = ["123456", "234567", "345678", "456789", "567891", "678912", "789123"]
        MatrixTurn(Matrix, 7, 6, 2)
        self.assertEqual(Matrix, ['321234', '454345', '567656', '678567', '787678', '891989', '912321'])

    def test_matrix_4(self):
        '''Проверяем пример'''
        Matrix = ["123456", "234567", "345678", "456789", "567891", "678912", "789123"]
        MatrixTurn(Matrix, 7, 6, 1)
        self.assertEqual(Matrix, ['212345', '343456', '456567', '567678', '678789', '789191', '891232'])

    def test_matrix_5(self):
        '''Проверяем пример'''
        Matrix = ["123456", "234567", "345678", "456789", "567891", "678912", "789123"]
        MatrixTurn(Matrix, 7, 6, 100)
        self.assertEqual(Matrix, ['232198', '154347', '967856', '876765', '785674', '691983', '543212'])




if __name__ == "__name__":
    unittest.main()