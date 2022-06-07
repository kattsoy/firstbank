# Creating a small bank.
The small project to practice classes/OOP paradigm. My bank stores the information about accounts and make transactions between accounts.

## Design

The bank has two enteties: Bank itself and Transaction.

Bank holds:
* User id: int, random number, unique
* Current balance: a dictionary with currency, balance and holder's name keys
* Transactions: a dictionary with tansactions ids
* Exchange rate: current exchange rate

Plus Bank has method to check is the account has enough money,  return the balance by holder's name and return the total balance.

Transaction holds:
* Id: int, random number, unique
* Type: deposit, transfer
* Amount
* Currency: a 2 letter code (e.g. 'USD')
* From and to accounts: str, name of account (e.g. 'Kate_BTC')

Transaction has validation methods using guardian condition, mwthod to check if the transaction was not alreday processed, and remember method. 

Finally we test if everything works correctly.

## Tech
Python 3.7
