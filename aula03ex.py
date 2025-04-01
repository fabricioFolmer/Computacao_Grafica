import glfw                 # Importa a biblioteca GLFW para gerenciar janelas e eventos
from OpenGL.GL import *     # Importa funções do OpenGL
import numpy as np, time


# Função para desenhar um triângulo, cuja altura varia com o tempo
def triangulo(base, altura, preencher_interior: bool = True):
    
    if preencher_interior:
        glBegin(GL_POLYGON)         # Inicia um polígono
    else:
        glBegin(GL_LINE_LOOP )       # Inicia um loop de linhas
    glColor3f(1, 0, 0)
    glVertex3f(-base/2,     -altura/2,      0)  # Vértice inferior esquerdo
    glColor3f(0, 1, 0)
    glVertex3f(base/2,      -altura/2,      0)  # Vértice inferior direito
    glColor3f(0, 0, 1)
    glVertex3f(0,           altura/2,       0)  # Vértice superior
    glEnd()  # Finaliza o desenho

# Função principal do programa
def main():
    if not glfw.init():  # Inicializa o GLFW e verifica se teve sucesso
        exit()

    # Cria janela
    janela = glfw.create_window(500, 500, "Minha janela", None, None)
    glfw.make_context_current(janela)  # Define o contexto OpenGL
    glfw.swap_interval(1)  # Sincroniza a taxa de atualização com o monitor

    preencher_interior = True

    while not glfw.window_should_close(janela):  # Loop principal até a janela ser fechada
        glClearColor(0, 0, 0, 1)  # Define a cor de fundo como preto
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)  # Limpa a tela

        triangulo(1, 1, preencher_interior)

        glfw.swap_buffers(janela)  # Troca os buffers para exibir o próximo frame
        glfw.poll_events()  # Processa eventos do teclado e mouse
        
        # Se espaço for teclado, altera modo de preenchimento do triangulo:
        if glfw.get_key(janela, glfw.KEY_SPACE):
            preencher_interior = not preencher_interior

        # Se Esc for teclado, sai do loop e fecha janela
        if glfw.get_key(janela, glfw.KEY_ESCAPE):
            break
        
        time.sleep(1/30)

    glfw.destroy_window(janela)  # Destroi a janela após o loop
    glfw.terminate()  # Encerra o GLFW

# Executa a função principal se o script for executado diretamente
if __name__ == "__main__":
    main()
