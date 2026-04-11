import turtle
import math
from colorspace import rainbow_hcl

t = turtle.Turtle()
t.speed(0)
t.pensize(50)


screen = turtle.Screen()
screen.bgcolor("#000066")
screen.tracer(0, 0)

# Create a full-spectrum HCL rainbow palette (256 shades)
palette = rainbow_hcl(c=250, l=50)
color_range = palette.colors(256)

def draw_shape():
    x_start = -200
    x_end = 200
    frequency = 40
    amplitude = 50

    t.penup()
    t.goto(x_start, math.sin(x_start / frequency) * amplitude)
    t.pendown()

    for x in range(x_start, x_end + 1):
        y = math.sin(x / frequency) * amplitude
        color_index = int((x - x_start) / (x_end - x_start) * (len(color_range) - 1))
        t.pencolor(color_range[color_index])
        t.goto(x, y)

    screen.update()
def random_safe_position(bounds):

def random_safe_position(bounds):
    min_x, max_x, min_y, max_y = bounds
    half_width = screen.window_width() / 2 - PADDING
    half_height = screen.window_height() / 2 - PADDING

    x_min = int(-half_width - min_x)
    x_max = int(half_width - max_x)
    y_min = int(-half_height - min_y)
    y_max = int(half_height - max_y)

    if x_min > x_max or y_min > y_max:
        return 0, 0

    return random.randint(x_min, x_max), random.randint(y_min, y_max)


def random_edge_biased_position(bounds, sample_count=12):
    best = random_safe_position(bounds)
    best_score = best[0] * best[0] + best[1] * best[1]

    for _ in range(sample_count - 1):
        candidate = random_safe_position(bounds)
        candidate_score = candidate[0] * candidate[0] + candidate[1] * candidate[1]
        if candidate_score > best_score:
            best = candidate
            best_score = candidate_score

    return best


def random_spaced_position(existing_positions, min_spacing, position_picker, attempts=SPAWN_ATTEMPTS):
    min_distance_sq = min_spacing * min_spacing

    for _ in range(attempts):
        candidate = position_picker()
        if all((candidate[0] - pos[0]) ** 2 + (candidate[1] - pos[1]) ** 2 >= min_distance_sq for pos in existing_positions):
            return candidate

    return position_picker()


class PatternDrawer:
    def __init__(self, scale, start_position):
        self.scale = scale
        self.outer_index = 0
        self.inner_index = 0
        self.done = False
        self.origin = start_position

        self.t = turtle.Turtle()
        self.t.hideturtle()
        self.t.speed(0)
        self.t.width(1)
        self.t.penup()
        self.t.goto(*start_position)
        self.t.pendown()

    def step(self):
        if self.done:
            return

        self.t.color(colors[(self.outer_index // 5) % len(colors)])
        self.t.left(90)
        self.t.forward(50 * self.scale)
        self.t.right(30)
        self.t.forward(40 * self.scale)
        self.t.right(30)
        self.t.forward(50 * self.scale)
        self.t.left(42)

        self.inner_index += 1
        if self.inner_index >= INNER_REPEATS:
            self.inner_index = 0
            self.t.forward(7 * self.scale)
            self.t.left(6)
            self.outer_index += 1

            if self.outer_index >= OUTER_REPEATS:
                self.done = True
                self.t.hideturtle()


scale = pick_scale_to_fit()
bounds = calculate_pattern_bounds(scale)

active_patterns = []
running = True
startup_spawns_remaining = ACTIVE_PATTERNS


def spawn_pattern():
    global startup_spawns_remaining

    existing_positions = [pattern.origin for pattern in active_patterns]
    if startup_spawns_remaining > 0:
        start_position = random_spaced_position(
            existing_positions,
            MIN_PATTERN_SPACING,
            lambda: random_edge_biased_position(bounds),
        )
        startup_spawns_remaining -= 1
    else:
        start_position = random_spaced_position(
            existing_positions,
            MIN_PATTERN_SPACING,
            lambda: random_safe_position(bounds),
        )

    active_patterns.append(PatternDrawer(scale, start_position))



draw_shape()
turtle.done()