import pygame
import random
import sys

# Initialisation de Pygame
pygame.init()

# Dimensions de la fenêtre
WIDTH, HEIGHT = 800, 400
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Geometry Dash - Plateformes et Pics")

# Couleurs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)  # Couleur des plateformes
PURPLE = (255, 0, 255)  # Couleur des pics

# Joueur
PLAYER_SIZE = 30
player_x = 100
player_y = HEIGHT - PLAYER_SIZE - 50
player_velocity_y = 0
GRAVITY = 1
JUMP_POWER = -15

# Obstacles
obstacles = []
OBSTACLE_WIDTH = 30
OBSTACLE_HEIGHT = 50
OBSTACLE_SPEED = 5
ACCELERATION = 0.01  # Augmentation progressive de la vitesse
SPAWN_OBSTACLE_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(SPAWN_OBSTACLE_EVENT, 1500)

# Plateformes
platforms = []
PLATFORM_WIDTH = 100
PLATFORM_HEIGHT = 20
PLATFORM_SPEED = 3
SPAWN_PLATFORM_EVENT = pygame.USEREVENT + 2
pygame.time.set_timer(SPAWN_PLATFORM_EVENT, 2000)

# Pics
spikes = []
SPIKE_WIDTH = 20
SPIKE_HEIGHT = 20
SPAWN_SPIKE_EVENT = pygame.USEREVENT + 3
pygame.time.set_timer(SPAWN_SPIKE_EVENT, 3000)

# Police et score
FONT = pygame.font.Font(None, 36)
score = 0
game_over = False

def draw_game():
    """Dessine les éléments du jeu sur l'écran."""
    WINDOW.fill(BLACK)

    # Dessiner le sol
    pygame.draw.rect(WINDOW, WHITE, (0, HEIGHT - 50, WIDTH, 50))

    # Dessiner le joueur
    pygame.draw.rect(WINDOW, BLUE, (player_x, player_y, PLAYER_SIZE, PLAYER_SIZE))

    # Dessiner les plateformes
    for platform in platforms:
        pygame.draw.rect(WINDOW, GREEN, platform)

    # Dessiner les obstacles
    for obstacle in obstacles:
        pygame.draw.rect(WINDOW, RED, obstacle)

    # Dessiner les pics
    for spike in spikes:
        pygame.draw.polygon(WINDOW, PURPLE, [(spike.x, spike.y), (spike.x + SPIKE_WIDTH, spike.y), 
                                             (spike.x + SPIKE_WIDTH / 2, spike.y - SPIKE_HEIGHT)])

    # Dessiner le score
    score_text = FONT.render(f"Score: {score}", True, YELLOW)
    WINDOW.blit(score_text, (10, 10))

    # Afficher "Game Over" si nécessaire
    if game_over:
        game_over_text = FONT.render("GAME OVER - Press R to Restart", True, YELLOW)
        WINDOW.blit(game_over_text, (WIDTH // 2 - 200, HEIGHT // 2 - 20))

    pygame.display.flip()

def reset_game():
    """Réinitialise les variables du jeu pour redémarrer."""
    global player_y, player_velocity_y, obstacles, platforms, spikes, score, game_over, OBSTACLE_SPEED
    player_y = HEIGHT - PLAYER_SIZE - 50
    player_velocity_y = 0
    obstacles = []
    platforms = []
    spikes = []
    score = 0
    game_over = False
    OBSTACLE_SPEED = 5  # Réinitialisation de la vitesse des obstacles

# Boucle principale
clock = pygame.time.Clock()
running = True

while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and player_y >= HEIGHT - PLAYER_SIZE - 50:
                player_velocity_y = JUMP_POWER
            if event.key == pygame.K_r and game_over:
                reset_game()
        if event.type == SPAWN_OBSTACLE_EVENT and not game_over:
            obstacle_x = WIDTH
            obstacle_y = HEIGHT - OBSTACLE_HEIGHT - 50
            obstacles.append(pygame.Rect(obstacle_x, obstacle_y, OBSTACLE_WIDTH, OBSTACLE_HEIGHT))

        if event.type == SPAWN_PLATFORM_EVENT and not game_over:
            platform_x = random.randint(WIDTH, WIDTH + 100)
            platform_y = random.randint(150, HEIGHT - 100)
            platforms.append(pygame.Rect(platform_x, platform_y, PLATFORM_WIDTH, PLATFORM_HEIGHT))

        if event.type == SPAWN_SPIKE_EVENT and not game_over:
            spike_x = random.randint(WIDTH, WIDTH + 100)
            spike_y = HEIGHT - 50
            spikes.append(pygame.Rect(spike_x, spike_y, SPIKE_WIDTH, SPIKE_HEIGHT))

    # Mise à jour du joueur
    if not game_over:
        player_velocity_y += GRAVITY
        player_y += player_velocity_y

        # Empêcher le joueur de tomber sous le sol
        if player_y > HEIGHT - PLAYER_SIZE - 50:
            player_y = HEIGHT - PLAYER_SIZE - 50
            player_velocity_y = 0

        # Vérifier les plateformes (le joueur saute dessus)
        player_rect = pygame.Rect(player_x, player_y, PLAYER_SIZE, PLAYER_SIZE)
        for platform in platforms:
            if player_rect.colliderect(platform) and player_velocity_y >= 0:
                player_y = platform.top - PLAYER_SIZE
                player_velocity_y = 0

        # Mise à jour des obstacles
        for obstacle in obstacles:
            obstacle.x -= OBSTACLE_SPEED
        obstacles = [obs for obs in obstacles if obs.x + OBSTACLE_WIDTH > 0]

        # Mise à jour des plateformes
        for platform in platforms:
            platform.x -= PLATFORM_SPEED
        platforms = [plat for plat in platforms if plat.x + PLATFORM_WIDTH > 0]

        # Mise à jour des pics
        for spike in spikes:
            spike.x -= OBSTACLE_SPEED
        spikes = [spike for spike in spikes if spike.x + SPIKE_WIDTH > 0]

        # Détecter les collisions
        for obstacle in obstacles:
            if player_rect.colliderect(obstacle):
                game_over = True

        for spike in spikes:
            if player_rect.colliderect(spike):
                game_over = True

        # Mettre à jour le score
        score += 1

        # Augmenter la vitesse des obstacles avec le score
        OBSTACLE_SPEED += ACCELERATION

    # Dessiner le jeu
    draw_game()

pygame.quit()
sys.exit()
