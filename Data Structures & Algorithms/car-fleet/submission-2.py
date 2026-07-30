class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        car_fleet=0
        maximum_time=0
        se=[]
        for r in range(len(position)):
            time=(target-position[r])/speed[r]
            se.append([position[r],time])
        se.sort(reverse=True)
        print(se)
        for i in range(len(se)):
            if se[i][1]>maximum_time:
                print(se[i][1],maximum_time,car_fleet)
                car_fleet+=1
                maximum_time=se[i][1]
        return car_fleet
            
        