"""
Question 7:
Write a program that computes the net amount of a bank account based a transaction log from console input. The transaction log format is shown as following:
D 100
W 200
D means deposit while W means withdrawal.
Expected Input:
D 300
D 300
W 200
D 100
Expected Output:
500
Note:
In case of taking data from the user, it should be in a comma-separated form.

"""
while True:
    logs = input("Please enter your transaction here - sample(D 100 or W 200): ")

    splited_input = logs.split(',')

    total_credit = 0
    total_debit = 0

    for transaction in splited_input:
        splited_log = transaction.strip().split(' ')
        if len(splited_log) != 2:
            print("Invalid input - start with upper D or W followed by space, followed by number.")
            break
        else:
            money = int(splited_log[1])
            term = str(splited_log[0])
            if term == "D":
                total_credit += money
            elif term == "W":
                total_debit += money
            else:
                print("Invalid transaction type! Use 'D' for deposit or 'W' for withdrawal.")
                break
    else:
        net_balance = total_credit - total_debit
        print()
        print(net_balance)
        break

"""
- Here the input is first seperated from comma
- then the individual values are assigned to a 
  conditional variable that when D is present 
  stored in credit and with W stored in debit
- Then they are processed to find net balance
- While true is used to break from invalid values
"""







