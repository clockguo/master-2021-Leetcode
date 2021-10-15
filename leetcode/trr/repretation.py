def isNumber(s):
    # oc={}
    # for i in s:
    #     if i in oc:
    #         oc[i] +=1
    #     else:
    #         oc[i] = 1
    #
    dp=[0 for i in range(len(s))]

    for i in range(len(s)):
        if i == 0:

            continue
        if s[i] in ['+','-']:
            if not s[i-1]:
                return