import copy 
from itertools import repeat
import random


class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        self.keys = list(kwargs.keys())
        self.values = list(kwargs.values())
        for key, val in zip(self.keys, self.values):
            self.contents.extend(repeat(key, val))
        print(self.contents)

    
    def draw(self, number):
        draw_list=[]
        if number > len(self.contents):
            return self.contents
        for i in range(number):
            
            removing_index = self.contents.pop(random.randrange(len(self.contents)))
            draw_list.append(removing_index)
        return draw_list
        

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    counter = 0
    
    for i in range(num_experiments):
        expected_balls_copy = copy.deepcopy(expected_balls)
        hat_copy = copy.deepcopy(hat)
        
        balls_draw=hat_copy.draw(num_balls_drawn)
        
        for ball in balls_draw:
            if ball in expected_balls_copy:
                
                expected_balls_copy[ball] -= 1
        if all(i <=0 for i in expected_balls_copy.values()):
            counter += 1
        
    result = counter / num_experiments
    return result    
