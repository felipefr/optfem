import sys
import numpy as np
sys.path.insert(0,'../src/femlib/')
from mesh import Mesh

class TestMesh:

    def setup_class(self):
        # inicializa qualquer coisa
        self.x = np.linspace(0,10)
        self.y = np.linspace(0,10)

    def test_should_create_mesh(self):
        mesh = Mesh()
        assert isinstance(mesh, Mesh)
        ...

