from ModuloEstatico import ModuloEstatico
from Sensor import Sensor
from Robot import Robot
from ModuloRotacion import ModuloRotacion
from ModuloTraslacion import ModuloTraslacion
from ModuloHelicoidal import ModuloHelicoidal
from MotorRotacion import MotorRotacion
from MotorTraslacion import MotorTraslacion

s = Sensor(4, "Color")
mr = MotorRotacion(3)
mt = MotorTraslacion(5)
mrr = MotorRotacion(8)
mtt = MotorTraslacion(9)

robot = Robot([])
modulo = ModuloEstatico(1, 50, 59, 50, robot, [s])
moduloRot = ModuloRotacion(2, 50, 50, 50, robot, mr)
moduloHelicoidal = ModuloHelicoidal(10, 50, 50, 50, robot, [mrr, mtt])
robot.modulos = [modulo, moduloRot, moduloHelicoidal]
robot.modulos[1].mover()
robot.modulos[0].captar_informacion()

print(robot)