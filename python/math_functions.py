# Greatest common devisor
def gcd(p, q):
    if q == 0:
        return p
    else:
        return gcd(q, p % q)


def convert_int_to_binary(n):
    stack = []  				# Use a list data structure for our stack
    binary_value = ""

    while n > 0:
        stack.append(n % 2)  	# append == push
        n = n / 2

    stack.reverse()				# Use as LIFO instead of FIFO

    for number in stack:
        binary_value += str(number)

    print(binary_value)


def nines(x, precision):
    return x + sum([10**(i*-1) for i in range(1, precision+1)])
