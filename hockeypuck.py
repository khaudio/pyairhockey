#!/usr/bin/env python

import pygame
import random
import xyobj

class HockeyPuck(xyobj.MovingXYObj, pygame.sprite.Sprite):
    def __init__(self, width, height, maxAbsX, maxAbsY, bgColor, objColor):
        super().__init__()
        pygame.sprite.Sprite.__init__(self)
        self.maximumAbsX = maxAbsX
        self.maximumAbsY = maxAbsY
        self.halfAbsX = self.maximumAbsX // 2
        self.halfAbsY = self.maximumAbsY // 2
        self.xLength = width * 2 / maxAbsX
        self.yLength = height * 2 / maxAbsY
        self.image = pygame.Surface([width, height])
        self.background = bgColor
        self.color = objColor
        pygame.draw.rect(self.image, self.color, [0, 0, width, height])
        self.rect = self.image.get_rect()

    @property
    def background(self):
        return self._bgColor

    @background.setter
    def background(self, bgColor):
        self._bgColor = bgColor
        self.image.fill(bgColor)
        self.image.set_colorkey(bgColor)

    def step(self):
        super()._step()
        self.rect.x = ((self.xPosition * .5) * self.maximumAbsX) + self.halfAbsX
        self.rect.y = ((self.yPosition * .5) * self.maximumAbsY) + self.halfAbsY
