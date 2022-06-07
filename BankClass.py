import random

#  set up the exchange rate
EXCHANGE_RATES = dict(disclaimer="Usage subject to terms: https://openexchangerates.org/terms",
                      license="https://openexchangerates.org/license", timestamp=1628753400, base="RUB",
                      rates={"AED": 0.049881, "AFN": 1.098356, "ALL": 1.39959, "AMD": 6.68235, "ANG": 0.024323,
                             "AOA": 8.663937, "ARS": 1.31686, "AUD": 0.018447, "AWG": 0.024447, "AZN": 0.023097,
                             "BAM": 0.02262, "BBD": 0.02716, "BDT": 1.152137, "BGN": 0.02262, "BHD": 0.00512,
                             "BIF": 26.929993, "BMD": 0.01358, "BND": 0.018423, "BOB": 0.093419, "BRL": 0.07088,
                             "BSD": 0.01358, "BTC": 3.00102e-7, "BTN": 1.010871, "BWP": 0.151062, "BYN": 0.034148,
                             "BZD": 0.027313, "CAD": 0.017003, "CDF": 26.92506, "CHF": 0.012523, "CLF": 0.00038,
                             "CLP": 10.475611, "CNH": 0.087985, "CNY": 0.087976, "COP": 53.799481, "CRC": 8.416396,
                             "CUC": 0.01358, "CUP": 0.349681, "CVE": 1.274155, "CZK": 0.293914, "DJF": 2.412269,
                             "DKK": 0.086066, "DOP": 0.771417, "DZD": 1.837139, "EGP": 0.213193, "ERN": 0.20376,
                             "ETB": 0.609887, "EUR": 0.011573, "FJD": 0.028321, "FKP": 0.009796, "GBP": 0.009796,
                             "GEL": 0.042084, "GGP": 0.009796, "GHS": 0.081773, "GIP": 0.009796, "GMD": 0.694609,
                             "GNF": 132.185559, "GTQ": 0.10523, "GYD": 2.84165, "HKD": 0.105668, "HNL": 0.321628,
                             "HRK": 0.086762, "HTG": 1.297114, "HUF": 4.094752, "IDR": 195.400305, "ILS": 0.043813,
                             "IMP": 0.009796, "INR": 1.009526, "IQD": 19.769762, "IRR": 572.254422, "ISK": 1.712825,
                             "JEP": 0.009796, "JMD": 2.09595, "JOD": 0.009628, "JPY": 1.49958414, "KES": 1.482239,
                             "KGS": 1.150984, "KHR": 55.379065, "KMF": 5.649892, "KPW": 12.221855, "KRW": 15.801524,
                             "KWD": 0.004086, "KYD": 0.011293, "KZT": 5.787195, "LAK": 129.865861, "LBP": 20.488379,
                             "LKR": 2.703271, "LRD": 2.33064, "LSL": 0.200154, "LYD": 0.061352, "MAD": 0.122011,
                             "MDL": 0.240501, "MGA": 51.7629, "MKD": 0.712619, "MMK": 22.303683, "MNT": 38.702165,
                             "MOP": 0.108608, "MRO": 4.848, "MRU": 0.489567, "MUR": 0.577822, "MVR": 0.209943,
                             "MWK": 11.015537, "MXN": 0.270859, "MYR": 0.057517, "MZN": 0.864221, "NAD": 0.195142,
                             "NGN": 5.575882, "NIO": 0.475798, "NOK": 0.120321, "NPR": 1.61345, "NZD": 0.01933,
                             "OMR": 0.005228, "PAB": 0.01358, "PEN": 0.055285, "PGK": 0.048265, "PHP": 0.685388,
                             "PKR": 2.221551, "PLN": 0.053075, "PYG": 93.597745, "QAR": 0.049457, "RON": 0.056868,
                             "RSD": 1.360031, "RUB": 1, "RWF": 13.535899, "SAR": 0.050922, "SBD": 0.10934,
                             "SCR": 0.182105, "SDG": 6.063398, "SEK": 0.11798, "SGD": 0.018437, "SHP": 0.009796,
                             "SLL": 139.23409, "SOS": 7.838862, "SRD": 0.289787, "SSP": 1.76891, "STD": 280.630933,
                             "STN": 0.284498, "SVC": 0.118573, "SYP": 17.078801, "SZL": 0.200117, "THB": 0.448861,
                             "TJS": 0.153833, "TMT": 0.047529, "TND": 0.037816, "TOP": 0.030624, "TRY": 0.116768,
                             "TTD": 0.092032, "TWD": 0.377852, "TZS": 31.491647, "UAH": 0.363278, "UGX": 47.946028,
                             "USD": 0.01358, "UYU": 0.592956, "UZS": 144.430118, "VES": 55391.073021, "VND": 309.298891,
                             "VUV": 1.502349, "WST": 0.034734, "XAF": 7.591271, "XAG": 0.00057961, "XAU": 0.00000774,
                             "XCD": 0.0367, "XDR": 0.00957, "XOF": 7.591271, "XPD": 0.00000515, "XPF": 1.381005,
                             "XPT": 0.00001334, "YER": 3.394961, "ZAR": 0.200066, "ZMW": 0.261587, "ZWL": 4.372708})


#  define the conversion function
def convert_amount(rates_data, currency_from, currency_to, amount):
    convert_amount = rates_data['rates'][currency_to] / rates_data['rates'][currency_from] * amount
    return convert_amount

# random number generation
def generate_random_number(length):
    min_v = 10 ** (length - 1)
    max_v = 10 ** length - 1
    return random.randint(min_v, max_v)


#  create a bank dictionary
class BankStorage:

    def __init__(self, exchange_rate):
        self.id = {}
        self.balance = {}
        self.transactions = {}
        self.exchange_rate = exchange_rate
        self.transactions['transactions'] = {}

    # create account
    def make_account(self, holder_name, currency):
        account_number = generate_random_number(10)
        self.id[account_number] = holder_name
        self.balance[account_number] = {"currency": currency, 'balance': 0, 'name': holder_name}
        return self, account_number

    #  check the account validity
    def is_valid_account(storage, account_number):
        if account_number not in self.id.items():
            return False
        else:
            return True

    #  check if the account has enough money
    def has_enough_money(storage, transaction):
        balance = self.balance[account_number]["balance"]
        account_currency = self.balance[account_number]["currency"]
        converted_amount = convert_amount(self.exchange_rate, transaction.currency, self.currency, transaction.amount)
        if converted_amount <= balance and currency == account_currency:
            return True
        else:
            return False

    # {7956745831: {'currency': 'USD', 'balance': 0, 'name': 'Kate'}} -how the balance looks

    # get the balance by holder's name
    def get_current_balance(self, holder_name):
        for k, v in self.balance.items():
            if holder_name == self.balance[k]['name']:
                current_balance = self.balance[k]['balance']
        return current_balance

    # check the balance after all the manipulations or just cause we can
    def get_total_balance(self, holder_name, in_currency):
        total_balance = 0
        for k, v in self.balance.items():
            balance = v['balance']
            account_currency = v['currency']
            converted_amount = convert_amount(self.exchange_rate, account_currency, in_currency, balance)
            if v['name'] == holder_name:
                total_balance += converted_amount

        return total_balance

    def increase_amount(self, account_number, amount):
        self.balance[account_number] += amount


bank_storage = BankStorage(EXCHANGE_RATES)
print(bank_storage)


# represent the Transaction class with several attributes
class Transaction:
    def __init__(self, tr_id, type, amount, currency, tr_to, tr_from):
        # create a Transaction
        self.tr_id = tr_id
        self.type = type
        self.amount = amount
        self.currency = currency
        self.tr_to = tr_to
        self.tr_from = tr_from

    # check the transaction
    def already_processed(self, storage):
        if self.tr_id not in storage['transactions']:
            return False
        else:
            return True

    # record the transaction
    def remember_transaction(self, storage):
        if self.tr_id not in storage['transactions']:
            storage['transactions'][self.tr_id] = {
                'type': self.type,
                'amount': self.amount,
                'currency': self.currency
                }

    # transaction validation
    def validate_transaction(self, storage):
     # btw. this is called "guardian condition": if something isn't valid, return False and don't proceed
        if not is_valid_account(self, storage):
         print("'to' account {} is not valid".format(self.tr_to))
         return False

        if 'from' in self:
         if not is_valid_account(self, storage):
             print("'from' account {} is not valid".format(self.tr_from))
             return False
        if not has_enough_money(self, storage):
         print("'from' account {} doesn't have enough money ;(".format(self.tr_from))
         return False

        if self.already_processed(self, storage):
         print("Trx {} already processed".format(self.tr_id))
         return False

        #validate currency
        if self.currency not in storage['exchange_rate']['rates']:
         return False

        else:
            return True

    def process_transaction(self, storage):
        if not self.validate_transaction(self, storage):
            print("Trx {} invalid, skipping".format(self.tr_id))
            return storage

        if type == 'transfer':
            storage = self.process_transfer(self, storage)
        # this is "else + if = elif"
        elif type == 'cash_deposit':
            storage = self.process_cash_deposit(self, storage)
        else:
            print("Wtf is this {}".format(self))
            return storage


    def process_transfer(self, storage):
        storage.increase_amount (self.tr_from, -1 * self.amount)
        storage.increase_amount(self.tr_to, self.amount)


    def process_cash_deposit(self, storage):
        storage.increase_amount (self.tr_from, self.amount)

        storage = remember_transaction(storage)
        return storage


#  check if it works

kotomka = BankStorage(EXCHANGE_RATES)
kotomka.make_account ('Alice_ USD', 'USD')
kotomka.make_account ('Alice_GBP', 'GBP')
kotomka.make_account ('Bob_RUB', 'RUB')
kotomka.make_account ('Bob_BTC', 'BTC')

def trx_id():
    return generate_random_number(10)

def make_transfer(from_acc, to_acc, amount, currency):
    transfer = {}
    transfer['id'] = trx_id()
    transfer['from'] = from_acc
    transfer['to'] = to_acc
    transfer['amount'] = amount
    transfer['currency'] = currency
    transfer['type'] = 'transfer'
    return transfer
# instantiation / create instances
first_tr = Transaction(trx_id(),'gluk', 10000, 'USD', 'Alice_USD', None )
second_tr = Transaction (trx_id(),'cash_deposit', 10000, 'EUR', 'Alice_USD', None )
third_tr = Transaction (trx_id(),'cash_deposit', 10000, 'CHO', 'Alice_USD', None )

transactions = [first_tr, second_tr, third_tr, make_transfer('Alice_USD', 'Bob_BTC', 0.00000001, 'BTC'),
                make_transfer('Alice_GDP', 'Bob_RUB', 1000, 'EUR')]

transactions.append(transactions[-1])
transactions.append(transactions[0])

# adding some duplicates

for trx in transactions:
    print("--- processing trx {} ---".format(trx))
    kotomka = process_transaction(kotomka)
    print("----- done -------")
    print()

print("Alice has {} USD".format(kotomka.get_total_balance('Alice', 'USD')))
print("Bob has {} USD".format(kotomka.get_total_balance('Bob', 'EUR')))


def make_transfer(from_acc, to_acc, amount, currency):
    transfer = {}
    transfer['id'] = trx_id()
    transfer['from'] = from_acc
    transfer['to'] = to_acc
    transfer['amount'] = amount
    transfer['currency'] = currency
    transfer['type'] = 'transfer'
    return transfer


print(make_transfer(44555, 100293, 100, "USD"))
