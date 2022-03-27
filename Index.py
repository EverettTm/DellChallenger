#Feito por Felipe Matos
#Gostaria de dizer antes de tudo que devido ao tempo curto fiz um projeto mais que funcionasse do que bonito, ignorei o frontend e o back fiz de forma rapida, sem usar tanto classes ou outros arquivos deixando em um padrao melhor
#Primeiro a importacao das lib, escolhi o PySimpleGUI pelo fato de ser mais pratico, o mesmo ja possui o botao de fechar, diminuindo assim um pouco minha tarefa


import csv
import PySimpleGUI as sg

#Primeiro abrir o arquivo
arquivo = csv.reader(open("info.csv"), delimiter = ';')

#Fazer uma tela usando o pysimplegui para frontend

class TelaPrograma:
    def __init__(self):
        sg.change_look_and_feel('Topanga')
        #Layout
        layout = [
        [sg.Text('Selecione a opcao desejada',text_color='red')],
        [sg.Text("  ")],
        [sg.Checkbox('1-Pesquisar aluno 0',key='1'),sg.Checkbox('2-Perquisar por nome',key='2'),sg.Checkbox('3-Media anual',key='3'),sg.Checkbox('4-Rank bolsas mais altas e baixas',key='4')],
        [sg.Text("  ")],
        [sg.Button('Enviar Dados')],
        [sg.Text("  ")],
        ]
        janela = sg.Window("Bot Disparador").layout(layout)
        self.button, self.value = janela.Read()

    def Iniciar(self):

        primeira_opcao = self.value['1']
        segunda_opcao  = self.value['2']
        terceira_opcao = self.value['3']
        quarta_opcao   = self.value['4']

        # Se ele selecionar a quarta opcao entra aqui
        if quarta_opcao == 1 :

            class TelaPrograma:
                def __init__(self):


                    #Defini valores muito altos para que qualquer numero entrasse no menor e muito baixo para que qualquer um entrasse no menos
                    valores_bolsas = []
                    increment = 0
                    valor_menor_1 = 10000
                    valor_menor_2 = 10000
                    valor_menor_3 = 10000

                    valor_maior_1 = 0
                    valor_maior_2 = 0
                    valor_maior_3 = 0
                    # Eu pensei em usar a funcao sort e depois utiliza outro for, mas o codigo ficaria mais estenco assim o mesmo fica de forma mais rapida e eficiente
                    for linha in arquivo:
                        if increment != 0:
                            #comparacoes para ve se esta no top 3, tanto com o valor maior quanto menor
                            if float(linha[10]) < valor_menor_1:
                                nome_menor_1 = linha[0]
                                valor_menor_1 = float(linha[10])
                            elif float(linha[10]) < valor_menor_2:
                                nome_menor_2 = linha[0]
                                valor_menor_2 = float(linha[10])
                            elif float(linha[10]) < valor_menor_3:
                                nome_menor_3 = linha[0]
                                valor_menor_3 = float(linha[10])

                            elif float(linha[10])  >valor_maior_1:
                                nome_maior_1 = linha[0]
                                valor_maior_1 = float(linha[10])
                            elif float(linha[10]) > valor_maior_2:
                                nome_maior_2 = linha[0]
                                valor_maior_2 = float(linha[10])
                            elif float(linha[10]) > valor_maior_3:
                                nome_maior_3 = linha[0]
                                valor_maior_3 = float(linha[10])
                        else:
                            increment = increment+1



                    sg.change_look_and_feel('Topanga')
                    # Layout para mostrar o top 3
                    layout = [
                        [sg.Text('Top 3 Alunos', text_color='red')],
                        [sg.Text("  ")],
                        [sg.Text("  ")],
                        [sg.Text('Mais baixo:', text_color='red')],
                        [sg.Text("  ")],
                        [sg.Text("1: "+ nome_menor_1, text_color='black')],
                        [sg.Text("  ")],
                        [sg.Text("2: "+ nome_menor_2, text_color='black')],
                        [sg.Text("  ")],
                        [sg.Text("3: "+ nome_menor_3, text_color='black')],
                        [sg.Text("  ")],
                        [sg.Text("  ")],

                        [sg.Text('Mais alto:', text_color='red')],
                        [sg.Text("  ")],
                        [sg.Text("1: " + nome_maior_3, text_color='black')],
                        [sg.Text("  ")],
                        [sg.Text("2: " + nome_maior_2, text_color='black')],
                        [sg.Text("  ")],
                        [sg.Text("3: " + nome_maior_1, text_color='black')],
                        [sg.Button('Fechar')],
                        [sg.Text("  ")],
                    ]
                    janela = sg.Window("Bot Disparador").layout(layout)
                    self.button, self.value = janela.Read()

            tela = TelaPrograma()
            tela.Iniciar()

        # Se selecionar a terceira opcao entra aqui
        elif terceira_opcao ==1:
            class TelaPrograma:
                def __init__(self):
                    sg.change_look_and_feel('Topanga')
                    # Layout
                    layout = [
                        [sg.Text('Digite o ano para descobrir a media dos valores das bolsas', text_color='red')],
                        [sg.Text("  ")],
                        [sg.Text("  ")],
                        [sg.Text('Ano:', size=(4, 0)), sg.Input(key='ano')],
                        [sg.Text("  ")],

                        [sg.Button('Enviar Dados')],
                        [sg.Text("  ")],
                    ]
                    janela = sg.Window("Bot Disparador").layout(layout)
                    self.button, self.value = janela.Read()

                def Iniciar(self):
                    #Aqui recebemos o ano que ele quer consultar as medias
                    ano = self.value['ano']
                    valor_total_bolsa = 0
                    incremento = 0
                    for linha in arquivo:
                        if linha[4] == ano:
                            #No for, sera para percorreer o arquivo inteiro, o if sera somente no ano pedido,
                            #Ele tambem usa uma variavel incremento para ir acrescentando e no futuro dividir para tirar a media
                            valor_total_bolsa = valor_total_bolsa +float(linha[10])
                            incremento =incremento +1
                    if incremento != 0:
                        class TelaPrograma:
                            def __init__(self):
                                sg.change_look_and_feel('Topanga')
                                # Layout
                                layout = [
                                    [sg.Text('MEDIA DO ANO DE '+ano, text_color='red')],
                                    [sg.Text("  ")],
                                    [sg.Text(f'Media de bolsa anual:' + str(valor_total_bolsa/incremento), size=(100, 0))],


                                ]
                                janela = sg.Window("Bot Disparador").layout(layout)
                                self.button, self.value = janela.Read()

                        tela = TelaPrograma()
                        tela.Iniciar()

                    tela = TelaPrograma()
                    tela.Iniciar()


        # Se ele selecionar a segunda opcao entra aqui
        elif segunda_opcao ==1:
            class TelaPrograma:
                def __init__(self):
                    sg.change_look_and_feel('Topanga')
                    # Layout
                    layout = [
                        #Pedindo o nome do aluno
                        [sg.Text('Digite o nome do aluno', text_color='red')],
                        [sg.Text("  ")],
                        [sg.Text("  ")],
                        [sg.Text('Nome:', size=(4, 0)), sg.Input(key='nome')],
                        [sg.Text("  ")],

                        [sg.Button('Enviar Dados')],
                        [sg.Text("  ")],
                    ]
                    janela = sg.Window("Bot Disparador").layout(layout)
                    self.button, self.value = janela.Read()

                def Iniciar(self):
                    nome = self.value['nome']

                    for linha in arquivo:
                        if nome in linha[0]:
                            # logica para codficar o nome no formato experado
                            # primeiro substituo pela proxima letra do alfabeto, mantenho a primeira e ultima letra e inverto as do meio
                            nome = nome
                            nome_separado = list(nome)
                            i = 0
                            nome_codificado = ""
                            while i < len(nome_separado):
                                letra = (nome_separado[i])
                                letra_assync = ord(letra)
                                letra_invertida = chr(letra_assync + 1)
                                print(letra_invertida)
                                i = i + 1
                                nome_codificado = nome_codificado + letra_invertida

                            txt = nome_codificado

                            txt1 = txt[0]
                            txtt = txt[-1]

                            txtremove = txt[1:]
                            txtremove2 = txtremove[:-1]

                            nome_final = (txt1 + txtremove2[::-1] + txtt)
                            #Finalizando o procecsso de decodificacao
                            class TelaPrograma:
                                def __init__(self):
                                    sg.change_look_and_feel('Topanga')
                                    # Layout
                                    layout = [
                                        [sg.Text('Horarios Disponiveis:', text_color='red')],
                                        [sg.Text("  ")],
                                        [sg.Text(f'Nome:' + nome_final, size=(100, 0))],
                                        [sg.Text("  ")],
                                        [sg.Text(f'Ano: ' + linha[4], size=(100, 0))],
                                        [sg.Text("  ")],
                                        [sg.Text(f'Entidade de ensino: ' + linha[2], size=(100, 0))],
                                        [sg.Text("  ")],
                                        [sg.Text(f'Bolsa: ' + linha[10], size=(100, 0))],

                                    ]
                                    janela = sg.Window("Bot Disparador").layout(layout)
                                    self.button, self.value = janela.Read()

                            tela = TelaPrograma()
                            tela.Iniciar()

            tela = TelaPrograma()
            tela.Iniciar()
            # Se ele selecionar a primeira opcao entra aqui
        elif primeira_opcao == 1:

            class TelaPrograma:
                def __init__(self):
                    sg.change_look_and_feel('Topanga')
                    # Layout
                    layout = [
                        #Ele pede o que deseja descobrir o aluno 0
                        [sg.Text('Digite o ano para descobrir o aluno 0', text_color='red')],
                        [sg.Text("  ")],
                        [sg.Text("  ")],
                        [sg.Text('Ano:', size=(4, 0)), sg.Input(key='ano')],
                        [sg.Text("  ")],

                        [sg.Button('Enviar Dados')],
                        [sg.Text("  ")],
                    ]
                    janela = sg.Window("Bot Disparador").layout(layout)
                    self.button, self.value = janela.Read()

                def Iniciar(self):
                    ano = self.value['ano']

                    # Se o ano do aluno for igual ao informado, ira mostrar os dados deles, lembrando que eu fiz por ondem da lista, ja que o me( mes) estavam todos igual a 1

                    for linha in arquivo:
                        if linha[4] == ano:

                            class TelaPrograma:
                                def __init__(self):
                                    sg.change_look_and_feel('Topanga')
                                    # Layout
                                    layout = [
                                        [sg.Text('Horarios Disponiveis:', text_color='red')],
                                        [sg.Text("  ")],
                                        [sg.Text(f'Nome:' + linha[0], size=(100, 0))],
                                        [sg.Text("  ")],
                                        [sg.Text(f'CPF: ' + linha[1], size=(100, 0))],
                                        [sg.Text("  ")],
                                        [sg.Text(f'Entidade de ensino: ' + linha[2], size=(100, 0))],
                                        [sg.Text("  ")],
                                        [sg.Text(f'Bolsa: ' + linha[10], size=(100, 0))],

                                    ]
                                    janela = sg.Window("Bot Disparador").layout(layout)
                                    self.button, self.value = janela.Read()

                            tela = TelaPrograma()
                            tela.Iniciar()
                        #Caso ele nao ache ou o ano informado seje invalido
                        else:
                            class TelaPrograma:
                                def __init__(self):
                                    sg.change_look_and_feel('Topanga')
                                    # Layout
                                    layout = [
                                        [sg.Text('ANO INVALIDO:', text_color='red')],
                                        [sg.Text("  ")],

                                    ]
                                    janela = sg.Window("Bot Disparador").layout(layout)
                                    self.button, self.value = janela.Read()

                            tela = TelaPrograma()
                            tela.Iniciar()

            tela = TelaPrograma()
            tela.Iniciar()


tela = TelaPrograma()
tela.Iniciar()
