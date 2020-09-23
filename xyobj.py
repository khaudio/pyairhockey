#!/usr/bin/env python

class XYObj:
    def __init__(self):
        self.xPosition = 0.0
        self.yPosition = 0.0
        self.xMinimum = -1.0
        self.xMaximum = 1.0
        self.yMinimum = -1.0
        self.yMaximum = 1.0

    @property
    def position(self):
        return self.xPosition, self.yPosition

    @position.setter
    def position(self, val):
        if len(val) != 2:
            raise IndexError('Both X and Y are required')
        if not xMinimum <= val[0] <= xMaximum:
            raise ValueError(f'Valid range is {xMinimum} - {xMaximum}')
        if not yMinimum <= val[1] <= yMaximum:
            raise ValueError(f'Valid range is {yMinimum} - {yMaximum}')
        self.xPosition = val[0]
        self.yPosition = val[1]

class MovingXYObj(XYObj):
    def __init__(self):
        super().__init__()
        self.xVelocity = 0.0
        self.yVelocity = 0.0
        self.xAccel = 0.0
        self.yAccel = 0.0
        self.xLength = 0.0
        self.yLength = 0.0

    @property
    def velocity(self):
        return self.xVelocity, self._yVelocity

    @velocity.setter
    def velocity(self, val):
        if len(val) != 2:
            raise IndexError('Both X and Y are required')
        for v in val:
            if not -1.0 <= v <= 1.0:
                raise ValueError('Valid range is -1.0 - 1.0')
        self.xVelocity = val[0]
        self.yVelocity = val[1]

    @property
    def accel(self):
        return self.xAccel, self.yAccel

    @accel.setter
    def accel(self, val):
        if len(val) != 2:
            raise IndexError('Both X and Y are required')
        for v in val:
            if not -1.0 <= v <= 1.0:
                raise ValueError('Valid range is -1.0 - 1.0')
        self.xAccel = val[0]
        self.yAccel = val[1]

    def _step(self):
        self.xPosition += self.xVelocity
        self.yPosition += self.yVelocity
        bounceX = (self.xPosition >= (self.xMaximum - self.xLength)) or (self.xPosition <= self.xMinimum)
        bounceY = (self.yPosition >= (self.yMaximum - self.yLength)) or (self.yPosition <= self.yMinimum)
        self.xVelocity = self.xVelocity * (-1 if bounceX else 1)
        self.yVelocity = self.yVelocity * (-1 if bounceY else 1)
        self.xPosition += self.xVelocity if bounceX else 0
        self.yPosition += self.yVelocity if bounceY else 0
