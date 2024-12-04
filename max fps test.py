import pygame
import time

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Max FPS Test")

# Create a Clock object to track FPS
clock = pygame.time.Clock()

# Track time and frame count
start_time = time.time()
frame_count = 0

# Test duration in seconds
TEST_DURATION = 5

# Run the test
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw a basic color on the screen
    screen.fill((0, 0, 0))
    pygame.display.flip()

    # Increment frame count
    frame_count += 1

    # End the test after the set duration
    if time.time() - start_time >= TEST_DURATION:
        running = False

# Calculate and display FPS
elapsed_time = time.time() - start_time
max_fps = frame_count / elapsed_time
print(f"Max FPS: {max_fps:.2f}")

# Quit Pygame
pygame.quit()
