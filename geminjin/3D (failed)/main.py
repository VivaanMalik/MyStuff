import render
import window
from classes import *

demo=0

imgres=Vector2(500, 500)
depth=500
sensorsize=Vector2(0.03, 0.03)

if demo==0:
    window.readyup(500, imgres.x, imgres.y, "RENDER")
    Cube=render.ObjectCube()
    roty=90

    window.Dotz(render.render(Cube.verts, Crot=
    Vector3(roty/2, roty, 0), sensorsize=sensorsize))
    light=render.LightSource(200, Vector3(-5, 0, 5), imgres, depth)
    while True:
        roty+=0.1
        dots=render.render(Cube.verts, Crot=Vector3(roty/2, roty, 0), sensorsize=sensorsize)
        data=window.Dotz(dots)
        #window.Linez(data, Cube.edges)
        window.Ngonz(data, Cube.faces, light)
        window.checkquit()

elif demo==1:
    ball=render.ExternalObject("Ball OBJ")
    window.readyup(1, imgres.x, imgres.y, "RENDER")
    light=render.LightSource(150, Vector3(0, 0, 0), imgres, depth)
    while True:
        dots=render.render(ball.verts, Crot=Vector3(0, 0, 0), sensorsize=sensorsize)
        data=window.Dotz(dots)
        window.Ngonz(data, ball.faces, light)
        window.checkquit()