Start = 'N'
while Start == 'N':
    print('Select one of the following gates: AND, OR, NOR, NAND, Xor, XNOR')
    gate = input('Type the name of gate and press ENTER:')
    print(gate,' operator is selected')
    A_Val = int(input('Enter value for A (0 or 1): '))
    while A_Val != 0 and A_Val != 1:
         print('Enter valid value for input 0 or 1')
         A_Val = int(input('ENter value for A (0 or 1): '))
    B_Val = int(input('Enter value for B (0 or 1): '))
    while B_Val != 0 and B_Val != 1:
         print('Enter valid value for input 0 or 1')
         B_Val = int(input('ENter value for B (0 or 1): ')) 
    if gate == 'AND':
          if A_Val == 0 and B_Val == 0:
               print('AND(0,0) = 0')
          elif A_Val == 0 and B_Val == 1:
               print('AND(0,1) = 0')
          elif A_Val == 1 and B_Val == 0:
               print('AND(1,0) = 0')
          elif A_Val == 1 and B_Val == 1:
               print('AND(1,1) = 1')
    elif gate == 'OR':
          if A_Val == 0 and B_Val == 0:
               print('OR(0,0) = 0')
          elif A_Val == 0 and B_Val == 1:
               print('OR(0,1) = 1')
          elif A_Val == 1 and B_Val == 0:
               print('OR(1,0) = 1')
          elif A_Val == 1 and B_Val == 1:
               print('OR(1,1) = 1')
    elif gate == 'NOR':
          if A_Val == 0 and B_Val == 0:
               print('NOR(0,0) = 1')
          elif A_Val == 0 and B_Val == 1:
               print('NOR(0,1) = 0')
          elif A_Val == 1 and B_Val == 0:
               print('NOR(1,0) = 0')
          elif A_Val == 1 and B_Val == 1:
               print('NOR(1,1) = 0')
    elif gate == 'NAND':
          if A_Val == 0 and B_Val == 0:
               print('NAND(0,0) = 1')
          elif A_Val == 0 and B_Val == 1:
               print('NAND(0,1) = 1')
          elif A_Val == 1 and B_Val == 0:
               print('NAND(1,0) = 1')
          elif A_Val == 1 and B_Val == 1:
               print('NAND(1,1) = 0')
    elif gate == 'XOR':
          if A_Val == 0 and B_Val == 0:
               print('XOR(0,0) = 0')
          elif A_Val == 0 and B_Val == 1:
               print('XOR(0,1) = 1')
          elif A_Val == 1 and B_Val == 0:
               print('XOR(1,0) = 1')
          elif A_Val == 1 and B_Val == 1:
               print('XOR(1,1) = 0')
    elif gate == 'XNOR':
          if A_Val == 0 and B_Val == 0:
               print('XNOR(0,0) = 1')
          elif A_Val == 0 and B_Val == 1:
               print('XNOR(0,1) = 0')
          elif A_Val == 1 and B_Val == 0:
               print('XNOR(1,0) = 0')
          elif A_Val == 1 and B_Val == 1:
               print('XNOR(1,1) = 1')    
    Start = input('To Exit type Y and press Enter Else to continue press N: ')