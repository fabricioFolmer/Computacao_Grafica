import random
import time
import glfw
from OpenGL.GL import *

# Criar uma janela no tamanho de 800x600, após pressionar a tecla ESQ  finalizar o programa.
# Troque randomicamente a cor de fundo da janela
# Para ser mais perceptível a mudança pode ser utilizado um timer

def main():
    # Inicializa glfw
    if not glfw.init():
        return

    # Cria janela
    janela = glfw.create_window(800, 600, "Minha janela", None, None)
    if not janela:
        glfw.terminate()
        return

    # Define o contexto OpenGL para a janela
    glfw.make_context_current(janela)

    # Sincroniza a taxa de atualização com o monitor
    glfw.swap_interval(1)

    ultimo_tempo = time.time()
    count_frames = 0        # Contador de frames
    tempo_troca_cor = .5    # segundos

    # Enquanto janela deve estar aberta
    while not glfw.window_should_close(janela):
        
        # Processa eventos do teclado e mouse
        glfw.poll_events()

        # Se Esc for teclado, sai do loop e fecha janela
        if glfw.get_key(janela, glfw.KEY_ESCAPE):
            break

        # Adiciona contador de frames
        count_frames += 1
        tempo_atual = time.time()

        # Se andou tempo necessário para processar próxima cor
        if tempo_atual - ultimo_tempo >= tempo_troca_cor:
            count_frames = 0            # Reseta o contador de frames
            ultimo_tempo = tempo_atual  

            # Define uma cor aleatório no plano de fundo
            glClearColor(random.random(), random.random(), random.random(), 0)
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # Limpa a tela

            # Exibe o próximo frame, trocando os buffers
            glfw.swap_buffers(janela)
            
    # Fecha janela
    glfw.destroy_window(janela)
    glfw.terminate()

if __name__ == "__main__":
    main()


