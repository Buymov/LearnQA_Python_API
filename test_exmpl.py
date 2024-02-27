class TestExample:
    def test_mate(self):
        a = 5
        b = 9
        expected_sum = 14
        assert a + b == expected_sum, f"Сумма значение a and b не равна {expected_sum}"


    def test_mate2(self):
        a = 5
        b = 13
        expected_sum = 14
        assert a + b == expected_sum, f"Сумма значение a and b не равна {expected_sum}"