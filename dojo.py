import unittest

def transpor(m):
    t = len(m)
    m2 = []
    for i in range(0,t):
        m2.append([])
        for j in range(0,t):
            m2[i].append([])

    for i in range(0,t):
        for j in range(0,t):
            m2[j][i] = m[i][j]

    return m2

def produto_linha(linha):
    
    result = []
    ini = 0
    fim = 5
    
    while fim <= len(linha):
        lista_aux = linha[ini:fim]
        p = 1
        for i in lista_aux:
            p *= i
        result.append(p)
        ini +=1
        fim +=1
        
    maior = 0
    for i in result:
        if i > maior:
            maior = i
    return maior

def produto(m):
    maior_produto = 0
    for linha in m:
        prod_linha = produto_linha(linha)
        if prod_linha > maior_produto:
            maior_produto = prod_linha
    return maior_produto

def remove_linha(m):
    t = len(m)
    m2 = []
    for i in range(0,t-1):
        m2.append([])
        for j in range(0,t):
            m2[i].append([])

    for i in range(1,t):
        for j in range(0,t):
            m2[i-1][j] = m[i][j]
    return m2

def remove_coluna(m):
    t = len(m[0])
    m2 = []
    for i in range(0,t):
        m2.append([])
        for j in range(0,t-1):
            m2[i].append([])

    for i in range(0,t):
        for j in range(1,t):
            m2[i][j-1] = m[i][j]
    return m2

def prod_diagonal(m, size):
    maior_produto = 0
    ini = 0
    fim = 5
    while fim <= size:
        produto = 1
        for i in range(ini,fim):
            produto *= m[i][i]

        if maior_produto < produto:
            maior_produto = produto

        ini += 1
        fim += 1


            
    return maior_produto

def diagonal(m):
    
    total_diagonal = len(m) - 4
    size = len(m)
    maior_produto = prod_diagonal(m, size)

    ml = m
    mc = m

    for i in range(1,total_diagonal):
        ml = remove_linha(ml)
        produto = prod_diagonal(ml, size -i)
        if produto > maior_produto:
            maior_produto = produto

        mc = remove_coluna(mc)

        produto = prod_diagonal(mc, size -i)
        
        if produto > maior_produto:
            maior_produto = produto

    return maior_produto


def inverte(m):
    t = len(m)
    m2 = []
    for i in range(0,t):
        m2.append([])
        for j in range(0,t):
            m2[i].append([])
    
    for i in range(0,t):
        for j in range(0,t):
            m2[t-i-1][j] = m[i][j]
    return m2


def seq5(m):
    linhas = len(m)

    if linhas < 5:
        return -1
    
    for linha in m:
        if linhas != len(linha):
            return -1

    maior_produto = produto(m)
    m2 = transpor(m)
    maior_produto_coluna = produto(m2)
    maior_produto_diagonal_esquerda = diagonal(m)
    m3 = inverte(m)
    maior_produto_diagonal_direita = diagonal(m3)
    
    if maior_produto < maior_produto_coluna:
        maior_produto = maior_produto_coluna

    if maior_produto < maior_produto_diagonal_esquerda:
        maior_produto = maior_produto_diagonal_esquerda
        
    if maior_produto < maior_produto_diagonal_direita:
        maior_produto = maior_produto_diagonal_direita
    
    return maior_produto
    
class Seq5Test(unittest.TestCase):

    def test_maior_produto_linha_1(self):
        #5x5
        m = [
            [1,10,1,1,1],
            [1,1,2,1,1],
            [1,1,1,3,1],
            [1,1,1,1,4],
            [5,1,1,1,1]
            ]
        self.assertEqual(seq5(m), 10)

    def test_maior_produto_linha1_5_consecutivos(self):
        #6x6
        m = [
            [2,1,2,1,1,10],
            [1,1,1,1,1,1],
            [1,1,1,1,1,1],
            [1,1,1,1,1,1],
            [1,1,1,1,1,1],
            [1,1,1,1,1,1]
            ]
        self.assertEqual(seq5(m), 20)

    def test_maior_produto_linha2_5_consecutivos(self):
        #6x6
        m = [
            [2,1,2,1,1,1],
            [2,1,1,5,1,10],
            [1,1,1,1,1,1],
            [1,1,1,1,1,1],
            [1,1,1,1,1,1],
            [1,1,1,1,1,1]
            ]
        self.assertEqual(seq5(m), 50)

    def test_maior_produto_coluna1_5_consecutivos(self):
        #6x6
        m = [
            [2,1,2,1,1,1],
            [2,1,1,5,1,10],
            [1,1,1,1,1,10],
            [1,1,1,1,1,1],
            [1,1,1,1,1,1],
            [1,1,1,1,1,1]
            ]
        self.assertEqual(seq5(m), 100)         

    def test_menor_5(self):
        #4x4
        m = [
            [1,1,1,1],
            [1,1,1,1],
            [1,1,1,1],
            [1,1,1,1],
            ]
        self.assertEqual(seq5(m), -1)
    
    def test_maior_igual_5(self):
        #5x5
        m = [
            [1,1,1,1,1],
            [1,1,1,1,1],
            [1,1,1,1,1],
            [1,1,1,1,1],
            [1,1,1,1,1]
            ]
        self.assertEqual(seq5(m), 1)

    def test_verifica_matriz_nao_quadrada(self):
        m = [
            [1,1,1,1,1],
            [1,1,1,1,1],
            [1,1,1,1,1],
            [1,1,1,1,1],
            [1,1,1,1,1,1]
            ]
        self.assertEqual(seq5(m), -1)

        m = [
            [1,1,1,1,1],
            [1,1,1,1,1],
            [1,1,1,1,1],
            [1,1,1,1,1],
            [1,1,1,1,1],
            [1,1,1,1,1]
            ]
        self.assertEqual(seq5(m), -1)
    
    def test_verifica_matriz_quadrada(self):
        matriz_quadrada = [
            [1,1,1,1,1],
            [1,1,1,1,1],
            [1,1,1,1,1],
            [1,1,1,1,1],
            [1,1,1,1,1]
            ]
        self.assertEqual(seq5(matriz_quadrada), 1)

    def test_maior_produto_diagonal_esquerda1(self):
        #5x5
        m = [
            [2,1,1,1,1],
            [1,2,1,1,1],
            [1,1,2,1,1],
            [1,1,1,2,1],
            [1,1,1,1,2]
            ]
        self.assertEqual(seq5(m), 32)

    def test_maior_produto_diagonal_esquerda2(self):
        #6x6
        m = [
            [2,1,1,1,1,1],
            [1,2,1,1,1,1],
            [1,1,2,1,1,1],
            [1,1,1,2,1,1],
            [1,1,1,1,2,1],
            [1,1,1,2,1,3]
            ]
        self.assertEqual(seq5(m), 48)

    def test_maior_produto_diagonal_esquerda3(self):
        #6x6
        m = [
            [1,2,1,1,1,1],
            [1,1,2,1,1,1],
            [1,1,1,2,1,1],
            [1,1,1,1,2,1],
            [1,1,1,1,1,2],
            [1,1,1,1,1,1]
            ]
        self.assertEqual(seq5(m), 32)

    def test_maior_produto_diagonal_esquerda4(self):
        #6x6
        m = [
            [1,2,1,1,1,1],
            [3,1,2,1,1,1],
            [1,3,1,2,1,1],
            [1,1,3,1,2,1],
            [1,1,1,3,1,2],
            [1,1,1,1,3,1]
            ]
        self.assertEqual(seq5(m), 3**5)

    def test_maior_produto_diagonal_esquerda5(self):
        #7x7
        m = [
            [1,1,2,1,1,1,1],
            [1,1,1,2,1,1,1],
            [1,1,1,1,2,1,1],
            [1,1,1,1,1,2,1],
            [1,1,1,1,1,1,2],
            [1,1,1,1,1,1,1],
            [1,1,1,1,1,1,1]
            ]
        self.assertEqual(seq5(m), 2**5)

    def test_maior_produto_diagonal_esquerda6(self):
        #7x7
        m = [
            [1,1,2,1,1,1,1],
            [1,1,1,2,1,1,1],
            [3,1,1,1,2,1,1],
            [1,3,1,1,1,2,1],
            [1,1,3,1,1,1,2],
            [1,1,1,3,1,1,1],
            [1,1,1,1,3,1,1]
            ]
        self.assertEqual(seq5(m), 3**5)
        
    def test_maior_produto_diagonal_esquerda7(self):
        #8x8
        m = [
            [1,1,1,1,1,1,1,1],
            [1,1,1,1,1,1,1,1],
            [1,1,1,1,1,1,1,1],
            [1,1,2,1,1,1,1,1],
            [1,1,1,2,1,1,1,1],
            [1,1,1,1,2,1,1,1],
            [1,1,1,1,1,2,1,1],
            [1,1,1,1,1,1,2,1]
            ]
        self.assertEqual(seq5(m), 2**5)

    def test_maior_produto_diagonal_direita1(self):
        #5x5
        m = [
            [1,1,1,1,2],
            [1,1,1,2,1],
            [1,1,2,1,1],
            [1,2,1,1,1],
            [2,1,1,1,1]
            ]
        self.assertEqual(seq5(m), 2**5)
        
    def test_maior_produto_diagonal_direita2(self):
        #6x6
        m = [
            [1,1,1,1,1,1],
            [1,1,1,1,2,1],
            [1,1,1,2,1,1],
            [1,1,2,1,1,1],
            [1,2,1,1,1,1],
            [2,1,1,1,1,1]
            ]
        self.assertEqual(seq5(m), 2**5)

    def test_maior_produto_diagonal_direita3(self):
        #6x6
        m = [
            [1,1,1,1,2,1],
            [1,1,1,2,1,1],
            [1,1,2,1,1,1],
            [1,2,1,1,1,1],
            [2,1,1,1,1,1],
            [1,1,1,1,1,1]
            ]
        self.assertEqual(seq5(m), 2**5)
        
    def test_maior_produto_diagonal_direita4(self):
        #6x6
        m = [
            [1,1,1,1,1,1],
            [1,1,1,1,1,2],
            [1,1,1,1,2,1],
            [1,1,1,2,1,1],
            [1,1,2,1,1,1],
            [1,2,1,1,1,1]
            ]
        self.assertEqual(seq5(m), 2**5)

    def test_maior_produto_diagonal_direita5(self):
        #7x7
        m = [
            [1,1,1,1,1,1,1],
            [1,1,1,1,1,1,1],
            [1,1,1,1,1,1,2],
            [1,1,1,1,1,2,1],
            [1,1,1,1,2,1,1],
            [1,1,1,2,1,1,1],
            [1,1,2,1,1,1,1],
            ]
        self.assertEqual(seq5(m), 2**5)
        
    def test_maior_produto_diagonal_direita6(self):
        #7x7
        m = [
            [1,1,1,1,1,2,1],
            [1,1,1,1,2,1,1],
            [1,1,1,2,1,1,1],
            [1,1,2,1,1,1,1],
            [1,2,1,1,1,1,1],
            [1,1,1,1,1,1,1],
            [1,1,1,1,1,1,1],
            ]
        self.assertEqual(seq5(m), 2**5)

    def test_maior_produto_diagonal_direita6(self):
        #8x8
        m = [
            [1,1,1,1,1,1,1,1],
            [1,1,1,1,1,1,1,1],
            [1,1,1,1,1,1,1,1],
            [1,1,1,1,1,1,2,1],
            [1,1,1,1,1,2,1,1],
            [1,1,1,1,2,1,1,1],
            [1,1,1,2,1,1,1,1],
            [1,1,2,1,1,1,1,1]
            ]
        self.assertEqual(seq5(m), 2**5)
        
if __name__ == '__main__':
    unittest.main()
