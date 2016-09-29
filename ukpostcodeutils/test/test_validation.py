import os
import unittest

from .. import validation


class TestPostcodeValidation(unittest.TestCase):

    def test_good_postcodes_validated_ok(self):
        here = os.path.dirname(os.path.abspath(__file__))
        with open(os.path.join(here, 'sample_postcodes.txt')) as input:
            lines = [line.strip() for line in input.readlines()]
            lines = [line for line in lines if line and line[:1] != '#']
        for line in lines:
            self.assertTrue(validation.is_valid_postcode(line), line)


if __name__ == '__main__':
    unittest.main()
