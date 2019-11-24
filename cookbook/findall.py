import re
#pattern = re.compile(r'((2(5[0-5]|[0-4]\d))|[0-1]?\d{1,2})(\.((2(5[0-5]|[0-4]\d))|[0-1]?\d{1,2})){3}')
#pattern = re.compile(r'^(((25[0-5]|2[0-4]\d|1\d{2})|([1-9]?\d))\.){3}((25[0-5]|2[0-4]\d|1\d{2})|([1-9]?\d))$')
#pattern = re.compile('"^(1\\d{2}|2[0-4]\\d|25[0-5]|[1-9]\\d|[1-9])\\." \
#        +"(1\\d{2}|2[0-4]\\d|25[0-5]|[1-9]\\d|\\d)\\."+ \
#        "(1\\d{2}|2[0-4]\\d|25[0-5]|[1-9]\\d|\\d)\\."+ \
#        "(1\\d{2}|2[0-4]\\d|25[0-5]|[1-9]\\d|\\d)$"')
resultlist = []

pattern = re.compile(r"\b(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b")
with open('resultList.txt','r') as a:
        filenames = a.readlines()
        for filename in filenames:
            filename = filename.rstrip('\n')
            try:
                with open(filename,'r') as f:
                    fileHasIp = 0
                    ftextlist = f.readlines()
                    for line in ftextlist:
                        if(pattern.findall(line)):
                            print(pattern.findall(line))
                            fileHasIp = 1
#                                resultlist.append(fileHasIp)
                        else:
                            if fileHasIp == 0:
                                fileHasIp = 0
                    if fileHasIp == 1:
                        print(filename)
            except Exception as e:
                pass
                
