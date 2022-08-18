#!/usr/bin/env python3

import sys

def divide(verbose, pay=0, parts=1):
    if verbose == True:
        pay = input('Amount Paid: ')
        parts = input('Divided Parts: ')
    print(pay/parts)

def disposableIncome(verbose, pay=0, expenses=[]):
    if verbose == False:
        monthly_pay = int(input('Monthly Pay: '))
        print('Expenses:')
        val = (input())
        while val != '':
            monthly_pay -= int(val)
            val = input()

    else:
        pay_type = input('Pay Type: [biweekly, monthly, hourly, annually]\n')
        pay = float(input('Amount paid: '))
        take_tax = input('Take out taxes: [y,n]\n')
        if take_tax == 'y':
            tax_amount = float(input('Approximate Amount:[0.xx]\n'))

        if pay_type == 'biweekly':
            monthly_pay = pay*2
        elif pay_type == 'hourly':
            monthly_pay = pay*40
        elif pay_type == 'annually':
            monthly_pay = pay/12
        else:
            monthly_pay = pay

        COSTS = []
        EXPENSES = []
        print('Expenses: [expense name] [cost] (enter nothing to quit)')
        expense = input().split()
        while expense != []:
            EXPENSES.append(expense[0])
            COSTS.append(int(expense[1]))
            expense = input().split()
        print('Monthly Expense Breakdown')
        for i in range(len(COSTS)):
            print('{expense}: {percent:.2f}%'.format(expense=EXPENSES[i],percent=100*COSTS[i]/monthly_pay))
        remain = monthly_pay
        for cost in COSTS:
            remain -= cost

    used = 100 * (monthly_pay-remain)/monthly_pay
    remainder = 100 * remain/monthly_pay
    print('Percentage used: {0:.2f} \t Percentage Saved: {1:.2f}'.format(used,remainder))
    print('remaining income:', remain)
    if monthly_pay < 0:
        print('Yeah thats not good dude')

def main():
    verbose = False
    if len(sys.argv) == 1:
        print('Use: budget.py [-opts] [cmd]')
        print('opts:\n\t -h \thelp \n\t -v \tverbose output')
        print('cmd:\n\t divide \tDivide arg into partitions. This is basically usesless')
        print('\t disposable  \tCalculate disposable income after expenses use -v to get more in depth data')
    else:
        if sys.argv[1] == '-v':
            verbose = True
            sys.argv.remove('-v')
        if sys.argv[1] == 'divide':
            divide(verbose, pay, equal_parts)
        if sys.argv[1] == 'disposable':
            disposableIncome(verbose)

if __name__ == "__main__":
    main()
