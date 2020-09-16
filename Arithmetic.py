input1 = int(input('Enter the first number:'))
if type(input1) != int:
    print('Please restart and try again')
else:
    input2 = int(input('Enter the second number'))
    if type(input2) != int:
        print('Please restart and try again')
    else:
        input3 = int(input('Enter the third number'))
        if type(input3) == int:
            sum = input1 + input2 + input3
            avrg = sum / 3
            prod = input1 * input2 * input3
            print('Sum =', sum)
            print('Average =', avrg)
            print('Product =', prod)
            print('Smallest number =', min([input1, input2, input3]))
            print('Largest number=', max([input1, input2, input3]))