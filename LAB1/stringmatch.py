def stringmatch(str1,str2,str3):
    j = 0
    result = []
    while j<len(str1):
        if str1[j]==str2[0]:
            mark = j
            count=0
            for i in range(len(str2)):
                if str1[j]==str2[i]:
                    count = count+1
                    j=j+1
            if count==len(str2):
                str1copy = str1[0:mark]
                str2copy = str1[mark+count:]
                x = str1copy+str3+str2copy
                result.append(x)        
        j = j+1
    return result

x = stringmatch("shakanthshikanth","kanth",'just')
print(x)
