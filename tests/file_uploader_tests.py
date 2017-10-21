import unittest
from file_uploader import file_uploader


class FileSplitTests(unittest.TestCase):
    # def test_file_uploader(self):
    #     file = 'text1.txt'
    #     names = file_uploader.file_uploader(file)
    #     self.assertEqual(names['first_name'], 'Federico')

    # def test_get_file_size(self):
    #     self.assertEqual(file_uploader._get_file_size('./tests/fixtures/files/text1.txt'), 3685)
    #     self.assertEqual(file_uploader._get_file_size('./tests/fixtures/files/pas217.txt'), 13295377)
    #     self.assertEqual(file_uploader._get_file_size('./tests/fixtures/files/oth18.txt'), 29001190)
    #     self.assertEqual(file_uploader._get_file_size('./tests/fixtures/files/pas216.txt'), 85489630)
    #
    # def test_if_file_too_large(self):
    #     self.assertFalse(file_uploader._is_file_too_large(file_uploader._get_file_size('./tests/fixtures/files/text1.txt')))
    #     self.assertFalse(file_uploader._is_file_too_large(file_uploader._get_file_size('./tests/fixtures/files/pas217.txt')))
    #     self.assertFalse(file_uploader._is_file_too_large(file_uploader._get_file_size('./tests/fixtures/files/oth18.txt')))
    #     self.assertFalse(file_uploader._is_file_too_large(file_uploader._get_file_size('./tests/fixtures/files/pas216.txt')))


    def test_split_file(self):
        # self.assertFalse(file_uploader.split_file('./tests/fixtures/files/', 'text1.txt'))
        # self.assertFalse(file_uploader.split_file('./tests/fixtures/files/', 'pas217.txt'))

        self.assertFalse(file_uploader.split_file('./tests/fixtures/files/', 'oth18.txt'))

        # self.assertFalse(file_uploader._is_file_too_large(file_uploader._get_file_size('./tests/fixtures/files/pas217.txt')))
        # self.assertFalse(file_uploader._is_file_too_large(file_uploader._get_file_size('./tests/fixtures/files/oth18.txt')))
        # self.assertFalse(file_uploader._is_file_too_large(file_uploader._get_file_size('./tests/fixtures/files/pas216.txt')))


# docker run -it --rm -v "$PWD":/usr/src/app --name python-split python/file_split python -m unittest discover -s tests -p "*_tests.py"
