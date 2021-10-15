def validateStackSequences(pushed,popped):
    list1 = []
    j = 0
    for i in range(len(popped)):
        while True:
            if j >= len(pushed) and len(list1) != 0 and list1[-1] != popped[i]: return False
            if j<len(pushed):
                if pushed[j] == popped[i]:
                    j+=1
                    break
            if len(list1) != 0 and list1[-1] == popped[i]:
                list1.remove(list1[-1])
                break
            list1.append(pushed[j])
            j += 1

    return True

pushed = [1,2,3,4,5]
popped = [4,5,3,1,2]
print(validateStackSequences(pushed,popped))