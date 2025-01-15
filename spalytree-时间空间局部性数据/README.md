# SplayTree 与 普通BST search/insert/delete操作的复杂度分析
- 对于无时间/空间局部性的复杂度验证--是否为logn
- 对于时间局部性数据的复杂度实验
- 对于空间局部性数据的复杂度实验


# 文件组成
- BST.py 包括BST的实现代码
- SplayTree.py 包括SplayTree的实现代码
- genTask.py 生成随机操作数以及操作序列，可选是否加入时间局部性、空间局部性
- view.py 树结构可视乎（但是没用到）
- time_complexity.py 最开始尝试验证时间复杂度是否为logn的代码
- **visualize_Experiment.ipynb** 主要的整个实验组成，包括所有实验的复杂度的结果图。请老师看这个文件