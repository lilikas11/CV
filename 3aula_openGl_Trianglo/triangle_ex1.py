import pygame as pg
from pygame.locals import *
from OpenGL.GL import *

pg.init()
windowsize = (700, 400)
pg.display.set_mode(windowsize, DOUBLEBUF | OPENGL | RESIZABLE)

glClearColor(0.0, 1.0, 0.8, 1.0)
glClear(GL_COLOR_BUFFER_BIT)

while True:
    pg.display.flip()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()