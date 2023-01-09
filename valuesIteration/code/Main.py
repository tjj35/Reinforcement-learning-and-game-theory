#coding: gbk
import MazeCreation
from MazeCreation import mazeStructure, printMaze, movementOptions
from valueIteration import valueIteration, policyPrint, solvingMaze
from time import sleep


# Main

def main():
    mazeStructure()  # �����Թ�
    printMaze(1)  # ��ӡ�Թ�
    sleep(2)  
    print('~~~~~~~~~~~~~~~')
    sleep(2) 
    print('~~~~~~~~~~~~~~~')

    movementOptions()  # ��ʼ��״̬�ռ�
    valueIteration(0.71)  # ���м�ֵ����

    sleep(2)  
    print('~~~~~~~~~~~~~~~')
    policyPrint()  
    sleep(2)  
    print('~~~~~~~~~~~~~~~')

    solvingMaze()  # ����Թ�����


if __name__ == '__main__':
    main()

