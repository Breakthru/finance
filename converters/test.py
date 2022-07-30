#!/usr/bin/env python3
from io import StringIO
from converters.santander import santander_convert


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
    for i in range(len(transactions) - 1, -1, -1):
        print(transactions[i])


if __name__ == "__main__":
    test_conversion()
