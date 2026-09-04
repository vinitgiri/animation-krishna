import pygame
import random
import math

pygame.init()
pygame.mixer.init()

# =========================
# WINDOW SETTINGS
# =========================

WIDTH = 510
HEIGHT = 830
FPS = 60

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Krishna Particle Animation")

clock = pygame.time.Clock()


# =========================
# MUSIC SETTINGS
# =========================

MUSIC_FILE = "song.mp3"

# Initially MUTED
music_on = False
music_started = False

try:
    pygame.mixer.music.load(MUSIC_FILE)
    pygame.mixer.music.set_volume(0.6)

    # IMPORTANT:
    # Music does NOT start automatically.
    # User must click the speaker icon.
    print("Music loaded successfully.")

except pygame.error as e:
    print("Could not load music:", e)


# =========================
# LOAD KRISHNA IMAGE
# =========================

try:
    image = pygame.image.load(
        "krishna.png"
    ).convert_alpha()

except pygame.error as e:
    print("Could not load krishna.png:", e)
    pygame.quit()
    raise SystemExit


max_width = 400
max_height = 650

img_w, img_h = image.get_size()

scale = min(
    max_width / img_w,
    max_height / img_h
)

new_w = int(img_w * scale)
new_h = int(img_h * scale)

image = pygame.transform.smoothscale(
    image,
    (new_w, new_h)
)

offset_x = (WIDTH - new_w) // 2
offset_y = (HEIGHT - new_h) // 2


# =========================
# NAME SETTINGS
# =========================

NAME = "Vinit Kumar Giri"

name_font = pygame.font.Font(
    None,
    42
)

name_y = offset_y + new_h + 20


# =========================
# PREMIUM MUTE / UNMUTE ICON
# =========================

def draw_speaker_icon(surface, center, muted):
    cx, cy = center
    radius = 30

    # --------------------------------
    # SOFT GOLDEN GLOW
    # --------------------------------
    for glow_radius in range(radius + 14, radius, -2):
        alpha = int(3 * (radius + 14 - glow_radius))
        glow = pygame.Surface(
            (glow_radius * 2 + 4, glow_radius * 2 + 4),
            pygame.SRCALPHA
        )
        pygame.draw.circle(
            glow,
            (255, 210, 110, alpha),
            (glow_radius + 2, glow_radius + 2),
            glow_radius
        )
        surface.blit(
            glow,
            (cx - glow_radius - 2, cy - glow_radius - 2)
        )

    # --------------------------------
    # OUTER GLASS CIRCLE — SAME SIZE
    # --------------------------------
    pygame.draw.circle(
        surface,
        (10, 10, 18),
        (cx, cy),
        radius
    )

    pygame.draw.circle(
        surface,
        (25, 25, 38),
        (cx, cy),
        radius - 2
    )

    pygame.draw.circle(
        surface,
        (235, 200, 120),
        (cx, cy),
        radius,
        2
    )

    # --------------------------------
    # SMALL INNER SPEAKER
    # --------------------------------
    speaker_color = (248, 248, 250)

    # Smaller speaker body
    speaker_points = [
        (cx - 12, cy - 5),
        (cx - 5, cy - 5),
        (cx + 5, cy - 11),
        (cx + 5, cy + 11),
        (cx - 5, cy + 5),
        (cx - 12, cy + 5)
    ]

    pygame.draw.polygon(
        surface,
        speaker_color,
        speaker_points
    )

    pygame.draw.rect(
        surface,
        speaker_color,
        (cx - 14, cy - 5, 6, 10),
        border_radius=2
    )

    # --------------------------------
    # SOUND WAVES — SMALLER
    # --------------------------------
    if not muted:

        # Small wave
        pygame.draw.arc(
            surface,
            (255, 255, 255),
            (cx + 1, cy - 7, 10, 14),
            -math.pi / 2,
            math.pi / 2,
            2
        )

        # Medium wave
        pygame.draw.arc(
            surface,
            (255, 255, 255),
            (cx + 1, cy - 11, 16, 22),
            -math.pi / 2,
            math.pi / 2,
            2
        )

        # Outer wave
        pygame.draw.arc(
            surface,
            (255, 255, 255),
            (cx + 1, cy - 15, 22, 30),
            -math.pi / 2,
            math.pi / 2,
            2
        )

    # --------------------------------
    # MUTED — SMALLER SLASH
    # --------------------------------
    else:

        pygame.draw.line(
            surface,
            (5, 5, 10),
            (cx - 16, cy - 16),
            (cx + 16, cy + 16),
            6
        )

        pygame.draw.line(
            surface,
            (255, 105, 105),
            (cx - 15, cy - 15),
            (cx + 15, cy + 15),
            3
        )

        pygame.draw.line(
            surface,
            (255, 225, 225),
            (cx - 14, cy - 14),
            (cx + 14, cy + 14),
            1
        )


# =========================
# MUSIC BUTTON SETTINGS
# =========================

BUTTON_RADIUS = 30

button_center_x = WIDTH - 42
button_center_y = HEIGHT - 42

music_button_center = (button_center_x, button_center_y)

music_button_rect = pygame.Rect(
    button_center_x - BUTTON_RADIUS,
    button_center_y - BUTTON_RADIUS,
    BUTTON_RADIUS * 2,
    BUTTON_RADIUS * 2
)


# =========================
# CREATE IMAGE PARTICLES
# =========================

particles = []

particle_gap = 5

for y in range(
    0,
    new_h,
    particle_gap
):

    for x in range(
        0,
        new_w,
        particle_gap
    ):

        color = image.get_at(
            (x, y)
        )

        if color.a > 40 and (
            color.r > 30 or
            color.g > 30 or
            color.b > 30
        ):

            target_x = offset_x + x
            target_y = offset_y + y

            # Random starting position
            start_x = (
                WIDTH // 2 +
                random.randint(
                    -250,
                    250
                )
            )

            start_y = (
                HEIGHT // 2 +
                random.randint(
                    -350,
                    350
                )
            )

            particles.append({

                "x": float(start_x),
                "y": float(start_y),

                "target_x": target_x,
                "target_y": target_y,

                "r": color.r,
                "g": color.g,
                "b": color.b,

                # Particles slowly start
                "delay": random.uniform(
                    0,
                    55
                ),

                "size": random.randint(
                    1,
                    3
                ),

                # Slow movement
                "speed": random.uniform(
                    0.002,
                    0.006
                ),

                "angle": random.uniform(
                    0,
                    math.pi * 2
                )
            })


# =========================
# ANIMATION VARIABLES
# =========================

time_passed = 0.0

running = True

glow_particles = []


# =========================
# MAIN LOOP
# =========================

while running:

    dt = clock.tick(FPS) / 1000.0

    time_passed += dt


    # =========================
    # BACKGROUND
    # =========================

    screen.fill(
        (5, 5, 12)
    )


    # =========================
    # IMAGE PARTICLES
    # =========================

    for p in particles:

        # Wait for particle delay
        if time_passed < p["delay"]:
            continue


        # Direction towards target
        dx = (
            p["target_x"] -
            p["x"]
        )

        dy = (
            p["target_y"] -
            p["y"]
        )


        # Slowly move particle
        p["x"] += (
            dx *
            p["speed"]
        )

        p["y"] += (
            dy *
            p["speed"]
        )


        # Small floating movement
        wave_x = math.sin(
            time_passed * 3 +
            p["angle"]
        ) * 0.8

        wave_y = math.cos(
            time_passed * 3 +
            p["angle"]
        ) * 0.8


        draw_x = int(
            p["x"] +
            wave_x
        )

        draw_y = int(
            p["y"] +
            wave_y
        )


        # Distance from final position
        distance = math.sqrt(
            dx * dx +
            dy * dy
        )


        # =========================
        # PARTICLE GLOW
        # =========================

        if distance < 30:

            glow_size = (
                p["size"] * 5
            )

            glow_surface = pygame.Surface(
                (
                    glow_size * 2,
                    glow_size * 2
                ),
                pygame.SRCALPHA
            )

            pygame.draw.circle(

                glow_surface,

                (
                    p["r"],
                    p["g"],
                    p["b"],
                    40
                ),

                (
                    glow_size,
                    glow_size
                ),

                glow_size
            )

            screen.blit(

                glow_surface,

                (
                    draw_x -
                    glow_size,

                    draw_y -
                    glow_size
                )
            )


        # =========================
        # MAIN PARTICLE
        # =========================

        pygame.draw.circle(

            screen,

            (
                p["r"],
                p["g"],
                p["b"]
            ),

            (
                draw_x,
                draw_y
            ),

            p["size"]
        )


    # =========================
    # EXTRA SPARKLES
    # =========================

    if time_passed > 5:

        if random.random() < 0.15:

            glow_particles.append({

                "x": random.randint(
                    offset_x,
                    offset_x + new_w
                ),

                "y": random.randint(
                    offset_y,
                    offset_y + new_h
                ),

                "life": random.uniform(
                    0.5,
                    1.5
                ),

                "max_life": 1.5,

                "size": random.randint(
                    1,
                    3
                )
            })


    # =========================
    # DRAW SPARKLES
    # =========================

    for g in glow_particles[:]:

        g["life"] -= dt


        if g["life"] <= 0:

            glow_particles.remove(g)

            continue


        alpha = int(

            255 *

            (
                g["life"] /
                g["max_life"]
            )
        )


        glow = pygame.Surface(
            (20, 20),
            pygame.SRCALPHA
        )


        pygame.draw.circle(

            glow,

            (
                255,
                255,
                255
            ),

            (
                10,
                10
            ),

            g["size"]
        )


        glow.set_alpha(
            alpha
        )


        screen.blit(

            glow,

            (
                g["x"] - 10,
                g["y"] - 10
            )
        )


    # =========================
    # FINAL IMAGE REVEAL
    # =========================

    if time_passed > 55:

        alpha = min(

            255,

            int(
                (
                    time_passed -
                    55
                ) * 51
            )
        )


        final_image = image.copy()

        final_image.set_alpha(
            alpha
        )


        screen.blit(

            final_image,

            (
                offset_x,
                offset_y
            )
        )


    # =========================
    # NAME ANIMATION
    # =========================

    name_start_time = 55.5


    if time_passed > name_start_time:

        name_progress = min(
            1.0,
            (
                time_passed -
                name_start_time
            ) / 2.0
        )


        # Smooth fade-in
        name_alpha = int(

            255 *

            (
                1 -
                math.cos(
                    name_progress *
                    math.pi
                )
            ) / 2
        )


        # Floating effect
        floating_y = math.sin(
            time_passed * 2
        ) * 3


        # Main name
        name_surface = (
            name_font.render(
                NAME,
                True,
                (
                    255,
                    215,
                    100
                )
            )
        )


        name_surface.set_alpha(
            name_alpha
        )


        # Center name
        name_x = (

            WIDTH -
            name_surface.get_width()

        ) // 2


        # =========================
        # NAME GLOW
        # =========================

        glow_surface = pygame.Surface(

            (
                name_surface.get_width()
                + 40,

                name_surface.get_height()
                + 40
            ),

            pygame.SRCALPHA
        )


        glow_text = name_font.render(

            NAME,

            True,

            (
                255,
                200,
                80
            )
        )


        glow_text.set_alpha(

            int(
                name_alpha *
                0.35
            )
        )


        for glow_offset in range(
            8,
            0,
            -2
        ):

            glow_surface.blit(

                glow_text,

                (
                    20 -
                    glow_offset // 2,

                    20 -
                    glow_offset // 2
                )
            )


        screen.blit(

            glow_surface,

            (
                name_x - 20,

                int(
                    name_y +
                    floating_y
                ) - 20
            )
        )


        # =========================
        # DRAW NAME
        # =========================

        screen.blit(

            name_surface,

            (
                name_x,

                int(
                    name_y +
                    floating_y
                )
            )
        )


    # =========================
    # DRAW MUSIC ICON
    # =========================

    draw_speaker_icon(

        screen,

        music_button_center,

        not music_on
    )


    # =========================
    # EVENTS
    # =========================

    for event in pygame.event.get():

        # -------------------------
        # CLOSE WINDOW
        # -------------------------

        if event.type == pygame.QUIT:

            running = False


        # -------------------------
        # MOUSE CLICK
        # -------------------------

        if event.type == pygame.MOUSEBUTTONDOWN:

            mouse_pos = event.pos


            # Check speaker button
            if music_button_rect.collidepoint(
                mouse_pos
            ):

                # =====================
                # TURN MUSIC ON
                # =====================

                if not music_on:

                    try:

                        pygame.mixer.music.play(
                            -1
                        )

                        music_on = True

                    except pygame.error:

                        print(
                            "Unable to play music."
                        )


                # =====================
                # TURN MUSIC OFF
                # =====================

                else:

                    pygame.mixer.music.pause()

                    music_on = False


    # =========================
    # UPDATE DISPLAY
    # =========================

    pygame.display.flip()


# =========================
# EXIT
# =========================

pygame.mixer.music.stop()

pygame.quit()