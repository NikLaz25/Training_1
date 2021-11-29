import unittest
from task_24_2 import MatrixTurn


class MatrixTestCase(unittest.TestCase):
    '''Тестирование'''

    def test_matrix(self):
        '''Проверяем пример по которому выдает ошибку'''
        format_matrix = MatrixTurn(["123456", "234567", "345678", "456789"], 4, 6, 1)
        self.assertEqual(format_matrix, ['212345', '343456', '456767', '567898'])


if __name__ == "__name__":
    unittest.main()