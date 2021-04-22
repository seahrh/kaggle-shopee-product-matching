from mylib import remove_stopwords


class TestRemoveStopwords:
    def test_monthly_campaign_labels(self):
        assert remove_stopwords("1.1") == ""
        assert remove_stopwords("12.12") == ""
        assert remove_stopwords("123.12") == "123.12"

    def test_case_1(self):
        assert remove_stopwords("you and me") == "  "
        assert remove_stopwords("official product") == " product"
        assert remove_stopwords("guarantee") == ""
        assert remove_stopwords("guaranteed") == ""
        assert remove_stopwords("big sale") == ""
        assert remove_stopwords("bigsale") == ""
        assert remove_stopwords("fashion") == ""
        assert remove_stopwords("fashionable") == ""
