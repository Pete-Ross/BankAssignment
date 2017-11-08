from Bank import *


bank1 = Bank(1, "Stanbic", "Makerere", "00-0009")
bank2 = Bank(2, "DFCU", "Wandegeya", "00-4509")

#Tellers for bank 1
teller1A = Teller(1, "Yazid", bank1)
teller1B = Teller(2, "Peter", bank1)
teller1C = Teller(3, "Alex", bank1)

#Tellers for bank2
teller2A = Teller(1, "Moses", bank2)
teller2B = Teller(2, "Kalungi", bank2)
teller2C = Teller(3, "Isanka", bank2)

customer = Customer(1, "miiro", "Lumumba", 900877)
customer.OpenAccount(teller1A, "savings")

customer2 = Customer(1, "miiro", "Lumumba", 900877)
customer2.OpenAccount(teller1A, "savings")

customer2.DepositMoney(4000, teller1A)
customer2.WithdrawMoney(4000, teller1A)

customer.ApplyForLoan(teller1A, 100000)
customer.Loan.pay_loan(4000)