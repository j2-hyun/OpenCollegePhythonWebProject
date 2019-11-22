names=["이광우","백정규","이욱호","이지은"]
nimNames=[]
for name in names:
    nimNames.append(name+'님')
for nimName in nimNames:
    print(nimName)

print("-------------------------")
nimNames2=[name+'님' for name in names]
for nimName in nimNames2:
    print(nimName)