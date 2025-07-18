import pygame
import sys

# Inicializar pygame
pygame.init()

# Configurar la ventana
WIDTH, HEIGHT = 400, 300
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Piano con teclas A-G")

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Cargar sonidos de notas
notas = {
    pygame.K_a: 'A.wav',
    pygame.K_b: 'B.wav',
    pygame.K_c: 'C.wav',
    pygame.K_d: 'D.wav',
    pygame.K_e: 'E.wav',
    pygame.K_f: 'F.wav',
    pygame.K_g: 'G.wav',
}

# Cargar objetos de sonido
sonidos = {}
for tecla, archivo in notas.items():
    try:
        sonidos[tecla] = pygame.mixer.Sound(archivo)
    except pygame.error:
        print(f"Error al cargar {archivo}")

# Bucle principal
running = True
while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Reproducir nota al presionar tecla
        if event.type == pygame.KEYDOWN:
            if event.key in sonidos:
                sonidos[event.key].play()

    # Mostrar texto
    font = pygame.font.SysFont(None, 36)
    texto = font.render("Presiona A-G para tocar notas", True, BLACK)
    screen.blit(texto, (50, HEIGHT // 2 - 20))

    pygame.display.flip()

# Salir de pygame
pygame.quit()
sys.exit()
