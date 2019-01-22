class ArvoreBinaria:
    def __init__(self):
        self.__raiz = None

    class No:
        def __init__(self, valor):
            self.pai = None
            self.esquerda = None
            self.direita = None
            self.valor = valor

    #Esquerda, Raiz, Direita
    #Exibe em ordem crescente
    def ordem(self, atual = None, visualizar = None, raiz =False):
        if not raiz:
            visualizar = []
            atual = self.__raiz
            raiz = True

        if atual is not None:
            self.ordem(atual.esquerda, visualizar, raiz)
            visualizar.append(atual.valor)
            self.ordem(atual.direita, visualizar, raiz)
        return visualizar

    #Raiz, Direita, Esquerda
    #Exibe em ordem crescente
    def posordem(self, atual = None, visualizar = None, raiz =False):
        if not raiz:
            visualizar = []
            atual = self.__raiz
            raiz = True

        if atual is not None:
            self.ordem(atual.esquerda, visualizar, raiz)
            self.ordem(atual.direita, visualizar, raiz)
            visualizar.append(atual.valor)
        return visualizar

    #Raiz, Esquerda, Direita
    #Exibe em ordem crescente
    def preordem(self, atual = None, visualizar = None, raiz =False):
        if not raiz:
            visualizar = []
            atual = self.__raiz
            raiz = True

        if atual is not None:
            visualizar.append(atual.valor)
            self.ordem(atual.esquerda, visualizar, raiz)
            self.ordem(atual.direita, visualizar, raiz)
        return visualizar

    def sucessor(self, raiz):
        if raiz.direita is not None:
            raiz = raiz.direita
            while raiz.esquerda is not None:
                raiz = raiz.esquerda
            return raiz
        return None

    def antecessor(self, raiz):
        if raiz.esquerda is not None:
            raiz = raiz.esquerda
            while raiz.direita is not None:
                raiz = raiz.direita
            return raiz
        return None

    def __delitem__(self, valor):
        raiz=self.buscar(valor)

        if raiz:
            if raiz.esquerda is None or raiz.direita is None:
                sucessor = raiz 
            else:
                sucessor = self.sucessor(raiz) 

            if sucessor.esquerda is not None:
                aux = sucessor.esquerda
            else:
                aux = sucessor.direita  

            if aux is not None:
                aux.pai = sucessor.pai

            if sucessor.pai is None:
                self.__raiz = aux
            elif sucessor == sucessor.pai.esquerda:
                sucessor.pai.esquerda = aux
            else:
                sucessor.pai.direita = aux

            if sucessor != raiz:

                raiz.valor = sucessor.valor

            return sucessor


    def minimo(self):
        atual = self.__raiz

        # enquanto houver um filho a esquerda, caminhar nessa direção
        while atual.esquerda is not None:
            atual = atual.esquerda

        # não tem mais filho a esquerda
        # então atual é o menor elemento da árvore
        return atual.valor

    def maximo(self):
        atual = self.__raiz

        # enquanto houver um filho a direita, caminhar nessa direção
        while atual.direita is not None:
            atual = atual.direita

        # não tem mais filho a direita
        # então atual é o maior elemento da árvore
        return atual.valor

    def buscar(self, elemento, atual=None, visitou_raiz=False):

        if not visitou_raiz:
            atual = self.__raiz
            visitou_raiz = True

        if atual is not None and elemento != atual.valor:  
            if elemento < atual.valor:
                return self.buscar(elemento, atual.esquerda, visitou_raiz)
            else:
                return self.buscar(elemento, atual.direita, visitou_raiz)

        return atual

    def inserir(self, valor):
        pai_atual = None
        atual = self.__raiz # começando pela raiz
        novo = self.No(valor) # criando o novo nó com o valor

        # vamos descer a partir da raiz
        # para encontrar a posição correta para inserir
        while atual is not None:
            pai_atual = atual

            # se o valor que queremos inserir for menor
            # ir para a sub-árvore da esquerda
            # caso contrário, ir para a sub-árvore da direita
            if novo.valor < atual.valor:
                atual = atual.esquerda
            else:
                atual = atual.direita

        # o último pai encontrado será o pai do novo nó
        # caso não exista, o novo nó será a raiz da árvore
        novo.pai = pai_atual

        if pai_atual is None:
            # novo não tem pai, é o nó raiz
            self.__raiz = novo
        elif novo.valor < pai_atual.valor:
            # novo é menor que o pai, então é um filho a esquerda
            pai_atual.esquerda = novo
        else:
            # novo é maior que o pai, então é um filho a direita
            pai_atual.direita = novo


arvore = ArvoreBinaria()

arvore.inserir(8)
arvore.inserir(81)
arvore.inserir(1)
arvore.inserir(3)
arvore.inserir(2)
arvore.inserir(6)

arvore.inserir(5)

arvore.deletar(5)


arvore.buscar(1)
print("{}".format(arvore.ordem()))