
import random

container = [i+1 for i in range(50)]
def lottery_game():
    
    lucky_balls = []
    new_ball = random.choice(container)
    for i in range(10):
        while new_ball in lucky_balls:
            new_ball = random.choice(container)
        lucky_balls.append(new_ball)

    lucky_balls.sort()
    return lucky_balls
    

if __name__ == "__main__":
    lucky_balls = lottery_game()
    print(lucky_balls)
