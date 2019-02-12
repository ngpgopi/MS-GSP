import logic as lc
import copy
import readFromFile

print("Program Started.....")
inputTransactions = readFromFile.readfromfileInput()
MIS, sdc = readFromFile.readFileRequirement()

sortedMIS = lc.sortMIS(MIS)
dict1, totalTransactions, itemList = lc.getItemCount(inputTransactions)
file = open('output.txt','w')

def writetofile(line,count):
    mainstr = 'Pattern : <'
    for each in line:
        strline = "{"
        for item in each:
            # print(item)
            strline = strline +  str(item) + ' '
        strline = strline + '}'
        mainstr = mainstr + strline
    mainstr = mainstr + '>' + ":Count=" + str(count) + "\n"
    file.write(mainstr)


# line2 and Line3 ((F1 generation)
L, acutalSupport, F1 = lc.initPass(sortedMIS, MIS, dict1, totalTransactions)
print("Running....")
file.write("The number of length 1 sequential patterns is " + str(len(F1)) + "\n")
for each in F1:
    writetofile(each, dict1[each[0]])

# Line4, Line 5, Line6 (2nd Level Candidate Generation)
c2 = lc.level2Candgen(L, acutalSupport, MIS, sdc)

# Second frequency generation
print("Running....")
F,count = lc.frequencyGeneration(c2, MIS, totalTransactions, inputTransactions)
file.write("The number of length 2 sequential patterns is " + str(len(F)) + "\n")
for i,f in enumerate(F):
    writetofile(f, count[i])

# Generate next set of candidates
f = 2
while len(F) > 1:
    print("Running....")
    f = f + 1
    finalMergedSequence = []
    for i in range(len(F)):
        for j in range(len(F)):
            value, value1 = lc.MScandidategenSPM(copy.deepcopy(F[i]), copy.deepcopy(F[j]),MIS,acutalSupport,sdc)
            if (value not in finalMergedSequence) and (value is not None) and (value != F[i]):
                finalMergedSequence.append(value)
            if (value1 not in finalMergedSequence) and (value1 is not None) and (value1 != F[i]):
                finalMergedSequence.append(value1)

    prunedList = []
    for eachS in finalMergedSequence:
        noList, leastItem = lc.checkpruning(eachS,F,MIS)
        if(leastItem not in noList) and (not noList):
            prunedList.append(eachS)

    F,count = lc.frequencyGeneration(prunedList, MIS, totalTransactions, inputTransactions)
    str1 = "The number of length " + str(f) +" sequential patterns is " + str(len(F)) + "\n"
    file.write(str1)
    for i, j in enumerate(F):
        writetofile(j, count[i])


print("Please read the output text file for the results")