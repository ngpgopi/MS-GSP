def readfromfileInput():
    file = open('input.txt', 'r')
    inputTransactions = []
    for line in file:
        # print(line)
        value = ''
        masterList = []
        newList = []
        count = 0
        for letter in line:
            if(letter == '<'):
                masterList = []
            elif(letter == '{'):
                newList = []
            elif(letter == '}'):
                newList.append(value)
                value = ''
                masterList.append(newList)
            elif(letter == ','):
                # value = ul.quote("'{}'").format(value)
                newList.append(value)
                value = ''
            elif(letter == ' '):
                count = count +1
            else:
                value = value + letter
        inputTransactions.append(masterList)
    return inputTransactions

def readFileRequirement():
    file2 = open('requirements.txt','r')
    MIS = {}
    sdc = 1
    for line in file2:
        index = line.find("(")
        index2 = line.find(")")
        if(index != -1):
            key = line[index+1:index2]
            equalIndex = line.find('=')
            lastIndex = line.rfind(" ")
            mis = line[equalIndex+1:lastIndex]
            MIS[str(key)] = float(mis)
        else:
            equalIndex = line.find('=')
            lastIndex = line.rfind(" ")
            sdc = float(line[equalIndex+1:])
    # print(MIS)
    return  MIS,sdc
