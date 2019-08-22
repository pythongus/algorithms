import unittest


def getUmbrellas(n, p):

    def check_fit():
        fit_size = len(fit)
        right_fit_size = len(right_fit)
        if fit_size or right_fit_size:
            return 1 if right_fit_size < fit_size else len(set(fit))
        return -1

    def change_fit(fitted, i):
        div = (n - fitted) // i
        fitted += i * div
        if n - fitted >= 0:
            fit.extend([i] * div)

        return fitted
    
    def change_right_fit(i):
        div = n // i
        if n - i * div == 0 and (not right_fit or len(right_fit) > div):
            right_fit.clear()
            right_fit.extend([i] * div)
       
    right_fit = []
    fit = []
    sizes = [v for v in sorted(p, reverse=True) if v <= n]
    fitted = 0
    for i in sizes:
        fitted = change_fit(fitted, i)
        change_right_fit(i)
    
    return check_fit()


class TestGetUmbrellas(unittest.TestCase):

    def test_get_umbrellas_0(self):
        n = 6
        p = [3, 5]
        result = getUmbrellas(n, p)
        assert result == 1, f"Actual: {result}" 

    def test_get_umbrellas_1(self):
        n = 1
        p = [2]
        assert getUmbrellas(n, p) == -1

    def test_get_umbrellas_2(self):
        n = 4
        p = [2, 4]
        result = getUmbrellas(n, p)
        assert result == 1, f"Actual: {result}"

    def test_get_umbrellas_3(self):
        n = 7
        p = [1, 4, 9, 2]
        result = getUmbrellas(n, p)
        assert result == 3, f"Actual: {result}"

    def test_get_umbrellas_4(self):
        n = 9
        p = [1, 4, 8, 2]
        result = getUmbrellas(n, p)
        assert result == 2, f"Actual: {result}"

    def test_get_umbrellas_5(self):
        n = 21
        p = [1, 4, 8, 2]
        result = getUmbrellas(n, p)
        assert result == 3, f"Actual: {result}"


if __name__ == "__main__":
    unittest.main()
