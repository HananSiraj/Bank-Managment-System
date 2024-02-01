class Bank:
  def __init__(self,name):
    self.name=name
    self.accounts=[]
  def add_account(self,account):
    self.accounts.append(account)
class Account:
  def __init__(self,number,owner,balance,username,password):
    self.number=number
    self.owner=owner
    self.balance=balance
    self.username=username
    self.password=password
    self.transactions=[]
  def deposit(self,amount):
    self.balance+=amount
    self.transactions.append(Transaction(amount,'Deposit'))
  def withdraw(self,amount):
   if self.balance>=amount:
      self.balance-=amount
      self.transactions.append(Transaction(amount,'Withdrawal'))
   else:
      print('insufficent funds')
class Transaction:
  def __init__(self,amount,type):
    self.amount=amount
    self.type=type
#user interface
def main():
  bank_name=input('Enter bank name:')
  bank=Bank(bank_name)
  print('Bank',bank_name,'created successfully')
  while True:
   print('1.Create Account')
   print('5.login')
   print('2.Deposit')
   print('3.Withdraw')
   print('4.Exit')
   choice=int(input('Enter your choice:'))
   if choice==1:
      acc_number=input('Enter account number:')
      acc_owner=input('Enter account owner name:')
      acc_balance=float(input('Enter opening balance:'))
      username = input('Enter username: ')
      password = input('Enter password: ')
      account=Account(acc_number,acc_owner,acc_balance,username,password)
      bank.add_account(account)
      print('Account created successfully')
   elif choice==5:
       username=input('Enter username: ')
       password=input('Enter password: ')
       account=find_account_by_username(bank.accounts,username)
       if account and account.password==password:
          print("logged in successfully")
       else:
         print('invalid username or password')
   elif choice==2:
      acc_number=input('Enter account number:')
      amount=float(input('Enter amount to deposit:'))
      account=find_account(bank.accounts,acc_number)
      if account:
         account.deposit(amount)
         print('Deposit successful')
      else:
        print('Account not found')
   elif choice==3:
    acc_number=input('Enter account number:')
    amount=float(input('Enter amount to deposit:'))
    account=find_account(bank.accounts,acc_number)
    if account:
       account.withdraw(amount)
       print('withdrawal successful')
    else:
      print('Account not found')

   elif choice==4:
       print('Thankyou for using the Bank Management System')
       break
  else:
       print('invalid choice')
def find_account(accounts,number):
  for account in accounts:
     if account.number==number:
        return account
  return None
def find_account_by_username(accounts,username):
    for account in accounts:
        if account.username==username:
            return account
    return None
main()
