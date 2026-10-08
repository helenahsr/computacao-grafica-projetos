import glfw
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np

# Ângulos de rotação para cada articulação em graus
angulo_A = 0.0  # Giro na base (Eixo Y)
angulo_B = 0.0  # Giro na articulação B (Eixo X)
angulo_C = 0.0  # Giro na articulação C (Eixo X)

def desenhar_cubo():
    """Desenha um cubo unitário (de -0.5 a 0.5 em todos os eixos) com linhas de contorno."""
    vertices = [
        [-0.5, -0.5, -0.5], [0.5, -0.5, -0.5], [0.5,  0.5, -0.5], [-0.5,  0.5, -0.5],
        [-0.5, -0.5,  0.5], [0.5, -0.5,  0.5], [0.5,  0.5,  0.5], [-0.5,  0.5,  0.5]
    ]
    
    faces = [
        (0, 1, 2, 3), (4, 5, 6, 7),
        (0, 1, 5, 4), (2, 3, 7, 6),
        (0, 3, 7, 4), (1, 2, 6, 5)
    ]
    
    # Desenho das faces sólidas
    glBegin(GL_QUADS)
    for face in faces:
        for vertice in face:
            glVertex3fv(vertices[vertice])
    glEnd()

    # Desenho das arestas para realce visual
    glColor3f(0.0, 0.0, 0.0)
    glLineWidth(1.5)
    for face in faces:
        glBegin(GL_LINE_LOOP)
        for vertice in face:
            glVertex3fv(vertices[vertice])
        glEnd()

def desenhar_braco_robotico():
    """Desenha a estrutura do braço robótico aplicando a hierarquia de transformações."""
    glPushMatrix()
    
    # --- BASE INFERIOR ---
    glColor3f(0.8, 0.8, 0.8)
    glPushMatrix()
    glTranslatef(0.0, -0.2, 0.0)
    glScalef(2.0, 0.4, 1.2)
    desenhar_cubo()
    glPopMatrix()
    
    # --- ARTICULAÇÃO A (Giro na Base) ---
    glRotatef(angulo_A, 0.0, 1.0, 0.0)
    
    # Primeiro Segmento (Haste A - B)
    glColor3f(0.2, 0.6, 0.9)
    glPushMatrix()
    glTranslatef(0.0, 1.0, 0.0)
    glScalef(0.5, 2.0, 0.5)
    desenhar_cubo()
    glPopMatrix()
    
    # --- ARTICULAÇÃO B (Ombro/Cotovelo) ---
    glTranslatef(0.0, 2.0, 0.0)  # Mover para o topo da haste A
    glRotatef(angulo_B, 1.0, 0.0, 0.0)
    
    # Segundo Segmento (Haste B - C)
    glColor3f(0.9, 0.5, 0.2)
    glPushMatrix()
    glTranslatef(0.0, 1.0, 0.0)
    glScalef(0.4, 2.0, 0.4)
    desenhar_cubo()
    glPopMatrix()
    
    # --- ARTICULAÇÃO C (Garra / Extremidade) ---
    glTranslatef(0.0, 2.0, 0.0)  # Mover para o topo da haste B
    glRotatef(angulo_C, 1.0, 0.0, 0.0)
    
    # Terceiro Segmento (Extremidade C)
    glColor3f(0.3, 0.8, 0.4)
    glPushMatrix()
    glTranslatef(0.0, 0.6, 0.0)
    glScalef(0.3, 1.2, 0.3)
    desenhar_cubo()
    glPopMatrix()
    
    glPopMatrix()

def tratar_teclado(janela, tecla, codigo_scancode, acao, modificadores):
    """Trata a entrada do teclado para movimentação dos eixos."""
    global angulo_A, angulo_B, angulo_C
    passo = 3.0  # Ângulo de rotação por passo
    
    if acao == glfw.PRESS or acao == glfw.REPEAT:
        # Articulação A: Esquerda e Direita[cite: 1]
        if tecla == glfw.KEY_LEFT:
            angulo_A -= passo
        elif tecla == glfw.KEY_RIGHT:
            angulo_A += passo
            
        # Articulação B: Cima e Baixo[cite: 1]
        elif tecla == glfw.KEY_UP:
            angulo_B -= passo
        elif tecla == glfw.KEY_DOWN:
            angulo_B += passo
            
        # Articulação C: Page Up e Page Down[cite: 1]
        elif tecla == glfw.KEY_PAGE_UP:
            angulo_C -= passo
        elif tecla == glfw.KEY_PAGE_DOWN:
            angulo_C += passo

def principal():
    if not glfw.init():
        return

    # Criação da janela GLFW
    janela = glfw.create_window(800, 600, "Exercício 07 - Braço Articulado 3D", None, None)
    if not janela:
        glfw.terminate()
        return

    glfw.make_context_current(janela)
    glfw.set_key_callback(janela, tratar_teclado)

    # Configurações de renderização do OpenGL
    glEnable(GL_DEPTH_TEST)
    glClearColor(0.95, 0.95, 0.95, 1.0)

    # Configuração da projeção 3D
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45.0, 800.0 / 600.0, 0.1, 100.0)

    # Loop principal
    while not glfw.window_should_close(janela):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        
        # Ajuste da câmera (Visão em perspectiva para observar os 3 eixos)
        gluLookAt(6.0, 5.0, 8.0,   # Posição da Câmera
                  0.0, 2.0, 0.0,   # Ponto para onde a câmera olha
                  0.0, 1.0, 0.0)   # Vetor Up
        
        desenhar_braco_robotico()

        glfw.swap_buffers(janela)
        glfw.poll_events()

    glfw.terminate()

principal()