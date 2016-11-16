# Computer Programming 1
# Unit 11 - Graphics
#
# A scene that uses loops to make stars and make a picket fence.


# Imports
import pygame, random, math

# Initialize game engine
pygame.init()

# Window
SIZE = (800, 600)
TITLE = "Nifty Dog and Night"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)

# Timer	
clock = pygame.time.Clock()
refresh_rate = 30

# Colors
BLACK = (0,0,0)
RAIN = (11, 37, 119)
GREEN = (0, 175, 0)
WHITE = (255, 255, 255)
SKY = (75, 200, 255)
YELLOW = (255, 255, 175)
CLOUD = (255, 255, 255)
NIGHTSKY = (5, 16, 43)
NIGHTCLOUD = (69, 72, 81)
NIGHTGRASS = (4, 58, 2)
NIGHTFENCE = (136, 139, 145)
NIGHTSUN = (5, 16, 43)
DAYCLOUD = (255, 255, 255)
DAYSKY = (75, 200, 255)
DAYFENCE = (255, 255, 255)
DAYGRASS = (0, 175, 0)
DAYSUN = (255, 255, 175)
DOGBROWN = (71, 27, 5)

def draw_cloud(x, y):
    pygame.draw.ellipse(screen, CLOUD, [x, y + 20, 40 , 40])
    pygame.draw.ellipse(screen, CLOUD, [x + 60, y + 20, 40 , 40])
    pygame.draw.ellipse(screen, CLOUD, [x + 20, y + 10, 25, 25])
    pygame.draw.ellipse(screen, CLOUD, [x + 35, y, 50, 50])
    pygame.draw.rect(screen, CLOUD, [x + 20, y + 20, 60, 40])

bark = False
bark_timer = 15
def draw_dog(x, y):
    #Tail
    pygame.draw.rect(screen, DOGBROWN, [x, y, 8, 16])
    pygame.draw.polygon(screen, DOGBROWN, [[x, y+16], [x+8, y+16],
                                           [x+8, y+24]])
    pygame.draw.rect(screen, DOGBROWN, [x+8, y+16, 16, 8])
    
    #Body
    pygame.draw.rect(screen, DOGBROWN, [x+24, y+16, 64, 24])

    #Legs
    pygame.draw.rect(screen, DOGBROWN, [x+24, y+32, 8, 24])
    pygame.draw.rect(screen, DOGBROWN, [x+33, y+32, 8, 22])
    pygame.draw.rect(screen, DOGBROWN, [x+80, y+32, 8, 24])
    pygame.draw.rect(screen, DOGBROWN, [x+78, y+32, 8, 22])

    #Head
    pygame.draw.ellipse(screen, DOGBROWN, [x+80, y+8, 25, 20])
    pygame.draw.ellipse(screen, WHITE, [x+88, y+12, 4, 4])
    
    #Mouth
    if not bark:
        pygame.draw.rect(screen, DOGBROWN, [x+100, y+15, 10, 6])
    if bark:
        pygame.draw.rect(screen, DOGBROWN, [x+100, y+15, 10, 4])
        pygame.draw.polygon(screen, DOGBROWN, [[x+100, y+19], [x+96, y+23],
                                        [x+104, y+27], [x+108, y+23]])
        #Bark lines
        pygame.draw.line(screen, BLACK, [x+115, y+15], [x+120, y+11], 3)
        pygame.draw.line(screen, BLACK, [x+ 115, y+19], [x+122, y+19], 3)
        pygame.draw.line(screen, BLACK, [x+115, y+23], [x+120, y+27], 3)
def draw_rain(x, y):
    pygame.draw.ellipse(screen, RAIN, [x, y, 2, 3])


#Night time cloud number increase variables
x_increase = random.randint(0, 200)
y_increase = random.randint(-50, 50)   
    
#Make rain
rain = []
front_rain = []
for i in range(600):
    x = random.randint(0, 1000)
    y = random.randint(-500,0)
    rain.append([x, y])
for i in range(400):
    x = random.randint(0,1000)
    y = random.randint(-300, 0)
    front_rain.append([x, y])


''' make clouds '''
clouds = []
for i in range(20):
    x = random.randrange(-100, 1600)
    y = random.randrange(0,200)
    clouds.append([x, y])

daytime = True 
# Game loop
done = False

while not done:
    bark_timer += 1
    if bark_timer == 10:
        bark = False
    # Event processing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                daytime = not daytime
            elif event.key == pygame.K_b:
                    bark = True
                    bark_timer = 0
                

    #Daytime / Nighttime colors
    if daytime:
        SKY = DAYSKY
        SUN = DAYSUN
        CLOUD = DAYCLOUD
        GRASS = DAYGRASS
        FENCE = DAYFENCE
    if not daytime:
        SKY = NIGHTSKY
        SUN = NIGHTSUN
        CLOUD = NIGHTCLOUD
        GRASS = NIGHTGRASS
        FENCE = NIGHTFENCE
        
        
    

    # Game logic
    ''' move clouds '''
    for c in clouds:
        c[0] -= 1
        if not daytime:
            if c[0] < -300:
                c[0] = random.randrange(800, 1600)
                c[1] = random.randrange(0, 200)
        elif c[0] < -100:
            c[0] = random.randrange(800, 1600)
            c[1] = random.randrange(0, 200)
    for r in rain:
        r[1] += 3
        if r[1] > 0:
            r[0] -= math.sqrt(r[1])/10

        ground_limit = random.randint(400, 700)
        if r[1] > ground_limit:
            r[1] = random.randint(-400,0)
            r[0] = random.randint(0, 1000)
    for f in front_rain:
        f[1]+= 5
        if f[1] > 0:
            f[0] -= math.sqrt(f[1])/25

        ground_limit = random.randint(400, 700)
        if f[1] > ground_limit:
            f[1] = random.randint(-300, 0)
            f[0] = random.randint(0,1000)
  
    # Drawing code
    ''' sky '''
    screen.fill(SKY)

    ''' sun '''
    pygame.draw.ellipse(screen, SUN, [575, 75, 100, 100])
    
    ''' grass '''
    pygame.draw.rect(screen, GRASS, [0, 400, 800, 200])
    draw_dog(100, 450)

    ''' rain ''' 
    for r in rain:
        if not daytime:
            draw_rain(r[0], r[1])

    ''' clouds '''
    if not daytime:
        for c in clouds:
            draw_cloud(c[0]+x_increase, c[1]+y_increase)
    for c in clouds:
        draw_cloud(c[0], c[1])

    '''front rain'''
    for f in front_rain:
        if not daytime:
            draw_rain(f[0], f[1])

    ''' fence '''
    y = 380
    for x in range(5, 800, 30):
        pygame.draw.polygon(screen, FENCE, [[x+5, y], [x+10, y+5],
                                            [x+10, y+40], [x, y+40],
                                            [x, y+5]])
    pygame.draw.line(screen, FENCE, [0, 390], [800, 390], 5)
    pygame.draw.line(screen, FENCE, [0, 410], [800, 410], 5)

    
    # Update screen
    pygame.display.flip()
    clock.tick(refresh_rate)

# Close window on quit
pygame.quit()
