#!/usr/bin/env python3
from io import StringIO
from converters.santander import santander_convert
from converters.tesco import tesco_convert
import unittest

class CCParserTest(unittest.TestCase):
    def test_example_report(self):
        f = StringIO("""
Transaction Date, Posting Date, Billing Amount, Merchant, Merchant City , Merchant State , Merchant Zip , Reference Number , Debit/Credit Flag , SICMCC Code
19/09/2016,20/09/2016,£10.55,"MERCHANT A","Example PC",,PC0 5EA,1234567890,D,1234
19/09/2016,20/09/2016,£5.69,"MERCHANT PLC SACA","Example",GBR,PC 8NB,123456789,D,1234
""")
        transactions = tesco_convert(f)
        self.assertEqual(len(transactions), 2)
        self.assertEqual(transactions[0].split(',')[3], "10.55")



class SantanderTest(unittest.TestCase):
    def test_conversion():
        fp = StringIO()
        fp.write(
            """From: 01/01/2019 to 02/02/2020
    
         Account: XXXX XXXX XXXX 1234
    
        Date: 02/01/2020
        Description: test description test description
        Amount: -100.00
        Balance: 200.00
    
        Date: 01/01/1970
        Description: test description test description
        Amount: -100.00
        Balance: 100.00
                                                            """
        )

        transactions = santander_convert(fp)

        # print transactions in reverse order
        self.assertEqual(len(transactions), 2)
        self.assertEqual(transactions[0].split(',')[3], "100.00")


if __name__=="__main__":
    unittest.main()
