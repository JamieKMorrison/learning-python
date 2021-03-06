import unittest

from classes import WordCounter

class TestWordCounter(unittest.TestCase):
    @unittest.skip("implement WordCounter")
    def test_word_counter_count(self):
        word_counter = WordCounter()
        word_counter.count("polly")
        word_counter.count("parrot")

        self.assertEquals(word_counter.count(), 2)
        self.assertEquals(word_counter.count(word="polly"), 1)
        self.assertEquals(word_counter.count(word="parrot"), 1)

    @unittest.skip("check that the count tracks dupes correctly")
    def test_word_counter(self):
        word_counter = WordCounter()

        for i in range(3):
            word_counter.count("spam")

        self.assertEquals(word_counter.count(), 3)
        self.assertEquals(word_counter.count(word="spam"), 3)

class TestCapiClient(unittest.TestCase):
    # CAPI has two endpoints: /search and /content_id
    # Each endpoint takes common parameters: page-size, api-key
    # Using test-driven development;
    # create a class hierarchy that creates appropriate url strings for each endpoint
    # but whose parameter handling is shared
    pass
