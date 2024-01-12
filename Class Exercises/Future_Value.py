'''
program: Future Value Program
date: 01/12/2024
author: Christian Dinn
'''

import locale as lc
lc.setlocale(lc.LC_ALL, 'en-ca')

def future_value_cal(mnth_inv, yearly_int, years):
    mnth_inter = yearly_int / 12 / 100
    future_value = 0
    counter = 1
    months = years * 12
    while counter <= months:
        future_value += mnth_inv
        interest_amount = future_value * mnth_inter
        future_value += interest_amount
        counter += 1
    return future_value


def main():
    loop = 'y'
    while loop.lower() == 'y':
        mnth_inv = int(input("Enter monthly investment:\t"))
        yearly_int = float(input("Enter yearly interest rate:\t"))
        years = int(input("Enter number of years:\t\t"))
        future_value = future_value_cal(mnth_inv, yearly_int, years)
        cur_mnt_inv = lc.currency(mnth_inv, grouping=True)
        cur_fut_value = lc.currency(future_value, grouping=True)
        print()
        print(f"{'Monthly Investment:':20}{cur_mnt_inv:>12}")
        print(f"{'Interest Rate:':20}{yearly_int:>12}")
        print(f"{'Years:':20}{years:>12}")
        print(f"{'Future Value:':20}{cur_fut_value:>12}")
        loop = input("\nContinue? (y/n): ")
        print()
    print("Bye!")

if __name__ == '__main__':
    main()