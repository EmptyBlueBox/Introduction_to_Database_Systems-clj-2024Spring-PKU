import numpy as np

def nmf_train(V, components, iternum, e):
    '''
    非负矩阵分解函数
    :param V:  原始矩阵
    :param components:  要提取多少个特征
    :param iternum: 迭代次数
    :param e: 误差阈值
    :return:
    '''
    m, n = V.shape 
    # 随机初始化两个矩阵
    W = np.random.random((m, components)) 
    H = np.random.random((components, n)) 


    for iter in range(iternum):
        V_pre = np.dot(W, H)
        E = V - V_pre

        err = np.sum(E * E)
        print(err)
        if err < e:
            break
        # 对照更新公式
        a = np.dot(W.T, V)
        b = np.dot(W.T, np.dot(W, H))
        H[b != 0] = (H * a / b)[b != 0]

        c = np.dot(V, H.T)
        d = np.dot(W, np.dot(H, H.T))

        W[d != 0] = (W * c / d)[d != 0]
    return W, H

def gen_cooccurrence_matrix(vocab_size):
    '''
    生成随机共现矩阵
    :param vocab_size: 词汇表大小(这里是人物的数量)
    '''
    co_occurrence_matrix = np.random.poisson(10, (vocab_size, vocab_size))  # 使用泊松分布生成基础数据
    co_occurrence_matrix = (co_occurrence_matrix + co_occurrence_matrix.T) // 2
    # 增加对角线上的值以表示更频繁的自我共现
    np.fill_diagonal(co_occurrence_matrix, np.random.poisson(30, vocab_size))
    return co_occurrence_matrix


if __name__ == '__main__':
    np.random.seed(42)
    vocab_size = 23
    co_occurrence_matrix = gen_cooccurrence_matrix(vocab_size)
    print('共现矩阵：')
    print(co_occurrence_matrix)
    components = 50
    print('Start training')
    W, H = nmf_train(co_occurrence_matrix, components, 1000, 1e-4)
    print('End training')
    print('W:')
    print(W)
