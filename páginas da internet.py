#Crie uma pilha que armazene as páginas visitadas em um navegador da web. Em
#seguida, crie uma função que remova a última página visitada.

class NavegadorWeb:
    def __init__(self):
        self.paginas = []

    def visitar_pagina(self, url):#recebe uma URL e adiciona essa página no final da lista de páginas visitadas.
        self.paginas.append(url)

    def voltar_pagina(self):#remove a última página visitada da lista
        if len(self.paginas) > 0:
            self.paginas.pop()

    def exibir_paginas_visitadas(self):
        print("Páginas visitadas:")
        for pagina in self.paginas:
            print(pagina)

#adiciondo páginas visitadas
navegador = NavegadorWeb()
navegador.visitar_pagina("https://www.google.com")
navegador.visitar_pagina("https://faculdadefastech.com.br/")
navegador.visitar_pagina("https://faculdadefastech.com.br/cursos/graduacao/engenharia_de_computacao_")

navegador.exibir_paginas_visitadas()# verificar páginas adicionadas
navegador.voltar_pagina()#remover a última página visitada
navegador.exibir_paginas_visitadas()#páginas adicionadas - página foi removida

