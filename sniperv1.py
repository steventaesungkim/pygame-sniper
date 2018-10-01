import pygame

KEY_UP = 273
KEY_DOWN = 274
KEY_LEFT = 276
KEY_RIGHT = 275

class Ball:
    def __init__(self, x_axis, y_axis):
        self.x = x_axis
        self.y = y_axis
        self.speed_x = 0
        self.speed_y = 0
        self.radius = 5
        self.radius2 = 30

    def update(self):
        self.x += self.speed_x
        self.y += self.speed_y

    def render(self, screen):
        pygame.draw.circle(screen,(250, 250, 250), (self.x, self.y), self.radius2)
        pygame.draw.circle(screen, (0, 0, 0), (self.x, self.y), self.radius)

def main():
    width = 500
    height = 500
    white_color = (0, 0, 0)#black_color = (0, 0, 0)
    pygame.init()
    screen = pygame.display.set_mode((width, height))

    ball = Ball(250, 250)

    stop_game = False
    while not stop_game:
        for event in pygame.event.get():
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
                    ball.speed_x = 0
                elif event.key == KEY_RIGHT:
                    ball.speed_x = 0
            if event.type == pygame.QUIT:
                stop_game = True
    
    
        ball.update()

        screen.fill(white_color)#screen.fill(black_color) #save until the end

        ball.render(screen)
        # font = pygame.font.Font(None, 25)
        # text = font.render("", True, (0, 0, 0))
        # screen.blit(text, (80, 230))

        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()
