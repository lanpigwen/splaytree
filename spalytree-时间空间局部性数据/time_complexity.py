import time
import matplotlib.pyplot as plt
from genTask import getTaskSeq,getRealTaskSeq

from BST import BST
from SplayTree import SplayTree

if __name__ == '__main__':
    input_sizes = []
    splay_times = []
    bst_times=[]
    epoch=5
    for size in range(10, 2**10, 10):

        input_sizes.append(size)
        splay_time_all=[]
        bst_time_all=[]
        for e in range(epoch):
            # Generating task sequences for the experiment
            seq1, op1, exist = getRealTaskSeq(existsLen=size, seqLen=10000, taskFreq=[1, 1, 1])
            # seq1, op1, exist = getTaskSeq(existsLen=size, seqLen=10000, taskFreq=[1, 1, 1])
            seq0 = exist
            op0 = [1 for i in range(len(seq0))]

            sp = SplayTree()
            sp.seq_op(seq0, op0)

            start_time = time.time()
            sp.seq_op(seq1, op1)
            end_time = time.time()
            splay_time_all.append((end_time - start_time) * 1000)


            sp = BST()
            sp.seq_op(seq0, op0)

            start_time = time.time()
            sp.seq_op(seq1, op1)
            end_time = time.time()
            bst_time_all.append((end_time - start_time) * 1000)

        splay_avg=sum(splay_time_all) / epoch
        bst_avg = sum(bst_time_all) / epoch


        splay_times.append(splay_avg)  # convert to ms
        bst_times.append(bst_avg)


    # Plotting the results
    plt.plot(input_sizes, splay_times, marker='o', color='b', label='Splay Tree')  # 'b'代表蓝色
    plt.plot(input_sizes, bst_times, marker='x', color='r', label='Binary Search Tree')  # 'r'代表红色

    # plt.xscale('log', base=2)  # 将x轴改成对数坐标
    plt.xlabel('Input Size')
    plt.ylabel('Operation Times')
    plt.title('Splay Tree Operation Steps vs Input Size')
    plt.grid(True)
    plt.show()