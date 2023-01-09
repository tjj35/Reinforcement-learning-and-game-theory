#coding: gbk
import MazeCreation
from MazeCreation import mazeStructure, printMaze, movementOptions
from valueIteration import valueIteration, policyPrint, solvingMaze
from time import sleep


# Main

def main():
    mazeStructure()  # 创建迷宫
    printMaze(1)  # 打印迷宫
    sleep(2)  
    print('~~~~~~~~~~~~~~~')
    sleep(2) 
    print('~~~~~~~~~~~~~~~')

    movementOptions()  # 初始化状态空间
    valueIteration(0.71)  # 进行价值迭代

    sleep(2)  
    print('~~~~~~~~~~~~~~~')
    policyPrint()  
    sleep(2)  
    print('~~~~~~~~~~~~~~~')

    solvingMaze()  # 完成迷宫问题


if __name__ == '__main__':
    main()

