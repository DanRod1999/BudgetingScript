# BudgetingScript
## Gets monthly breakdown of expenses

### Usage:
`budget.py [-opts] [cmd]
opts:
  -h    help
  -v    verbose output, extended functionality
 
cmd:
  divide        This isn't usesful. I gotta make this something cool or get rid of it lol
  disposable    Calculate disposable income after expenses. Use -v to get full functionality`
  
### Example:
`Pay Type: [biweekly, monthly, hourly, annually]
monthly
Amount paid: 1000
Take out taxes: [y,n]
n
Expenses: [expense name] [cost] (enter nothing to quit)
rent 500
food 100
save 150
loans 200

Monthly Expense Breakdown
rent: 50.00%
food: 10.00%
save: 15.00%
loans: 20.00%
Percentage used: 95.00   Percentage Saved: 5.00
remaining income: 50.0`

### TODO:
  Potential additions:
   - Tax breakdowns
   - 401k percentage calc
