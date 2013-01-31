import unittest
from .. import validation

class TestPostcodeValidation(unittest.TestCase):


    def test_good_postcodes_validated_ok(self):
        self.assertTrue(validation.is_valid_postcode('SW1A1AA'))

if __name__ == '__main__':
    unittest.main()