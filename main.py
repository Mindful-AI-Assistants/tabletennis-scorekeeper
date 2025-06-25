import pandas as pd # Importa a biblioteca pandas para manipulação de dados
import flet as ft # Importa a biblioteca flet para criação do App
from DataBase import DataBase # Importa a classe Ranking do arquivo Ranking.py
from RankingDetalhado import RankingDetalhado # Importa a classe RankingDetalhado do arquivo RankingDetalhado.py
from Signup import Signup # Importa a função mainLogin do arquivo mainLogin.py
from Game import game # Importa a função game para contagem dos pontos

def main(page: ft.Page):
    # Configurações gerais do App
    page.title = 'Tênis de Mesa' # Define o título do App
    page.theme_mode = ft.ThemeMode.SYSTEM # Definindo tema escuro
    
    page.theme_mode = ft.ThemeMode.DARK if page.platform_brightness == ft.Brightness.DARK else ft.ThemeMode.LIGHT # Define o tema do App com base no brilho da plataforma
    
    #page.window.full_screen = True # Define o App para tela cheia
    page.window.maximized = True
    page.window.icon = 'Icon/ping-pong.png' # Caminho do ícone do App


    page_Home = True # Variável para controlar a página inicial
    page_RankingDetalhado = False # Variável para controlar a página de ranking detalhado
    page_Game = False # Variável para controlar a página do jogo

    player_1_Code = False # Variável para controlar se o jogador 1 está definido e pronto para jogar
    player_2_Code = False # Variável para controlar se o jogador 2 está definido e pronto para jogar

    Points_To_Win = 0
    Sets = 0
    
    Player_1 = ''
    Player_2 = ''
    
    Player_1_Password = ''
    Player_2_Password = ''

    dataBase = DataBase() # Cria uma instância da classe DataBase para manipulação do banco de dados


    def close_App() -> None:
        dataBase.close()
        page.window.close()


    def change_Theme() -> None:
        '''Função para alternar entre os temas claro e escuro do App, dependendo do tema atual.'''
        
        if page.theme_mode == ft.ThemeMode.DARK: # Se o tema atual for escuro, muda para o tema claro
            page.theme_mode = ft.ThemeMode.LIGHT # Define o tema claro
        
        else: # Se o tema atual for claro, muda para o tema escuro
            page.theme_mode = ft.ThemeMode.DARK # 
            
        page.update()


    def go_To_Home() -> None:
        '''Função para voltar à página inicial do App'''
        
        '''A palavra-chave nonlocal é usada para indicar que uma variável definida em um escopo externo (mas não global) será modificada dentro de uma função interna. 
        Ela permite alterar o valor de variáveis de funções envolventes sem precisar passá-las como parâmetro.'''
        nonlocal page_RankingDetalhado, page_Home, page_Game 
        
        page_Game = False # Desativa a página do jogo
        page_Home = True # Ativa a página inicial
        page_RankingDetalhado = False # Desativa a página de ranking detalhado
        
        update_layout() # Chama a função update_layout para atualizar o layout da página


    def go_To_RankingDetalhado() -> None:
        '''Função para ir para a página de ranking detalhado do App'''
        
        '''A palavra-chave nonlocal é usada para indicar que uma variável definida em um escopo externo (mas não global) será modificada dentro de uma função interna. 
        Ela permite alterar o valor de variáveis de funções envolventes sem precisar passá-las como parâmetro.'''
        nonlocal page_RankingDetalhado, page_Home, page_Game
        
        page_Game = False # Desativa a página do jogo
        page_Home = False # Desativa a página inicial
        page_RankingDetalhado = True # Ativa a página de ranking detalhado
        update_layout() # Chama a função update_layout para atualizar o layout da página


    def go_To_Game() -> None:
        '''Função usada para reiniciar uma partida.'''
        
        '''A palavra-chave nonlocal é usada para indicar que uma variável definida em um escopo externo (mas não global) será modificada dentro de uma função interna. 
        Ela permite alterar o valor de variáveis de funções envolventes sem precisar passá-las como parâmetro.'''
        nonlocal page_Game, page_Home, page_RankingDetalhado
        
        page_Home = True # Ir para a página inicial da partida
        page_Game = True # ir para a partida com a configuração anterior
        page_RankingDetalhado = False # Desativa a página de ranking detalhado
        update_layout() # Chama a função update_layout para atualizar o layout da página


    def runSignup() -> None:
        '''Função usada para ir para a página de cadastro de jogadores.'''
         
        nonlocal page_RankingDetalhado, page_Home, page_Game
        
        page_Game = False # Desativa a página do jogo
        page_Home = False # Desativa a página inicial
        page_RankingDetalhado = False # Desativa a página de ranking detalhado
        
        # Com tudo acima desativado, o código irá automaticamente para a aba de cadastro de jogadores.
        update_layout() # Chama a função update_layout para atualizar o layout da página


    def password_Confirmation(database: pd.DataFrame, alert: ft.AlertDialog) -> None:
        nonlocal Player_1_Password, Player_2_Password, player_1_Code, player_2_Code

        Player_1_Password.error = False
        Player_1_Password.error_text = ''
        
        Player_2_Password.error = False
        Player_2_Password.error_text = ''


        if Player_1_Password.value == '':
            Player_1_Password.error = True
            Player_1_Password.error_text = 'Senha não pode ser vazia!' # Verifica se a senha do jogador 1 está vazia
        
        elif Player_1_Password.value != database.loc[database["id"] == int(chosen_Match.value), "senha"].values[0]:
            Player_1_Password.error = True
            Player_1_Password.error_text = 'Senha incorreta!' # Verifica se a senha do jogador 1 está incorreta
        
        Player_1_Password.update()


        if Player_2_Password.value == '':
            Player_2_Password.error = True
            Player_2_Password.error_text = 'Senha não pode ser vazia!' # Verifica se a senha do jogador 2 está vazia
        
        elif Player_2_Password.value != database.loc[database["id"] == int(chosen_Match.value), "senha"].values[1]:
            Player_2_Password.error = True
            Player_2_Password.error_text = 'Senha incorreta!' # Verifica se a senha do jogador 2 está incorreta
        
        Player_2_Password.update()


        if not Player_1_Password.error and not Player_2_Password.error: # Verifica se há erros nas senhas dos jogadores
            player_1_Code = True
            player_2_Code = True
            
            alert.title = "Senhas estão corretas!"
            alert.message = "As senhas estão corretas, feche a tela e inicie a partida!" # Mensagem de confirmação de senha correta
            alert.actions = []
            alert.update()

    def set_Players(database: pd.DataFrame) -> None:
        nonlocal Player_1, Player_2, player_1_Code, player_2_Code, Player_1_Password, Player_2_Password
        
        player_1_Code = False # Reseta o código do jogador 1
        player_2_Code = False # Reseta o código do jogador 2
        Player_1 = database.loc[database["id"] == int(chosen_Match.value), "nome_completo"].values[0]
        Player_2 = database.loc[database["id"] == int(chosen_Match.value), "nome_completo"].values[1]
        
        
        alert = ft.AlertDialog(
            title = ft.Text("Senha dos Atletas!"), # Título do diálogo de alerta
            content = ft.Text(f"Digite a senha dos atletas {Player_1} e {Player_2} para continuar!"), # Conteúdo do diálogo de alerta
            scrollable = True,
            actions=[
                
                Player_1_Password := ft.TextField(
                    label = f'Senha do {Player_1}',
                    hint_text = f'Digite a senha do {Player_1}', # Texto de dica do campo de senha
                    password = True, # Define o campo como senha
                    can_reveal_password= True, # Permite revelar a senha
                    max_length = 100,
                    prefix_icon = ft.Icons.LOCK_OUTLINE,
                    keyboard_type = ft.KeyboardType.VISIBLE_PASSWORD,
                    border = ft.InputBorder.UNDERLINE,
                    input_filter = ft.InputFilter(
                        regex_string = r'^[a-zA-Z0-9_@$!%*?&#]*$',
                        allow = False
                    )
                ),
                
                Player_2_Password := ft.TextField(
                    label = f'Senha do {Player_2}',
                    hint_text = f'Digite a senha do {Player_2}', # Texto de dica do campo de senha
                    password = True, # Define o campo como senha
                    can_reveal_password= True, # Permite revelar a senha
                    max_length = 100,
                    prefix_icon = ft.Icons.LOCK_OUTLINE,
                    keyboard_type = ft.KeyboardType.VISIBLE_PASSWORD,
                    border = ft.InputBorder.UNDERLINE,
                    input_filter = ft.InputFilter(
                        regex_string = r'^[a-zA-Z0-9_@$!%*?&#]*$',
                        allow = False
                    ),
                    on_submit = lambda e: password_Confirmation(database, alert) # Ação do campo de senha para confirmar as senhas dos atletas
                ),
                
                ft.FloatingActionButton(
                    content = ft.Text("Confirmar", size = 20, weight = 'bold', color = ft.Colors.WHITE), # Texto do botão de confirmação
                    icon = ft.Icons.CHECK, # Ícone do botão de confirmação
                    bgcolor = ft.Colors.GREEN, # Cor de fundo do botão de confirmação
                    expand = True,
                    height = 50,
                    width = 200,
                    on_click = lambda e: password_Confirmation(database, alert)
                )
            ],
            actions_alignment = ft.MainAxisAlignment.CENTER # Alinhamento das ações do diálogo de alerta
        )
        
        page.open(alert) # Abre o diálogo de alerta para solicitar as senhas dos atletas



    def Choice_match() -> None:
        nonlocal right_screen, chosen_Match, Points_To_Win, Sets
        
        Points_To_Win = tournaments.loc[tournaments['id'] == int(chosen_tournament.value), 'ponto'].values[0] # Obtém os pontos necessários para vencer a partida do torneio selecionado
        Sets = tournaments.loc[tournaments['id'] == int(chosen_tournament.value), 'set'].values[0] # Obtém o número de sets necessários para vencer a partida do torneio selecionado
        
        
        matchs = DataBase().get_DataBase(
            'select p.*,' +
            '\nconcat(a.nome, \' \', a.sobrenome) as nome_completo,' +
            '\na.senha as senha' +
            '\nfrom atleta_partida ap' +
            '\ninner join partida p on p.id = ap.id_partida' +
            '\ninner join atleta a on a.id = ap.id_atleta' +
            f'\nwhere p.id_torneio = {chosen_tournament.value} and p.set = 0;'
        )
        
        right_screen.content.controls.clear() # Limpa os controles da tela direita antes de adicionar novos
        
        right_screen.content.controls.append(chosen_tournament)
        
        chosen_Match = ft.Dropdown(
            label= 'Escolha a Partida', # Rótulo do dropdown
            hint_text= 'Selecione a partida', # Texto de dica do dropdown
            options=[
                ft.dropdown.Option(key, f'{matchs.loc[matchs["id"] == int(key), "nome_completo"].values[0]} VS {matchs.loc[matchs["id"] == key, "nome_completo"].values[1]}') # Cria uma opção para cada partida obtida do banco de dados
                
                for key in matchs['id'][matchs['id'].duplicated()].tolist() # Itera sobre os dados das partidas obtidos do banco de dados
            ],
            editable= True, # Permite edição do dropdown
            enable_filter = True, # Habilita o filtro do dropdown
            menu_height = 300,
            width = 340,
            on_change = lambda e: set_Players(matchs) if e.control.value else None, # Ação do dropdown para escolher a partida
        )
        
        right_screen.content.controls.append(chosen_Match)
        
        right_screen.content.controls.append(
            ft.FloatingActionButton(
                content = ft.Text("Começar", color = ft.Colors.WHITE, weight = 'bold', size = 20),
                bgcolor = ft.Colors.BLUE,
                width = 340,
                height = 40,
                on_click = lambda e: go_To_Game()
            )    
        )
        
        right_screen.content.update()
    
    
    
    def update_layout() -> None:
        '''Função usada para atualizar o layout da página do App.'''
        
        '''A palavra-chave nonlocal é usada para indicar que uma variável definida em um escopo externo (mas não global) será modificada dentro de uma função interna. 
        Ela permite alterar o valor de variáveis de funções envolventes sem precisar passá-las como parâmetro.'''
        nonlocal users, Player_1, Player_2, page_Game
        
        page.clean() # Limpa a página antes de adicionar novos elementos
        
        # Verifica se a página inicial está ativa
        if page_Home:
            
            # Verifica se a página do jogo está ativa
            if page_Game:
                
                # Verifica se os jogadores estão definidos
                if not player_1_Code and not player_2_Code:
                    # Cria um diálogo de alerta para informar que ambos os jogadores não estão definidos
                    alert = ft.AlertDialog(
                        title = ft.Text("Jogadores não definidos!"), # Define o título do diálogo de alerta
                        content = ft.Text(f"Ambos jogadores devem ser definidos para continuar!"), # Define o conteúdo do diálogo de alerta
                        # Define as ações do diálogo de alerta, que incluem um botão de fechar
                        actions = [
                            ft.TextButton("Fechar", on_click=lambda e: page.close(alert)) # Define a ação do botão de fechar para fechar o diálogo
                        ]
                    )
                    
                    page_Game = False # Desativa a página do jogo
                    page.add(ft.Row(controls = [left_screen, right_screen], expand = True)) # Adiciona a tela esquerda e direita à página
                    
                    page.open(alert) # Abre o diálogo de alerta para informar que ambos os jogadores não estão definidos
                
                # Verifica se apenas o jogador 1 não está definido
                elif not player_1_Code:
                    # Cria um diálogo de alerta para informar que o jogador 1 não está defin
                    alert = ft.AlertDialog(
                        title = ft.Text("Jogador não definido!"), # Define o título do diálogo de alerta
                        content = ft.Text(f"Jogador 1 precisa ser definido para continuar!"), # Define o conteúdo do diálogo de alerta
                        actions = [ 
                            ft.TextButton("Fechar", on_click=lambda e: page.close(alert)) # Define a ação do botão de fechar para fechar o diálogo
                        ]
                    )
                    page_Game = False # Desativa a página do jogo
                    page.add(ft.Row(controls = [left_screen, right_screen], expand = True)) # Adiciona a tela esquerda e direita à página
                    
                    page.open(alert) # Abre o diálogo de alerta para informar que o jogador 1 não está definido
                
                # Verifica se apenas o jogador 2 não está definido
                elif not player_2_Code:
                    # Cria um diálogo de alerta para informar que o jogador 2 não está definido
                    alert = ft.AlertDialog(
                        title = ft.Text("Jogador não definido!"), # Define o título do diálogo de alerta
                        content = ft.Text(f"Jogador 2 precisa ser definido para continuar!"), # Define o conteúdo do diálogo de alerta
                        # Define as ações do diálogo de alerta, que incluem um botão de fechar
                        actions = [
                            ft.TextButton("Fechar", on_click=lambda e: page.close(alert)) # Define a ação do botão de fechar para fechar o diálogo
                        ]
                    )
                    page_Game = False # Desativa a página do jogo
                    page.add(ft.Row(controls = [left_screen, right_screen], expand = True)) # Adiciona a tela esquerda e direita à página
                    
                    page.open(alert) # Abre o diálogo de alerta para informar que o jogador 2 não está definido
                    
                # Se ambos os jogadores estão definidos corretamente
                else:
                    # Cria um diálogo de alerta para informar que ambos os jogadores estão
                    page.add(
                        ft.Row(
                            controls = [
                                left_screen, # Tela esquerda do App
                                
                                # Tela direita do App com o jogo
                                ft.Column(
                                    controls = [
                                        ft.Row(
                                            controls = [
                                                ft.IconButton( # Botão de iniciar o jogo
                                                    icon = ft.Icons.CLOSE, # Ícone do botão
                                                    tooltip = 'Encerrar partida', # Tooltip do botão
                                                    icon_color = ft.Colors.ON_SURFACE_VARIANT, # Cor do ícone do botão
                                                    icon_size = 60, # Tamanho do ícone do botão
                                                    on_click = lambda e: go_To_Home() # Ação do botão para voltar à página inicial
                                                ),
                                                
                                                
                                                # Botão de reiniciar a partida
                                                ft.IconButton( 
                                                    icon = ft.Icons.REFRESH, # Ícone do botão
                                                    tooltip = 'Reiniciar partida', # Tooltip do botão
                                                    icon_color = ft.Colors.ON_SURFACE_VARIANT, # Cor do ícone do botão
                                                    icon_size = 60, # Tamanho do ícone do botão
                                                    alignment = ft.alignment.center_right, # Alinhamento do botão
                                                    on_click = lambda e: go_To_Game() # Ação do botão para reiniciar a partida
                                                ),
                                            ],
                                            alignment = ft.MainAxisAlignment.SPACE_BETWEEN # Alinhamento dos botões na linha
                                        ),
                                        
                                        game(page, Player_1, Player_2, str(Points_To_Win), 
                                             str(Sets), str(chosen_tournament.value), str(chosen_Match.value),
                                             dataBase.get_DataBase(
                                                 f'select fase from partida where id = {chosen_Match.value};' # Obtém a fase da partida selecionada
                                             ).values[0][0] # Obtém o valor da fase da partida selecionada
                                            ) # Chama a função game para iniciar o jogo com os jogadores selecionados e as configurações definidas
                                    ],
                                    horizontal_alignment = ft.CrossAxisAlignment.CENTER, # Alinhamento horizontal da coluna
                                    alignment = ft.MainAxisAlignment.SPACE_BETWEEN, # Alinhamento vertical da coluna
                                    expand = True # Expande a coluna para ocupar todo o espaço disponível
                                )
                            ],
                            expand = True # Expande a linha para ocupar todo o espaço disponível
                        )
                    )
            
            # Verifica se a página do jogo não está ativa
            else:
                page.add(ft.Row(controls = [left_screen, right_screen], expand = True)) # Adiciona a tela esquerda e direita à página
                
                users = dataBase.get_DataBase(
                    '''
                    select nome, sobrenome, concat(nome, ' ', sobrenome) as nome_completo, id_time, "id_país", sexo, senha from atleta
                    order by nome asc;
                    '''.replace('  ', '')
                ) # Obtém os dados dos atletas do banco de dados

        # Verifica se a página de ranking detalhado está ativa
        elif page_RankingDetalhado:
            page.add(ft.Row(controls = [left_screen, RankingDetalhado(page)], expand = True)) # Adiciona a tela esquerda e a página de ranking detalhado à página

        # Verifica se a página de cadastro de jogadores está ativa
        else:
            
            page.add(ft.Row(controls = [left_screen, Signup(page, dataBase)], expand = True)) # Adiciona a tela esquerda e a página de cadastro de jogadores à página
        
        page.update() # Atualiza a página para refletir as mudanças feitas


    if dataBase.verify_connection():
        
        # Conteúdo a esquerda do App
        left_screen = ft.Container(
            content = ft.Column(
                controls = [
                    ft.Column(
                        controls = [
                            ft.IconButton(
                                icon = ft.Icons.MENU, # Ícone do botão de menu
                                icon_color = ft.Colors.ON_SURFACE_VARIANT, # Cor do ícone do botão de menu
                                icon_size = 45, # Tamanho do ícone do botão de menu
                                height = 50, # Altura do botão de menu
                                alignment = ft.alignment.center # Alinhamento do botão de menu
                            ),

                            # Botão de ir para a página inicial
                            ft.IconButton(
                                tooltip = "Página Inicial", # Tooltip do botão de página inicial
                                icon = ft.Icons.SPORTS_ESPORTS, # Ícone do botão de página inicial
                                icon_color = ft.Colors.ON_SURFACE_VARIANT, # Cor do ícone do botão de página inicial
                                icon_size = 35, # Tamanho do ícone do botão de página inicial
                                height = 50, # Altura do botão de página inicial
                                alignment = ft.alignment.center, # Alinhamento do botão de página inicial
                                on_click = lambda e: go_To_Home() # Ação do botão para voltar à página inicial
                            ),

                            # Botão de ir para a página de ranking detalhado
                            ft.IconButton(
                                tooltip = "Cadastrar", # Tooltip do botão de cadastro
                                icon = ft.Icons.PERSON_ADD, # Ícone do botão de cadastro
                                icon_color = ft.Colors.ON_SURFACE_VARIANT, # Cor do ícone do botão de cadastro
                                icon_size = 35, # Tamanho do ícone do botão de cadastro
                                height = 50, # Altura do botão de cadastro
                                alignment = ft.alignment.center, # Alinhamento do botão de cadastro
                                on_click = lambda e: runSignup() # Ação do botão para ir para a página de cadastro de jogadores
                            ),

                            # Botão de ir para a página de ranking detalhado
                            ft.IconButton(
                                tooltip = "Ranking Completo dos Jogadores", # Tooltip do botão de ranking
                                icon = ft.Icons.EMOJI_EVENTS, # Ícone do botão de ranking
                                icon_color = ft.Colors.ON_SURFACE_VARIANT, # Cor do ícone do botão de ranking
                                icon_size = 35, # Tamanho do ícone do botão de ranking
                                on_click = lambda e: go_To_RankingDetalhado(), # Ação do botão para ir para a página de ranking detalhado
                                height = 50, # Altura do botão de ranking
                                alignment = ft.alignment.center # Alinhamento do botão de ranking
                            )
                        ]
                    ),
                    
                    ft.Column(
                        controls = [
                            # Botão de ir para a página de ranking geral
                            ft.IconButton(
                                tooltip = "Mudar tema", # Tooltip do botão de mudança de tema
                                icon = ft.Icons.BRIGHTNESS_6, # Ícone do botão de mudança de tema
                                icon_color = ft.Colors.ON_SURFACE_VARIANT, # Cor do ícone do botão de mudança de tema
                                icon_size = 25, # Tamanho do ícone do botão de mudança de tema
                                on_click = lambda e: change_Theme(), # Ação do botão para mudar o tema do App
                                height = 50, # Altura do botão de mudança de tema
                                alignment = ft.alignment.center # Alinhamento do botão de mudança de tema
                            ),
                            
                            # Botão de sair do App
                            ft.IconButton(
                                tooltip = "Sair", # Tooltip do botão de sair
                                icon = ft.Icons.EXIT_TO_APP, # Ícone do botão de sair
                                icon_color = ft.Colors.ON_SURFACE_VARIANT, # Cor do ícone do botão de sair
                                icon_size = 25, # Tamanho do ícone do botão de sair
                                on_click = lambda e: close_App(), # Ação do botão para fechar o App
                                height = 50, # Altura do botão de sair
                                alignment = ft.alignment.center # Alinhamento do botão de sair
                            )
                        ]
                    )
                ],
                alignment = ft.MainAxisAlignment.SPACE_BETWEEN # Alinhamento dos controles na coluna
            ),
            width = 50 # Largura da tela esquerda do App
        )
        
        
        users = dataBase.get_DataBase(
            '''
            select nome, sobrenome, concat(nome, ' ', sobrenome) as nome_completo, id_time, "id_país", sexo, senha from atleta
            order by nome asc;
            '''.replace('  ', '')
        ) # Obtém os dados dos atletas do banco de dados
        
        
        tournaments = DataBase().get_DataBase('select * from torneio order by id asc;') # Obtém os dados dos torneios do banco de dados
        
        
        # Tela direita do App com os controles de seleção de jogadores e configurações da partida
        right_screen = ft.Container(
            content = ft.Column(
                controls = [
                    chosen_tournament := ft.Dropdown( # Dropdown para escolher o torneio
                        label = "Escolha o Torneio", # Rótulo do dropdown
                        hint_text = "Selecione o torneio", # Texto de dica do dropdown
                        options = [
                            ft.dropdown.Option(key, tournament) # Cria uma opção para cada torneio obtido do banco de dados
                            
                            for key, tournament in tournaments[['id', 'nome']].values.tolist() # Itera sobre os torneios obtidos do banco de dados
                        ],
                        editable = True,
                        enable_filter = True,
                        menu_height = 300,
                        width = 340,
                        on_change = lambda e: Choice_match() if e.control.value else None # Ação do dropdown para escolher o torneio
                    ),
                    
                    chosen_Match := ft.Dropdown(
                        label= 'Escolha a Partida', # Rótulo do dropdown
                        hint_text= 'Selecione a partida', # Texto de dica do dropdown
                        width = 340
                    )
                ],
                horizontal_alignment = ft.CrossAxisAlignment.CENTER, # Alinhamento horizontal da coluna
                alignment = ft.MainAxisAlignment.CENTER, # Alinhamento vertical da coluna
                spacing = 100 # Espaçamento entre os controles na coluna
            ),
            # height = 700,
            expand = True # Expande a tela direita para ocupar todo o espaço disponível
        )
        
        update_layout() # Atualiza o layout da página do App
    
    else:
        page.add(
            ft.Container(
                content = ft.Text(
                    "Erro ao conectar ao banco de dados! 😥\nEntre em contato com o Suporte para resolver esse pro", # Mensagem de erro ao conectar ao banco de dados
                    size = 30, # Tamanho do texto
                    weight = ft.FontWeight.BOLD, # Peso do texto
                ),
                alignment = ft.alignment.center, # Alinhamento do texto no centro
                expand = True # Expande o container para ocupar todo o espaço disponível
            )
        )
        page.update()


if __name__ == "__main__":
    # Inicia o App
    ft.app(target=main, name='Tênis de Mesa', use_color_emoji = True) # Inicia o App com o nome 'Tênis de Mesa' e ativa o uso de emojis coloridos
