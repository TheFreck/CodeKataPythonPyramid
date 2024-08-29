def pyramid(stones):
    stones.sort(reverse = True)
    print(stones)
    threeStones = None
    twoStones = None
    oneStone = None
    outString = ""
    pyramidValue = 0
    for stone in stones:
        count = stones.count(stone)
        if stone != threeStones and stone != twoStones and stone != oneStone and threeStones == None and count >= 3:
            threeStones = stone
        elif stone != threeStones and stone != twoStones and stone != oneStone and twoStones == None and count >= 2:
            twoStones = stone
        elif stone != threeStones and stone != twoStones and stone != oneStone and oneStone == None:
            oneStone = stone
    print(f'{threeStones}{threeStones}{threeStones}|{twoStones}{twoStones}|{oneStone}')
    if threeStones != None and twoStones != None and oneStone != None:
        print(3*threeStones+2*twoStones+oneStone)
        return 3*threeStones+2*twoStones+oneStone
    else:
        return None
    

# print(pyramid([3,1,3,2,2,3]))
# print("***")
# print(pyramid([3,1,1,2,2,1]))
# print("***")
# print(pyramid([2,7,3,7,7,3]))
# print("***")
# print(pyramid([1,1,7,3,7,7,3]))
# print("***")
# print(pyramid([1,3,2,4,5,6,1]))
# print("***")
print(pyramid([5, 3, 5, 3, 0, 0, -1, 0, 0, 3, 3, 3]))
print("***")
