from mylib import hand_translate


class TestHandTranslate:
    def test_input_is_already_en(self):
        assert (
            hand_translate("Paper Bag Victoria Secret") == "Paper Bag Victoria Secret"
        )

    def test_case_1(self):
        assert (
            hand_translate("CELANA WANITA  (BB 45-84 KG)Harem wanita (bisa cod)")
            == "pants women  (BB 45-84 KG)Harem women (can cod)"
        )
        assert (
            hand_translate("Parfum Mobil Botol VLEO SCENTS")
            == "perfume car bottle VLEO SCENTS"
        )

    def test_sarung(self):
        assert (
            hand_translate("sarung")
            == hand_translate("sarong")
            == "wrap knot cover lower body"
        )
