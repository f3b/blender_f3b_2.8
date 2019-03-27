
class Vertex ():
    def __init__(self):
        self.p = None
        self.n = None
        self.c = None
        self.tg = None
        self.tx = None
        self.i = None
        self.from_vertex = None
        self.from_loop = None
        
    

class Skin ():
    def __init__(self):
        self.boneCount = []
        self.boneIndex = []
        self.boneWeight = []
        
    

class Mesh ():
    def __init__(self):
        self.verts = []
        self.indexes = []
        self.skin = Skin()
        self.has_skin = False
        
    