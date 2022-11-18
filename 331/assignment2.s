.data
A: .word 27, 20, 2, 24, 7, 19, 2, 10, 10, 22
B: .word 0, 0, 0, 0, 0, 0
.text
la x10, A
la x11, B
li x12, 6
li x13, 5
li x5, 0
li x6, 0

loopi:
    bge x5, x12, ENDi 
    slli x1, x5, 2
    add x1, x11, x1     
    sw x0, 0(x1)    
    addi x6, x0, 0
loopj:
    bge x6, x13, ENDj   
    add x4, x5, x6    
    slli x4, x4, 2
    add x4, x4, x10    
    lw x4, 0(x4)    
    lw x7, 0(x1)
    add x4, x7, x4     
    sw x4, 0(x1)     
    addi x6, x6, 1     
    j loopj 
ENDj:
    addi x5, x5, 1    
    j loopi
ENDi:
    
    exit:
        nop
