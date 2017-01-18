# a very sophisticated algorithm to print 'hello world'

print("~*~*~*~ ohai world !! ^_^  ~*~*~*~")

# bonus fizzbuzz

for i in range(25):
    st = "  "
    if i % 3 == 0:
        st += "fizz"
    if i % 5 == 0:
        st += "buzz"
    print(str(i) + st)
