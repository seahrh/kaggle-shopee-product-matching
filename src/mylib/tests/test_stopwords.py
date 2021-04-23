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
        assert remove_stopwords("cod cash on delivery") == " "
        assert remove_stopwords("seller reseller bestseller") == "  "
        assert remove_stopwords("over overall") == " "
        assert remove_stopwords("day days daily") == "  "
        assert remove_stopwords("hour hours hourly") == "  "
        assert remove_stopwords("avail available") == " "
        assert remove_stopwords("for forever") == " "
        assert remove_stopwords("brand branded") == " "
