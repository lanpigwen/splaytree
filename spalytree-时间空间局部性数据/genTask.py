import random
def getTaskSeq(seqLen=200,maxNum=400,existsLen=500,seed=1,taskFreq=[0.7,0.2,0.1]):
    # random.seed(seed)
    existNum=[random.randint(0, maxNum) for i in range(existsLen) ]
    origin_existNum = existNum.copy()
    copy_existNum=existNum.copy()
    # 先进行 树的构建
    # print(existNum)
    random.shuffle(existNum)

    search20=existNum[int(0.8*len(existNum)):]
    search80=existNum[0:int(0.8*len(existNum))]

    # search20=existNum[int(0.95*len(existNum)):]
    # search80=existNum[0:int(0.95*len(existNum))]


    # 改成最近访问的

    # print(existNum)
    # print(search80)
    # print(search20)

    insertTask=[]
    deleteTask=[]
    searchTask=[]
    opTask=[]
    opNum=[]
    # ops=[0,1,2]
    taskLen=seqLen
    t=0
    cnt20 = 0
    cnt80 = 0
    x=float(sum(taskFreq))
    taskFreq=[i/x for i in taskFreq]
    # print(taskFreq)

    while t<taskLen:
        t+=1
        rd=random.random()
        # random.seed(rd)
        if rd<taskFreq[0]:
            task=0
        elif rd<taskFreq[0]+taskFreq[1]:
            task=1
        else:
            task=2

        #     do task
        num=0

        if task==0:
            searchFrom=random.random()
            if searchFrom<0.8:
                cnt20+=1
                num = random.choice(search20)
                if len(insertTask)>0 and searchFrom<0.8*0.2:
                    num = random.choice(insertTask)
            else:
                cnt80+=1
                num = random.choice(search80)
                if len(insertTask)>0 and searchFrom<0.8+0.2*0.2:
                    num = random.choice(insertTask)
            # searchTask.append(num)
        if task==1:
            num = random.randint(0, maxNum)
            insertTask.append(num)
            copy_existNum.append(num)
            # opTask.append()
        if task==2:
            num = random.choice(copy_existNum)

        opTask.append(task)
        opNum.append(num)
    return opNum,opTask,origin_existNum

# opTask,opNum=getTaskSeq(taskFreq=[2,1,1])
# # print(copy_existNum)
# print(opNum)
# print(opTask)
# print(len(opNum)==len(opTask))
# # print(cnt20,cnt80)


def getTaskSeq_searchRecent(seqLen=200,maxNum=400,existsLen=500,seed=1,taskFreq=[0.7,0.2,0.1],preOp=5,recentFreq=[0.6,0.3,0.1]):

    existNum=[random.randint(0, 4*existsLen) for i in range(existsLen) ]
    origin_existNum = existNum.copy()
    copy_existNum=existNum.copy()
    random.shuffle(existNum)

    search20=existNum[int(0.8*len(existNum)):]
    search80=existNum[0:int(0.8*len(existNum))]

    # 改成最近访问的

    insertTask=[]

    opTask=[]
    opNum=[]
    Searched=[]
    taskLen=seqLen
    t=0
    cnt20 = 0
    cnt80 = 0
    x=float(sum(taskFreq))
    taskFreq=[i/x for i in taskFreq]

    x=float(sum(recentFreq))
    recentFreq=[i/x for i in recentFreq]

    while t<taskLen:
        t+=1
        rd=random.random()
        if rd<taskFreq[0]:
            task=0
        elif rd<taskFreq[0]+taskFreq[1]:
            task=1
        else:
            task=2

        #     do task
        num=0

        if task==0:
            searchFrom=random.random()
            # 从最近preOp次的opNum中再次搜索 /  过去搜索过的/ 随机搜索=0.3：0.6：0.1
            if searchFrom<recentFreq[0] and len(opNum)>0:
                # print(opNum)
                pre = min(len(opNum),min(existsLen, preOp))
                num = random.choice(opNum[-pre:])
            elif searchFrom<recentFreq[0]+recentFreq[1] and len(Searched)>50:
                num = random.choice(Searched)
            else:
                num = random.randint(0, 4*existsLen)

            Searched.append(num)

        if task==1:
            num = random.randint(0, 4*existsLen)
            insertTask.append(num)
            copy_existNum.append(num)
        if task==2:
            num = random.choice(copy_existNum)

        opTask.append(task)
        opNum.append(num)
    return opNum,opTask,origin_existNum


def getRealTaskSeq(seqLen=200,existsLen=500,taskFreq=[0.7,0.2,0.1]):
    # random.seed(1)
    existNum=[random.randint(0, 4*existsLen) for i in range(existsLen) ]

    opTask=[]
    opNum=[]
    taskLen=seqLen
    t=0
    x=float(sum(taskFreq))
    taskFreq=[i/x for i in taskFreq]

    while t<taskLen:
        t+=1
        rd=random.random()
        if rd<taskFreq[0]:
            task=0
        elif rd<taskFreq[0]+taskFreq[1]:
            task=1
        else:
            task=2
        num = random.randint(0, 4*existsLen)
        opTask.append(task)
        opNum.append(num)
    return opNum,opTask,existNum


def getTaskSeq_allRecent(seqLen=200,existsLen=500,taskFreq=[0.7,0.2,0.1],preOp=0,recentFreq=[0,1],sigma=0):

    existNum=[random.randint(0, 4*existsLen) for i in range(existsLen) ]

    opTask=[]
    opNum=[]

    taskLen=seqLen
    t=0
    x=float(sum(taskFreq))
    taskFreq=[i/x for i in taskFreq]

    x=float(sum(recentFreq))
    recentFreq=[i/x for i in recentFreq]

    while t<taskLen:
        t+=1
        rd=random.random()
        if rd<taskFreq[0]:
            task=0
        elif rd<taskFreq[0]+taskFreq[1]:
            task=1
        else:
            task=2
        #     do task
        opNumFrom=random.random()
        # 从最近preOp次的opNum中 / 随机=0.5：0.5
        if opNumFrom<recentFreq[0] and len(opNum)>0:
            # 时间局部性
            # preOp>0时，使用指定的前preOp个操作数
            # pre = min(len(opNum),min(existsLen, preOp))
            pre = min(len(opNum),preOp)
            num = random.choice(opNum[-pre:])
            # 空间局部性 ，操作数是上一个操作数x  x-sigma,x+sigma中的随机数
            if sigma:
                last_num=opNum[-1]
                num = random.randint(last_num - sigma, last_num + sigma)
                num = max(0,num)
        else:
            num = random.randint(0, 4*existsLen)

        opTask.append(task)
        opNum.append(num)
    return opNum,opTask,existNum
