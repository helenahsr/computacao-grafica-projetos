import glfw
from OpenGL.GL import *
from OpenGL.GLU import *

angulo_articulacao_a = 0.0
angulo_articulacao_b = 0.0
angulo_articulacao_c = 0.0

vertices_cubo = (
    (0.5, -0.5, -0.5), (0.5, 0.5, -0.5),
    (-0.5, 0.5, -0.5), (-0.5, -0.5, -0.5),
    (0.5, -0.5, 0.5), (0.5, 0.5, 0.5),
    (-0.5, -0.5, 0.5), (-0.5, 0.5, 0.5)
)

faces_cubo = (
    (0, 1, 2, 3), (3, 2, 7, 6), (6, 7, 5, 4),
    (4, 5, 1, 0), (1, 5, 7, 2), (4, 0, 3, 6)
)

def processar_teclado(janela, tecla, codigo_escaneamento, acao, modificadores):
    if acao == glfw.PRESS:
        print(f"Tecla detectada: {tecla}")
    global angulo_articulacao_a, angulo_articulacao_b, angulo_articulacao_c
    if acao == glfw.PRESS or acao == glfw.REPEAT:
        if tecla == glfw.KEY_LEFT:
            angulo_articulacao_a -= 5.0
        elif tecla == glfw.KEY_RIGHT:
            angulo_articulacao_a += 5.0
        elif tecla == glfw.KEY_UP:
            angulo_articulacao_b -= 5.0
        elif tecla == glfw.KEY_DOWN:
            angulo_articulacao_b += 5.0
        elif tecla == glfw.KEY_PAGE_UP:
            angulo_articulacao_c -= 5.0
        elif tecla == glfw.KEY_PAGE_DOWN:
            angulo_articulacao_c += 5.0

def construir_bloco(largura, altura, profundidade):
    glPushMatrix()
    glScalef(largura, altura, profundidade)
    
    glColor3f(1.0, 1.0, 1.0)
    glBegin(GL_QUADS)
    for face in faces_cubo:
        for vertice in face:
            glVertex3fv(vertices_cubo[vertice])
    glEnd()
    
    glColor3f(0.0, 0.0, 0.0)
    for face in faces_cubo:
        glBegin(GL_LINE_LOOP)
        for vertice in face:
            glVertex3fv(vertices_cubo[vertice])
        glEnd()
        
    glPopMatrix()

def renderizar_modelo():
    construir_bloco(4.0, 1.0, 4.0)
    
    glRotatef(angulo_articulacao_a, 0.0, 1.0, 0.0)
    
    glTranslatef(0.0, 0.5, 0.0)
    glTranslatef(0.0, 1.5, 0.0)
    construir_bloco(1.0, 3.0, 1.0)
    
    glTranslatef(0.0, 1.5, 0.0)
    glRotatef(angulo_articulacao_b, 0.0, 0.0, 1.0)
    
    glTranslatef(0.0, 1.5, 0.0)
    construir_bloco(0.8, 3.0, 0.8)
    
    glTranslatef(0.0, 1.5, 0.0)
    glRotatef(angulo_articulacao_c, 0.0, 0.0, 1.0)
    
    glTranslatef(0.0, 1.5, 0.0)
    construir_bloco(0.6, 3.0, 0.6)

glfw.init()
janela_aplicacao = glfw.create_window(800, 600, "Exercicio 07 - Braco Robotico", None, None)
glfw.make_context_current(janela_aplicacao)
glfw.set_key_callback(janela_aplicacao, processar_teclado)

glEnable(GL_DEPTH_TEST)
glClearColor(0.8, 0.8, 0.8, 1.0)

while not glfw.window_should_close(janela_aplicacao):
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45.0, 800.0/600.0, 0.1, 100.0)
    
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(10.0, 8.0, 12.0, 0.0, 4.0, 0.0, 0.0, 1.0, 0.0)
    
    renderizar_modelo()
    
    glfw.swap_buffers(janela_aplicacao)
    glfw.poll_events()

glfw.terminate()