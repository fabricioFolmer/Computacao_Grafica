import glfw
from OpenGL.GL import *
import numpy as np
import time

def eixos():
    glLineWidth(5)
    glBegin(GL_LINES)
    glColor3f(1.0, 1, 1)
    glVertex3f(-1.0, 0.0, 0.0)
    glVertex3f(1.0, 0.0, 0.0)

    glColor3f(1, 1.0, 1)
    glVertex3f(0.0, -1.0, 0.0)
    glVertex3f(0.0, 1.0, 0.0)
    glEnd()

# Dados do triângulo: vértices e cores
vertices = np.array([
    -0.5, -0.5, 0.0,  # Vértice 1
     0.5, -0.5, 0.0,   # Vértice 2
     0.0, 0.5, 0.0     # Vértice 3
], dtype=np.float32)

cores = np.array([
    0.0, 0.0, 1.0,  # Azul
    0.0, 1.0, 0.0,  # Verde
    1.0, 0.0, 0.0   # Vermelho
], dtype=np.float32)

# Esses comandos, quando usados em conjunto, permitem o uso eficiente de VBOs para desenhar geometrias na GPU,
# reduzindo a sobrecarga na comunicação entre CPU e GPU e melhorando o desempenho da renderização gráfica.
def inicializa_triangulo():
    # Gera um identificador para o VBO de vértices
    vbo_vertices = glGenBuffers(1)
    # Vincula o buffer
    glBindBuffer(GL_ARRAY_BUFFER, vbo_vertices)
    # Carrega os dados dos vértices no buffer
    glBufferData(GL_ARRAY_BUFFER, vertices.nbytes, vertices, GL_STATIC_DRAW)

    # Gera um identificador para o VBO de cores
    vbo_cores = glGenBuffers(1)
    # Vincula o buffer
    glBindBuffer(GL_ARRAY_BUFFER, vbo_cores)
    # Carrega os dados das cores no buffer
    # GL_STATIC_DRAW indica que os dados não serão alterados e serão usados muitas vezes para desenhar
    glBufferData(GL_ARRAY_BUFFER, cores.nbytes, cores, GL_STATIC_DRAW)

    # Limpa o vínculo atual para evitar alterações acidentais
    glBindBuffer(GL_ARRAY_BUFFER, 0)

    return vbo_vertices, vbo_cores

def triangulo(vbo_vertices, vbo_cores):
    # Habilitam o uso de arrays de vértices e cores, respectivamente. Isso informa ao OpenGL que vamos usar esses dados para renderização
    glEnableClientState(GL_VERTEX_ARRAY)
    glEnableClientState(GL_COLOR_ARRAY)

    # Vincula o buffer de vértices para que possa ser usado.
    glBindBuffer(GL_ARRAY_BUFFER, vbo_vertices)
    # Define como os dados do vértice serão interpretados
    glVertexPointer(3, GL_FLOAT, 0, None)

    glBindBuffer(GL_ARRAY_BUFFER, vbo_cores)
    glColorPointer(3, GL_FLOAT, 0, None)

    # Executa o desenho dos vértices como triângulos
    glDrawArrays(GL_TRIANGLES, 0, 3)

    glBindBuffer(GL_ARRAY_BUFFER, 0)
    glDisableClientState(GL_VERTEX_ARRAY)
    glDisableClientState(GL_COLOR_ARRAY)

desenha_em_linhas = False
def key_callback(window, key, scancode, action, mods):
    global desenha_em_linhas
    if key == glfw.KEY_SPACE and action == glfw.PRESS:
        desenha_em_linhas = not desenha_em_linhas
def main():
    if not glfw.init():
        return

    janela = glfw.create_window(500, 500, "Minha janela", None, None)
    if not janela:
        glfw.terminate()
        return

    glfw.make_context_current(janela)
    glfw.set_key_callback(janela, key_callback)

    global desenha_em_linhas
    vbo_vertices, vbo_cores = inicializa_triangulo()
    while not glfw.window_should_close(janela):
        glfw.poll_events()
        glClearColor(0, 0, 0, 1)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        eixos()
        if (desenha_em_linhas):
            glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
        else:
            glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
        triangulo(vbo_vertices, vbo_cores)

        glfw.swap_buffers(janela)

    glfw.destroy_window(janela)
    glfw.terminate()

if __name__ == "__main__":
    main()