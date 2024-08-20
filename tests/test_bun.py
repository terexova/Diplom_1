from data import TestText
from praktikum.bun import Bun


class TestBun:
    def test_get_bun_name(self):
        bun = Bun(TestText.bun_name, TestText.bun_price)
        assert bun.get_name() == TestText.bun_name

    def test_get_bun_price(self):
        bun = Bun(TestText.bun_name, TestText.bun_price)
        assert bun.get_price() == TestText.bun_price



