def replace_space(s):
    s = list(s)
    print(s)
    for i,q in enumerate(s):
        if s[i] == ' ':
            s[i]='%20'
        else:
            continue
    s=''.join(s)
    return s
s = "We are happy."
print(replace_space(s))