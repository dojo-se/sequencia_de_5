import unittest

def seq5(m):
    linhas = len(m)

    if (linhas < 5):
        return -1
    
    for linha in m:
        if ((linhas != len(linha)) or linha < 5):
            return -1
    return 1
    
class Seq5Test(unittest.TestCase):

    def test_menor_5(self):
        m = [
            [1,1,1,1],
            [1,1,1,1],
            [1,1,1,1],
            [1,1,1,1],
            ]
        self.assertEquals(seq5(m), -1)
    
    def test_maior_igual_5(self):
        m = [
            [1,1,1,1,1],
            [1,1,1,1,1],
            [1,1,1,1,1],
            [1,1,1,1,1],
            [1,1,1,1,1]
            ]
        self.assertEquals(seq5(m), 1)

    def test_verifica_matriz_nao_quadrada(self):
        m = [
            [1,1,1,1,1],
            [1,1,1,1,1],
            [1,1,1,1,1],
            [1,1,1,1,1],
            [1,1,1,1,1,1]
            ]
        self.assertEquals(seq5(m), -1)
    
    def test_verifica_matriz_quadrada(self):
        matriz_quadrada = [
            [1,1,1,1,1],
            [1,1,1,1,1],
            [1,1,1,1,1],
            [1,1,1,1,1],
            [1,1,1,1,1]
            ]
        self.assertEquals(seq5(matriz_quadrada), 1)
        
        
if __name__ == '__main__':
    unittest.main()
