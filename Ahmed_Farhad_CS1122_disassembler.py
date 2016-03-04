'''
Farhad Ahmed
CS 1122
HW05

Disassembler functions for LMC program.
'''


# Operation code to mnemonic dictionary
# You can use this to lookup the machine code
# and translate it to the mnemonic instruction
INS_REF = {
    1: "ADD",
    2: "SUB",
    3: "STA",
    5: "LDA",
    6: "BRA",
    7: "BRZ",
    8: "BRP"
}

def disassemble(operation_code):
    # this function should take in an integer operation code
    # and convert it to a LMC mnemonic instruction and return
    # it as a string
    if (operation_code > 900):
        if (operation_code == 901):
            print("INP")
        else:
            print("OUT")

    else:
        if (operation_code == 0):
            print("HLT")
        else:
            LMC_command = operation_code // 100
            data_location = operation_code % (100 * LMC_command)
            if (data_location >= 10):
                print(INS_REF[LMC_command], " "+str(data_location))
            else:
                print(INS_REF[LMC_command], " 0"+str(data_location))
        
    
    pass

def main():
    # The main function should read all operation codes from the
    # user until the HLT instruction is read. Once it is read,
    # all operation codes should be disassembled using "disasassembled"
    # and then printed out to the user

    list_of_codes = []
    current_code = int(input("Enter the operation code: "))
    list_of_codes.append(current_code)
    while (current_code != 000):
        current_code = int(input("Enter the operation code: "))
        list_of_codes.append(current_code)
    for index in range(len(list_of_codes)):
        disassemble(list_of_codes[index])
    
    pass

if __name__ == "__main__":
    main()
