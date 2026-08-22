import glfw
from OpenGL.GL import *
from OpenGL.GLU import *

# 0. Variáveis globais
left = -1.0
right = 1.0
bottom = -1.0
top = 1.0

# 1. Inicializa a GLFW
if not glfw.init():
    raise RuntimeError("Falha ao inicializar GLFW")

# 2. Cria a janela
window = glfw.create_window(800, 800, "Aula 01 - OpenGL - Janela, Linha e Triângulo", None, None)
if not window:
    glfw.terminate()
    raise RuntimeError("Falha ao criar janela")

# 2. Call back para o teclado
def key_callback(window,key,scancode,action, mode):
    global left, right, bottom, top
    if action == glfw.PRESS:
        if key == glfw.KEY_EQUAL:
            #Este erro corrigimos durante a aula: ESTAVA keyEQUAL e o certo é KEY_EQUAL
            left=-4
            right=4
            bottom=-4
            top=4
            #Aqui estava o outro erro: todas as variáveis estavam iguais à -4
            #resultando em um RECORTE NULO (Xmin=-4 e Xmax=-4)
            #Assim   Xmin = -4 e Xmax = 4 -> intervalo = 8
            #        Ymin = -4 e Xmax = 4 -> intervalo = 8

 
# 3. Configurações básicas
glfw.make_context_current(window)
glfw.set_key_callback(window,key_callback) #ativa o ouvinte de evento para o teclado
glClearColor(0, 0, 0, 1)  # cor de fundo preta

# 4. Desenha
    # Comandos de desenho
def desenha():
    glColor(1, 1, 1)  # cor branca
    glBegin(GL_QUADS) # inicia o desenho do quadrado
    glVertex(-0.8,0.8)
    glVertex(0.8,0.8)
    glVertex(0.8,-0.8)
    glVertex(-0.8,-0.8)
    glEnd()

    glColor(1,0,0) #cor vermelha
    glBegin(GL_TRIANGLES) #inicia o desenho do triângulo
    glVertex(-0.6,-0.6)
    glVertex(0.0,0.6)
    glVertex(0.6,-0.6)
    glEnd()

    glColor(0,1,0)
    glBegin(GL_POLYGON)
    glVertex(-0.6,-0.6)
    glVertex(-0.6,-0.4)
    glVertex(0.0,-0.2)
    glVertex(0.6,-0.4)
    glVertex(0.6,-0.6)
    glEnd()

    glColor(0,0,1) #cor prteta
    glBegin(GL_LINES)# inicia o desenho da linha
    glVertex(-1, 1)
    glVertex(1, -1)
    glEnd()

# 4. Loop principal
while not glfw.window_should_close(window):
    
    glClear(GL_COLOR_BUFFER_BIT)
    desenha()

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(left,right,bottom,top)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glViewport(0,0,800,800)
    
    glfw.swap_buffers(window)  # exibe o frame
    glfw.poll_events()         # processa eventos

# 5. Finaliza
glfw.terminate()

# Correçao do professor