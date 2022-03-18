import render
import window
from classes import *


imgres=Vector2(500, 500)
sensorsize=Vector2(0.03, 0.03)

window.readyup(500, imgres.x, imgres.y, "RENDER")

Cube=render.ObjectCube()
roty=90

window.Dotz(render.render(Cube.verts, Crot=Vector3(roty/2, roty, 0), sensorsize=sensorsize))
light=render.LightSource(150, Vector3(0, 0, 0))

while True:
    roty+=0.1
    dots=render.render(Cube.verts, Crot=Vector3(roty/2, roty, 0), sensorsize=sensorsize)
    data=window.Dotz(dots)
    #window.Linez(data, Cube.edges)
    window.Ngonz(data, Cube.faces, light)
    window.checkquit()