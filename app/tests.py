import unittest

class csv_merger(unittest.TestCase):
    def test_output(self):
        self.assertEqual(open('C:\Coder\cvs_merger\csv_files\\resultFile.csv', 'r'), open('C:\Coder\cvs_merger\csv_files\\resultFilePandas.csv', 'r'))

    #TODO
    def test_output_left(self):
        self.assertEqual(True, False)
    def test_output_right(self):
        self.assertEqual(True, False)
    def test_output_inner(self):
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
