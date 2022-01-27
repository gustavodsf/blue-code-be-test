
from app.src.short_urls.converter import Converter
from unittest import TestCase

class TestConverter(TestCase):

    def test_give_string_to_generate_shorter(self):
        converter = Converter()
        with self.assertRaises(Exception):
          converter.id_to_shortURL('');

    def test_give_send_number_disconvert_generate_shorter(self):
        converter = Converter()
        with self.assertRaises(Exception):
          converter.shortURL_to_id(10);

    def test_with_small_number(self):
        converter = Converter()
        self.assertEqual(converter.id_to_shortURL(10), 'k');
        self.assertEqual(converter.shortURL_to_id("k"), 10);

    def test_with_medium_number(self):
        converter = Converter()
        self.assertEqual(converter.id_to_shortURL(1000), 'qi');
        self.assertEqual(converter.shortURL_to_id("qi"), 1000);

    def test_with_big_number(self):
        converter = Converter()
        self.assertEqual(converter.id_to_shortURL(100000), 'Aa4');
        self.assertEqual(converter.shortURL_to_id("Aa4"), 100000);