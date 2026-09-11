import glfw
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np
import math
import sys

pausado = False
angulo_pas = 0.0
pos_x_carro = -15.0
velocidade_carro = 5.0
raio_roda = 0.5
angulo_roda = 0.0

distancia_cam = 25.0
ang_cam_h = 45.0
ang_cam_v = 30.0
ultimo_x, ultimo_y = 0.0, 0.0
mouse_pressionado = False
ultimo_tempo = 0.0

def callback_teclado(janela, tecla, codigo_scancode, acao, modificadores):
    global pausado
    if tecla == glfw.KEY_P and acao == glfw.PRESS:
        pausado = not pausado
    elif tecla == glfw.KEY_ESCAPE and acao == glfw.PRESS:
        glfw.set_window_should_close(janela, True)

def callback_botao_mouse(janela, botao, acao, modificadores):
    global mouse_pressionado
    if botao == glfw.MOUSE_BUTTON_LEFT:
        if acao == glfw.PRESS:
            mouse_pressionado = True
        elif acao == glfw.RELEASE:
            mouse_pressionado = False

def callback_posicao_cursor(janela, pos_x, pos_y):
    global ultimo_x, ultimo_y, ang_cam_h, ang_cam_v, mouse_pressionado
    if mouse_pressionado:
        dx = pos_x - ultimo_x
        dy = pos_y - ultimo_y
        ang_cam_h += dx * 0.3
        ang_cam_v += dy * 0.3
        ang_cam_v = max(-89.0, min(89.0, ang_cam_v))
    ultimo_x = pos_x
    ultimo_y = pos_y

def callback_rolagem(janela, deslocamento_x, deslocamento_y):
    global distancia_cam
    distancia_cam -= deslocamento_y * 2.0
    distancia_cam = max(5.0, min(100.0, distancia_cam))

def desenhar_cubo():
    vertices = np.array([
        [-0.5, -0.5,  0.5], [ 0.5, -0.5,  0.5], [ 0.5,  0.5,  0.5], [-0.5,  0.5,  0.5],
        [-0.5, -0.5, -0.5], [-0.5,  0.5, -0.5], [ 0.5,  0.5, -0.5], [ 0.5, -0.5, -0.5],
        [-0.5,  0.5, -0.5], [-0.5,  0.5,  0.5], [ 0.5,  0.5,  0.5], [ 0.5,  0.5, -0.5],
        [-0.5, -0.5, -0.5], [ 0.5, -0.5, -0.5], [ 0.5, -0.5,  0.5], [-0.5, -0.5,  0.5],
        [ 0.5, -0.5, -0.5], [ 0.5,  0.5, -0.5], [ 0.5,  0.5,  0.5], [ 0.5, -0.5,  0.5],
        [-0.5, -0.5, -0.5], [-0.5, -0.5,  0.5], [-0.5,  0.5,  0.5], [-0.5,  0.5, -0.5]
    ], dtype=np.float32)

    normais = np.array([
        [ 0,  0,  1], [ 0,  0,  1], [ 0,  0,  1], [ 0,  0,  1],
        [ 0,  0, -1], [ 0,  0, -1], [ 0,  0, -1], [ 0,  0, -1],
        [ 0,  1,  0], [ 0,  1,  0], [ 0,  1,  0], [ 0,  1,  0],
        [ 0, -1,  0], [ 0, -1,  0], [ 0, -1,  0], [ 0, -1,  0],
        [ 1,  0,  0], [ 1,  0,  0], [ 1,  0,  0], [ 1,  0,  0],
        [-1,  0,  0], [-1,  0,  0], [-1,  0,  0], [-1,  0,  0]
    ], dtype=np.float32)

    glEnableClientState(GL_VERTEX_ARRAY)
    glEnableClientState(GL_NORMAL_ARRAY)
    glVertexPointer(3, GL_FLOAT, 0, vertices)
    glNormalPointer(GL_FLOAT, 0, normais)
    glDrawArrays(GL_QUADS, 0, 24)
    glDisableClientState(GL_NORMAL_ARRAY)
    glDisableClientState(GL_VERTEX_ARRAY)

def desenhar_solo():
    glPushMatrix()
    glColor3f(0.2, 0.6, 0.2)
    glTranslatef(0.0, -0.5, 0.0)
    glScalef(50.0, 1.0, 50.0)
    desenhar_cubo()
    glPopMatrix()

def desenhar_moinho():
    glPushMatrix()
    glColor3f(0.6, 0.4, 0.2)
    glTranslatef(0.0, 3.0, -5.0)
    glScalef(2.0, 6.0, 2.0)
    desenhar_cubo()
    glPopMatrix()

    glPushMatrix()
    glTranslatef(0.0, 5.0, -3.8)
    glRotatef(angulo_pas, 0.0, 0.0, 1.0)

    glColor3f(0.8, 0.8, 0.8)
    for i in range(4):
        glPushMatrix()
        glRotatef(i * 90.0, 0.0, 0.0, 1.0)
        glTranslatef(0.0, 2.0, 0.0)
        glScalef(0.4, 4.0, 0.1)
        desenhar_cubo()
        glPopMatrix()
    glPopMatrix()

def desenhar_carro():
    glPushMatrix()
    glTranslatef(pos_x_carro, 1.0, 5.0)

    glColor3f(0.8, 0.1, 0.1)
    glPushMatrix()
    glScalef(4.0, 1.0, 2.0)
    desenhar_cubo()
    glPopMatrix()
    
    glColor3f(0.9, 0.2, 0.2)
    glPushMatrix()
    glTranslatef(-0.5, 1.0, 0.0)
    glScalef(2.0, 1.0, 1.8)
    desenhar_cubo()
    glPopMatrix()

    glColor3f(0.1, 0.1, 0.1)
    posicoes_rodas = [
        (-1.2, -0.5,  1.1), ( 1.2, -0.5,  1.1),
        (-1.2, -0.5, -1.1), ( 1.2, -0.5, -1.1)
    ]
    for pos in posicoes_rodas:
        glPushMatrix()
        glTranslatef(*pos)
        glRotatef(-angulo_roda, 0.0, 0.0, 1.0)
        glScalef(raio_roda * 2, raio_roda * 2, 0.4)
        desenhar_cubo()
        glPopMatrix()

    glPopMatrix()

def main():
    global angulo_pas, pos_x_carro, angulo_roda, ultimo_tempo

    if not glfw.init():
        sys.exit()

    janela = glfw.create_window(800, 600, "Cena 3D - Moinho e Carro", None, None)
    if not janela:
        glfw.terminate()
        sys.exit()

    glfw.make_context_current(janela)
    glfw.set_key_callback(janela, callback_teclado)
    glfw.set_mouse_button_callback(janela, callback_botao_mouse)
    glfw.set_cursor_pos_callback(janela, callback_posicao_cursor)
    glfw.set_scroll_callback(janela, callback_rolagem)

    glEnable(GL_DEPTH_TEST)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_COLOR_MATERIAL)
    
    glLightfv(GL_LIGHT0, GL_POSITION, [10.0, 20.0, 10.0, 0.0])
    glLightfv(GL_LIGHT0, GL_DIFFUSE, [1.0, 1.0, 1.0, 1.0])
    glLightfv(GL_LIGHT0, GL_AMBIENT, [0.3, 0.3, 0.3, 1.0])

    ultimo_tempo = glfw.get_time()

    while not glfw.window_should_close(janela):
        tempo_atual = glfw.get_time()
        dt = tempo_atual - ultimo_tempo
        ultimo_tempo = tempo_atual

        if not pausado:
            angulo_pas += 100.0 * dt
            pos_x_carro += velocidade_carro * dt
            
            if pos_x_carro > 20.0:
                pos_x_carro = -20.0
            
            angulo_roda = (pos_x_carro / raio_roda) * (180.0 / math.pi)

        glClearColor(0.5, 0.7, 1.0, 1.0)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        largura, altura = glfw.get_framebuffer_size(janela)
        if altura == 0: altura = 1
        gluPerspective(45.0, largura / altura, 0.1, 100.0)

        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        
        cam_x = distancia_cam * math.cos(math.radians(ang_cam_v)) * math.sin(math.radians(ang_cam_h))
        cam_y = distancia_cam * math.sin(math.radians(ang_cam_v))
        cam_z = distancia_cam * math.cos(math.radians(ang_cam_v)) * math.cos(math.radians(ang_cam_h))
        gluLookAt(cam_x, cam_y, cam_z, 0.0, 2.0, 0.0, 0.0, 1.0, 0.0)

        desenhar_solo()
        desenhar_moinho()
        desenhar_carro()

        glfw.swap_buffers(janela)
        glfw.poll_events()

    glfw.terminate()


main()