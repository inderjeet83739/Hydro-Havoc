import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600

obstacle_width, obstacle_height = 80, 80

# Create a window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hydro Havoc")

# Level variables
current_level = 1  # Start with level 1
score_to_next_level = 1000  # Score needed to reach the next level

# Level variables
current_level = 1  # Start with level 1
score_to_level_2 = 1250  # Score needed to reach level 2
score_to_level_3 = 2500  # Score needed to reach level 3
score_to_level_4 = 3750  # Score needed to reach level 4

# Load road images for levels
level_1_road = pygame.image.load('road.png')  # Replace with your Level 1 road image
level_2_road = pygame.image.load('calgary_road.png')  # Replace with your Level 2 road image
level_3_road = pygame.image.load('Vancouver_road.png')  # Replace with your Level 3 road image
level_4_road = pygame.image.load('Toronto road.png')  # Replace with your Level 4 road image

# Transform road images
level_1_road = pygame.transform.scale(level_1_road, (WIDTH + 100, HEIGHT))
level_2_road = pygame.transform.scale(level_2_road, (WIDTH + 100, HEIGHT))
level_3_road = pygame.transform.scale(level_3_road, (WIDTH + 100, HEIGHT))
level_4_road = pygame.transform.scale(level_4_road, (WIDTH + 100, HEIGHT))

# Load obstacle images for levels
level_1_obstacle = pygame.image.load('straight_car.png')  # Level 1 obstacle image
level_2_obstacle = pygame.image.load('Calgary_obstacle.png')  # Level 2 obstacle image
level_3_obstacle = pygame.image.load('Vancouver_obstacle.png')  # Level 3 obstacle image
level_4_obstacle = pygame.image.load('toronto_obstacle.png')  # Level 4 obstacle image

# Transform obstacle images
level_1_obstacle = pygame.transform.scale(level_1_obstacle, (obstacle_width, obstacle_height))
level_2_obstacle = pygame.transform.scale(level_2_obstacle, (obstacle_width, obstacle_height))
level_3_obstacle = pygame.transform.scale(level_3_obstacle, (obstacle_width, obstacle_height))
level_4_obstacle = pygame.transform.scale(level_4_obstacle, (obstacle_width, obstacle_height))

# Load road images for levels
level_1_road = pygame.image.load('road.png')  # Replace with your level 1 road image
level_2_road = pygame.image.load('calgary_road.png')  # Replace with your level 2 road image

# Transform road images
level_1_road = pygame.transform.scale(level_1_road, (WIDTH + 100, HEIGHT))
level_2_road = pygame.transform.scale(level_2_road, (WIDTH + 100, HEIGHT))

# Load obstacle images for levels
level_1_obstacle = pygame.image.load('straight_car.png')  # Replace with level 1 obstacle image
level_2_obstacle = pygame.image.load('calgary_obstacle.png')  # Replace with level 2 obstacle image

# Transform obstacle images
level_1_obstacle = pygame.transform.scale(level_1_obstacle, (obstacle_width, obstacle_height))
level_2_obstacle = pygame.transform.scale(level_2_obstacle, (obstacle_width, obstacle_height))

# Load the background image
side_img = pygame.image.load('road.png')  # Replace with your image file
side_img = pygame.transform.scale(side_img, (WIDTH + 100, HEIGHT))

# Load the player's car image
car_width, car_height = 80, 80

# Load player car images for levels
level_1_car_img = pygame.image.load('car 1.png')  # Level 1 car
level_2_car_img = pygame.image.load('Calgary_car.png')  # Level 2 car
level_3_car_img = pygame.image.load('Vancouver_car.png')  # Level 3 car (replace with your image)
level_4_car_img = pygame.image.load('Toronto_car.png')  # Level 4 car (replace with your image)

# Transform the car images to fit the player's car dimensions
level_1_car_img = pygame.transform.scale(level_1_car_img, (car_width, car_height))
level_2_car_img = pygame.transform.scale(level_2_car_img, (car_width, car_height))
level_3_car_img = pygame.transform.scale(level_3_car_img, (car_width, car_height))
level_4_car_img = pygame.transform.scale(level_4_car_img, (car_width, car_height))



# Load the obstacle car image
obstacle_img = pygame.image.load('straight_car.png')  # Replace with your obstacle car image
obstacle_width, obstacle_height = 80, 80
obstacle_img = pygame.transform.scale(obstacle_img, (obstacle_width, obstacle_height))

# Load the power-up image
power_up_img = pygame.image.load('coin.png')  # Replace with your image file
power_up_width, power_up_height = 60, 60  # Adjust based on your image size
power_up_img = pygame.transform.scale(power_up_img, (power_up_width, power_up_height))

# Load the boat image
boat_img = pygame.image.load('boat.png')  # Replace with your boat image file
boat_width, boat_height = 100, 60  # Adjust size as needed
boat_img = pygame.transform.scale(boat_img, (boat_width, boat_height))

# Initialize positions for two background images
side_img_x = -50
side_img_y1 = 0
side_img_y2 = -HEIGHT
side_img_speed = 5

# Initialize the player's car position
car_x = WIDTH // 2 - car_width // 2
car_y = HEIGHT - car_height - 20
x_change = 0

# Adjust boundaries based on lane positions
# Lanes for levels
lanes_level_1_and_2 = [250, 325, 470]  # Lanes for levels 1 and 2
lane_level_3 = 325  # Single lane for level 3
lanes_level_4 = [250, 325, 470]  # Multiple lanes for level 4
left_boundary = min(lanes_level_1_and_2)  # 250
right_boundary = max(lanes_level_1_and_2) + obstacle_width  # 470 + 80 = 550

# Water area boundaries for boats
water_left_boundary = 60  # Left boundary of water
water_right_boundary = 120  # Right boundary of water

# Ensure the boats are fixed within the valid range
boat_x_fixed = water_left_boundary

# Power-up variables
power_up_x = random.randint(left_boundary, right_boundary - power_up_width)
power_up_y = random.randint(-600, -power_up_height)  # Start off-screen
power_up_speed = 5
power_up_active = True

# Boat variables
boats = []
boat_speed = 3  # Boat speed

def show_level_completed(screen, message, duration=2000):
    """
    Display a level completion message with a fade-in effect.

    :param screen: Pygame screen object
    :param message: The message to display (e.g., "Level 1 Completed")
    :param duration: Duration to display the message (in milliseconds)
    """
    font = pygame.font.Font(None, 80)  # Adjust font size as needed
    text = font.render(message, True, (0, 255, 0))  # White text
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))  # Center the text

    # Fade-in effect
    start_time = pygame.time.get_ticks()
    while pygame.time.get_ticks() - start_time < duration:
        alpha = int(255 * ((pygame.time.get_ticks() - start_time) / duration))  # Calculate opacity
        faded_text = text.copy()
        faded_text.set_alpha(alpha)
        screen.fill((0, 0, 0))  # Clear the screen
        screen.blit(faded_text, text_rect)  # Draw the fading text
        pygame.display.flip()
        pygame.time.delay(30)  # Control the fade speed

# Function to check for boat overlaps
def is_boat_overlapping(new_boat, boats, min_distance=120):
    for boat in boats:
        if abs(new_boat[1] - boat[1]) < min_distance:  # Check vertical distance
            return True
    return False

def show_end_game_screen(screen, message):
    """
    Display an end-game message when the score reaches 5000.

    :param screen: Pygame screen object
    :param message: The message to display
    """
    font = pygame.font.Font(None, 80)  # Set font size
    text = font.render(message, True, (0, 255, 0))  # Green text
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))  # Center the text

    # Display the message and wait for a short duration
    screen.fill((0, 0, 0))  # Clear the screen
    screen.blit(text, text_rect)  # Draw the text
    pygame.display.flip()  # Update the display
    pygame.time.delay(3000)  # Wait for 3 seconds

# Spawn initial boats without overlap
for _ in range(3):
    retry = 0
    while retry < 10:  # Retry limit to avoid infinite loops
        boat_x = boat_x_fixed  # Fixed X position
        boat_y = random.randint(-600, -boat_height)  # Spawn off-screen
        new_boat = [boat_x, boat_y]
        if not is_boat_overlapping(new_boat, boats):
            boats.append(new_boat)
            break
        retry += 1

# Obstacle cars
cars = []
obstacle_speed = 3  # Downward obstacle car speed
score = 0
spawn_timer = 0

# Function to check if a new car overlaps with existing cars
def is_overlapping(new_car, cars, min_distance=150):
    for car in cars:
        if car[0] == new_car[0] and abs(car[1] - new_car[1]) < min_distance:
            return True
    return False

# Spawn initial downward cars in specific lanes without overlap
for _ in range(3):
    retry = 0
    while retry < 10:  # Retry limit to avoid infinite loop
        lane = random.choice(lanes_level_1_and_2)
        y_pos = random.randint(-500, -obstacle_height)  # Spawn above the screen
        new_car = [lane, y_pos]
        if not is_overlapping(new_car, cars):
            cars.append(new_car)
            break
        retry += 1

# Player's health
max_health = 5  # Maximum health points
health = max_health  # Start with full health

# Health bar properties
health_bar_width = 200  # Total width of the health bar
health_bar_height = 20   # Height of the health bar
health_bar_x = 10        # X position of the bar
health_bar_y = 50        # Y position of the bar

# Clock for controlling frame rate
clock = pygame.time.Clock()

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Check if the score has reached 5000
        if score >= 5000:
            show_end_game_screen(screen, "You've reached 5000 points!")
            running = False  # End the game loop

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -3
            if event.key == pygame.K_RIGHT:
                x_change = 3

        if event.type == pygame.KEYUP:
            if event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
                x_change = 0

    screen.fill((0, 0, 0))

    # Move the background
    side_img_y1 += side_img_speed
    side_img_y2 += side_img_speed

    if side_img_y1 >= HEIGHT:
        side_img_y1 = side_img_y2 - HEIGHT
    if side_img_y2 >= HEIGHT:
        side_img_y2 = side_img_y1 - HEIGHT

    # Move the player's car
    car_x += x_change
    if car_x < 0:
        car_x = 0
    if car_x > WIDTH - car_width:
        car_x = WIDTH - car_width

    # Gradually decrease health (gas) over time
    health -= 0.002  # Decrease rate; adjust for gameplay balance
    health = max(0, health)  # Ensure health doesn't drop below 0

    # Check for game over
    if health <= 0:
        print("Game Over")  # Debug message
        running = False  # End the game

    # Move the power-up
    if power_up_active:
        power_up_y += power_up_speed
        if power_up_y > HEIGHT:  # Reset when the power-up moves off-screen
            power_up_x = random.randint(left_boundary, right_boundary - power_up_width)
            power_up_y = random.randint(-600, -power_up_height)

    # Move and reset boats only in level 1
    if current_level == 1:
        new_boats = []
        for boat in boats:
            boat[1] += boat_speed
            if boat[1] > HEIGHT:  # Reset when the boat moves off-screen
                retry = 0
                while retry < 10:  # Retry limit to avoid infinite loops
                    boat_x = boat_x_fixed  # Fixed X position
                    boat_y = random.randint(-600, -boat_height)
                    new_boat = [boat_x, boat_y]
                    if not is_boat_overlapping(new_boat, new_boats):
                        new_boats.append(new_boat)
                        break
                    retry += 1
            else:
                new_boats.append(boat)
        boats = new_boats

    # Spawn obstacles periodically
    spawn_timer += clock.get_time()
    if spawn_timer >= 2000:
        retry = 0
        while retry < 10:  # Retry limit to avoid infinite loop
            # Choose lanes based on the current level
            if current_level in [1, 2]:
                lane = random.choice(lanes_level_1_and_2)  # Multiple lanes for levels 1 and 2
            elif current_level == 3:
                lane = lane_level_3  # Single lane for level 3
            elif current_level == 4:
                lane = random.choice(lanes_level_4)  # Multiple lanes for level 4

            y_pos = random.randint(-500, -obstacle_height)  # Spawn above the screen
            new_car = [lane, y_pos]
            if not is_overlapping(new_car, cars):
                cars.append(new_car)
                break
            retry += 1
        spawn_timer = 0

    # Check for collision with power-up (coin)
    power_up_rect = pygame.Rect(power_up_x, power_up_y, power_up_width, power_up_height)
    player_rect = pygame.Rect(car_x, car_y, car_width, car_height)

    # Check for collision with power-up (coin)
    power_up_rect = pygame.Rect(power_up_x, power_up_y, power_up_width, power_up_height)
    player_rect = pygame.Rect(car_x, car_y, car_width, car_height)

    if player_rect.colliderect(power_up_rect):
        health = min(max_health, health + 1)  # Increase health by 1, clamp to max_health
        power_up_active = False  # Disable power-up temporarily

        # Reset power-up position
        power_up_x = random.randint(left_boundary, right_boundary - power_up_width)
        power_up_y = random.randint(-600, -power_up_height)
        power_up_active = True

    # Check for collision with obstacle cars
    # for car in cars:
    # # Check horizontal alignment
    #     horizontally_aligned = (
    #         car_x < car[0] + obstacle_width and  # Player's car left edge is left of obstacle's right edge
    #         car_x + car_width > car[0]          # Player's car right edge is right of obstacle's left edge
    #     )
    #     # Check front-to-back vertical collision
    #     front_touching_back = (
    #         car_y == car[1] + obstacle_height  # Player's car front touches obstacle's back
    #     )
    #     if horizontally_aligned and front_touching_back:
    #         health = max(0, health - 1)  # Decrease health by 1, but do not go below 0
    #         cars.remove(car)  # Remove the car after collision
    #         if health <= 0:
    #             print("Game Over")  # Debug message
    #             running = False  # End the game
    #         break  # Exit the loop after handling collision

    # Move and draw the obstacles
    new_cars = []
    for car in cars:
        car[1] += obstacle_speed
        if car[1] > HEIGHT + obstacle_height:  # Reset when the car moves off-screen
            retry = 0
            while retry < 10:  # Retry limit to avoid infinite loop
                lane = random.choice(lanes_level_1_and_2)
                y_pos = random.randint(-500, -obstacle_height)
                new_position = [lane, y_pos]
                if not is_overlapping(new_position, cars):
                    new_cars.append([lane, y_pos])
                    break
                retry += 1
            score += 10  # Increment score for avoiding the car

        # Level transition logic
        elif current_level == 1 and score >= score_to_level_2:
            show_level_completed(screen, "Level 1 Completed!")
            current_level = 2
            print("Level Up! Welcome to Level 2!")
            cars = []  # Clear obstacles
            for _ in range(3):  # Spawn new obstacles for level 2
                lane = random.choice(lanes_level_1_and_2)
                y_pos = random.randint(-500, -obstacle_height)
                cars.append([lane, y_pos])

        elif current_level == 2 and score >= score_to_level_3:
            show_level_completed(screen, "Level 2 Completed!")
            current_level = 3
            print("Level Up! Welcome to Level 3!")
            cars = []  # Clear obstacles
            for _ in range(1):  # Spawn more obstacles for level 3
                lane = lane_level_3
                y_pos = random.randint(-500, -obstacle_height)
                cars.append([lane, y_pos])

        elif current_level == 3 and score >= score_to_level_4:
            show_level_completed(screen, "Level 3 Completed!")
            current_level = 4
            print("Level Up! Welcome to Level 4!")
            cars = []  # Clear obstacles
            for _ in range(5):  # Spawn more obstacles for level 4
                lane = random.choice(lanes_level_4)
                y_pos = random.randint(-500, -obstacle_height)
                cars.append([lane, y_pos])
        else:
            new_cars.append(car)
    cars = new_cars  # Replace the cars list with updated positions

    # Draw the road based on the current level
    if current_level == 1:
        screen.blit(level_1_road, (side_img_x, side_img_y1))
        screen.blit(level_1_road, (side_img_x, side_img_y2))
    elif current_level == 2:
        screen.blit(level_2_road, (side_img_x, side_img_y1))
        screen.blit(level_2_road, (side_img_x, side_img_y2))
    elif current_level == 3:
        screen.blit(level_3_road, (side_img_x, side_img_y1))
        screen.blit(level_3_road, (side_img_x, side_img_y2))
    elif current_level == 4:
        screen.blit(level_4_road, (side_img_x, side_img_y1))
        screen.blit(level_4_road, (side_img_x, side_img_y2))

    # Draw the obstacles based on the current level
    for car in cars:
        if current_level == 1:
            screen.blit(level_1_obstacle, (car[0], car[1]))
        elif current_level == 2:
            screen.blit(level_2_obstacle, (car[0], car[1]))
        elif current_level == 3:
            screen.blit(level_3_obstacle, (car[0], car[1]))
        elif current_level == 4:
            screen.blit(level_4_obstacle, (car[0], car[1]))

    # Draw the boats only in level 1
    if current_level == 1:
        for boat in boats:
            screen.blit(boat_img, (boat[0], boat[1]))

    # Draw the player's car based on the current level
    if current_level == 1:
        screen.blit(level_1_car_img, (car_x, car_y))
    elif current_level == 2:
        screen.blit(level_2_car_img, (car_x, car_y))
    elif current_level == 3:
        screen.blit(level_3_car_img, (car_x, car_y))
    elif current_level == 4:
        screen.blit(level_4_car_img, (car_x, car_y))

    # Draw the power-up
    if power_up_active:
        screen.blit(power_up_img, (power_up_x, power_up_y))

    # Draw the score
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Dodge: {score}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))

    # Draw the health bar
    health_ratio = health / max_health  # Ratio of health remaining
    current_bar_width = int(health_bar_width * health_ratio)  # Filled bar width

    # Change color based on remaining health
    if health_ratio > 0.7:
        health_color = (0, 255, 0)  # Green
    elif health_ratio > 0.2:
        health_color = (255, 255, 0)  # Yellow
    else:
        health_color = (255, 0, 0)  # Red

    pygame.draw.rect(screen, (100, 100, 100), (health_bar_x, health_bar_y, health_bar_width, health_bar_height))  # Background
    pygame.draw.rect(screen, health_color, (health_bar_x, health_bar_y, current_bar_width, health_bar_height))  # Current health
    pygame.draw.rect(screen, (0, 0, 0), (health_bar_x, health_bar_y, health_bar_width, health_bar_height), 2)  # Border

    # Update the display and regulate frame rate
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()