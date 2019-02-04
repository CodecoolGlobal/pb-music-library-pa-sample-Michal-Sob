import unittest
import test_helpers

from file_handling import import_data, export_data
from music_reports import get_albums_by_genre, get_genre_stats,\
    get_last_oldest, get_last_oldest_of_genre, get_longest_album,\
    get_total_albums_length


class BasicTestCase(unittest.TestCase):

    def setUp(self):
        self.test_filename = 'test_albums_data.txt'
        self.albums = [
            ["Pink Floyd", "The Dark Side Of The Moon", "1973", "progressive rock", "43:00"],
            ["Britney Spears", "Baby One More Time", "1999", "pop", "42:20"],
            ["The Beatles", "Revolver", "1966", "rock", "34:43"],
            ["Deep Purple", "Machine Head", "1972", "hard rock", "37:25"],
            ["Old Timers", "Old Time", "966", "ancient", "123:45"],
            ["Pink Floyd", "Wish You Were Here", "1975", "progressive rock", "44:28"],
            ["Boston", "Boston", "1976", "hard rock", "37:41"],
            ["Monika Brodka", "Granada", "2010", "pop", "37:42"],
            ["David Bowie", "Low", "1977", "rock", "38:26"],
            ["rock", "rock", "966", "pop", "13:37"],
            ["Massive Attack", "Blue Lines", "1991", "hip hop", "45:02"]
        ]

    def test_import_data(self):
        actual = import_data(self.test_filename)

        self.assertListEqual(actual, self.albums)

    def test_export_data(self):
        import os
        tmp_filename = 'test_albums_data_tmp.txt'
        export_data(self.albums, tmp_filename)
        are_identical = test_helpers.compare_file_contents(
            self.test_filename, tmp_filename)
        os.remove(tmp_filename)

        self.assertTrue(are_identical)

    def test_if_export_raise_error_when_given_wrong_mode(self):
        self.assertRaisesRegex(ValueError, 'Wrong write mode', export_data,
                               self.albums, self.test_filename, 'r')

    def test_get_albums_by_genre(self):
        expected = [
            ["The Beatles", "Revolver", "1966", "rock", "34:43"],
            ["David Bowie", "Low", "1977", "rock", "38:26"]
        ]
        albums = get_albums_by_genre(self.albums, 'rock')

        self.assertListEqual(albums, expected)

    def test_get_albums_by_year(self):
        expected = [
            ["The Beatles", "Revolver", "1966", "rock", "34:43"],
            ["David Bowie", "Low", "1977", "rock", "38:26"]
        ]
        albums = get_albums_by_genre(self.albums, 'rock')

        self.assertListEqual(albums, expected)

    def test_if_get_by_genre_raise_error_when_given_non_existing_genre(self):
        self.assertRaisesRegex(ValueError, 'Wrong genre', get_albums_by_genre,
                               self.albums, 'folk')

    def test_get_genre_stats(self):
        expected = {
            "hip hop": 1,
            "progressive rock": 2,
            "ancient": 1,
            "pop": 3,
            "rock": 2,
            "hard rock": 2
        }
        genre_stats = get_genre_stats(self.albums)

        self.assertDictEqual(genre_stats, expected)

    def test_get_oldest_album(self):
        expected = ["rock", "rock", "966", "pop", "13:37"]
        oldest = get_last_oldest(self.albums)

        self.assertListEqual(oldest, expected)

    def test_get_oldest_of_genre(self):
        expected = ["Deep Purple", "Machine Head", "1972", "hard rock", "37:25"]
        oldest = get_last_oldest_of_genre(self.albums, "hard rock")

        self.assertListEqual(oldest, expected)

    def test_get_longest_album(self):
        expected = ["Old Timers", "Old Time", "966", "ancient", "123:45"]
        longest = get_longest_album(self.albums)

        self.assertListEqual(longest, expected)

    def test_get_total_albums_length(self):
        expected = 9.18
        albums = [
            ["rock", "rock", "966", "pop", "3:51"],
            ["Shorts", "Short", "1991", "hip hop", "5:20"]
        ]
        total_length = get_total_albums_length(albums)

        self.assertAlmostEqual(total_length, expected, 2)

if __name__ == '__main__':
    unittest.main()
