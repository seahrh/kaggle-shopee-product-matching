from mylib import get_brands


class TestGetBrands:
    def test_case_1(self):
        assert get_brands("smooth anchor beer") == {"anchor"}
        assert get_brands("vanilla anderson's ice cream") == {"anderson's"}
        assert get_brands("vanilla Anderson's ice cream") == {"Anderson's"}
        assert get_brands("vanilla anderson's ice cream anchor beer") == {
            "anderson's",
            "anchor",
        }
