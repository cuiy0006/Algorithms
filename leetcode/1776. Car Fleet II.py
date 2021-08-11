class Solution:
    def getCollisionTimes(self, cars: List[List[int]]) -> List[float]:
        lives = [-1] * len(cars)
        stack = [len(cars) - 1]
        
        
        for i in range(len(cars) - 2, -1, -1):
            car = cars[i]
            while len(stack) != 0:
                car_ahead = cars[stack[-1]]
                if car[1] <= car_ahead[1]:
                    stack.pop()
                else:
                    break
            
            while len(stack) != 0:
                car_ahead = cars[stack[-1]]
                time_to_collide = (car_ahead[0] - car[0]) / (car[1] - car_ahead[1])
                if time_to_collide <= lives[stack[-1]] or lives[stack[-1]] == -1:
                    lives[i] = time_to_collide
                    break
                stack.pop()
            
            stack.append(i)
            
        return lives
