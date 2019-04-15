from feature import CellGroup
from observer import Observer
import random

num = 2

# 建立观察者、特征与目标
observer = Observer()
feature = CellGroup('Feature', 2 * num, observer, False)
target = CellGroup('Target', num, observer, True)

# 训练迭代
for epoch in range(0, 1):

    # 随机生产特征
    a = 1
    b = 1
    # a = random.randint(0, num - 1)
    # b = random.randint(0, num - 1)
    c = a + b

    # 特征二进制化
    a = bin(a).split('0b')[1]
    b = bin(b).split('0b')[1]
    c = bin(c).split('0b')[1]

    # 特征字符串话
    oa = str(a)
    ob = str(b)
    oc = str(c)

    # 清理观察者内存 开始观察特征激活情况
    observer.clean()
    # 映射激活特征与目标
    for i in range(1, max(max(len(oa), len(ob)), len(oc)) + 1):

        # 激活特征
        # 添加特征与目标
        if len(oa) + 1 > i:
            a = oa[-i]
            observer.push_feature(feature.get_at(int(a)))
        else:
            a = None
        if len(ob) + 1 > i:
            b = ob[-i]
            observer.push_feature(feature.get_at(num + int(b)))
        else:
            b = None
        if len(oc) + 1 > i:
            c = oc[-i]
            observer.push_target(target.get_at(int(c)))
        else:
            c = None

        # 激活特征 交由观察者观察
        observer.activation()

        # 打印特征
        print("a+b=c:", a, b, c)
        #
        # # 开始构建
        # observer.build()

        print("---------loop_" + str(i) + "-----------")
    print("========================\n")
