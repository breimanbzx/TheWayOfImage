import unittest


def get_formatted_name(first, last):
    full_name = f'{first} {last}'
    return full_name.title()


class MyTestCase(unittest.TestCase):
    def test_something(self):
        formatted_name = get_formatted_name('bai', 'zixian')
        self.assertEqual(formatted_name, 'Bai Zixian')


if __name__ == '__main__':
    unittest.main()
