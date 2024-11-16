acct_num: str = "123456"
acct_bal: float = 0.0


def deposit(cust_num: str, amount: float) -> None:
    global acct_bal
    if acct_num == cust_num:
        acct_bal += amount
    else:
        print("Check Your Account Details")


def check_bal(cust_num: str) -> float:
    if acct_num == cust_num:
        return acct_bal


def withdrew(cust_num: str, amount: float) -> float | str:
    global acct_bal
    if acct_num == cust_num:
        if amount > acct_bal:
            return "Insufficient Balance"
        else:
            acct_bal -= amount
    else:
        return "Check Your Account Details"


deposit("123456", 2500)
deposit("123456", 30000)
deposit("123456", 100000)
with_money = withdrew("123456", 50000)
print(with_money)
with_money2 = withdrew("123456", 10000)
print(with_money2)
# acct_bal = check_bal("123456")
# print(acct_bal + 1234567788 * 234)
print(acct_bal)
