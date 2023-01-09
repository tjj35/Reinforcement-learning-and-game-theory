#coding: gbk
import numpy as np
from Square import Square

maze_structure = []
jjWorld = np.zeros((8,8), Square)
iteration = 1

def mazeStructure():
    global maze_structure
                        #  0  1  2  3  4  5  6  7
    maze_structure.append([0, 0, 0, 0, 0, 0, 0, 0])#0
    maze_structure.append([0, 1, 1, 1, 1, 1, 1, 0])#1
    maze_structure.append([2, 1, 0, 0, 1, 0, 1, 0])#2
    maze_structure.append([0, 1, 1, 0, 0, 1, 1, 0])#3
    maze_structure.append([0, 0, 1, 1, 0, 1, 0, 0])#4
    maze_structure.append([0, 1, 0, 1, 0, 1, 1, 0])#5
    maze_structure.append([0, 1, 1, 1, 1, 0, 1, 1])#6
    maze_structure.append([0, 0, 0, 0, 0, 0, 0, 0])#7

def printMaze(isGraphic):
    global maze_structure
    if isGraphic:
        for i in range(8):
            for j in range(8):
                if maze_structure[i][j] == 0:
                    print("# ", end='')
                elif maze_structure[i][j] == 1:
                    print("  ", end='')
                elif maze_structure[i][j] == 2:
                    print("@ ", end='')
            print("")
    else:
        for i in range(8):
            print(maze_structure[i])

def movementOptions():
    global jjWorld, maze_structure

    for i in range(0, 8):
        for j in range(0, 8):
            right = left = up = down = 0
            try:
                if maze_structure[i][j+1]:
                    right = 1
            except IndexError:
                pass
            try:
                if maze_structure[i][j-1]:
                    left = 1
            except IndexError:
                pass
            try:
                if maze_structure[i-1][j]:
                    up = 1
            except IndexError:
                pass
            try:
                if maze_structure[i+1][j]:
                    down = 1
            except IndexError:
                pass
            if maze_structure != 0:
                jjWorld[i][j] = Square(up, down, right, left) #定义jjWorld每一块的状态

    jjWorld[6][7].reward = 11 #定义出口的reward