import os
import unittest

import pep8


# This code is a unit test for PEP8 style conformance in a Python project. 
# It uses the pep8 package to check the coding style of all Python files in a specified folder location, 
# and sets the maximum line length to 100 characters. 
# The test will pass if there are no PEP8 style errors in the checked files, 
# and fail if there are any errors, with the number of errors displayed in the failure message

class Pep8Test(unittest.TestCase):

    def test_pep8(self):
        style = pep8.StyleGuide()
        style.options.max_line_length = 100  # Set this to desired maximum line length
        filenames = []
        for root, _, files in os.walk('[folder path]'):  # Set this to desired folder location
            python_files = [f for f in files if f.endswith('.py')]
            for file in python_files:
                filename = '{0}/{1}'.format(root, file)
                filenames.append(filename)
        check = style.check_files(filenames)
        self.assertEqual(check.total_errors, 0, 'PEP8 style errors: %d' % check.total_errors)


if __name__ == '__main__':
    unittest.main()