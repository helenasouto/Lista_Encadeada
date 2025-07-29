class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None


class ListaEncadeada:
    def __init__(self):
        self.cabeca = None
        self.tamanho = 0

    def esta_vazia(self):
        return self.tamanho == 0

    def obter_tamanho(self):
        return self.tamanho

    def obter_elemento(self, posicao):
        if posicao < 1 or posicao > self.tamanho:
            raise IndexError("Posição inválida.")
        
        atual = self.cabeca
        for _ in range(posicao - 1):
            atual = atual.proximo
        return atual.valor

    def modificar_elemento(self, posicao, valor):
        if posicao < 1 or posicao > self.tamanho:
            raise IndexError("Posição inválida.")
        
        atual = self.cabeca
        for _ in range(posicao - 1):
            atual = atual.proximo
        atual.valor = valor

    def inserir(self, posicao, valor):
        if posicao < 1 or posicao > self.tamanho + 1:
            raise IndexError("Posição inválida.")
        
        novo_no = No(valor)
        
        if posicao == 1:
            novo_no.proximo = self.cabeca
            self.cabeca = novo_no
        else:
            anterior = self.cabeca
            for _ in range(posicao - 2):
                anterior = anterior.proximo
            novo_no.proximo = anterior.proximo
            anterior.proximo = novo_no
            
        self.tamanho += 1

    def remover(self, posicao):
        if self.esta_vazia():
            raise ValueError("Lista vazia.")
        if posicao < 1 or posicao > self.tamanho:
            raise IndexError("Posição inválida.")
        
        if posicao == 1:
            removido = self.cabeca.valor
            self.cabeca = self.cabeca.proximo
        else:
            anterior = self.cabeca
            for _ in range(posicao - 2):
                anterior = anterior.proximo
            removido = anterior.proximo.valor
            anterior.proximo = anterior.proximo.proximo
            
        self.tamanho -= 1
        return removido

    def imprimir(self):
        atual = self.cabeca
        elementos = []
        while atual is not None:
            elementos.append(str(atual.valor))
            atual = atual.proximo
        print("Lista:", " -> ".join(elementos))


# Casos de teste incorporados
def testar_lista_encadeada():
    print("\n=== INICIANDO TESTES DA LISTA ENCADEADA ===")
    
    lista = ListaEncadeada()
    
    # Teste 1: Lista vazia
    assert lista.esta_vazia(), "A lista deveria estar vazia"
    assert lista.obter_tamanho() == 0, "Tamanho deveria ser 0"
    print("Teste 1 - Lista vazia: OK")
    
    # Teste 2: Inserção no início
    lista.inserir(1, 10)
    assert not lista.esta_vazia(), "A lista não deveria estar vazia"
    assert lista.obter_tamanho() == 1, "Tamanho deveria ser 1"
    assert lista.obter_elemento(1) == 10, "Elemento na posição 1 deveria ser 10"
    print("Teste 2 - Inserção no início: OK")
    
    # Teste 3: Inserção no final
    lista.inserir(2, 20)
    assert lista.obter_tamanho() == 2, "Tamanho deveria ser 2"
    assert lista.obter_elemento(2) == 20, "Elemento na posição 2 deveria ser 20"
    print("Teste 3 - Inserção no final: OK")
    
    # Teste 4: Inserção no meio
    lista.inserir(2, 15)
    assert lista.obter_tamanho() == 3, "Tamanho deveria ser 3"
    assert lista.obter_elemento(2) == 15, "Elemento na posição 2 deveria ser 15"
    assert lista.obter_elemento(3) == 20, "Elemento na posição 3 deveria ser 20"
    print("Teste 4 - Inserção no meio: OK")
    
    # Teste 5: Modificação de elemento
    lista.modificar_elemento(2, 18)
    assert lista.obter_elemento(2) == 18, "Elemento na posição 2 deveria ser 18"
    print("Teste 5 - Modificação de elemento: OK")
    
    # Teste 6: Remoção do início
    removido = lista.remover(1)
    assert removido == 10, "Elemento removido deveria ser 10"
    assert lista.obter_tamanho() == 2, "Tamanho deveria ser 2"
    assert lista.obter_elemento(1) == 18, "Elemento na posição 1 deveria ser 18"
    print("Teste 6 - Remoção do início: OK")
    
    # Teste 7: Remoção do final
    removido = lista.remover(2)
    assert removido == 20, "Elemento removido deveria ser 20"
    assert lista.obter_tamanho() == 1, "Tamanho deveria ser 1"
    print("Teste 7 - Remoção do final: OK")
    
    # Teste 8: Remoção do meio (quando aplicável)
    lista.inserir(2, 30)
    lista.inserir(3, 40)
    removido = lista.remover(2)
    assert removido == 30, "Elemento removido deveria ser 30"
    assert lista.obter_elemento(2) == 40, "Elemento na posição 2 deveria ser 40"
    print("Teste 8 - Remoção do meio: OK")
    
    # Teste 9: Impressão da lista
    print("Teste de impressão - Deveria mostrar: Lista: 18 -> 40")
    lista.imprimir()
    
    # Teste 10: Verificação de erros
    try:
        lista.obter_elemento(0)
        assert False, "Deveria ter lançado exceção para posição inválida"
    except IndexError:
        pass
    
    try:
        lista.inserir(5, 50)
        assert False, "Deveria ter lançado exceção para posição inválida"
    except IndexError:
        pass
    
    try:
        lista_vazia = ListaEncadeada()
        lista_vazia.remover(1)
        assert False, "Deveria ter lançado exceção para lista vazia"
    except ValueError:
        pass
    
    print("Teste 10 - Verificação de erros: OK")
    print("=== TODOS OS TESTES PASSARAM COM SUCESSO! ===")


if __name__ == "__main__":
    # Executar os testes quando o arquivo for executado diretamente
    testar_lista_encadeada()