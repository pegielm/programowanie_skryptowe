import unittest
from unittest.mock import patch
import io
import skrypt1

class test_capture_stdout(unittest.TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display(self, mock_stdout):
        skrypt1.display(["a","b","c"],False)
        captured_output = mock_stdout.getvalue()
        self.assertIn("a\nb\nc\n", captured_output)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_run(self,mock_stdout):
        skrypt1.run(["f","b","l","r","x","d"],skrypt1.move_descriptions)
        captured_output = mock_stdout.getvalue()
        self.assertIn("Zwierzak idzie do przodu\nZwierzak idzie do tyłu\nZwierzak skręca w lewo\nZwierzak skręca w prawo\n", captured_output)


if __name__ == '__main__':
    unittest.main()

#python .\test_skrypt1_unittest.py