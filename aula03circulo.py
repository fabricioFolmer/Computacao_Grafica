import glfw                 # Importa a biblioteca GLFW para gerenciar janelas e eventos
from OpenGL.GL import *     # Importa funções do OpenGL
import numpy as np, time

# Função para desenhar os eixos cartesianos
# Desenha duas linhas que representam os eixos X e Y
def eixos():
    glBegin(GL_LINES)  # Inicia o modo de desenho de linhas
    glColor3f(1.0, 1, 1)  # Define a cor para o eixo X (branco)
    glVertex3f(-1.0, 0.0, 0.0)  # Ponto inicial do eixo X
    glVertex3f(1.0, 0.0, 0.0)  # Ponto final do eixo X

    glColor3f(1, 1.0, 1)  # Define a cor para o eixo Y (branco)
    glVertex3f(0.0, -1.0, 0.0)  # Ponto inicial do eixo Y
    glVertex3f(0.0, 1.0, 0.0)  # Ponto final do eixo Y
    glEnd()  # Finaliza o desenho

# Função para desenhar um círculo com raio e número de segmentos especificados
def circulo(raio, segmentos):
    #glBegin(GL_TRIANGLE_FAN)  # Inicia o modo de desenho de um círculo preenchido
    glBegin(GL_POLYGON)
    glColor3f(1,1,0)  # Define a cor amarela
    for i in range(segmentos):  # Percorre cada segmento do círculo
        angulo = 2.0 * np.pi * i / segmentos  # Calcula o ângulo para cada ponto
        x = raio * np.cos(angulo)  # Calcula a coordenada X do ponto
        y = raio * np.sin(angulo)  # Calcula a coordenada Y do ponto
        glVertex3f(x, y, 0)  # Adiciona o vértice ao círculo
    glEnd()  # Finaliza o desenho

# Função para desenhar um triângulo, cuja altura varia com o tempo
def triangulo(altura):
    glColor3f(0,0,0)  # Define a cor preta
    glBegin(GL_TRIANGLES)  # Inicia o modo de desenho de triângulos
    glVertex3f(0,0, 0)  # Primeiro vértice na origem
    glVertex3f(0.5,altura, 0)  # Segundo vértice, altura variável
    glVertex3f(0.5, -altura,0)  # Terceiro vértice, altura variável
    glEnd()  # Finaliza o desenho

# Função principal do programa
def main():
    if not glfw.init():  # Inicializa o GLFW e verifica se teve sucesso
        exit()

    # Cria janela
    janela = glfw.create_window(500, 500, "Minha janela", None, None)
    glfw.make_context_current(janela)  # Define o contexto OpenGL
    glfw.swap_interval(1)  # Sincroniza a taxa de atualização com o monitor

    while not glfw.window_should_close(janela):  # Loop principal até a janela ser fechada
        glClearColor(0, 0, 0, 1)  # Define a cor de fundo como preto
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)  # Limpa a tela

        # eixos()  # (Comentado) Desenha os eixos cartesianos
        circulo(0.5, 64)  # Desenha um círculo de raio 0.5 com 32 segmentos

       # altura = 0.2 * np.sin(time.time()*7)  # Calcula a altura do triângulo, variando com o tempo
       # triangulo(altura)  # Desenha o triângulo com altura oscilante

        glfw.swap_buffers(janela)  # Troca os buffers para exibir o próximo frame
        glfw.poll_events()  # Processa eventos do teclado e mouse
        
        # Se Esc for teclado, sai do loop e fecha janela
        if glfw.get_key(janela, glfw.KEY_ESCAPE):
            break


    glfw.destroy_window(janela)  # Destroi a janela após o loop
    glfw.terminate()  # Encerra o GLFW

# Executa a função principal se o script for executado diretamente
if __name__ == "__main__":
    main()
