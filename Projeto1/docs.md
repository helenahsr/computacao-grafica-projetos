# Projeto 1 - Anotações

## OpenGL

OpenGL é uma API (Application Programming Interface) para renderização de gráficos 2D e 3D. É uma biblioteca de funções que permite criar e manipular gráficos em tempo real.

## GLFW

GLFW é uma biblioteca de funções que permite criar e manipular janelas em tempo real.

## OpenGL vs GLFW

- OpenGL = Desenha gráficos

- GLFW = Cria e gerencia janelas

## Primitivas

- GL_QUADS = Cria um quadrado

- GL_TRIANGLES = Cria um triangulo

- GL_POINTS = Cria um ponto

- GL_POLYGON = Cria um poligono (une os pontos com uma linha)

- GL_LINE_LOOP = Cria uma linha conectando todos os pontos e fechando o loop

- GL_LINE_STRIP = Cria uma linha conectando todos os pontos

- GL_QUADS_STRIP = Cria um strip de quadrados

- GL_TRIANGLE_STRIP = Cria um strip de triangulos

- GL_TRIANGLE_FAN = Cria um triangulo fan

## Cores

As cores são representadas por tuplas de 3 valores (R, G, B), onde cada valor varia de 0 a 1. 

- Vermelho = (1, 0, 0)

- Verde = (0, 1, 0)

- Azul = (0, 0, 1)

- Branco = (1, 1, 1)

- Preto = (0, 0, 0)

## Funções

- glfw.init() = Inicializa o GLFW

- glfw.create_window() = Cria uma janela

- glfw.make_context_current() = Torna a janela atual

- glfw.window_should_close() = Verifica se a janela deve ser fechada

- glfw.swap_buffers() = Troca os buffers

- glfw.poll_events() = Processa os eventos

- glfw.terminate() = Encerra o GLFW

- glClearColor() = Define a cor de fundo

- glClear() = Limpa o buffer

- glBegin() = Inicia o desenho

- glEnd() = Encerra o desenho

- glVertex2f() = Define um vértice (2D)

- glVertex3f() = Define um vértice (3D)