import asyncio
import pygame

# Initialize pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))


async def main():

    # Square setup
    square_size = 50
    x, y = 100, 100
    speed_x, speed_y = 5, 5
    WHITE = (255, 255, 255)

    # Paddle setup
    paddle_width, paddle_height = 20, 100
    paddle_x, paddle_y = WIDTH - 40, HEIGHT // 2 - paddle_height // 2
    paddle_speed = 6

    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Paddle movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and paddle_y > 0:
            paddle_y -= paddle_speed
        if keys[pygame.K_DOWN] and paddle_y + paddle_height < HEIGHT:
            paddle_y += paddle_speed

        # Update square position
        x += speed_x
        y += speed_y

        # Bounce off edges
        if x + square_size > WIDTH or x < 0:
            speed_x = -speed_x
        if y + square_size > HEIGHT or y < 0:
            speed_y = -speed_y

        # Bounce off paddle
        if x + square_size >= paddle_x and paddle_y < y + square_size and y < paddle_y + paddle_height:
            speed_x = -speed_x

        # Draw everything
        screen.fill((0, 0, 0))
        pygame.draw.rect(screen, WHITE, (x, y, square_size, square_size))
        pygame.draw.rect(screen, WHITE, (paddle_x, paddle_y, paddle_width, paddle_height))
        pygame.display.flip()

        # Control loop speed
        clock.tick(60)
        await asyncio.sleep(0)

    pygame.quit()




