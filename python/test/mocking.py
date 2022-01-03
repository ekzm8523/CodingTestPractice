from unittest.mock import MagicMock


# def test(a, b, /, d):
#     return a, b, d


class ProductionClass:
    def method(self):
        self.something(1, 2, 3)
    def something(self, a, b, c):
        pass

if __name__ == '__main__':

    real = ProductionClass()
    real.something = MagicMock()
    real.method()
    real.something.assert_called_once_with(1, 2, 4)

