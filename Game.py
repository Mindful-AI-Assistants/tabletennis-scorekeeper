import flet as ft
import pandas as pd
from DataBase import DataBase # Importando a classe DataBase do arquivo DataBase.py

def game(
    page: ft.Page,
    Player_1: str,
    Player_2: str,
    Points_To_Win: str,
    Sets: str,
    id_tournament: str,
    id_match: str,
    current_Fase: str,
    
):
    '''Função com todo o sistema de jogo, onde os jogadores podem somar pontos e sets.'''
    Container_Game = ft.Ref[ft.Container]() # Referência para o Container do jogo
    Draw = False # Variável para controlar se houve empate na pontuação

    
    
    def sum_Point_Player1():
        '''Soma 1 ponto para o Player 1 e verifica se houve empate ou vitória.'''
        
        nonlocal Draw
        
        point_Player1.value = str(int(point_Player1.value) + 1) # Soma 1 ponto ao Player 1
        
        # Verifica se ambos os jogadores estão com 1 ponto a menos do que o necessário para vencer
        if point_Player1.value == str(int(Points_To_Win) - 1) and point_Player2.value == str(int(Points_To_Win) - 1): Draw = True
        
        update_layout() # Atualiza o layout do jogo após a soma do ponto
        
    
    def sum_Point_Player2():
        '''Soma 1 ponto para o Player 2 e verifica se houve empate ou vitória.'''
        
        nonlocal Draw
        
        point_Player2.value = str(int(point_Player2.value) + 1) # Soma 1 ponto ao Player 2

        # Verifica se ambos os jogadores estão com 1 ponto a menos do que o necessário para vencer        
        if point_Player1.value == str(int(Points_To_Win) - 1) and point_Player2.value == str(int(Points_To_Win) - 1): Draw = True 
        
        update_layout() # Atualiza o layout do jogo após a soma do ponto


    def update_layout():
        '''Atualiza o layout do jogo, verificando se houve vitória ou empate.'''
        nonlocal Container_Game, Draw
        
        # Verifica se houve empate na pontuação
        if Draw:
            # Se ambos os jogadores estão com 1 ponto a menos do que o necessário para vencer
            if int(point_Player1.value) - int(point_Player2.value) == 2:
                set_Player1.value = str(int(set_Player1.value) + 1) # Soma 1 set ao Player 1
                Draw = False # Reseta o empate
                point_Player1.value = '0' # Reseta os pontos do Player 1
                point_Player2.value = '0'  # Reseta os pontos do Player 2
            
            # Se ambos os jogadores estão com 1 ponto a menos do que o necessário para vencer
            elif int(point_Player2.value) - int(point_Player1.value) == 2:
                set_Player2.value = str(int(set_Player2.value) + 1) # Soma 1 set ao Player 2
                Draw = False # Reseta o empate
                point_Player1.value = '0' # Reseta os pontos do Player 1
                point_Player2.value = '0' # Reseta os pontos do Player 2
        
        # Verifica se algum dos jogadores atingiu a pontuação necessária para vencer
        else:      
            # Se o Player 1 atingiu a pontuação necessária para vencer
            if point_Player1.value == Points_To_Win:
                set_Player1.value = str(int(set_Player1.value) + 1) # Soma 1 set ao Player 1
                point_Player1.value = '0' # Reseta os pontos do Player 1
                point_Player2.value = '0' # Reseta os pontos do Player 2
            
            # Se o Player 2 atingiu a pontuação necessária para vencer
            elif point_Player2.value == Points_To_Win:
                set_Player2.value = str(int(set_Player2.value) + 1) # Soma 1 set ao Player 2
                point_Player1.value = '0' # Reseta os pontos do Player 1
                point_Player2.value = '0' # Reseta os pontos do Player 2
        
        # Verifica se algum dos jogadores atingiu o número de sets necessários para vencer
        if set_Player1.value == Sets:
            Container_Game.current.content = ft.Container( # Container para exibir a mensagem de vitória do Player 1
                content = ft.Column( # Coluna para organizar os controles
                    controls = [
                        # Texto de vitória do Player 1
                        ft.Text(
                            'Processando informações, aguarde...', # Mensagem temporária enquanto processa as informações
                            size = 40, # Tamanho do texto
                            weight = 'bold', # Peso do texto
                            color = ft.Colors.ON_SURFACE_VARIANT # Cor do texto Variante, para caso o tema mude.
                        )
                    ],
                    
                    horizontal_alignment = ft.CrossAxisAlignment.CENTER, # Alinhamento horizontal dos controles
                    alignment = ft.MainAxisAlignment.CENTER # Alinhamento vertical dos controles
                ),
                expand = True # Expande o container para ocupar todo o espaço disponível
            )
            page.update()

            # Atualiza o ranking do usuário que venceu
            if Player_1 != 'Player 1':
                database = DataBase() # Cria uma instância da classe DataBase
                database.update_Player(
                    f'UPDATE partida set \"set\" = {set_Player1.value} where id = {id_match};' + # Atualiza o número de sets do Player 1 na partida
                    '\n' +
                    f'\nUPDATE atleta_partida ap set \"set\" = {set_Player1.value} from atleta a where a.id = ap.id_atleta and ap.id_partida = {id_match} and concat(a.nome, \' \', a.sobrenome) = \'{Player_1}\';' +
                    f'\nUPDATE atleta_partida ap set \"set\" = {set_Player2.value} from atleta a where a.id = ap.id_atleta and ap.id_partida = {id_match} and concat(a.nome, \' \', a.sobrenome) = \'{Player_2}\';'
                )
                
                if current_Fase != 'Final':
                    next_step = ['Round of 128', 'Round of 64', 'Round of 32', 'Round of 16', 'Quartas', 'Semifinais', 'Final'] # Lista das fases do torneio
                    next_step = next_step[next_step.index(current_Fase) + 1] # Próxima fase do torneio 
                    
                    matchs = database.get_DataBase(f'select * from partida where id_torneio = {id_tournament} order by id asc;')
                    id_player = database.get_DataBase(f'select * from atleta where concat(nome, \' \', sobrenome) = \'{Player_1}\';').loc[0, 'id'] # Obtém o ID do Player 1
                    
                    aux = matchs[matchs['fase'] == next_step].reset_index(drop = True) # Filtra as partidas da próxima fase
                    
                    prox_match = int(matchs.loc[matchs['id'] == int(id_match), 'proxima_fase'].values[0]) # Obtém a próxima partida
                    
                    id_next_match = aux.loc[prox_match - 1, 'id']
                    
                    database.insert_Player(
                        'atleta_partida',
                        '(id_partida, id_atleta, \"set\")',
                        (int(id_next_match), int(id_player), 0)
                    )
            
            Container_Game.current.content = ft.Container( # Container para exibir a mensagem de vitória do Player 1
                content = ft.Column( # Coluna para organizar os controles
                    controls = [
                        # Texto de vitória do Player 1
                        ft.Text(
                            "PARABÉNS " + Player_1 + ', VOCÊ GANHOU! 🎉🎉',
                            size = 40, # Tamanho do texto
                            weight = 'bold', # Peso do texto
                            color = ft.Colors.ON_SURFACE_VARIANT # Cor do texto Variante, para caso o tema mude.
                        )
                    ],
                    
                    horizontal_alignment = ft.CrossAxisAlignment.CENTER, # Alinhamento horizontal dos controles
                    alignment = ft.MainAxisAlignment.CENTER # Alinhamento vertical dos controles
                ),
                expand = True # Expande o container para ocupar todo o espaço disponível
            )
            page.update() # Atualiza a página para refletir as mudanças no layout do jogo
            

        # Verifica se o Player 2 atingiu o número de sets necessários para vencer
        elif set_Player2.value == Sets:
            Container_Game.current.content = ft.Container( # Container para exibir a mensagem de vitória do Player 2
                content = ft.Column(
                    controls = [
                        # Texto de vitória do Player 2
                        ft.Text(
                            "Processando informações, aguarde...", # Mensagem temporária enquanto processa as informações',
                            size = 40, # Tamanho do texto
                            weight = 'bold', # Peso do texto
                            color = ft.Colors.ON_SURFACE_VARIANT # Cor do texto Variante, para caso o tema mude.
                        )
                    ],
                    
                    horizontal_alignment = ft.CrossAxisAlignment.CENTER, # Alinhamento horizontal dos controles
                    alignment = ft.MainAxisAlignment.CENTER # Alinhamento vertical dos controles
                ),
                expand = True # Expande o container para ocupar todo o espaço disponível
            )
            page.update()
            
            
            # Atualiza o ranking do usuário que venceu
            if Player_2 != 'Player 2':
                database = DataBase() # Cria uma instância da classe DataBase
                database.update_Player(
                    f'UPDATE partida set \"set\" = {set_Player2.value} where id = {id_match};' + # Atualiza o número de sets do Player 1 na partida
                    '\n' +
                    f'\nUPDATE atleta_partida ap set \"set\" = {set_Player1.value} from atleta a where a.id = ap.id_atleta and ap.id_partida = {id_match} and concat(a.nome, \' \', a.sobrenome) = \'{Player_1}\';' +
                    f'\nUPDATE atleta_partida ap set \"set\" = {set_Player2.value} from atleta a where a.id = ap.id_atleta and ap.id_partida = {id_match} and concat(a.nome, \' \', a.sobrenome) = \'{Player_2}\';'
                )
                
                if current_Fase != 'Final':
                    next_step = ['Round of 128', 'Round of 64', 'Round of 32', 'Round of 16', 'Quartas', 'Semifinais', 'Final'] # Lista das fases do torneio
                    next_step = next_step[next_step.index(current_Fase) + 1] # Próxima fase do torneio 
                    
                    matchs = database.get_DataBase(f'select * from partida where id_torneio = {id_tournament} order by id asc;')
                    id_player = database.get_DataBase(f'select * from atleta where concat(nome, \' \', sobrenome) = \'{Player_2}\';').loc[0, 'id'] # Obtém o ID do Player 1
                    
                    aux = matchs[matchs['fase'] == next_step].reset_index(drop=True) # Filtra as partidas da próxima fase
                    
                    prox_match = int(matchs.loc[matchs['id'] == int(id_match), 'proxima_fase'].values[0]) # Obtém a próxima partida
                    
                    id_next_match = aux.loc[prox_match - 1, 'id']
                    
                    database.insert_Player(
                        'atleta_partida',
                        '(id_partida, id_atleta, \"set\")',
                        (int(id_next_match), int(id_player), 0)
                    )
            
            Container_Game.current.content = ft.Container( # Container para exibir a mensagem de vitória do Player 1
                content = ft.Column( # Coluna para organizar os controles
                    controls = [
                        # Texto de vitória do Player 1
                        ft.Text(
                            "PARABÉNS " + Player_2 + ', VOCÊ GANHOU! 🎉🎉',
                            size = 40, # Tamanho do texto
                            weight = 'bold', # Peso do texto
                            color = ft.Colors.ON_SURFACE_VARIANT # Cor do texto Variante, para caso o tema mude.
                        )
                    ],
                    
                    horizontal_alignment = ft.CrossAxisAlignment.CENTER, # Alinhamento horizontal dos controles
                    alignment = ft.MainAxisAlignment.CENTER # Alinhamento vertical dos controles
                ),
                expand = True # Expande o container para ocupar todo o espaço disponível
            )
                
                
            
        page.update() # Atualiza a página para refletir as mudanças no layout do jogo
            
    
    # Criação do Container do jogo com os controles necessários
    Container_Game.current = ft.Container(
        content = ft.Column(
            controls = [
                ft.Row(
                    controls = [
                        ft.Row(
                            controls = [
                                # Controles para exibir os pontos e sets dos jogadores
                                point_Player1 := ft.Text(
                                    "0", # Ponto inicial do Player 1
                                    size = 200, # Tamanho do texto
                                    weight = 'bold' # Peso do texto
                                ),
                                
                                # Controles para exibir os sets do Player 1
                                set_Player1 := ft.Text(
                                    "0", # Set inicial do Player 1
                                    size = 50 # Tamanho do texto
                                )
                            ],
                            spacing = 80, # Espaçamento entre os controles
                            alignment = ft.MainAxisAlignment.CENTER # Alinhamento dos controles
                        ),
                        
                        # Texto para exibir "VS" entre os jogadores
                        ft.Text(
                            "VS", # Texto de confronto entre os jogadores
                            size = 30, # Tamanho do texto
                            weight = "bold" # Peso do texto
                        ),
                        
                        # Controles para exibir os pontos e sets do Player 2
                        ft.Row(
                            controls = [
                                set_Player2 := ft.Text( # Set inicial do Player 2
                                    "0", # Tamanho do texto
                                    size = 50 # Tamanho do texto
                                ),
                                
                                # Controles para exibir os pontos do Player 2
                                point_Player2 := ft.Text(
                                    "0", # Ponto inicial do Player 2
                                    size = 200, # Tamanho do texto
                                    weight = 'bold' # Peso do texto
                                )
                            ],
                            spacing = 80, # Espaçamento entre os controles
                            alignment = ft.MainAxisAlignment.CENTER # Alinhamento dos controles
                        )
                    ],
                    alignment = ft.MainAxisAlignment.CENTER, # Alinhamento horizontal dos controles
                    spacing = 100 # Espaçamento entre os controles
                ),
                
                
                ft.Row(
                    controls = [
                        # Controles para exibir os nomes dos jogadores
                        ft.FloatingActionButton(
                            content = ft.Text(Player_1, color = ft.Colors.WHITE, size = 30), # Nome do Player 1
                            tooltip = 'Somar 1 ponto para ' + Player_1, # Tooltip para o botão do Player 1
                            bgcolor = ft.Colors.GREEN, # Cor de fundo do botão do Player 1
                            height = 100, # Altura do botão do Player 1
                            expand = True, # Expande o botão do Player 1 para ocupar todo o espaço disponível
                            on_click = lambda e: sum_Point_Player1() # Ação ao clicar no botão do Player 1
                        ),
                        
                        # Espaço entre os botões dos jogadores
                        ft.Text(
                            '           ',  # Espaço em branco para separar os botões
                            size = 50, # Tamanho do texto
                            weight = "bold" # Peso do texto
                        ),
                        
                        # Controles para exibir os nomes dos jogadores
                        ft.FloatingActionButton(
                            content = ft.Text(Player_2, color = ft.Colors.WHITE, size = 30), # Nome do Player 2
                            tooltip = 'Somar 1 ponto para ' + Player_2, # Tooltip para o botão do Player 2
                            bgcolor = ft.Colors.GREEN, # Cor de fundo do botão do Player 2
                            height = 100, # Altura do botão do Player 2
                            expand = True, # Expande o botão do Player 2 para ocupar todo o espaço disponível
                            on_click = lambda e: sum_Point_Player2() # Ação ao clicar no botão do Player 2
                        )
                    ],
                    alignment = ft.MainAxisAlignment.SPACE_BETWEEN # Alinhamento horizontal dos botões dos jogadores
                )
            ],
            horizontal_alignment = ft.CrossAxisAlignment.CENTER, # Alinhamento horizontal dos controles
            alignment = ft.MainAxisAlignment.CENTER, # Alinhamento vertical dos controles
            expand = True # Expande a coluna para ocupar todo o espaço disponível
        ),
        expand = True # Expande o container do jogo para ocupar todo o espaço disponível
    )
    
    update_layout() # Chama a função para atualizar o layout do jogo com os controles criados
    
    
    return Container_Game.current # Retorna o Container do jogo com todos os controles e lógica implementados
