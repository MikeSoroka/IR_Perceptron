import pygame
import csv

class GridEditor:
    def __init__(self):
        # Initialize Pygame
        pygame.init()

        # Constants
        self.screen_width = 300
        self.screen_height = 300
        self.cell_size = 30
        self.rows = 10
        self.cols = 10

        # Colors
        self.black = (0, 0, 0)
        self.white = (255, 255, 255)

        # Initialize the screen
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Grid Editor")

        # Matrix data
        self.data = [[0 for _ in range(self.cols)] for _ in range(self.rows)]  # 0 represents black

        # File to store matrix data
        self.file_name = "matrix.csv"

        # Running the application
        self.running = True
        self.dragging = False
        self.last_colored = set()  # To track which cells have changed color during the current drag
        self.main_loop()

    def main_loop(self):
        while self.running:
            self.handle_events()
            self.draw_grid()
            pygame.display.flip()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.dragging = True
                self.update_cell_color()
            elif event.type == pygame.MOUSEBUTTONUP:
                self.dragging = False
                self.last_colored.clear()  # Clear the cells tracked for the current drag
            elif event.type == pygame.MOUSEMOTION and self.dragging:
                self.update_cell_color()

    def update_cell_color(self):
        mouse_pos = pygame.mouse.get_pos()
        col = mouse_pos[0] // self.cell_size
        row = mouse_pos[1] // self.cell_size

        # Update cell color
        if 0 <= row < self.rows and 0 <= col < self.cols:
            cell = (row, col)
            if cell not in self.last_colored:  # Only update if cell hasn't been colored during this drag
                if self.data[row][col] == 0:
                    self.data[row][col] = 1
                else:
                    self.data[row][col] = 0
                self.last_colored.add(cell)

            # Write matrix data to CSV file
            self.write_to_csv()

    def draw_grid(self):
        self.screen.fill(self.black)
        for y in range(0, self.screen_height, self.cell_size):
            for x in range(0, self.screen_width, self.cell_size):
                rect = pygame.Rect(x, y, self.cell_size, self.cell_size)
                row = y // self.cell_size
                col = x // self.cell_size

                # Draw grid
                pygame.draw.rect(self.screen, self.white, rect, 1)

                # Fill cells based on matrix data
                if self.data[row][col] == 1:
                    pygame.draw.rect(self.screen, self.white, rect)

    def write_to_csv(self):
        with open(self.file_name, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(self.data)

grid_editor = GridEditor()
