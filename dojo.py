import unittest

def transposicao(m):
    t = len(m)
    m2 = []
    for i in range(0,t):
        m2.setdefault(i,[])
        
    for i in range(0,t):
        for j in range(0,t):
            m2[j].append(m[i][j])
    return m2

def produto_linha(linha):
    
    result = []
    ini = 0
    fim = 4
    
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

def seq5(m):
    linhas = len(m)

    if linhas < 5:
        return -1
    
    for linha in m:
        if linhas != len(linha):
            return -1

    maior_produto = 0
    for linha in m:
        prod_linha = produto_linha(linha)
        if prod_linha > maior_produto:
            maior_produto = prod_linha

#    for linha in transposicao(m):
#        prod_linha = produto_linha(linha)
#        if prod_linha > maior_produto:
#            maior_produto = prod_linha
            
    return maior_produto
    
class Seq5Test(unittest.TestCase):

    def test_maior_produto_linha_1(self):
        m = [
            [1,10,1,1,1],
            [1,1,2,1,1],
            [1,1,1,3,1],
            [1,1,1,1,4],
            [5,1,1,1,1]
            ]
        self.assertEquals(seq5(m), 10)

    def test_maior_produto_linha1_5_consecutivos(self):
        m = [
            [2,1,2,1,1,10],
            [1,1,1,1,1,1],
            [1,1,1,1,1,1],
            [1,1,1,1,1,1],
            [1,1,1,1,1,1],
            [1,1,1,1,1,1]
            ]
        self.assertEquals(seq5(m), 20)

    def test_maior_produto_linha2_5_consecutivos(self):
        m = [
            [2,1,2,1,1,1],
            [2,1,1,5,1,10],
            [1,1,1,1,1,1],
            [1,1,1,1,1,1],
            [1,1,1,1,1,1],
            [1,1,1,1,1,1]
            ]
        self.assertEquals(seq5(m), 50)

#    def test_maior_produto_coluna1_5_consecutivos(self):
#        m = [
#            [2,1,2,1,1,1],
#            [2,1,1,5,1,10],
#            [1,1,1,1,1,10],
#            [1,1,1,1,1,1],
#            [1,1,1,1,1,1],
#            [1,1,1,1,1,1]
#            ]
#        self.assertEquals(seq5(m), 100)         

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

        m = [
            [1,1,1,1,1],
            [1,1,1,1,1],
            [1,1,1,1,1],
            [1,1,1,1,1],
            [1,1,1,1,1],
            [1,1,1,1,1]
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
