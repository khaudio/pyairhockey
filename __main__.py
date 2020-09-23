#!/usr/bin/env python

import hockeypuck
import pygame
import math

# Simulated dimensions 170' x 96'

# Total screen size
screenWidth, screenHeight = 1920, 1080

# Maximum framerate
framesPerSecond = 60

def ratio_to_value(*ratios, bitDepth=8):
    maxValue = (2 ** bitDepth) - 1
    return tuple(int(ratio * maxValue) for ratio in ratios)

# RGB colors
colorBackground = ratio_to_value(1.0, 1.0, 1.0)
colorRed = ratio_to_value(1.0, 0, 0)
colorBlue = ratio_to_value(0, 0, 1.0)
colorLightBlue = ratio_to_value(.396, .62, 1.0)
colorDarkGrey = ratio_to_value(.22, .22, .22)

# Rink lines
lineWidth = 12
lineLeft = int(screenWidth * .35) - lineWidth
lineRight = int(screenWidth * .65)

# Solid center line
lineCenter = int((screenWidth * .5) - (lineWidth * .5))

# Goal Boxes
goalBoxSize = (int(.06 * screenWidth), int(.35 * screenHeight))
goalBoxTop = int((screenHeight * .5) - (goalBoxSize[1] / 2) - (lineWidth * .5))
goalBoxLeft = pygame.Rect(0, goalBoxTop, goalBoxSize[0], goalBoxSize[1])
goalBoxRight = pygame.Rect(int(screenWidth - goalBoxSize[0]), goalBoxTop, goalBoxSize[0], goalBoxSize[1])

# Global pygame init
pygame.init()
size = (screenWidth, screenHeight)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
pygame.display.set_caption("Gnop: Reckoning")
puck = hockeypuck.HockeyPuck(
        *(screenWidth * .025 for i in range(2)),
        screenWidth, screenHeight,
        colorBackground, colorDarkGrey
    )
puck.velocity = .0125, .004


def draw_lines():
    pygame.draw.line(screen, colorRed, [lineCenter, 0], [lineCenter, screenHeight], lineWidth)
    pygame.draw.line(screen, colorBlue, [lineLeft, 0], [lineLeft, screenHeight], lineWidth)
    pygame.draw.line(screen, colorBlue, [lineRight, 0], [lineRight, screenHeight], lineWidth)
    pygame.draw.rect(screen, colorLightBlue, goalBoxLeft)
    pygame.draw.rect(screen, colorLightBlue, goalBoxRight)


def main():
    allSprites = pygame.sprite.Group()
    allSprites.add(puck)

    while True:
        # Logic
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                break

        allSprites.update()

        # Game logic loop
        puck.step()

        # Screen Draws
        screen.fill(colorBackground)
        draw_lines()
        allSprites.draw(screen)

        # Update Screen
        pygame.display.flip()
        
        # 60 FPS
        clock.tick(framesPerSecond)

    pygame.quit()


if __name__ == '__main__':
    main()
