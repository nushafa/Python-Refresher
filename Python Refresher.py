#Patters
# Basic Star Pattern
print("Star Pattern \n")
for i in range(1,6):
    for j in range(i):
        print("*", end="")
    print('\n')

# Inverted Star Pattern
print("Inverted Star Pattern \n")
for i in range(6,1,-1):
    for j in range(i, 1, -1):
        print("*", end="")
    print('\n')

#Denomination
def no_notes(a):
    Q = [2000, 500, 200, 100, 50, 20, 10]
    x = 0
    for i in range(7):
        q = Q[i]
        x = a // q
        print("Notes of {} = {}".format(q, x))
        a = a % q

amount = int(input("Enter Total Amount"))
no_notes(amount)


# Fibonacci Series
def fib_series(nterms):
    # first two terms
    n1, n2 = 0, 1
    count = 0
    while count < nterms:
        print(n1)
        nth = n1 + n2
        # update values
        n1 = n2
        n2 = nth
        count += 1

nterms = int(input("How many terms? "))

# check if the number of terms is valid
if nterms <= 0:
    print("Please enter a positive integer")
elif nterms == 1:
    print("Fibonacci sequence upto", nterms, ":")
    fib_series(nterms)
else:
    print("Fibonacci sequence:")
    fib_series(nterms)