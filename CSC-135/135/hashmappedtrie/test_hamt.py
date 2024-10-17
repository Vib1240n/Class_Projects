from hamt import hamt

class TestHamtSolution:

    a = hamt("A", "a")
    b = a.set("B", "b")
    c = b.set("C", "c")
    d = c.set("D", "d")
    e = d.set("E", "e")
    f = e.set("F", "f")

    def test_get_key_A_value_a(self):
        assert self.a.get("A") == 'a'

    def test_get_key_B_value_b(self):
        assert self.b.get("B") == 'b'

    def test_get_key_C_value_c(self):
        assert self.c.get("C") == 'c'

    def test_get_key_D_value_d(self):
        assert self.d.get("D") == 'd'

    def test_get_key_E_value_e(self):
        assert self.e.get("E") == 'e'

    def test_get_key_F_value_f(self):
        assert self.f.get("F") == 'f'
