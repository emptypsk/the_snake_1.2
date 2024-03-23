from random import choice, randint
import time
import pygame
# Инициализация микшера.
pygame.mixer.init()
# Инициализация PyGame.
pygame.init()

# Константы для размеров поля и сетки:
SCREEN_WIDTH, SCREEN_HEIGHT = 640, 480
GRID_SIZE = 20
GRID_WIDTH = SCREEN_WIDTH // GRID_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // GRID_SIZE

# Направления движения:
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# Цвет поля - чёрный.
BOARD_BACKGROUND_COLOR = (0, 0, 0)
# Цвет границы ячейки.
BORDER_COLOR = (93, 216, 228)
# Стартовый цвет змейки.
SNAKE_COLOR = (153, 153, 0)
# Словарь цветов змейки в зависимости от очков.
SNAKE_COLOR_DICT = {5: (204, 204, 0),
                    10: (255, 255, 0),
                    15: (255, 255, 51),
                    20: (255, 255, 102),
                    25: (255, 255, 153),
                    30: (255, 255, 204),
                    35: (128, 255, 0),
                    40: (0, 255, 0),
                    45: (0, 255, 255),
                    50: (255, 0, 255)
                    }

# Настройка игрового окна:
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)
pygame.display.set_caption('')
clock = pygame.time.Clock()
pygame.mixer.music.load("background_music.mp3")
pygame.mixer.music.play(loops=-1)
# Загрузка картинок для объектов:
game_over_image = pygame.image.load('game_over.png')
snake_head_image = pygame.image.load('snake_head.png')
bad_apple_image = pygame.image.load('bad_apple.png')
apple_image = pygame.image.load('apple.png')


class GameObject:
    """Основной класс для представления игровых объектов"""

    def __init__(self, position=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)):
        self.position = position
        self.body_color = None

    def draw(self):
        """Отрисовывает игровой объект."""
        raise NotImplementedError

    def rect(self, position):
        """Отрисовывает ячейки"""
        rect = pygame.Rect(position, (GRID_SIZE, GRID_SIZE))
        return rect

class Apple(GameObject):
    """Класс для представления яблока на игровом поле."""

    def __init__(self):
        super().__init__()
        self.image = apple_image

    def randomize_position(self, snake):
        """Устанавливает случайное положение яблока на игровом поле."""
        while True:
            self.position = (randint(0, GRID_WIDTH - 1) * GRID_SIZE,
                             randint(0, GRID_HEIGHT - 1) * GRID_SIZE)
            if self.position not in snake.positions:
                break

    def draw(self):
        """Отрисовывает яблоко на игровой поверхности."""
        screen.blit(self.image, self.position)

class BadApple(GameObject):
    """Класс для представления плохого яблока на игровом поле."""

    def __init__(self):
        super().__init__()
        self.is_visible = False
        self.randomize_position()
        self.image = bad_apple_image

    def randomize_position(self, snake):
        """Устанавливает случайное положение плохого яблока на игровом поле."""
        while True:
            self.position = (randint(0, GRID_WIDTH - 1) * GRID_SIZE,
                             randint(0, GRID_HEIGHT - 1) * GRID_SIZE)
            if self.position not in snake.positions:
                break

    def draw(self):
        """Отрисовывает плохое яблоко на игровой поверхности."""
        screen.blit(self.image, self.position)
        self.is_visible = True





def handle_keys(snake):
    """
    Обрабатывает нажатия клавиш для изменения направления
    движения змейки.
    """
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake.direction != DOWN:
                snake.next_direction = UP
            elif event.key == pygame.K_DOWN and snake.direction != UP:
                snake.next_direction = DOWN
            elif event.key == pygame.K_LEFT and snake.direction != RIGHT:
                snake.next_direction = LEFT
            elif event.key == pygame.K_RIGHT and snake.direction != LEFT:
                snake.next_direction = RIGHT
            elif event.key == pygame.K_ESCAPE:
                pygame.quit()
                raise SystemExit
        elif event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
        
def draw_borders():
    """Отрисовка границ экрана."""
    border_thickness = 2
    # Верхняя граница.
    pygame.draw.rect(
        screen, BORDER_COLOR, (0, 0, SCREEN_WIDTH, border_thickness))
    # Левая граница.
    pygame.draw.rect(
        screen, BORDER_COLOR, (0, 0, border_thickness, SCREEN_HEIGHT))
    # Нижняя граница.
    pygame.draw.rect(
        screen, BORDER_COLOR, (0, SCREEN_HEIGHT - border_thickness,
                               SCREEN_WIDTH, border_thickness))
    # Правая граница.
    pygame.draw.rect(
        screen, BORDER_COLOR, (SCREEN_WIDTH - border_thickness,
                               0, border_thickness, SCREEN_HEIGHT))
