from mylib import remove_stopwords


class TestRemoveStopwords:
    def test_monthly_campaign_labels(self):
        assert remove_stopwords("1.1") == ""
        assert remove_stopwords("12.12") == ""
        assert remove_stopwords("123.12") == "123.12"

    def test_case_1(self):
        assert remove_stopwords("you and me") == "  "
        assert remove_stopwords("official product") == " "
        assert remove_stopwords("guarantee guaranteed") == " "
        assert remove_stopwords("big sale bigsale") == " "
        assert remove_stopwords("fashion fashionable") == " "
        assert remove_stopwords("offer") == ""
        assert remove_stopwords("promo promotion") == " "
        assert remove_stopwords("to too") == " "
