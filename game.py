import sys, pygame
pygame.init()

size = width, height = 320, 240
gray = 128, 128, 128

screen = pygame.display.set_mode(size)

# NKS Rules

nks_base = (
    (0,0,0),
    (0,0,1),
    (0,1,0),
    (0,1,1),
    (1,0,0),
    (1,0,1),
    (1,1,0),
    (1,1,1)
)

nks_rules = { 
    '30':   '00011110',
    '54':   '00110110',
    '60':   '00111100',
    '62':   '00111110',
    '90':   '01011010',
    '94':   '01011110',
    '102':  '01100110',
    '110':  '01101110',
    '122':  '01111010',
    '126':  '01111110',
    '150':  '10010110',
    '158':  '10011110',
    '182':  '10110110',
    '188':  '10111100',
    '190':  '10111110',
    '220':  '11011100',
    '222':  '11011110',
    '250':  '11111010'
}

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    # Game logic

    screen.fill(black)
    for bit, coord in zip(bits, coords):
        screen.blit(bit, coord)
    pygame.display.flip()