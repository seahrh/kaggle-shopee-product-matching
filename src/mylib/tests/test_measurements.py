from mylib import get_measurements, Measurement


class TestGetMeasurements:
    def test_gram(self):
        e = {Measurement(quantity=10, uom="gram")}
        assert get_measurements("10 gram") == e
        assert get_measurements("10 grams") == e
        assert get_measurements("10 gr") == e
        assert get_measurements("10 g") == e
        assert get_measurements("10g") == e

    def test_kilogram(self):
        e = {Measurement(quantity=10_000, uom="gram")}
        assert get_measurements("10 kilogram") == e
        assert get_measurements("10 kilograms") == e
        assert get_measurements("10 kilo") == e
        assert get_measurements("10 kilos") == e
        assert get_measurements("10 kg") == e
        assert get_measurements("10kg") == e

    def test_millimetre(self):
        e = {Measurement(quantity=10, uom="millimetre")}
        assert get_measurements("10 millimetre") == e
        assert get_measurements("10 millimetres") == e
        assert get_measurements("10 millimeter") == e
        assert get_measurements("10 mm") == e
        assert get_measurements("10mm") == e

    def test_centimetre(self):
        e = {Measurement(quantity=100, uom="millimetre")}
        assert get_measurements("10 centimetre") == e
        assert get_measurements("10 centimetres") == e
        assert get_measurements("10 centimeter") == e
        assert get_measurements("10 cm") == e
        assert get_measurements("10cm") == e

    def test_metre(self):
        e = {Measurement(quantity=10_000, uom="millimetre")}
        assert get_measurements("10 metre") == e
        assert get_measurements("10 metres") == e
        assert get_measurements("10 meter") == e
        assert get_measurements("10 m") == e
        assert get_measurements("10m") == e

    def test_multiple_lengths(self):
        assert get_measurements("10x20") == {
            Measurement(quantity=10, uom="millimetre"),
            Measurement(quantity=20, uom="millimetre"),
        }
        assert get_measurements("10x20x30") == {
            Measurement(quantity=10, uom="millimetre"),
            Measurement(quantity=20, uom="millimetre"),
            Measurement(quantity=30, uom="millimetre"),
        }
        assert get_measurements("10 x 20") == {
            Measurement(quantity=10, uom="millimetre"),
            Measurement(quantity=20, uom="millimetre"),
        }
        assert get_measurements("10 x 20 x 30") == {
            Measurement(quantity=10, uom="millimetre"),
            Measurement(quantity=20, uom="millimetre"),
            Measurement(quantity=30, uom="millimetre"),
        }

    def test_millilitre(self):
        e = {Measurement(quantity=10, uom="millilitre")}
        assert get_measurements("10 millilitre") == e
        assert get_measurements("10 millilitres") == e
        assert get_measurements("10 milliliter") == e
        assert get_measurements("10 ml") == e
        assert get_measurements("10ml") == e

    def test_litre(self):
        e = {Measurement(quantity=10_000, uom="millilitre")}
        assert get_measurements("10 litre") == e
        assert get_measurements("10 litres") == e
        assert get_measurements("10 liter") == e
        assert get_measurements("10 l") == e
        assert get_measurements("10l") == e

    def test_piece(self):
        e = {Measurement(quantity=10, uom="piece")}
        assert get_measurements("10 piece") == e
        assert get_measurements("10 pieces") == e
        assert get_measurements("10 pc") == e
        assert get_measurements("10 pcs") == e
        assert get_measurements("10pcs") == e

    def test_box(self):
        e = {Measurement(quantity=10, uom="box")}
        assert get_measurements("10 box") == e
        assert get_measurements("10 boxs") == e
        assert get_measurements("10 boxes") == e
        assert get_measurements("10box") == e

    def test_packet(self):
        e = {Measurement(quantity=10, uom="packet")}
        assert get_measurements("10 packet") == e
        assert get_measurements("10 packets") == e
        assert get_measurements("10 pkt") == e
        assert get_measurements("10 pkts") == e
        assert get_measurements("10packet") == e

    def test_bottle(self):
        e = {Measurement(quantity=10, uom="bottle")}
        assert get_measurements("10 bottle") == e
        assert get_measurements("10 bottles") == e
        assert get_measurements("10bottle") == e
