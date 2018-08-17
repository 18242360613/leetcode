#!usr/bin/env python
# encoding:utf-8

import random
import sys

def random_matrix_genetor(vex_num=10):
    '''
    随机图顶点矩阵生成器
    输入：顶点个数，即矩阵维数
    '''
    data_matrix = []
    for i in range(vex_num):
        one_list = []
        for j in range(vex_num):
            one_list.append(random.randint(1, 100))
        data_matrix.append(one_list)
    return data_matrix


def floyd(data_matrix):
    '''
    输入：原数据矩阵，即：一个二维数组
    输出：顶点间距离
    '''
    dist_matrix = []
    path_matrix = []
    vex_num = len(data_matrix)
    for h in range(vex_num):
        one_list = ['N'] * vex_num
        path_matrix.append(one_list)
        dist_matrix.append(one_list)
    for i in range(vex_num):
        for j in range(vex_num):
            dist_matrix = data_matrix
            path_matrix[i][j] = j
    for k in range(vex_num):
        for i in range(vex_num):
            for j in range(vex_num):
                temp = dist_matrix[i][k] + dist_matrix[k][j]
                if dist_matrix[i][j] > temp:
                    dist_matrix[i][j] = temp
                    path_matrix[i][j] = path_matrix[i][k]
    return dist_matrix, path_matrix


def main_test_func(vex_num=10):
    '''
    主测试函数
    '''
    data_matrix = random_matrix_genetor(vex_num)
    dist_matrix, path_matrix = floyd(data_matrix)
    for i in range(vex_num):
        print(dist_matrix[i])


if __name__ == '__main__':
    main_test_func(10)

