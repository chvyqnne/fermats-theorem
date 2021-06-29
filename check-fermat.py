def check_fermat(a,b,c,n):
    """
    checks that a to the nth power multiplied by b to the nth power equals c to the nth power
    given that a, b, and c are positive integers greater than 0
    and n is a positive integer greater than 2
    """

    a,b,c < 0
    n < 2

    if a**n + b**n == c**n:
        print("Holy smokes, Fermat was wrong!")
    else:
        print("Sorry, that doesn't work.")


def convert_inputs():
    """
    takes user-inputted a, b, c, and n converts a, b, c, and n to integers
    before adding as arguments to check_fermat function
    """
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    c = int(input("Enter c: "))
    n = int(input("Enter n: "))
    check_fermat(a,b,c,n)
    return check_fermat

check_fermat(5,6,7,8)
(convert_inputs())
