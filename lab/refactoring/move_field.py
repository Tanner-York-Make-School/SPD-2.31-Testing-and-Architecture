"""
By Kamran Bigdely Nov. 2020
Refactored by Tanner York
Move Field (attribute)
"""

class Gun:
    def __init__(self, name, total_bullet_capacity):
        self.name = name
        self.total_bullet_capacity = total_bullet_capacity
        self.num_bullets = total_bullet_capacity

    def shoot(self):
        if self.num_bullets > 0:
            self.num_bullets -= 1
            print('shoot')
        else:
            print('click')

    def reload(self):
        self.num_bullets = self.total_bullet_capacity
        print('reload')

class Player:
    def __init__(self, guns):        
        self.guns = guns

    def fire_once(self):
        for gun in self.guns:
            if gun.num_bullets > 0:
                gun.shoot()
                break
            
def game_loop():
    while (True):
        player.fire_once()
        break


if __name__ == '__main__':
    guns = [Gun('pistol', 10), Gun('rifle', 10)]
    player = Player(guns)
    game_loop()
