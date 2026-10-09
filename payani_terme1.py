
javab = 'yes'

while javab == 'yes':
    number1 = int(input('adad aval ra vared konid: '))
    number2 = int(input('adad dovom ra vared konid: '))

    while number1 <= number2:
        if number1 % 2 == 0:
            print(number1)

        number1 = number1 + 1

    javab = input('aya mikahid edame dahid? yes or no: ')

'''
while True:
    number1 = int(input("adad aval ra vared konid : "))
    number2 = int(input("adad dovom ra vared konid : "))

    while number1 <= number2:
        if number1 % 3 == 0:
            print(number1)
        number1 += 1

    answer = input("aya edame midahid ?: ")

    if answer == "no":
        break
'''
