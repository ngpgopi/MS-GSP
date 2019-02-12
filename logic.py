import copy
file = open('output.txt','w')

def getItemCount(inputTransactions):
    dict1 = {}
    totalTransactions = len(inputTransactions)
    for i in range(len(inputTransactions)):
        templist = []
        for j in range(len(inputTransactions[i])):
            for k in range(len(inputTransactions[i][j])):
                if inputTransactions[i][j][k] not in templist:
                    if inputTransactions[i][j][k] in dict1:
                        val = dict1[inputTransactions[i][j][k]]
                        val = val + 1
                        dict1[inputTransactions[i][j][k]] = val
                    else:
                        dict1[inputTransactions[i][j][k]] = 1
                    templist.append(inputTransactions[i][j][k])
    itemList = list(dict1.keys())
    return dict1, totalTransactions, itemList


def sortMIS(MIS):
    sortedMIS = {}
    sorted_by_value = sorted(MIS.items(), key=lambda kv: kv[1])
    for i in sorted_by_value:
        sortedMIS[i[0]] = i[1]
    return (sortedMIS)


def initPass(sortedMIS, MIS, dict1, totalTransactions):
    L = []
    leastMISValue = 0
    acutalSupport = {}
    tempList = []
    for key, value in dict1.items():
        acutalSupport[key] = value / totalTransactions
    for key, value in sortedMIS.items():
        if key in dict1.keys():
            if (acutalSupport[key] >= value) and not L:
                L.append(key)
                leastMISValue = value
            if (acutalSupport[key] >= leastMISValue) and (key not in L) and (len(L) > 0):
                L.append(key)
    for item in L:
        if acutalSupport[item] >= MIS[item]:
            tempList.append([item])
    finalS = copy.deepcopy(tempList)
    return L, acutalSupport, finalS


def level2Candgen(L, acutalSupport, MIS, sdc):
    c2 = []
    for i, item in enumerate(L):
        if (acutalSupport[item] >= MIS[item]):
            for item1 in L:
                if (acutalSupport[item1] >= MIS[item]) and (abs(acutalSupport[item1] - acutalSupport[item]) <= sdc):
                    if [[item, item1]] not in c2:
                        c2.append([[item, item1]])
                    if [[item1, item]] not in c2:
                        c2.append([[item1,item]])
                    if [[item], [item1]] not in c2:
                        c2.append([[item], [item1]])
                    if [[item1],[item]] not in c2:
                        c2.append([[item1],[item]])
    return c2


def checkforOrder(item, inputSubSeq):
    index = -1
    tempList = []
    for element in item:
        if (index < inputSubSeq.index(element)):
            index = inputSubSeq.index(element)
            tempList.append(element)
    if (tempList == item):
        return True
    else:
        return False


def candidateCount(c1, inputTransactions):
    count = 0
    for inputSeq in inputTransactions:
        addedItems = []
        tempc1 = copy.deepcopy(c1)
        tempInputSeq = copy.deepcopy(inputSeq)
        for i, ab in enumerate(tempc1):
            for j, rz in enumerate(tempInputSeq):
                if (set(ab).issubset(set(rz))):
                    val = checkforOrder(ab, rz)
                    if (val):
                        tempInputSeq = tempInputSeq[j + 1:]
                        addedItems.append(ab)
                        break
        if addedItems == c1:
            count = count + 1
    return (count)


def findLeastMISitem(s, MIS):
    MISdefault = 1
    subIndex = 0
    mainIndex = 0
    leastItem = ''
    for i, each in enumerate(s):
        for j, item in enumerate(each):
            if MIS[item] < MISdefault:
                mainIndex = i
                subIndex = j
                leastItem = item
                MISdefault = MIS[item]
    if(leastItem is ''):
        mainIndex = 0
        subIndex = 0
        leastItem = s[0][0]
    return mainIndex, subIndex, leastItem

def findLeastMISitem1(s, MIS):
    MISdefault = 1
    subIndex = 0
    mainIndex = 0
    leastItem = ''
    for i, each in enumerate(s):
        for j, item in enumerate(each):
            if MIS[item] <= MISdefault:
                mainIndex = i
                subIndex = j
                leastItem = item
                MISdefault = MIS[item]
    if(leastItem is ''):
        mainIndex = 0
        subIndex = 0
        leastItem = s[0][0]
    return mainIndex, subIndex, leastItem


def checkforMerging(s1, s2, MIS,acutalSupport,sdc):
    merged = []
    for each1 in s1:
        merged = merged + each1
    for each2 in s2:
        merged = merged + each2
    lastItem = merged[len(merged) - 1]
    merged.pop(len(merged) - 1)
    merged.pop(1)
    a = merged[:len(merged) // 2]
    b = merged[len(merged) // 2:]
    checkVal = True
    for each in s1:
        for item in each:
            if(abs(acutalSupport[item] - acutalSupport[lastItem]) <= sdc):
                continue
            else:
                checkVal = False
    if (a == b) and (MIS[a[0]] <= MIS[lastItem]) and checkVal:
        return 'True'
    else:
        return 'False'

def checkforMerging2(s1,s2,MIS,acutalSupport,sdc):
    merged = []
    for each1 in s1:
        merged = merged + each1
    for each2 in s2:
        merged = merged + each2
    lastItem = merged[len(merged)-1]
    merged.pop(len(merged)-2)
    merged.pop(0)
    a = merged[:len(merged)//2]
    b = merged[len(merged)//2:]
    checkVal = True
    for each in s2:
        for item in each:
            if(abs(acutalSupport[item] - acutalSupport[s1[0][0]]) <= sdc):
                continue
            else:
                checkVal = False
    if (a == b) and (MIS[s1[0][0]] > MIS[lastItem]) and checkVal:
        return 'True'
    else:
        return 'False'

def findFirstItemofSequence(sequence):
    v1 = len(sequence)
    v2 = len(sequence[0])
    q = sequence[0][0]
    return q,v1,v2

def combineTwoSequences2(s1,s2):
    merge1 = copy.deepcopy(s2)
    merge2 = copy.deepcopy(s2)
    lengthOfS2 = 0
    for each in s2:
        for item in each:
            lengthOfS2 = lengthOfS2 +1
    firstItemofS2,sizeOfS2,SizeoffirstItemS2 = findFirstItemofSequence(s2)
    firstItemofS1,sizeOfS1,SizeoffirstItemS1 = findFirstItemofSequence(s1)
    if(SizeoffirstItemS1 == 1) :
        merge1.insert(0,[firstItemofS1])
        if (lengthOfS2 == 2 and sizeOfS2 == 2) and (firstItemofS1 < firstItemofS2):
            merge2[0].insert(0,firstItemofS1)
    elif ((lengthOfS2 == 2 and sizeOfS2 ==1) and (firstItemofS1 < firstItemofS2)) or (lengthOfS2 > 2):
        merge1[0].insert(0,firstItemofS1)
    if(merge1 == s2):
        return None,None
    else:
        return merge1,merge2

def GSPCheckforMerge(s1, s2,acutalSupport,sdc):
    merged = []
    for each1 in s1:
        merged = merged + each1
    for each2 in s2:
        merged = merged + each2
    lastItem = merged[len(merged) - 1]
    merged.pop(len(merged) - 1)
    merged.pop(0)
    a = merged[:len(merged) // 2]
    b = merged[len(merged) // 2:]
    checkVal = True
    for each in s1:
        for item in each:
            if(abs(acutalSupport[item] - acutalSupport[lastItem]) <= sdc):
                continue
            else:
                checkVal = False
    if a == b and checkVal:
        return 'True'
    else:
        return 'False'


def GSPCombineLogic(s1, s2):
    merged = copy.deepcopy(s1)
    if len(s2[len(s2) - 1]) == 1:
        merged.append(s2[len(s2) - 1])
    else:
        merged[len(merged) - 1].append(s2[len(s2) - 1][len(s2[len(s2) - 1]) - 1])
    return (merged)


def findLastItemofSequence(sequence):
    v1 = len(sequence)
    v2 = len(sequence[len(sequence) - 1])
    q = sequence[v1 - 1][v2 - 1]
    return q, v1, v2


def combineTwoSequences(s1, s2):
    merge1 = copy.deepcopy(s1)
    merge2 = copy.deepcopy(s1)
    lengthOfS1 = 0
    for each in s1:
        for item in each:
            lengthOfS1 = lengthOfS1 + 1
    lastItemofS2, sizeOfS2, SizeofLastItemS2 = findLastItemofSequence(s2)
    lastItemofS1, sizeOfS1, SizeofLastItemS1 = findLastItemofSequence(s1)
    if SizeofLastItemS2 == 1:
        merge1.append([lastItemofS2])
        if (lengthOfS1 == 2 and sizeOfS1 == 2) and (lastItemofS2 > lastItemofS1):
            merge2[sizeOfS1 - 1].append(lastItemofS2)
    elif ((lengthOfS1 == 2 and sizeOfS1 == 1) and (lastItemofS2 > lastItemofS1)) or (lengthOfS1 > 2):
        merge1[sizeOfS1 - 1].append(lastItemofS2)
    return merge1, merge2


def MScandidategenSPM(s1, s2, MIS,acutalSupport,sdc):
    mainIndex, subIndex, leastItem = findLeastMISitem(copy.deepcopy(s1), MIS)
    mainIndex2, subIndex2, leastItem2 = findLeastMISitem(copy.deepcopy(s2), MIS)
    if mainIndex == 0 and subIndex == 0:
        val = checkforMerging(s1, s2, MIS,acutalSupport,sdc)
        if val == 'True':
            v1, v11 = combineTwoSequences(copy.deepcopy(s1), copy.deepcopy(s2))
            return v1, v11
        else:
            return None, None
    elif mainIndex2 == (len(s2) - 1) and subIndex2 == (len(s2[len(s2) - 1]) - 1):
        val = checkforMerging2(s1, s2, MIS,acutalSupport,sdc)
        if val == 'True':
            v2, v21 = combineTwoSequences2(copy.deepcopy(s1), copy.deepcopy(s2))
            return v2, v21
        else:
            return None, None
    else:
        val = GSPCheckforMerge(s1, s2,acutalSupport,sdc)
        if val == 'True':
            v3 = GSPCombineLogic(copy.deepcopy(s1), copy.deepcopy(s2))
            return v3, None
        else:
            return None, None


def frequencyGeneration(candidates, MIS, totalTransactions, inputTransactions):
    F = []
    count1 = []
    for eachItem in candidates:
        count = candidateCount(eachItem, inputTransactions)
        if count > 0:
            mainIndex, subIndex, leastItem = findLeastMISitem1(eachItem, MIS)
            if (count / totalTransactions) >= (MIS[leastItem]) and (eachItem not in F):
                # print(eachItem, 'Count:', count)
                count1.append(count)
                F.append(eachItem)
    return F,count1


def checkpruning(candidate, F,MIS):
    mainIndex, subIndex, leastItem = findLeastMISitem1(candidate,MIS)
    length = len(candidate)
    noList = []
    yesList = []
    for i in range(length):
        temp = copy.deepcopy(candidate)
        if len(temp[i]) > 1:
            for j in range(len(temp[i])):
                temp = copy.deepcopy(candidate)
                temp[i].pop(j)
                if temp in F:
                    yesList.append(candidate[i][j])
                elif leastItem in candidate[i][j]:
                    yesList.append(candidate[i][j])
                else:
                    noList.append(candidate[i][j])
        else:
            temp.pop(i)
            if temp in F:
                yesList.append(candidate[i])
            elif leastItem in candidate[i]:
                yesList.append(candidate[i])
            else:
                noList.append(candidate[i])
    return noList, leastItem
