from array import array
#get inpu
link1 = input("Enter link 1: ")
link2 = input("Enter link 2: ")

match = False
counter = 0
mismatch = False

#mismatch position array
a = array("i",[])

#compare the lengths of 2 links
if len(link1) == len(link2):
    length = len(link1)

    #compare each element in 2 links
    for i in range(0,len(link1)):
        if link1[i] == link2[i]:
            counter = counter+1
        else:
            match = False
            a.append(i)
    if counter == length:
        match = True
    #output if success
    if match:
        print("Two links does match")

    #output if unsuccess
    else:
        print("Two links does not match. Mismatch in following positions")
        #display each mismatch position
        for i in range(0,len(a)):
            print("position:" + str(a[i]))

        ##display each mismatch in link
        for i in range(0,length):
            mismatch = False
            for j in range(0, len(a)):
                if i == a[j]:
                    print('_', end="")
                    mismatch = True
                    break
            if mismatch:
                continue
            print(link1[i], end="")



else:
    print("Two links does not match")

