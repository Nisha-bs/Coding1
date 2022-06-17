#!/usr/bin/python3
import itertools

def key_pad(number):
    keypad = (' ','.','abc','def','ghi','jkl','mnop','qrst','uvw','xyz')
    #number = input("enter the number")
    rslt = ''
    rslt_list = []
    for i in number:
        #print(i)
        if i == '0':
            #rslt += keypad[0]
            rslt = keypad[0]
            print(rslt)
            rslt_list.append(rslt)
        elif i == '1':
            #rslt += keypad[1]
            rslt = keypad[1]
            rslt_list.append(rslt)
        elif i == '2':
            #rslt += keypad[2]
            rslt = keypad[2]
            rslt_list.append(rslt)
        elif i == '3':
            #rslt += keypad[3]
            rslt = keypad[3]
            rslt_list.append(rslt)
        elif i == '4':
            #rslt += keypad[4]
            rslt = keypad[4]
            rslt_list.append(rslt)
        elif i == '5':
            #rslt += keypad[5]
            rslt = keypad[5]
            rslt_list.append(rslt)
        elif i == '6':
            #rslt += keypad[6]
            rslt = keypad[6]
            rslt_list.append(rslt)
        elif i == '7':
            #rslt += keypad[7]
            rslt = keypad[7]
            rslt_list.append(rslt)
        elif i == '8':
            #rslt += keypad[8]
            rslt = keypad[8]
            rslt_list.append(rslt)
        elif i == '9':
            #rslt += keypad[9]
            rslt = keypad[9]
            rslt_list.append(rslt)
    print(rslt_list)

    '''comb = list(itertools.combinations(rslt, 2))
    for c in comb:
        print(c)'''

    for ele in range(len(rslt_list)):
        list1 = []
        list1.append(rslt_list[ele])
        for nxt_ele in range(1,len(rslt_list)):
            if rslt_list[ele] != rslt_list[nxt_ele]:
                list2 = []
                list2.append(rslt_list[nxt_ele])
                print(list1,list2)
                for inner_ele in range(len(list1)):
                    print(type(inner_ele))
                    for inner_nxt_ele in range(len(list2)):
                        print("ii")
key_pad('123')
