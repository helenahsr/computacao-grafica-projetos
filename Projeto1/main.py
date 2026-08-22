import glfw
from OpenGL.GL import *

if not glfw.init():
    raise RuntimeError("Falha ao inicializar GLFW")

def geraQuadrado(x1, y1, x2, y2, x3, y3, x4, y4):
    glColor3f(1.0, 1.0, 1.0)
    glBegin(GL_QUADS)
    glVertex2f(x1, y1)
    glVertex2f(x2, y2)
    glVertex2f(x3, y3)
    glVertex2f(x4, y4)
    glEnd()

def geraTriangulo(x1, y1, x2, y2, x3, y3):
    glColor3f(1.0, 0.0, 0.0)
    glBegin(GL_TRIANGLES)
    glVertex2f(x1, y1)
    glVertex2f(x2, y2)
    glVertex2f(x3, y3)
    glEnd()

def geraPoligono(x1, y1, x2, y2, x3, y3, x4, y4, x5, y5):
    glColor3f(0.0, 1.0, 0.0)
    glBegin(GL_POLYGON)
    glVertex2f(x1, y1)
    glVertex2f(x2, y2)
    glVertex2f(x3, y3)
    glVertex2f(x4, y4)
    glVertex2f(x5, y5)
    glEnd()

window = glfw.create_window(800, 800, "Exercício 1", None, None)

if not window:
    glfw.terminate()
    raise RuntimeError("Falha ao criar janela")

glfw.make_context_current(window)
glClearColor(0, 0, 0, 1)

while not glfw.window_should_close(window):
    glClear(GL_COLOR_BUFFER_BIT)
    geraQuadrado(-0.8, 0.8, 0.8, 0.8, 0.8, -0.8, -0.8, -0.8)
    geraTriangulo(-0.3, -0.6, 0.3, -0.6, 0.0, 0.6)
    geraPoligono(-0.6, -0.6, 0.6, -0.6, 0.6, -0.4, 0.0, -0.2, -0.6, -0.4)
    glfw.swap_buffers(window)
    glfw.poll_events()

glfw.terminate()