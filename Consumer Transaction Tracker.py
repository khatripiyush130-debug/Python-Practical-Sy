#Develop a tracking program that accepts 5 consumer transaction values stores them in a list array , and output the largest transaction amount along side average speed.

transactions=[]

for i in range(5):
    amount=float(input(f"Enter transaction{i+1}: ₹"))
    transactions.append(amount)
    largest = max(transactions)
    average = sum(transactions)/len(transactions)

    print("\n Transaction Values:",transactions)
    print(f"Largest transaction: ₹{largest:.2f}")
    print(f"Average spend: ₹{average:.2f}")