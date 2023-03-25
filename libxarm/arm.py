#!/usr/bin/python3

import xarm


class Arm:
    def __init__(self):
        self.arm = xarm.Controller('USB')

    def __repr__(self):
        return f"libxarm.Arm({', '.join([str(i) for i in self.getAllServoPosition()])})"

    def getServoPosition(self, servo):
        return self.arm.getPosition(servo)

    def getAllServoPosition(self):
        pos = []
        for servo in range(1, 6 + 1):
            pos.append(self.getServoPosition(servo))
        return pos

    def moveServoByIncrement(self, servo, increment):
        pos = self.getServoPosition(servo)
        newPos = pos + increment
        if newPos > 1000:
            newPos = 1000
        elif newPos < 0:
            newPos = 0
        self.moveServoTo(servo, newPos)

    def moveServoTo(self, servo, position, speedMs=1000):
        self.arm.setPosition(servo, position, speedMs)

    def moveServoToDefault(self, servo):
        self.moveServoTo(servo, 500)

    def moveAllServoToDefault(self):
        for servo in range(1, 6 + 1):
            self.moveServoToDefault(servo)

    def turnOff(self):
        for servo in range(1, 6 + 1):
            self.arm.servoOff(servo)
