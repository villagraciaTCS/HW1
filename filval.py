import os
import math

def base(x):
    first_ten = ['isa', 'dalawa', 'tatlo', 'apat', 'lima', 'anim', 'pito', 'walo', 'siyam']
    if x != 0:
        return first_ten[x-1]
    else:
        return ''

def triples(sliced):
    triple = ''
    sliced = str(sliced)
    
    for i in range(len(str(int(sliced)))-1, -1, -1):
        digit = (int(sliced) // 10**i) % 10
        temp = base(digit)
        if(i == 2 and temp != ''):
            if digit in [4, 6, 9]:
                temp += " na raan"
            else:
                temp += "ng daan"
            
            if(int(sliced[i-1]) != 0 or int(sliced[-1]) != 0):
                temp += " at "
            
        elif(i == 1 and temp != ""):
            if digit == 1:
                if int(sliced[-1]) in [1, 4, 6, 8]:
                    triple += "labing-" + base(int(sliced[-1]))
                elif int(sliced[-1]) == 0:
                    triple += "sampu"
                elif int(sliced[-1]) == 7:
                    triple += "labim" + base(int(sliced[-1]))
                else:
                    triple += "labin" + base(int(sliced[-1]))
                break
            elif digit in [4,6,9]:
                temp += "napu"
            else:
                temp = temp.replace('o', 'u')
                temp += "mpu"
            
            if int(sliced[-1]) != 0:
                temp += "'t "
        triple += temp
    return triple

given = input("\nEnter a digit: ")
while(not given.isdigit() or len(given) > 12):          #Only accepts digits until the billions
    given = input("[!] Please enter a valid digit: ")

final = ''
right_value = 0
for i in range(0, len(given), 3):
    group = triples((int(given) // 10**i) % 10**3)
    if group != '':
        if i == 0:
            group += ""
        else:
            if group[-1] == 'n':
                group = group[0:-1]

            if group[-1] not in ['o', 'a']:
                group += " na "
            else: 
                group += "ng "
            
            if i == 3:
                group += "libo"
            elif i == 6:
                group += "milyon"
            elif i == 9:
                group += "bilyon"
            else:
                group += "somethingW"

            if right_value != 0:
                group += " at "
        right_value += 1

    final = group + final

os.system('cls' or 'clear')
print("You have chosen the number", given, "or '\033[32;1m" + final, end="\033[m'.\n\n")