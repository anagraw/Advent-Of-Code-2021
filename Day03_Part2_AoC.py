def maxo(lst):
    cnt1=0
    cnt0=0
    for ele in lst:
        if ele== '0':
            cnt0+=1
        elif ele== '1':
            cnt1+=1
    if cnt1> cnt0:
        return ('1')
    elif cnt0> cnt1:
        return('0')
    elif cnt0== cnt1:
        return('1')
flst,lst=[],[]
while True:
    num= input('')
    if num== 'no':
        break
    lst.append(num)
num=0
temp=[]
tflst=[]
for i in range(12):
    if len(lst)==1:
        print(lst)
        exit()
    for ele in lst:
        temp.append(ele[i])
    num= maxo(temp)
    flst.append(num)
    for elen in lst:
        if elen[i]== num:
            tflst.append(elen)
    lst= tflst
    num=0
    tflst,temp=[],[]
print(flst)
    
