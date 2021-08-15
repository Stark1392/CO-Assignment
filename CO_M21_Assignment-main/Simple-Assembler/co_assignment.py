#input text file
import sys

read_file = sys.stdin.read()

lines = read_file.split("\n")

#file_object = open('test2')
#lines = file_object.readlines()

#lines = ["var xyz", "add R0 R1 R2", "label: R0 R1 R2 ","hlt"]
#lines = ["add R0 R1 R2", "boy: add R0", "jmp boy"]
#lines = ["add R0 R1 R2","sub R0 R1 R2", "hlt"]

#print(lines)
n = len(lines)

mem_add = {} 

r = {'000':0000000000000000, '001':0000000000000000, '010':0000000000000000, 
              #R0                     #R1                     #R2
         '011':0000000000000000, '100':0000000000000000, '101':0000000000000000,
                #R3                   #R4                   #R5
         '110':0000000000000000, '111':0000000000000000}
                #R6                   #FLAG

output = []

pc = 0                      #program counter
pc_error = 0                #program counter while checking errors
pc_address = 0 
start1 = 0
end1 = n
start2 = 0
end2 = n

#global error
error = True
ins = ["add", "sub", "mov", "ld", "st", "mul", "div", "ls", "rs", "xor", "or", "label:", "and", "not", "cmp", "jlt", "jmp", "jgt", "je", "hlt", "R0", "R1", "R2", "R3", "R4", "R5", "R6", "FLAGS", "var"]
variable = []
label = []









#global error_2
error_2 = False
def check_error(lines,r,ins,variable, label):
    global error
    
    def error1(lines):
        global error_2
        if lines[-1] != "hlt":
            print("Error: hlt statement not present!")

            #global error
            #error = True

            
            error_2 = True

        #global error
        #error = False
    
    def error2(lines):
        global error_2
        for z in range(0,n):
            if (lines[z] == "hlt" and z != n-1):
                print("Error: hlt can only be used at the end")

                #global error
                #error = True
                
                error_2 = True
                break
        #global error
        #error = False
    
    def error3(lines,ins):
        global error_2
        loop_flag = False
        loop_flag2 = False
        for z in range(0,n):
            ele = lines[z].split()
            for j in range(0, len(ele)):
                if ele[j][-1] == ":":
                    pass
                elif ele[j] == "var":
                    pass
                else:
                    for el in ele:
                        if el not in ins:
                            
                            print("Error: Typo in line: ",z)
                            #global error
                            #error = True
                            
                            error_2 = True
                            loop_flag = True
                            loop_flag2 = True
                            break
                    if loop_flag2 == True:
                        break
            if loop_flag == True:
                break
        #global error
        #error = False

    def error4(lines,variable):
        global error_2
        loop_flag = False
        for z in range(0,n):
            ele = lines[z].split()
            for j in range(0, len(ele)):
                if ele[0] == "ld" or ele[0] == "st":
                    if ele[2] not in variable:
                        print("Error: Undefined variable used in line: ",z)
                        #global error
                        #error = True
                        
                        error_2 = True
                        loop_flag = True
                        break
            if loop_flag == True:
                break
        #global error
        #error = False

    def error5(lines,label):
        global error_2
        loop_flag = False
        for z in range(0,n):
            ele = lines[z].split()
            for j in range(0, len(ele)):
                if ele[0] == "jmp" or ele[0] == "jlt" or ele[0] == "jgt" or ele[0] == "je":
                    if ele[1] not in label:
                        print("Error: Undefined label used in line: ",z)
                        #global error
                        #error = True
                        
                        error_2 = True
                        loop_flag = True
                        break
            if loop_flag == True:
                break
        #global error
        #error = False

    def error6(lines):
        global error_2
        for z in range(0,n):
            ele = lines[z].split()
            if "FLAGS" in ele:
                if ele[0] != "mov":
                    print("Error: Illegal use of FLAGS regect in line: ",z)
                    #global error
                    #error = True
                    
                    error_2 = True
                    break
        #global error
        #error = False

    def error7(lines):
        global error_2
        for z in range(0,n):
            ele = lines[z].split()
            if (ele[0] == "mov" or ele[0] == "rs" or ele[0] == " ls"):
                if ele[2] == "FLAGS" :
                    #global error
                    #error = False
                    pass
                elif ele[2][0] == "R":
                    pass
                elif ele[2][0] == "$":
                    num = ele[2][1:]
                    num_int = int(num)
                    #print(num_int)
                    #print(type(num_int))
                    if(num_int<=0 or num_int>=255):
                        print("Error: Immediate value out of range in line: ",z)
                        #global error
                        #error = True
                        
                        error_2 = True
                        break
                    
        #global error
        #error = False

    def error8(lines, variable, label):
        global error_2
        for z in range(0,n):
            ele = lines[z].split()
            if (ele[0] == "jmp" or ele[0] == "jlt" or ele[0] == "je" or ele[0] == "jgl"):
                if ele[1] in variable:
                    print("Error: Variable used as label in line: ",z)
                    #global error
                    #error = True
                    
                    error_2 = True
                    break
                elif (ele[0] == "ld" or ele[0] == "st"):
                    if ele[2] in label:
                        print("Error: Label used a variable in line: ",z)
                        #error = True

                        
                        error_2 = True

                        break
        #global error
        #error = False

    def error9(lines):
        global error_2
        check_flag = False
        check = lines[0].split()
        if check[0] != "var":
            check_flag = True

        loop_flag = False
        for z in range(0,n):
            ele = lines[z].split()
            for j in range(0, len(ele)):
                if (ele[0] == "var" and check_flag == True):
                    print("Error: Variable must be declared in the beginning not in line: ",z)
                    #global error
                    #error = True
                    
                    error_2 = True
                    loop_flag = True
                    break
            if loop_flag == True:
                break
        #global error
        #error = False



    error1(lines)
    if error_2 == False:
        error2(lines)
    if error_2 == False:
        error3(lines, ins)
    if error_2 == False:
        error4(lines,variable)
    if error_2 == False:
        error5(lines,label)
    if error_2 == False:
        error6(lines)
    if error_2 == False:
        error7(lines)
    if error_2 == False:
        error8(lines,variable,label)
    if error_2 == False:
        error9(lines)

    if error_2 == False:
        global error
        error = False


            



        

        




       
start3 = 0
end3 = n
count = 0
    
while(start3<end3):
    u = lines[start3].split()
    if u[0] == "var":
        variable.append(u[1])
        ins.append(u[1])
        count += 1
    start3 += 1
    
variable_pointer = end2 - count
while(start2<end2):
    #Code to find location of lables and variables yet to written and stored in
    #mem_add
    t = lines[start2].split()
    if t[0][-1] == ":":
        label.append(t[0])
        label.append(t[0][:-1])
        ins.append(t[0][:-1])
        mem_add.update({t[0][:-1]: start2})
    if t[0] == "var":
        mem_add.update({t[1]:variable_pointer })
        variable_pointer += 1
    if t[0] == "mov":
        if t[2][0] == "$":
            ins.append(t[2])
    start2+=1

if error == True:
    check_error(lines,r,ins,variable, label)
    

        
if error == False:
    for i in range(0,n):
        
        def convert_to_8bit(z):
            bnr = bin(z).replace('0b','')
            x = bnr[::-1] #this reverses an array
            while len(x) < 8:
                x += '0'
            bnr = x[::-1]
            return bnr
        
        def convert_to_16bits(z):
            bnr = bin(z).replace('0b','')
            x = bnr[::-1] #this reverses an array
            while len(x) < 16:
                x += '0'
            bnr = x[::-1]
            return bnr

        def ins_add(r,s):
                
                if s[2] == "R0":
                    a = r["000"]
                    locate_a = "000"
                elif s[2] == "R1":
                    a = r["001"]
                    locate_a = "001"
                elif s[2] == "R2":
                    a = r["010"]
                    locate_a = "010"
                elif s[2] == "R3":
                    a = r["011"]
                    locate_a = "011"
                elif s[2] == "R4":
                    a = r["100"]
                    locate_a = "100"
                elif s[2] == "R5":
                    a = r["101"]
                    locate_a = "101"
                elif s[2] == "R6":
                    a = r["110"]
                    locate_a = "110"
                elif s[2] == "FLAGS":
                    a = r["111"]
                    locate_a = "111"
                
                if s[3] == "R0":
                    b = r["000"]
                    locate_b = "000"
                elif s[3] == "R1":
                    b = r["001"]
                    locate_b = "001"
                elif s[3] == "R2":
                    b = r["010"]
                    locate_b = "010"
                elif s[3] == "R3":
                    b = r["011"]
                    locate_b = "011"
                elif s[3] == "R4":
                    b = r["100"]
                    locate_b = "100"
                elif s[3] == "R5":
                    b = r["101"]
                    locate_b = "101"
                elif s[3] == "R6":
                    b = r["110"]
                    locate_b = "110"
                elif s[3] == "FLAGS":
                    b = r["111"]
                    locate_b = "111"

                #sum = convert_to_16bits(int(a, 2) + int(b, 2))
                
                #need to check overflow

                if s[1] == "R0":
                    #c = r["000"]
                    locate_c = "000"
                elif s[1] == "R1":
                    #c = r["001"]
                    locate_c = "001"
                elif s[1] == "R2":
                    #c = r["010"]
                    locate_c = "010"
                elif s[1] == "R3":
                    #c = r["011"]
                    locate_c = "011"
                elif s[1] == "R4":
                    #c = r["100"]
                    locate_c = "100"
                elif s[1] == "R5":
                    #c = r["101"]
                    locate_c = "101"
                elif s[1] == "R6":
                    #c = r["110"]
                    locate_c = "110"
                elif s[1] == "FLAGS":
                    #c = r["111"]
                    locate_c = "111"

                
                #r[locate_c] = sum

                output.append("0000000"+locate_c+locate_a+locate_b)

        def ins_sub(r,s):
                
                if s[2] == "R0":
                    a = r["000"]
                    locate_a = "000"
                elif s[2] == "R1":
                    a = r["001"]
                    locate_a = "001"
                elif s[2] == "R2":
                    a = r["010"]
                    locate_a = "010"
                elif s[2] == "R3":
                    a = r["011"]
                    locate_a = "011"
                elif s[2] == "R4":
                    a = r["100"]
                    locate_a = "100"
                elif s[2] == "R5":
                    a = r["101"]
                    locate_a = "101"
                elif s[2] == "R6":
                    a = r["110"]
                    locate_a = "110"
                elif s[2] == "FLAGS":
                    a = r["111"]
                    locate_a = "111"
                
                if s[3] == "R0":
                    b = r["000"]
                    locate_b = "000"
                elif s[3] == "R1":
                    b = r["001"]
                    locate_b = "001"
                elif s[3] == "R2":
                    b = r["010"]
                    locate_b = "010"
                elif s[3] == "R3":
                    b = r["011"]
                    locate_b = "011"
                elif s[3] == "R4":
                    b = r["100"]
                    locate_b = "100"
                elif s[3] == "R5":
                    b = r["101"]
                    locate_b = "101"
                elif s[3] == "R6":
                    b = r["110"]
                    locate_b = "110"
                elif s[3] == "FLAGS":
                    b = r["111"]
                    locate_b = "111"

                #diff = int(a, 2) - int(b, 2)
                #if diff < 0:
                #    diff = 0
                #diff = convert_to_16bits(diff)
                    #set flag
                
                #need to check overflow

                if s[1] == "R0":
                    #c = r["000"]
                    locate_c = "000"
                elif s[1] == "R1":
                    #c = r["001"]
                    locate_c = "001"
                elif s[1] == "R2":
                    #c = r["010"]
                    locate_c = "010"
                elif s[1] == "R3":
                    #c = r["011"]
                    locate_c = "011"
                elif s[1] == "R4":
                    #c = r["100"]
                    locate_c = "100"
                elif s[1] == "R5":
                    #c = r["101"]
                    locate_c = "101"
                elif s[1] == "R6":
                    #c = r["110"]
                    locate_c = "110"
                elif s[1] == "FLAGS":
                    #c = r["111"]
                    locate_c = "111"

                #c = "0000000000000000"
                #r[locate_c] = diff

                output.append("0000100"+locate_c+locate_a+locate_b)

        def ins_mov(r,s):
    
                if s[1] == "R0":
                    a = r["000"]
                    locate_a = "000"
                elif s[1] == "R1":
                    a = r["001"]
                    locate_a = "001"
                elif s[1] == "R2":
                    a = r["010"]
                    locate_a = "010"
                elif s[1] == "R3":
                    a = r["011"]
                    locate_a = "011"
                elif s[1] == "R4":
                    a = r["100"]
                    locate_a = "100"
                elif s[1] == "R5":
                    a = r["101"]
                    locate_a = "101"
                elif s[1] == "R6":
                    a = r["110"]
                    locate_a = "110"
                elif s[1] == "FLAGS":
                    a = r["111"]
                    locate_a = "111"

                if s[2][0] == "R" or s[2] == "FLAGS":
                    
                    if s[2] == "R0":
                        b = r["000"]
                        locate_b = "000"
                    elif s[2] == "R1":
                        b = r["001"]
                        locate_b = "001"
                    elif s[2] == "R2":
                        b = r["010"]
                        locate_b = "010"
                    elif s[2] == "R3":
                        b = r["011"]
                        locate_b = "011"
                    elif s[2] == "R4":
                        b = r["100"]
                        locate_b = "100"
                    elif s[2] == "R5":
                        b = r["101"]
                        locate_b = "101"
                    elif s[2] == "R6":
                        b = r["110"]
                        locate_b = "110"
                    elif s[2] == "FLAGS":
                        b = r["111"]
                        locate_b = "111"

                    #r[locate_a] = r[locate_b]

                    output.append("0001100000"+locate_a+locate_b)
                elif s[2][0] == "$":
                    if s[2][0] == "$":
                        c = int(s[2][1:])
                        c = convert_to_8bit(c)
                        #r[locate_a] = c    convert to 16 bit for this
                        
                        output.append("00010"+locate_a+c)
        
        def ins_ld(r,s,mem_add):
                
                if s[2] == "R0":
                    a = r["000"]
                    locate_a = "000"
                elif s[2] == "R1":
                    a = r["001"]
                    locate_a = "001"
                elif s[2] == "R2":
                    a = r["010"]
                    locate_a = "010"
                elif s[2] == "R3":
                    a = r["011"]
                    locate_a = "011"
                elif s[2] == "R4":
                    a = r["100"]
                    locate_a = "100"
                elif s[2] == "R5":
                    a = r["101"]
                    locate_a = "101"
                elif s[2] == "R6":
                    a = r["110"]
                    locate_a = "110"
                elif s[2] == "FLAGS":
                    a = r["111"]
                    locate_a = "111"

                for k in mem_add:
                    if k == s[1]:
                        address = mem_add[k]
                address = convert_to_8bit(address)

                output.append("00100"+ locate_a+address)

        def ins_st(r,s,mem_add):
                if s[1] == "R0":
                    a = r["000"]
                    locate_a = "000"
                elif s[1] == "R1":
                    a = r["001"]
                    locate_a = "001"
                elif s[1] == "R2":
                    a = r["010"]
                    locate_a = "010"
                elif s[1] == "R3":
                    a = r["011"]
                    locate_a = "011"
                elif s[1] == "R4":
                    a = r["100"]
                    locate_a = "100"
                elif s[1] == "R5":
                    a = r["101"]
                    locate_a = "101"
                elif s[1] == "R6":
                    a = r["110"]
                    locate_a = "110"
                elif s[1] == "FLAGS":
                    a = r["111"]
                    locate_a = "111"

                for k in mem_add:
                    if k == s[2]:
                        address = mem_add[k]
                address = convert_to_8bit(address)

                output.append("00101"+ locate_a+address)

        def ins_mul(r,s):
                
                if s[2] == "R0":
                    a = r["000"]
                    locate_a = "000"
                elif s[2] == "R1":
                    a = r["001"]
                    locate_a = "001"
                elif s[2] == "R2":
                    a = r["010"]
                    locate_a = "010"
                elif s[2] == "R3":
                    a = r["011"]
                    locate_a = "011"
                elif s[2] == "R4":
                    a = r["100"]
                    locate_a = "100"
                elif s[2] == "R5":
                    a = r["101"]
                    locate_a = "101"
                elif s[2] == "R6":
                    a = r["110"]
                    locate_a = "110"
                elif s[2] == "FLAGS":
                    a = r["111"]
                    locate_a = "111"
                
                if s[3] == "R0":
                    b = r["000"]
                    locate_b = "000"
                elif s[3] == "R1":
                    b = r["001"]
                    locate_b = "001"
                elif s[3] == "R2":
                    b = r["010"]
                    locate_b = "010"
                elif s[3] == "R3":
                    b = r["011"]
                    locate_b = "011"
                elif s[3] == "R4":
                    b = r["100"]
                    locate_b = "100"
                elif s[3] == "R5":
                    b = r["101"]
                    locate_b = "101"
                elif s[3] == "R6":
                    b = r["110"]
                    locate_b = "110"
                elif s[3] == "FLAGS":
                    b = r["111"]
                    locate_b = "111"

                #prod = int(a, 2) * int(b, 2)
                #prod = convert_to_16bits(prod)
                
                
                #need to check overflow

                if s[1] == "R0":
                    #c = r["000"]
                    locate_c = "000"
                elif s[1] == "R1":
                    #c = r["001"]
                    locate_c = "001"
                elif s[1] == "R2":
                    #c = r["010"]
                    locate_c = "010"
                elif s[1] == "R3":
                    #c = r["011"]
                    locate_c = "011"
                elif s[1] == "R4":
                    #c = r["100"]
                    locate_c = "100"
                elif s[1] == "R5":
                    #c = r["101"]
                    locate_c = "101"
                elif s[1] == "R6":
                    #c = r["110"]
                    locate_c = "110"
                elif s[1] == "FLAGS":
                    #c = r["111"]
                    locate_c = "111"

                
                #r[locate_c] = prod

                output.append("0011000"+locate_c+locate_a+locate_b)

        def ins_div(r,s):
                
                if s[1] == "R0":
                    a = r["000"]
                    locate_a = "000"
                elif s[1] == "R1":
                    a = r["001"]
                    locate_a = "001"
                elif s[1] == "R2":
                    a = r["010"]
                    locate_a = "010"
                elif s[1] == "R3":
                    a = r["011"]
                    locate_a = "011"
                elif s[1] == "R4":
                    a = r["100"]
                    locate_a = "100"
                elif s[1] == "R5":
                    a = r["101"]
                    locate_a = "101"
                elif s[1] == "R6":
                    a = r["110"]
                    locate_a = "110"
                elif s[1] == "FLAGS":
                    a = r["111"]
                    locate_a = "111"
                
                if s[2] == "R0":
                    b = r["000"]
                    locate_b = "000"
                elif s[2] == "R1":
                    b = r["001"]
                    locate_b = "001"
                elif s[2] == "R2":
                    b = r["010"]
                    locate_b = "010"
                elif s[2] == "R3":
                    b = r["011"]
                    locate_b = "011"
                elif s[2] == "R4":
                    b = r["100"]
                    locate_b = "100"
                elif s[2] == "R5":
                    b = r["101"]
                    locate_b = "101"
                elif s[2] == "R6":
                    b = r["110"]
                    locate_b = "110"
                elif s[2] == "FLAGS":
                    b = r["111"]
                    locate_b = "111"

                output.append("0011100000"+locate_a+locate_b)

        def ins_rs(r,s):
                
                if s[1] == "R0":
                    a = r["000"]
                    locate_a = "000"
                elif s[1] == "R1":
                    a = r["001"]
                    locate_a = "001"
                elif s[1] == "R2":
                    a = r["010"]
                    locate_a = "010"
                elif s[1] == "R3":
                    a = r["011"]
                    locate_a = "011"
                elif s[1] == "R4":
                    a = r["100"]
                    locate_a = "100"
                elif s[1] == "R5":
                    a = r["101"]
                    locate_a = "101"
                elif s[1] == "R6":
                    a = r["110"]
                    locate_a = "110"
                elif s[1] == "FLAGS":
                    a = r["111"]
                    locate_a = "111"

                p = int(s[2][1:])
                q = int(r[locate_a],2) >> p
                #r[locate_a] = convert_to_16bits(q)
                d = convert_to_8bit(p)

                output.append("01000"+ locate_a+d)

        def ins_ls(r,s):
                if s[1] == "R0":
                    a = r["000"]
                    locate_a = "000"
                elif s[1] == "R1":
                    a = r["001"]
                    locate_a = "001"
                elif s[1] == "R2":
                    a = r["010"]
                    locate_a = "010"
                elif s[1] == "R3":
                    a = r["011"]
                    locate_a = "011"
                elif s[1] == "R4":
                    a = r["100"]
                    locate_a = "100"
                elif s[1] == "R5":
                    a = r["101"]
                    locate_a = "101"
                elif s[1] == "R6":
                    a = r["110"]
                    locate_a = "110"
                elif s[1] == "FLAGS":
                    a = r["111"]
                    locate_a = "111"

                p = int(s[2][1:])
                q = int(r[locate_a],2) << p
                #r[locate_a] = convert_to_16bits(q)
                d = convert_to_8bit(p)

                output.append("01000"+ locate_a+d)

        def ins_xor(r,s):
                
                if s[2] == "R0":
                    a = r["000"]
                    locate_a = "000"
                elif s[2] == "R1":
                    a = r["001"]
                    locate_a = "001"
                elif s[2] == "R2":
                    a = r["010"]
                    locate_a = "010"
                elif s[2] == "R3":
                    a = r["011"]
                    locate_a = "011"
                elif s[2] == "R4":
                    a = r["100"]
                    locate_a = "100"
                elif s[2] == "R5":
                    a = r["101"]
                    locate_a = "101"
                elif s[2] == "R6":
                    a = r["110"]
                    locate_a = "110"
                elif s[2] == "FLAGS":
                    a = r["111"]
                    locate_a = "111"
                
                if s[3] == "R0":
                    b = r["000"]
                    locate_b = "000"
                elif s[3] == "R1":
                    b = r["001"]
                    locate_b = "001"
                elif s[3] == "R2":
                    b = r["010"]
                    locate_b = "010"
                elif s[3] == "R3":
                    b = r["011"]
                    locate_b = "011"
                elif s[3] == "R4":
                    b = r["100"]
                    locate_b = "100"
                elif s[3] == "R5":
                    b = r["101"]
                    locate_b = "101"
                elif s[3] == "R6":
                    b = r["110"]
                    locate_b = "110"
                elif s[3] == "FLAGS":
                    b = r["111"]
                    locate_b = "111"

                #xor = int(a, 2) ^ int(b, 2)
                #xor = convert_to_16bits(xor)
                
                
                

                if s[1] == "R0":
                    #c = r["000"]
                    locate_c = "000"
                elif s[1] == "R1":
                    #c = r["001"]
                    locate_c = "001"
                elif s[1] == "R2":
                    #c = r["010"]
                    locate_c = "010"
                elif s[1] == "R3":
                    #c = r["011"]
                    locate_c = "011"
                elif s[1] == "R4":
                    #c = r["100"]
                    locate_c = "100"
                elif s[1] == "R5":
                    #c = r["101"]
                    locate_c = "101"
                elif s[1] == "R6":
                    #c = r["110"]
                    locate_c = "110"
                elif s[1] == "FLAGS":
                    #c = r["111"]
                    locate_c = "111"

                
                #r[locate_c] = xor

                output.append("0101000"+locate_c+locate_a+locate_b)

        def ins_or(r,s):
                
                if s[2] == "R0":
                    a = r["000"]
                    locate_a = "000"
                elif s[2] == "R1":
                    a = r["001"]
                    locate_a = "001"
                elif s[2] == "R2":
                    a = r["010"]
                    locate_a = "010"
                elif s[2] == "R3":
                    a = r["011"]
                    locate_a = "011"
                elif s[2] == "R4":
                    a = r["100"]
                    locate_a = "100"
                elif s[2] == "R5":
                    a = r["101"]
                    locate_a = "101"
                elif s[2] == "R6":
                    a = r["110"]
                    locate_a = "110"
                elif s[2] == "FLAGS":
                    a = r["111"]
                    locate_a = "111"
                
                if s[3] == "R0":
                    b = r["000"]
                    locate_b = "000"
                elif s[3] == "R1":
                    b = r["001"]
                    locate_b = "001"
                elif s[3] == "R2":
                    b = r["010"]
                    locate_b = "010"
                elif s[3] == "R3":
                    b = r["011"]
                    locate_b = "011"
                elif s[3] == "R4":
                    b = r["100"]
                    locate_b = "100"
                elif s[3] == "R5":
                    b = r["101"]
                    locate_b = "101"
                elif s[3] == "R6":
                    b = r["110"]
                    locate_b = "110"
                elif s[3] == "FLAGS":
                    b = r["111"]
                    locate_b = "111"

                #orr = int(a, 2) | int(b, 2)
                #orr = convert_to_16bits(orr)
                
                
                

                if s[1] == "R0":
                    #c = r["000"]
                    locate_c = "000"
                elif s[1] == "R1":
                    #c = r["001"]
                    locate_c = "001"
                elif s[1] == "R2":
                    #c = r["010"]
                    locate_c = "010"
                elif s[1] == "R3":
                    #c = r["011"]
                    locate_c = "011"
                elif s[1] == "R4":
                    #c = r["100"]
                    locate_c = "100"
                elif s[1] == "R5":
                    #c = r["101"]
                    locate_c = "101"
                elif s[1] == "R6":
                    #c = r["110"]
                    locate_c = "110"
                elif s[1] == "FLAGS":
                    #c = r["111"]
                    locate_c = "111"

                
                #r[locate_c] = orr

                output.append("0000100"+locate_c+locate_a+locate_b)

        def ins_and(r,s):
                
                if s[2] == "R0":
                    a = r["000"]
                    locate_a = "000"
                elif s[2] == "R1":
                    a = r["001"]
                    locate_a = "001"
                elif s[2] == "R2":
                    a = r["010"]
                    locate_a = "010"
                elif s[2] == "R3":
                    a = r["011"]
                    locate_a = "011"
                elif s[2] == "R4":
                    a = r["100"]
                    locate_a = "100"
                elif s[2] == "R5":
                    a = r["101"]
                    locate_a = "101"
                elif s[2] == "R6":
                    a = r["110"]
                    locate_a = "110"
                elif s[2] == "FLAGS":
                    a = r["111"]
                    locate_a = "111"
                
                if s[3] == "R0":
                    b = r["000"]
                    locate_b = "000"
                elif s[3] == "R1":
                    b = r["001"]
                    locate_b = "001"
                elif s[3] == "R2":
                    b = r["010"]
                    locate_b = "010"
                elif s[3] == "R3":
                    b = r["011"]
                    locate_b = "011"
                elif s[3] == "R4":
                    b = r["100"]
                    locate_b = "100"
                elif s[3] == "R5":
                    b = r["101"]
                    locate_b = "101"
                elif s[3] == "R6":
                    b = r["110"]
                    locate_b = "110"
                elif s[3] == "FLAGS":
                    b = r["111"]
                    locate_b = "111"

                #andd = int(a, 2) & int(b, 2)
                #andd = convert_to_16bits(andd)
                

                if s[1] == "R0":
                    #c = r["000"]
                    locate_c = "000"
                elif s[1] == "R1":
                    #c = r["001"]
                    locate_c = "001"
                elif s[1] == "R2":
                    #c = r["010"]
                    locate_c = "010"
                elif s[1] == "R3":
                    #c = r["011"]
                    locate_c = "011"
                elif s[1] == "R4":
                    #c = r["100"]
                    locate_c = "100"
                elif s[1] == "R5":
                    #c = r["101"]
                    locate_c = "101"
                elif s[1] == "R6":
                    #c = r["110"]
                    locate_c = "110"
                elif s[1] == "FLAGS":
                    #c = r["111"]
                    locate_c = "111"

                #c = "0000000000000000"
                #r[locate_c] = andd

                output.append("0000100"+locate_c+locate_a+locate_b)

        def ins_not(r,s):
                
                if s[1] == "R0":
                    a = r["000"]
                    locate_a = "000"
                elif s[1] == "R1":
                    a = r["001"]
                    locate_a = "001"
                elif s[1] == "R2":
                    a = r["010"]
                    locate_a = "010"
                elif s[1] == "R3":
                    a = r["011"]
                    locate_a = "011"
                elif s[1] == "R4":
                    a = r["100"]
                    locate_a = "100"
                elif s[1] == "R5":
                    a = r["101"]
                    locate_a = "101"
                elif s[1] == "R6":
                    a = r["110"]
                    locate_a = "110"
                elif s[1] == "FLAGS":
                    a = r["111"]
                    locate_a = "111"
                
                if s[2] == "R0":
                    b = r["000"]
                    locate_b = "000"
                elif s[2] == "R1":
                    b = r["001"]
                    locate_b = "001"
                elif s[2] == "R2":
                    b = r["010"]
                    locate_b = "010"
                elif s[2] == "R3":
                    b = r["011"]
                    locate_b = "011"
                elif s[2] == "R4":
                    b = r["100"]
                    locate_b = "100"
                elif s[2] == "R5":
                    b = r["101"]
                    locate_b = "101"
                elif s[2] == "R6":
                    b = r["110"]
                    locate_b = "110"
                elif s[2] == "FLAGS":
                    b = r["111"]
                    locate_b = "111"

                output.append("0110100000"+ locate_a+locate_b)

        def ins_cmp(r,s):
                
                if s[1] == "R0":
                    a = r["000"]
                    locate_a = "000"
                elif s[1] == "R1":
                    a = r["001"]
                    locate_a = "001"
                elif s[1] == "R2":
                    a = r["010"]
                    locate_a = "010"
                elif s[1] == "R3":
                    a = r["011"]
                    locate_a = "011"
                elif s[1] == "R4":
                    a = r["100"]
                    locate_a = "100"
                elif s[1] == "R5":
                    a = r["101"]
                    locate_a = "101"
                elif s[1] == "R6":
                    a = r["110"]
                    locate_a = "110"
                elif s[1] == "FLAGS":
                    a = r["111"]
                    locate_a = "111"

                if s[2] == "R0":
                    b = r["000"]
                    locate_b = "000"
                elif s[2] == "R1":
                    b = r["001"]
                    locate_b = "001"
                elif s[2] == "R2":
                    b = r["010"]
                    locate_b = "010"
                elif s[2] == "R3":
                    b = r["011"]
                    locate_b = "011"
                elif s[2] == "R4":
                    b = r["100"]
                    locate_b = "100"
                elif s[2] == "R5":
                    b = r["101"]
                    locate_b = "101"
                elif s[2] == "R6":
                    b = r["110"]
                    locate_b = "110"
                elif s[2] == "FLAGS":
                    b = r["111"]
                    locate_b = "111"
                
                output.append("0111000000"+locate_a+locate_b)

        def ins_jmp(mem_add,s):
    
                for k in mem_add:
                    if s[1] == k:
                        address = mem_add[k]
                address = convert_to_8bit(address)

                output.append("01111000"+ address)

        def ins_jlt(mem_add,s):
                for k in mem_add:
                    if s[1] == k:
                        address = mem_add[k]
                address = convert_to_8bit(address)

                output.append("10000000"+ address)

        def ins_jgt(mem_add,s):
                for k in mem_add:
                    if s[1] == k:
                        address = mem_add[k]
                address = convert_to_8bit(address)

                output.append("10001000"+ address)

        def ins_je(mem_add,s):
                for k in mem_add:
                    if s[1] == k:
                        address = mem_add[k]
                address = convert_to_8bit(address)

                output.append("10010000"+ address)
        
        def ins_hlt():
            output.append("1001100000000000")

        s = lines[i].split()

        if s[0] == "add":
            pc += 1
            ins_add(r,s)
        elif s[0] == "sub":
            pc += 1
            ins_sub(r,s)
        elif s[0] == "mov":
            pc += 1
            ins_mov(r,s)
        elif s[0] == "ld":
            pc += 1
            ins_ld(r,s, mem_add)
        elif s[0] == "st":
            pc += 1
            ins_st(r,s, mem_add)
        elif s[0] == "mul":
            pc += 1
            ins_mul(r,s)
        elif s[0] == "div":
            pc += 1
            ins_div(r,s)
        elif s[0] == "rs":
            pc += 1
            ins_rs(r,s)
        elif s[0] == "ls":
            pc += 1
            ins_ls(r,s)
        elif s[0] == "xor":
            pc += 1
            ins_xor(r,s)
        elif s[0] == "or":
            pc += 1
            ins_or(r,s)
        elif s[0] == "and":
            pc += 1
            ins_and(r,s)
        elif s[0] == "not":
            pc += 1
            ins_not(r,s)
        elif s[0] == "cmp":
            pc += 1
            ins_cmp(r,s)
        elif s[0] == "jmp":
            pc += 1
            ins_jmp(mem_add,s)
        elif s[0] == "jlt":
            pc += 1
            ins_jlt(mem_add,s)
        elif s[0] == "jgt":
            pc += 1
            ins_jgt(mem_add,s)
        elif s[0] == "je":
            pc += 1
            ins_je(mem_add,s)
        elif s[0] == "hlt":
            pc += 1
            ins_hlt()
        elif s[0] == "var":
            pc -= 1
    

for i in output:
    print(i)              

  
                