import pygame
import datetime
import os

pygame.init()
screen = pygame.display.set_mode((1200, 700))
pygame.display.set_caption("Mickey Mouse Clock")
WHITE = (255, 255, 255)

# Путь к папке с изображениями
base = r'C:\pp2\Practice09\mickey_maus\images'

# Загрузка изображений
try:
    image_surface = pygame.image.load(os.path.join(base, 'clock.png')).convert_alpha()
    mickey = pygame.image.load(os.path.join(base, 'mUmrP.png')).convert_alpha()
    hand_l = pygame.image.load(os.path.join(base, 'hand_left.png')).convert_alpha() # Секунды
    hand_r = pygame.image.load(os.path.join(base, 'hand_right.png')).convert_alpha() # Минуты
except pygame.error as e:
    print(f"Ошибка загрузки изображений: {e}")
    pygame.quit()
    exit()

# Масштабирование
resized_image = pygame.transform.scale(image_surface, (800, 600))
res_mickey = pygame.transform.scale(mickey, (350, 350))
# Подбери размер рук под свой циферблат (длиннее для секунд, короче для минут)
hand_l_base = pygame.transform.scale(hand_l, (200, 200)) # Левая (секунды)
hand_r_base = pygame.transform.scale(hand_r, (160, 160)) # Правая (минуты)

CLOCK_CENTER = (600, 350) # Центральная точка для всех элементов

clock = pygame.time.Clock()
done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # Получаем текущее время
    now = datetime.datetime.now()
    m = now.minute
    s = now.second

    # Расчет углов (в Pygame 0 градусов — это "на 3 часа", поэтому может понадобиться 
    # корректировка смещения, если картинки рук изначально смотрят не вверх)
    # Обычно картинки стрелок рисуют смотрящими вверх (на 12 часов)
    seconds_angle = -(s * 6)  # 360 / 60 = 6 градусов за секунду
    minutes_angle = -(m * 6)  # 360 / 60 = 6 градусов за минуту

    # Вращение
    # Левая рука (hand_l) — секунды
    rotated_seconds = pygame.transform.rotate(hand_l_base, seconds_angle)
    # Правая рука (hand_r) — минуты
    rotated_minutes = pygame.transform.rotate(hand_r_base, minutes_angle)

    # Выравнивание центров после вращения
    sec_rect = rotated_seconds.get_rect(center=CLOCK_CENTER)
    min_rect = rotated_minutes.get_rect(center=CLOCK_CENTER)

    # Отрисовка
    screen.fill(WHITE)

    # 1. Циферблат
    image_rect = resized_image.get_rect(center=CLOCK_CENTER)
    screen.blit(resized_image, image_rect)

    # 2. Тело Микки
    mic_rect = res_mickey.get_rect(center=CLOCK_CENTER)
    screen.blit(res_mickey, mic_rect)

    # 3. Стрелки (рисуем минуты, потом секунды поверх)
    screen.blit(rotated_minutes, min_rect)
    screen.blit(rotated_seconds, sec_rect)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()