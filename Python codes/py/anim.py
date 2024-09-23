import pygame
from matplotlib.animation import FuncAnimation

# Initialize pygame
pygame.init()

# Create a window
screen = pygame.display.set_mode((640, 480))

# Load the images for the person
person_images = []
for i in range(10):
  person_images.append(pygame.image.load("person_frame_" + str(i) + ".png"))

# Create a clock
clock = pygame.time.Clock()

# Define the animation function
def animate(i):
  screen.blit(person_images[i], (0, 0))

# Create the animation
animation = FuncAnimation(
    screen, animate, interval=100, frames=len(person_images) - 1
)

# Start the animation loop
running = True
while running:
  # Get the current time
  time = clock.tick()

  # Update the animation
  animation.update(time)

  # Render the frame
  pygame.display.flip()

  # Check for events
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

# Quit pygame
pygame.quit()
