class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        plantedFlowers: int = 0

        if(len(flowerbed) == 1 and flowerbed[0] == 0):
            return 1 >= n

        if(len(flowerbed) == 2 and flowerbed[0] == 0 and flowerbed[1] == 0):
            return 1 >= n

        if(flowerbed[0] == 0 and flowerbed[1] == 0):
            plantedFlowers += 1
            flowerbed[0] = 1

        for i in range(0, len(flowerbed)-2):
            if flowerbed[i] == 0 and flowerbed[i+1] == 0 and flowerbed[i+2] == 0:
                flowerbed[i+1] = 1
                plantedFlowers += 1
    
        if(flowerbed[-1] == 0 and flowerbed[-2] == 0):
            plantedFlowers += 1
            flowerbed[-1] = 1

        return plantedFlowers >= n

[1,0,1,0,1,0,1]
