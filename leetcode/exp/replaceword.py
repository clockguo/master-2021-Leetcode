def replaceWords(roots, sentence):
    rootset = set(roots)
    max1 = 0
    for i in roots:
        max1 = max(max1,len(i))
    def replace(word):
        left = 0
        while left <len(word):
            tem = ''
            for i in range(left, len(word)):
                if len(tem)> max1:
                    break
                if word[i]!=' ' :
                    tem += word[i]
                    if tem in rootset:
                        word = word[:left]+' '+tem+' '+word[i+1:]
                        left = i
                else:
                    continue
            left += 1
        return word
    result = replace(sentence)
    if result[0]==' ':
        result = result[1:]
    if result[-1]==' ':
        result = result[:-1]
    return result

print(replaceWords(['ded'],'aa bcd edf deda'))
print(replaceWords(['愧不敢当','娘娘谬'],'娘娘 谬赞 ， 臣妾愧 不敢 当'))
