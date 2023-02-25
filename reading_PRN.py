import csv

# take user input for PRN
PRN = input("Enter PRN: ")

# open csv file and check if PRN is found and active
with open('data.csv', mode='r') as file:
    reader = csv.reader(file)
    rows = list(reader)
    for row in rows:
        if row[1] == PRN:
            if row[4] == 'Inactive':
                print("User inactive")
                exit()
            elif row[4] == 'Active':
                # take user input for Amount
                Amount = int(input("Enter amount: "))
                if Amount > int(row[2]):
                    print("Insufficient balance")
                    exit()
                else:
                    # take user input for PIN
                    PIN = input("Enter PIN: ")
                    if PIN == row[3]:
                        # subtract entered amount from balance and update csv
                        new_balance = int(row[2]) - Amount
                        row[2] = str(new_balance)
                        with open('data.csv', mode='w', newline='') as file:
                            writer = csv.writer(file)
                            writer.writerows(rows)
                        print("New balance:", new_balance)
                        exit()
                    else:
                        print("Wrong PIN")
                        exit()

# if PRN is not found in csv file
print("PRN not found")
