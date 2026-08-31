import glfw
from OpenGL.GL import *
import numpy as np

def desenha():
    glClearColor(1.0, 1.0, 1.0, 1.0)
    glClear(GL_COLOR_BUFFER_BIT)
    glLineWidth(2.0)

    # linha preta
    glColor3f(0.0, 0.0, 0.0)
    glBegin(GL_LINES)
    glVertex2f(-1.0, -0.4)
    glVertex2f(1.0, -0.4)
    glEnd()

    # forma vermelha
    verticesVermelhos = np.array([
        [-0.3, -0.4], [-0.3,  0.0], [ 0.3,  0.0], [ 0.3, -0.4],
        [ 0.2, -0.4], [ 0.2, -0.3], [-0.2, -0.3], [-0.2, -0.4]
    ], dtype=np.float32)
    
    glColor3f(1.0, 0.0, 0.0)
    glBegin(GL_LINE_LOOP)
    for vertice in verticesVermelhos:
        glVertex2f(vertice[0], vertice[1])
    glEnd()

    # retangulo verde
    verticesVerdes = np.array([
        [-0.08, -0.2], [-0.08,  0.3], [ 0.08,  0.3], [ 0.08, -0.2]
    ], dtype=np.float32)

    glColor3f(0.0, 1.0, 0.0)
    glBegin(GL_LINE_LOOP)
    for vertice in verticesVerdes:
        glVertex2f(vertice[0], vertice[1])
    glEnd()

    # retangulo azul
    verticesAzuis = np.array([
        [-0.08,  0.2], [-0.08,  0.6], [ 0.08,  0.6], [ 0.08,  0.2]
    ], dtype=np.float32)

    glColor3f(0.0, 0.0, 1.0)
    glBegin(GL_LINE_LOOP)
    for vertice in verticesAzuis:
        glVertex2f(vertice[0], vertice[1])
    glEnd()

def app():
    if not glfw.init():
        return

    window = glfw.create_window(500, 500, "teste", None, None)
    if not window:
        glfw.terminate()
        return

    glfw.make_context_current(window)

    while not glfw.window_should_close(window):
        desenha()
        glfw.swap_buffers(window)
        glfw.poll_events()

    glfw.terminate()

app()