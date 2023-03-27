#!/usr/bin/python3


class Math:
    @staticmethod
    def unitToAngle(unit):
        if unit > 1000 or unit < 0:
            raise Exception("Invalid input unit")
        return float((unit * 360) / 1000)

    @staticmethod
    def angleToUnit(angle):
        angle = angle % 360
        return int((angle * 1000) / 360)
