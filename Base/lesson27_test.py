def is_prime(p: int) -> bool:
    """
    Checks the number P for simplicity using finding the
    remainder of the division in the range [2, P).
    >>> is_prime(42)
    False
    >>> is_prime(73)
    True
    >>> is_prime(3.14)
    Traceback (most recent call last):
    ...
    TypeError: The number P must be an integer type
    >>> is_prime(-100)
    Traceback (most recent call last):
    ...
    ValueError: The number P must be greater than 1
    >>> is_prime(1)
    Traceback (most recent call last):
    ...
    ValueError: The number P must be greater than 1
    >>> is_prime(100_000_001)
    If the number P is prime, the check may take a long time. Working...
    False
    >>> is_prime(100_000_007)
    If the number P is prime, the check may take a long time. Working...
    True
    """
    if not isinstance(p, int):
        raise TypeError('The number P must be an integer type')
    elif p < 2:
        raise ValueError('The number P must be greater than 1')
    elif p > 100_000_000:
        print('If the number P is prime, the check may take a long time. Working...')
    for i in range(2, p):
        if p % i == 0:
            return False
    return True

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)

#запуск из терминала
#python -m doctest Base/lesson27_test.py -v

import unittest
class TestSample(unittest.TestCase):
    def setUp(self) -> None:
        with open('top_secret.txt', 'w', encoding='utf-8') as f:
            for i in range(10):
                f.write(f'{i:05}\n')
    def test_line(self):
        with open('top_secret.txt', 'r', encoding='utf-8') as f:
            for i, line in enumerate(f, start=1):
                pass
            self.assertEqual(i, 10)
    def test_first(self):
        with open('top_secret.txt', 'r', encoding='utf-8') as f:
            first = f.read(5)
            self.assertEqual(first, '00000')
    def tearDown(self) -> None:
        from pathlib import Path
        Path('top_secret.txt').unlink()

if __name__ == '__main__':
    unittest.main(verbosity=2)