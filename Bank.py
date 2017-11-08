class Bank(object):

    def __init__(self, id, name, location, account_no_head):
        self.accounts = 0
        self.Id = id
        self.Name = name
        self.Location = location
        self.AccountNoHead = account_no_head  # to be part of each account number for a particular bank

        self.Accounts = {}
        self.loans = {}

    def add_customer(self, customer):
        self.accounts += 1  # accounts increment
        customer.AccNo = self.AccountNoHead + str(self.accounts)  # give the customer an account number
        if customer.AccountType == "Savings":
            customer.AccountType = Savings(self.accounts, customer.Id)
        self.Accounts[self.accounts] = customer

    def remove_customer(self, customer):
        try:
            print("Account", self.Accounts.pop(customer.AccountType.Id), "has been closed")
        except(AttributeError):
            print("The Account Your are trying does not exist")

    def add_loan(self, loan):
        self.loans[loan.Id] = loan


class Teller:

    def __init__(self, id, name, bank):
        self.Id = id
        self.Name = name
        self.Bank = bank

    def CollectMoney(self, customer, amount, reason):
        found = False
        if reason == "deposit":
            for key, value in self.Bank.Accounts.items():
                if value.Name == customer.Name:
                    customer.AccountType.Balance += amount
                    found = True
                    break

            if found:
                print("Deposited Shs %d\nYour new balance is: %d" % (amount, customer.AccountType.Balance))
                print("Teller: ", self.Name)
                print()
            else:
                print("Unable to deposit\n")
        elif reason == "withdraw":
            for key, value in self.Bank.Accounts.items():
                if value.Name == customer.Name:
                    balance = customer.AccountType.Balance
                    if balance < amount:
                        print("You don't have sufficient amount")
                        break
                    else:
                        balance -= balance
                        customer.AccountType.Balance = balance
                        found = True
                        break

            if found:
                print("Withdrew Shs %d\nYour new balance is: %d" % (amount, customer.AccountType.Balance))
                print("Teller: ", self.Name)
                print()
            else:
                print("Operation failed\n")

    def OpenAccount(self, customer, acc_type):
        if acc_type == "savings":
            customer.AccountType = "Savings"
        elif acc_type == "checking":
            customer.AccountType = "Checking"
        self.Bank.add_customer(customer)
        print("The Account ", customer.Name, "has been created.\n Your Account number is: ", customer.AccNo)
        print()

    def CloseAccount(self, customer):
        self.Bank.remove_customer(customer)

    def LoanRequest(self, customer, amount):
        loan_id = len(self.Bank.loans) + 1
        interest = (10.0/100.0) * amount
        loan = Loan(loan_id, "Salary Loan", customer.AccNo, customer.Id)  # Only salary loan
        loan.give_loan(amount+int(interest))
        print("You have received a loan and your total debt is ", str(interest+amount), " with 10% interest")
        print()
        customer.Loan = loan
        self.Bank.add_loan(loan)

    def ProvideInfo(self, customer):
        print("Account Name: ", customer.Name)
        print("Account No: ", customer.AccNo)
        print("Balance: ", customer.Balance)
        print("Account Type: ", customer.AccountType)

    def IssueCard(self, teller):
        pass


class Customer:

    def __init__(self, Id, name, address, phone_number, account_number=None):
        self.Id = Id
        self.Name = name,
        self.Address = address
        self.PhoneNo = phone_number
        self.AccNo = account_number
        self.AccountType = None

    def GeneratingInquiry(self, teller):
        teller.ProvideInfo(self)

    def DepositMoney(self, amount, teller):
        teller.CollectMoney(self, amount, "deposit")

    def WithdrawMoney(self, amount, teller):
        teller.CollectMoney(self, amount, "withdraw")

    def OpenAccount(self, teller, acc_type):
        teller.OpenAccount(self, acc_type)

    def CloseAccount(self, teller):
        teller.CloseAccount(self)

    def ApplyForLoan(self, teller, amount):
        teller.LoanRequest(self, amount)

    def RequestCard(self):
        pass


class Account:
    def __init__(self, id, customer_id):
        self.Id = id
        self.CustomerId = customer_id


class Checking(Account):
    def __init__(self, id, customer_id):
        Account.__init__(self,id,customer_id)
        self.Balance = 0

    def __str__(self):
        return "Checking Account"


class Savings(Account):
    def __init__(self, Id, customer_id):
        Account.__init__(self, Id, customer_id)
        self.Balance = 0

    def __str__(self):
        return "Savings Account"


class Loan:
    def __init__(self, id, type, account_id, customer_id):
        self.Id = id
        self.Type = type
        self.AccountId = account_id
        self.CustomerId = customer_id
        self.amount = 0

    def give_loan(self, amount):
        self.amount += amount  # can get loan top-up

    def pay_loan(self, amount):
        if self.amount-amount > 0:
            self.amount -= amount
            print("Paid Amount: %d\nYour balance is now %d" %(amount, self.amount))
        elif self.amount - amount <= 0:  # loan cleared
            print("Paid Amount: %d\nYour loan has been cleared" % amount)
            print()


    def __str__(self):
        return "you currently have a loan with a balance", self.amount



