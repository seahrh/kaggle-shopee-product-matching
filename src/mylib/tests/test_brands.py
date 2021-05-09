from mylib import get_brands


class TestGetBrands:
    def test_case_1(self):
        assert get_brands("smooth anchor beer") == {"anchor"}
        assert get_brands("vanilla anderson's ice cream") == {"anderson's"}
        assert get_brands("vanilla ANDERSON's ice cream") == {"anderson's"}
        assert get_brands("vanilla anderson's ice cream anchor beer") == {
            "anderson's",
            "anchor",
        }

    def test_real_titles(self):
        assert get_brands("Nescafe Eclair Latte 220ml") == {"nescafe"}
        assert get_brands(
            "battery Lenovo A7000  7000 K3 Note BL243 BL 243 Double Power battery Batrai"
        ) == {"lenovo"}
        assert get_brands(
            "cable Data short Pipih Powerbank Charger Handphone Android Micro 20CM Samsung Xiaomi Oppo VIvo"
        ) == {"vivo", "samsung", "xiaomi", "oppo"}
