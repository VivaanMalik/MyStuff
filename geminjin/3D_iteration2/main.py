import pygame
import moderngl
import sys

from model import *

#       #00425A      #1F8A70      #BFDB38      #FC7300

class Graphics():
    def __init__(self, winres=(1366, 768), fps=60):
        pygame.init()
        self.WindowResolution = winres
        self.FramesPerSecond = fps
        pygame.display.gl_set_attribute(pygame.GL_CONTEXT_MAJOR_VERSION, 3)
        pygame.display.gl_set_attribute(pygame.GL_CONTEXT_MINOR_VERSION, 3)
        pygame.display.gl_set_attribute(pygame.GL_CONTEXT_PROFILE_MASK, pygame.GL_CONTEXT_PROFILE_CORE)

        pygame.display.set_mode(winres, flags=pygame.OPENGL | pygame.DOUBLEBUF)
        self.Context = moderngl.create_context()
        self.Clock = pygame.time.Clock()
        self.Scene = Triangle(self)

    def Quit(self):
        self.Scene.Destroy()
        pygame.quit()
        sys.exit()
    
    def Event(self):
        for evt in pygame.event.get():
            if evt.type==pygame.QUIT or (evt.type == pygame.KEYDOWN and evt.key == pygame.K_ESCAPE):
                self.Quit()
    
    def Render(self):
        self.Context.clear(0, 0.259, 0.353)
        self.Scene.Render()
        pygame.display.flip()
    
    def Run(self):
        while True:
            self.Event()
            self.Render()
            self.Clock.tick(self.FramesPerSecond)
    
if __name__ == "__main__":
    app = Graphics()
    app.Run()