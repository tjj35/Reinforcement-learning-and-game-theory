#coding: gbk
import numpy as np
from MazeCreation import maze_structure, jjWorld, printMaze
from time import sleep


policy = [] #选择方向的决策
numOfIteration = 0 #迭代次数
actions = ['U', 'D', 'R', 'L'] #up, down, right, left
current_i = 2 #current row
current_j = 0 #current column
last_i = 0 #last row
last_j = 0 #last column

def returnVal(i, j, action): #返回下一块的value
    hasChanged = 0
    try:
        if action == 'R' and maze_structure[i][j+1]:
            j = j + 1
            hasChanged = 1
    except IndexError:                                                                                                                                                                                                                                                                                                                                                                                                                                
        pass
    try:
        if action == 'L' and maze_structure[i][j-1]:
            j = j - 1
            hasChanged = 1
    except IndexError:
        pass
    try:
        if action == 'D' and maze_structure[i+1][j]:
            i = i + 1
            hasChanged = 1
    except IndexError:
        pass
    try:
        if action == 'U' and maze_structure[i-1][j]:
            i = i - 1
            hasChanged = 1
    except IndexError:
        pass
    if hasChanged:
        return jjWorld[i][j].val
    else:
        return False

def policyPrint(): #print the policy
    global policy, numOfIteration
    for i in range(8):
        for j in range(8):
            if maze_structure[i][j]!=0:
                if i == 6 and j == 7:
                    print('$', end=' ') #出口
                else:
                    if policy[i][j] == 'U':
                        print('↑', end=' ')
                    if policy[i][j] == 'D':
                        print('↓', end=' ')
                    if policy[i][j] == 'R':
                        print('→', end=' ')
                    if policy[i][j] == 'L':
                        print('←', end=' ')
            else:
                print('#',end = ' ') #障碍物
        print('')
    print("迭代次数为：", numOfIteration)

def returnActions(i,j): #返回可用动作
    global actions
    availableActions = []
    if jjWorld[i][j].U == 1:
        availableActions.append('U')
    if jjWorld[i][j].D == 1:
        availableActions.append('D')
    if jjWorld[i][j].R == 1:
        availableActions.append('R')
    if jjWorld[i][j].L == 1:
        availableActions.append('L')
    return availableActions

#价值迭代算法
def valueIteration(gamma): 
    global policy, numOfIteration, actions
    policy = np.zeros((8,8), str)

    #初始化policy
    for i in range(8):
        for j in range(8):
            if maze_structure[i][j] != 0:
                policy[i][j] = 'D'
            else:
                policy[i][j] = '# '

    jjWorldHasChanged = True #开始第一次迭代

    while jjWorldHasChanged:
        jjWorldHasChanged = False
        for i in range(8):
            for j in range(8):
                if maze_structure[i][j] != 0: #当该块不是障碍物
                    values = []
                    availableActions = returnActions(i,j) #确定可用动作
                    for act in availableActions:
                        val = returnVal(i,j,act)
                        values.append(jjWorld[i][j].reward + gamma * val)

                    if values: #当values不为空
                        val = max(values)
                        if val != jjWorld[i][j].val: #当val值改变
                            jjWorldHasChanged = True #说明jjworld已经发生改变
                            jjWorld[i][j].val = val #更新val

        numOfIteration = numOfIteration + 1 #迭代次数+1

    for i in range(8):
        for j in range(8):
            if maze_structure != 0: 
                availableActions = returnActions(i,j)
                try:
                    maxVal = returnVal(i,j,availableActions[0])
                except IndexError:
                    pass
                for act in availableActions:
                    if returnVal(i,j,act) >= maxVal:
                        maxVal = returnVal(i,j,act)
                        policy[i][j] = act

            else:
                policy[i][j] == '# '
    return policy

def move(action):  # Move the smiley from current location to the next square by the given action
    global current_i, current_j, last_i, last_j
    last_i = current_i
    last_j = current_j
    if action == 'D':
        current_i = current_i + 1
    if action == 'U':
        current_i = current_i - 1
    if action == 'L':
        current_j = current_j - 1
    if action == 'R':
        current_j = current_j + 1

    maze_structure[current_i][current_j] = 2  # The current location of the smiley
    maze_structure[last_i][last_j] = 1  # The last location the smiley was in

def screenClear():  # Clearing the screen - to have an animation/to make the run look better
    print('\n' * 1)  # prints 30 line breaks

def solvingMaze():
    global current_i, current_j
    while maze_structure[6][7] != 2:
        move(policy[current_i][current_j])
        sleep(0.8)
        screenClear()
        printMaze(1)
    screenClear()
    print("Congratulations! You have get out the maze!")


