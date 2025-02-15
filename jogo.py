import pygame
import sys



class Poo:
    def __init__(self):
        self.fome = 100
        self.sujidade = 100000

meu_poo = Poo()

# Inicializar o Pygame
pygame.init()

# Criar a janela
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Jogo do POU")


# Cores
BRANCO = (255, 255, 255)
AZUL = (100, 100, 255)
AZUL_MOUSE = (150, 150, 255)

# Carregar imagem
image = pygame.image.load('pou.png')
image_rect = image.get_rect(center=(400, 200))

# Posições e tamanhos dos botões
button1 = pygame.Rect(300, 400, 200, 50)
button2 = pygame.Rect(300, 480, 200, 50)

# Funções para os botões
def button1_clicked():
    meu_poo.fome -= 10
    print("Clicaste no Botão 1!")

def button2_clicked():
    print("Clicaste no Botão 2!")

# Loop principal do jogo
running = True
while running:
    screen.fill(BRANCO)  # Preencher a tela com branco

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Clique do botão esquerdo do rato
                if button1.collidepoint(event.pos):
                    button1_clicked()
                if button2.collidepoint(event.pos):
                    button2_clicked()

    # Desenhar a imagem

    if meu_poo.fome >= 0:
        screen.blit(image, image_rect)

    # Desenhar os botões
    mouse_pos = pygame.mouse.get_pos()
    if button1.collidepoint(mouse_pos):
        pygame.draw.rect(screen, AZUL_MOUSE, button1)
    else:
        pygame.draw.rect(screen, AZUL, button1)

    if button2.collidepoint(mouse_pos):
        pygame.draw.rect(screen, AZUL_MOUSE, button2)
    else:
        pygame.draw.rect(screen, AZUL, button2)

    # Mostrar o texto nos botões
    font = pygame.font.SysFont('Arial', 30)
    text1 = font.render("Botão 1", True, (255, 255, 255))
    text2 = font.render("Botão 2", True, (255, 255, 255))

    screen.blit(text1, (button1.centerx - text1.get_width() // 2, button1.centery - text1.get_height() // 2))
    screen.blit(text2, (button2.centerx - text2.get_width() // 2, button2.centery - text2.get_height() // 2))

    texto_fome = font.render(f"Fome: {meu_poo.fome} Sujidade: {meu_poo.sujidade}", False, (0, 0, 0))
    screen.blit(texto_fome, (0, 0))
    screen.blit(texto_fome, pygame.mouse.get_pos())

    pygame.display.flip()  # Atualizar a tela

# Terminar o jogo
pygame.quit()
sys.exit()
