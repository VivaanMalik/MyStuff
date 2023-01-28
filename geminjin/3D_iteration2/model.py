import numpy as np

class Triangle():
    def __init__(self, app):
        self.Application = app
        self.Context = app.Context
        self.VertexBufferObject = self.GetVertexBufferObject()
        self.Shader = self.GetShader("default")
        self.VertexArrayObject = self.GetVertexArrayObject()
    
    def GetVertexArrayObject(self):
        vao = self.Context.vertex_array(self.Shader, [(self.VertexBufferObject, '3f', 'in_position')])
        return vao
    
    def GetVertexData(self):
        VertexData = [(-0.6, -0.8, 0.0), (0.6, -0.8, 0.0), (0.0, 0.8, 0.0)]
        VertexData = np.array(VertexData, dtype="float32")
        return VertexData
    
    def GetVertexBufferObject(self):
        VertexData = self.GetVertexData()
        VertexBufferObject = self.Context.buffer(VertexData)
        return VertexBufferObject
    
    def GetShader(self, name):
        with open(f'shaders\\{name}.vert') as file:
            v_shader = file.read()
        with open(f'shaders\\{name}.frag') as file:
            f_shader = file.read()
        prog = self.Context.program(vertex_shader=v_shader, fragment_shader=f_shader)
        return prog

    def Render(self):
        self.VertexArrayObject.render()
    
    def Destroy(self):
        self.VertexBufferObject.release()
        self.Shader.release()
        self.VertexArrayObject.release()