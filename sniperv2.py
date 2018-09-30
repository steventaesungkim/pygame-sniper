## getting the target to appear and randomize

import pygame
import random
import time

KEY_UP = 273
KEY_DOWN = 274
KEY_LEFT = 276
KEY_RIGHT = 275

class Ball():
    def __init__(self, x_axis, y_axis):
        self.x = x_axis
        self.y = y_axis
        self.position = [x_axis, y_axis]
        self.speed_x = 0
        self.speed_y = 0
        self.radius = 3

    def movement(self):
        self.x += self.speed_x
        self.y += self.speed_y
    
    def render(self, screen):
        pygame.draw.circle(screen, (0, 0, 0,), (self.x, self.y), self.radius)

    def collide(self, target_pos):
        if self.position == target_pos:
            return 1
        else:
            return 0
    
    def wall_parameters(self):
        if self.x > 490 or self.x < 0:
            return 1
        elif self.y > 490 or self.y < 0:
            return 1

class Target_Spawner():
    def __init__(self):
        self.position = [(random.randrange (1, 50) * 10), (random.randrange (1, 50) * 10)]
        self.isTargetOnScreen = True
    def spawnTarget(self):
        if self.isTargetOnScreen == False:
            self.position = [(random.randrange (1, 50) * 10), (random.randrange (1, 50) * 10)]
            self.isTargetOnScreen = True
        return self.position

    def set_Target(self, scr):
        self.isTargetOnScreen = scr


screen = pygame.display.set_mode((500,500))
# pygame.display.set_caption("")    
fps = pygame.time.Clock()

score = 0

ball = Ball(250, 250)
target = Target_Spawner()


def gameOver():
    pygame.quit()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOver()
        if event.type == pygame.KEYDOWN:
            if event.key == KEY_DOWN:
                ball.speed_y = 5
            elif event.key == KEY_UP:
                ball.speed_y = -5
            elif event.key == KEY_LEFT:
                ball.speed_x = -5
            elif event.key == KEY_RIGHT:
                ball.speed_x = 5
        if event.type == pygame.KEYUP:
            if event.key == KEY_DOWN:
                ball.speed_y = 0
            elif event.key == KEY_UP:
                ball.speed_y = 0
            elif event.key == KEY_LEFT:
                    all.speed_x = 0
            elif event.key == KEY_RIGHT:
                ball.speed_x = 0
        if event.type == pygame.QUIT:
            stop_game = True

    target_pos = Target_Spawner.spawnTarget()
    if (Ball.move(target_pos) == 1):
        score += 1
        Target_Spawner.set_Target(False)

    screen.fill(pygame.color(250, 250, 250))
    for features in Target.render():
        pygame.draw.circle(screen, (225, 0, 0,), (target_pos.x, target_pos.y), self.radius)
    if (ball.collide() == 1):
        gameOver()
    pygame.display.set_caption("Don't hit the walls.. Score: " +srt(score))
    pygame.display.flip()
    fps.tick(24)












# class Ball:
#     def __init__(self, x_axis, y_axis):
#         self.x = x_axis
#         self.y = y_axis
#         self.speed_x = 0
#         self.speed_y = 0
#         self.radius = 2

#     def update(self):
#         self.x += self.speed_x
#         self.y += self.speed_y

#     def render(self, screen):
#         pygame.draw.circle(screen, (0, 0, 0), (self.x, self.y), self.radius)

#     # def checkparameter(self, target):
#     #     if self.x > 790 or self.x < 0:
#     #         return 1
#     #     if self.y > 790 or self.y < 0:
#     #         return 1
    
# class Target():
#     def __init__(self):
#         # self.x = x_axis
#         # self.y = y_axis
#         self.radius = 2
#         self.postion = [(random.randrange(10,790) * 2), (random.randrange(10, 790) * 2)]
#         self.isTargetOnScreen = True

#     def spawnTarget(self):
#         if self.isTargetOnScreen == False:
#             self.postion = [(random.randrange(10,790) * 2), (random.randrange(10, 790) * 2)]
#             self.isTargetOnScreen == True
#         return self.postion
#     def setTartgetOnScreen(self,gg):
#         self.isTargetOnScreen = gg
    
    




# def main():
#     pygame.init()
#     width = 800
#     height = 800
#     white_color = (250, 250, 250)#black_color = (0, 0, 0)
#     screen = pygame.display.set_mode((width, height))
#     fps = pygame.time.Clock()

#     score = 0

#     ball = Ball(400, 400)
#     target = Target()


#     stop_game = False
#     while not stop_game:
#         for event in pygame.event.get():
#             if event.type == pygame.KEYDOWN:
#                 if event.key == KEY_DOWN:
#                     ball.speed_y = 5
#                 elif event.key == KEY_UP:
#                     ball.speed_y = -5
#                 elif event.key == KEY_LEFT:
#                     ball.speed_x = -5
#                 elif event.key == KEY_RIGHT:
#                     ball.speed_x = 5
#             if event.type == pygame.KEYUP:
#                 if event.key == KEY_DOWN:
#                     ball.speed_y = 0
#                 elif event.key == KEY_UP:
#                     ball.speed_y = 0
#                 elif event.key == KEY_LEFT:
#                     ball.speed_x = 0
#                 elif event.key == KEY_RIGHT:
#                     ball.speed_x = 0
#             if event.type == pygame.QUIT:
#                 stop_game = True
    
#         targetPos = Target.spawnTarget()
#         if(ball.move(targetPos) == 1):
#         ball.update()
#         # target.update()

#         screen.fill(white_color)#screen.fill(black_color) #save until the end

#         ball.render(screen)
#         font = pygame.font.Font(None, 25)
#         text = font.render("", True, (0, 0, 0))
#         screen.blit(text, (80, 230))

#         pygame.display.update()

#     pygame.quit()

# if __name__ == "__main__":
#     main()
