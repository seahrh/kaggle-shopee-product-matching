from mylib import get_measurements, Measurement


class TestGetMeasurements:
    def test_gram(self):
        e = {Measurement(quantity=10.1, uom="gram")}
        assert get_measurements("10.1 gram") == e
        assert get_measurements("10.1 grams") == e
        assert get_measurements("10.1 gr") == e
        assert get_measurements("10.1 g") == e
        assert get_measurements("10.1g") == e

    def test_kilogram(self):
        e = {Measurement(quantity=10_100, uom="gram")}
        assert get_measurements("10.1 kilogram") == e
        assert get_measurements("10.1 kilograms") == e
        assert get_measurements("10.1 kilo") == e
        assert get_measurements("10.1 kilos") == e
        assert get_measurements("10.1 kg") == e
        assert get_measurements("10.1kg") == e

    def test_millimetre(self):
        e = {Measurement(quantity=10.1, uom="millimetre")}
        assert get_measurements("10.1 millimetre") == e
        assert get_measurements("10.1 millimetres") == e
        assert get_measurements("10.1 millimeter") == e
        assert get_measurements("10.1 mm") == e
        assert get_measurements("10.1mm") == e

    def test_centimetre(self):
        e = {Measurement(quantity=101, uom="millimetre")}
        assert get_measurements("10.1 centimetre") == e
        assert get_measurements("10.1 centimetres") == e
        assert get_measurements("10.1 centimeter") == e
        assert get_measurements("10.1 cm") == e
        assert get_measurements("10.1cm") == e

    def test_metre(self):
        e = {Measurement(quantity=10_100, uom="millimetre")}
        assert get_measurements("10.1 metre") == e
        assert get_measurements("10.1 metres") == e
        assert get_measurements("10.1 meter") == e
        assert get_measurements("10.1 m") == e
        assert get_measurements("10.1m") == e

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
        e = {Measurement(quantity=10.1, uom="millilitre")}
        assert get_measurements("10.1 millilitre") == e
        assert get_measurements("10.1 millilitres") == e
        assert get_measurements("10.1 milliliter") == e
        assert get_measurements("10.1 ml") == e
        assert get_measurements("10.1ml") == e

    def test_litre(self):
        e = {Measurement(quantity=10_100, uom="millilitre")}
        assert get_measurements("10.1 litre") == e
        assert get_measurements("10.1 litres") == e
        assert get_measurements("10.1 liter") == e
        assert get_measurements("10.1 l") == e
        assert get_measurements("10.1l") == e

    def test_megabyte(self):
        e = {Measurement(quantity=10.1, uom="megabyte")}
        assert get_measurements("10.1 mb") == e
        assert get_measurements("10.1 mib") == e
        assert get_measurements("10.1mb") == e

    def test_gigabyte(self):
        e = {Measurement(quantity=10_100, uom="megabyte")}
        assert get_measurements("10.1 gb") == e
        assert get_measurements("10.1 gib") == e
        assert get_measurements("10.1gb") == e

    def test_megahertz(self):
        e = {Measurement(quantity=10.1, uom="megahertz")}
        assert get_measurements("10.1 mhz") == e
        assert get_measurements("10.1mhz") == e

    def test_gigahertz(self):
        e = {Measurement(quantity=10_100, uom="megahertz")}
        assert get_measurements("10.1 ghz") == e
        assert get_measurements("10.1ghz") == e

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

    def test_real_titles(self):
        assert get_measurements(
            "Apple MacBook Air 13 inch 8GB, 256GB, 1.1GHz Space Gray"
        ) == {
            Measurement(quantity=8000, uom="megabyte"),
            Measurement(quantity=256_000, uom="megabyte"),
            Measurement(quantity=1100, uom="megahertz"),
        }
