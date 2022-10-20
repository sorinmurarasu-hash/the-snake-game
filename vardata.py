import  pygame

resolution_X        = 640
resolution_Y        = 480
header_height       = 50

blue                = ( 0, 0, 255 )
red                 = ( 255, 0, 0 )
black               = ( 0, 0, 0 )
lightgray           = ( 83, 83, 83 )
white               = ( 255, 255 ,255 )
header_color        = ( 100, 100, 100 )
fonts = {}

sizex, sizey              = 20, 20
speed                     = 8

clock = pygame.time.Clock()

pygame.init()
dis = pygame.display.set_mode(( resolution_X, resolution_Y + header_height ))
 