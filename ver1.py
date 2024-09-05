import pygame
from random import choice, randrange

pygame.init()

WIDTH, HEIGHT = 1920, 1080
RES = (WIDTH, HEIGHT)

FONT_SIZE = 35

alpha_value = randrange(30,40,5)
chars = [
    # Nguyên âm
    "ア", "イ", "ウ", "エ", "オ",
    
    # Hàng K
    "カ", "キ", "ク", "ケ", "コ",
    
    # Hàng S
    "サ", "シ", "ス", "セ", "ソ",
    
    # Hàng T
    "タ", "チ", "ツ", "テ", "ト",
    
    # Hàng N
    "ナ", "ニ", "ヌ", "ネ", "ノ",
    
    # Hàng H
    "ハ", "ヒ", "フ", "ヘ", "ホ",
    
    # Hàng M
    "マ", "ミ", "ム", "メ", "モ",
    
    # Hàng Y
    "ヤ", "ユ", "ヨ",
    
    # Hàng R
    "ラ", "リ", "ル", "レ", "ロ",
    
    # Hàng W
    "ワ", "ヲ", "ン", '1', '2', '3','4','5','6','7','8','9','0','.',',','+','-','*','|',':'
]

font = pygame.font.Font('ms mincho.ttf', FONT_SIZE)
font2 = pygame.font.Font('ms mincho.ttf', FONT_SIZE - FONT_SIZE // 6)
font3 = pygame.font.Font('ms mincho.ttf', FONT_SIZE - FONT_SIZE // 3)
green_chars = [font.render(char, True, (randrange(0,100), 255, randrange(0,100))) for char in chars]
green_chars2 = [font.render(char, True, (40, randrange(100,175), 40)) for char in chars]
green_chars3 = [font.render(char, True, (40, randrange(50,100), 40)) for char in chars]

screen = pygame.display.set_mode(RES)
display_surface = pygame.Surface(RES)
display_surface.set_alpha(alpha_value)


clock = pygame.time.Clock()

class Symbol:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.speed = 40
        self.value =  choice(green_chars)

    def draw(self):
        self.value = choice(green_chars)
        self.y = self.y + self.speed if self.y < HEIGHT else -FONT_SIZE * randrange(1,10)
        screen.blit(self.value, (self.x, self.y))
    
    def draw2(self):
        self.value2 = choice(green_chars2)
        self.y = self.y + self.speed if self.y < HEIGHT else -FONT_SIZE * randrange(1,10)
        screen.blit(self.value2, (self.x, self.y))

    def draw3(self):
        self.value3 = choice(green_chars3)
        self.y = self.y + self.speed if self.y < HEIGHT else -FONT_SIZE * randrange(1,10)
        screen.blit(self.value3, (self.x, self.y))

symbols = [Symbol(x, randrange(-HEIGHT, 0)) for x in range(0, WIDTH, FONT_SIZE*3)]
symbols2 = [Symbol(x, randrange(-HEIGHT, 0)) for x in range(FONT_SIZE, WIDTH, FONT_SIZE*3)]
symbols3 = [Symbol(x, randrange(-HEIGHT, 0)) for x in range(FONT_SIZE*2, WIDTH, FONT_SIZE*3)]

paused = False
run = True
while run:
    
    screen.blit(display_surface, (0,0))
    display_surface.fill(pygame.Color('black'))

    [symbol.draw() for symbol in symbols]
    [symbol2.draw() for symbol2 in symbols2]
    [symbol3.draw() for symbol3 in symbols3]


    pygame.time.delay(140)
    if not paused:
        pygame.display.update()

    clock.tick(60)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False
            if event.key == pygame.K_SPACE:
                paused = not paused