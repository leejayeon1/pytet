from matrix import *
import random


def draw_matrix(m):
    array = m.get_array()
    for y in range(m.get_dy()):
        for x in range(m.get_dx()):
            if array[y][x] == 0:
                print("□", end='')
            elif array[y][x] == 1:
                print("■", end='')
            else:
                print("XX", end='')
        print()


###
### initialize variables
###     
Blk1 = [ [ [ 0 , 0 , 1 ,0 ] , [ 0 , 0 , 1 , 0 ] , [ 0 , 0 , 1 , 0 ] , [ 0 , 0 , 1 , 0 ] ], 
        [ [ 1 , 1 , 1 , 1 ] , [ 0 , 0 , 0 , 0 ] , [ 0 , 0 , 0 , 0 ] , [ 0 , 0 , 0 , 0 ] ],
        [ [ 0 , 0 , 1 , 0] , [ 0 , 0 , 1 , 0 ] , [ 0 , 0 , 1 , 0 ] , [ 0 , 0 , 1 , 0 ] ],        
        [ [ 1 , 1 , 1 , 1 ] , [ 0 , 0 , 0 , 0 ] , [ 0 , 0 , 0 , 0 ] , [ 0 , 0 , 0 , 0 ] ] ]
Blk2 = [ [ [ 1 , 0 , 0 , 0 ] , [ 1 , 1 , 1 , 0 ] , [ 0 , 0 , 0 , 0 ] , [ 0 , 0 , 0 , 0 ] ],
         [ [ 1 , 1 , 0 , 0 ] , [ 1 , 0 , 0 , 0 ] , [ 1 , 0 , 0 , 0 ] , [ 0 , 0 , 0 , 0 ] ],
         [ [ 1 , 1 , 1 , 0 ] , [ 0 , 0 , 1 , 0 ] , [ 0 , 0 , 0 , 0 ] , [ 0 , 0 , 0 , 0 ] ],
         [ [ 0 , 0 , 1 , 0 ] , [ 0 , 0 , 1 , 0 ] , [ 0 , 1 , 1 , 0 ] , [ 0 , 0 , 0 , 0 ] ] ]
Blk3 = [ [ [ 0 , 1 , 0 , 0 ] , [ 0 , 1 , 1 , 0 ] , [ 0 , 0 , 1 , 0 ] , [ 0 , 0 , 0 , 0 ] ],
         [ [ 0 , 0 , 1 , 1 ] , [ 0 , 1 , 1 , 0 ] , [ 0 , 0 , 0 , 0 ] , [ 0 , 0 , 0 , 0 ] ],
         [ [ 0 , 1 , 0 , 0 ] , [ 0 , 1 , 1 , 0 ] , [ 0 , 0 , 1 , 0 ] , [ 0 , 0 , 0 , 0 ] ],
         [ [ 0 , 0 , 1 , 1 ] , [ 0 , 1 , 1 , 0 ] , [ 0 , 0 , 0 , 0 ] , [ 0 , 0 , 0 , 0 ] ] ]
Blk4 = [ [ [ 0 , 0 , 1 , 0 ] , [ 0 , 1 , 1 , 1 ] , [ 0 , 0 , 0 , 0 ] , [ 0 , 0 , 0 , 0 ] ],
         [ [ 0 , 0 , 1 , 0 ] , [ 0 , 0 , 1 , 1 ] , [ 0 , 0 , 1 , 0 ] , [ 0 , 0 , 0 , 0 ] ],
         [ [ 0 , 1 , 1 , 1 ] , [ 0 , 0 , 1 , 0 ] , [ 0 , 0 , 0 , 0 ] , [ 0 , 0 , 0 , 0 ] ],
        [ [ 0 , 0 , 1 , 0 ] , [ 0 , 1 , 1 , 0 ] , [ 0 , 0 , 1 , 0 ] , [ 0 , 0 , 0 , 0 ] ] ]
Blk5 = [ [ [ 0 , 0 , 1 , 0 ] , [ 0 , 1 , 1 , 0 ] , [ 0 , 1 , 0 , 0 ] , [ 0 , 0 , 0 , 0 ] ],
         [ [ 0 , 1 , 1 , 0 ] , [ 0 , 0 , 1 , 1 ] , [ 0 , 0 , 0 , 0 ] , [ 0 , 0 , 0 , 0 ] ],
         [ [ 0 , 0 , 1 , 0 ] , [ 0 , 1 , 1 , 0 ] , [ 0 , 1 , 0 , 0 ] , [ 0 , 0 , 0 , 0 ] ],
         [ [ 0 , 1 , 1 , 0 ] , [ 0 , 0 , 1 , 1 ] , [ 0 , 0 , 0 , 0 ] , [ 0 , 0 , 0 , 0 ] ] ]
Blk6 = [ [ [ 0 , 0 , 0 , 1 ] , [ 0 , 1 , 1 , 1 ] , [ 0 , 0 , 0 , 0 ] , [ 0 , 0 , 0 , 0 ] ],
         [ [ 0 , 0 , 1 , 0 ] , [ 0 , 0 , 1 , 0 ] , [ 0 , 0 , 1 , 1 ] , [ 0 , 0 , 0 , 0 ] ],
         [ [ 0 , 1 , 1 , 1 ] , [ 0 , 1 , 0 , 0 ] , [ 0 , 0 , 0 , 0 ] , [ 0 , 0 , 0 , 0 ] ],
         [ [ 0 , 0 , 1 , 1 ] , [ 0 , 0 , 0 , 1 ] , [ 0 , 0 , 0 , 1 ] , [ 0 , 0 , 0 , 0 ] ] ]
Blk7 = [ [ [ 0 , 1 , 1 , 0 ] , [ 0 , 1 , 1 , 0 ] , [ 0 , 0 , 0 , 0 ] , [ 0 , 0 , 0 , 0 ] ],
         [ [ 0 , 1 , 1 , 0 ] , [ 0 , 1 , 1 , 0 ] , [ 0 , 0 , 0 , 0 ] , [ 0 , 0 , 0 , 0 ] ],
         [ [ 0 , 1 , 1 , 0 ] , [ 0 , 1 , 1 , 0 ] , [ 0 , 0 , 0 , 0 ] , [ 0 , 0 , 0 , 0 ] ],
         [ [ 0 , 1 , 1 , 0 ] , [ 0 , 1 , 1 , 0 ] , [ 0 , 0 , 0 , 0 ] , [ 0 , 0 , 0 , 0 ] ] ]
### integer variables: must always be integer!
iScreenDy = 15
iScreenDx = 10
iScreenDw = 4
top = 0
left = iScreenDw + iScreenDx//2 - 2
h=random.randrange(0,7)
i=0
newBlockNeeded = False

arrayScreen = [
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ] ]

arrayBlk=[Blk1, Blk2, Blk3, Blk4, Blk5, Blk6, Blk7]

###
### prepare the initial screen output
###  
iScreen = Matrix(arrayScreen)
oScreen = Matrix(iScreen)
currBlk = Matrix(arrayBlk[h][i])
tempBlk = iScreen.clip(top, left, top+currBlk.get_dy(), left+currBlk.get_dx())
tempBlk = tempBlk + currBlk
oScreen.paste(tempBlk, top, left)
draw_matrix(oScreen); print()

###
### execute the loop
###

while True:
    key = input('Enter a key from [ q (quit), a (left), d (right), s (down), w (rotate), \' \' (drop) ] : ')
    if key == 'q':
        print('Game terminated...')
        break
    elif key == 'a': # move left
        left -= 1
    elif key == 'd': # move right
        left += 1
    elif key == 's': # move down
        top += 1
    elif key == 'w': # rotate the block clockwise
        i=(i+1)%4
        currBlk = Matrix(arrayBlk[h][i])
    elif key == ' ': # drop the block
        while not tempBlk.anyGreaterThan(1):
            top+=1
            tempBlk = iScreen.clip(top, left, top+currBlk.get_dy(), left+currBlk.get_dx())
            tempBlk = tempBlk + currBlk
    else:
        print('Wrong key!!!')
        continue

    tempBlk = iScreen.clip(top, left, top+currBlk.get_dy(), left+currBlk.get_dx())
    tempBlk = tempBlk + currBlk
    if tempBlk.anyGreaterThan(1):
        if key == 'a': # undo: move right
            left += 1
        elif key == 'd': # undo: move left
            left -= 1
        elif key == 's': # undo: move up
            top -= 1
            newBlockNeeded = True
        elif key == 'w': # undo: rotate the block counter-clockwise
            i=(i-1)%4
            currBlk=Matrix(arrayBlk[h][i])
        elif key == ' ': # undo: move up
            if tempBlk.anyGreaterThan(1):
                top-=1
                newBlockNeeded = True

        tempBlk = iScreen.clip(top, left, top+currBlk.get_dy(), left+currBlk.get_dx())
        tempBlk = tempBlk + currBlk

    oScreen = Matrix(iScreen)
    oScreen.paste(tempBlk, top, left)
    draw_matrix(oScreen); print()

    if newBlockNeeded:
        iScreen = Matrix(oScreen)
        top = 0
        left = iScreenDw + iScreenDx//2 - 2
        newBlockNeeded = False
        h = random.randrange(0,7)
        i = 0
        currBlk = Matrix(arrayBlk[h][i])
        tempBlk = iScreen.clip(top, left, top+currBlk.get_dy(), left+currBlk.get_dx())
        tempBlk = tempBlk + currBlk
        if tempBlk.anyGreaterThan(1):
            print('Game Over!!!')
            break
        
        oScreen = Matrix(iScreen)
        oScreen.paste(tempBlk, top, left)
        draw_matrix(oScreen); print()
        
###
### end of the loop
###
