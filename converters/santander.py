#!/usr/bin/env python3
import sys
import re


def santander_convert(fp):
    """parser for santander text file format transactions are represented
    as date description amount balance separated by newlines"""
    transactions = []  # list of transactions to return
    while True:
        line = fp.readline()
        if not line:
            break
        m = re.search("Account:.XXXX XXXX XXXX ([0-9]+)", line)
        if m:
            print("account ending " + m.group(1))
            print("date , description,  amount, balance")
        m = re.search("Date:.([0-9]{2}/[0-9]{2}/[0-9]{4})", line)
        if m:
            date = m.group(1)
            desc = fp.readline().replace(",", "_").replace('"', "'")
            amt = fp.readline()
            amount = re.search("Amount:.(-?[0-9]+\.[0-9]+).", amt).group(1)
            bal = fp.readline()
            balance = re.search("Balance:.(-?[0-9]+\.[0-9]+).", bal).group(1)
            # desc[13] because description starts on the 14th character
            transactions.append(
                date + ',"' + desc[13:-2] + '",' + amount + "," + balance
            )
    return transactions


def main():
    with open(sys.argv[1], "r", encoding="latin_1") as fp:
        transactions = santander_convert(fp)

    # print transactions in reverse order
    for i in range(len(transactions) - 1, -1, -1):
        print(transactions[i])


if __name__ == "__main__":
    main()
