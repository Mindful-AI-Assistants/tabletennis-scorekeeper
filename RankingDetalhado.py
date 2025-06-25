import flet as ft # Import a biblioteca Flet para criar do App
from DataBase import DataBase 


def RankingDetalhado(page: ft.Page) -> ft.Column | ft.Container:
    """Função que cria a tela de Ranking Detalhado do App."""
    Container_Ranking = ft.Ref[ft.Container]() # Cria uma referência para o Container de Ranking
    
    tournament = DataBase().get_DataBase('SELECT * FROM torneio order by id;') # Obtém os dados do torneio do banco de dados
    
    def upload_layout() :
        nonlocal Container_Ranking, steps

        matchs = DataBase().get_DataBase(
            'select p.id as id, p.id_torneio as id_torneio, p.fase as fase, p.proxima_fase as proxima_fase,'+
            '\nconcat(a.nome, \' \', a.sobrenome) as nome_completo,' +
            '\nap.set as set' +
            '\nfrom atleta_partida ap' +
            '\ninner join partida p on p.id = ap.id_partida' +
            '\ninner join atleta a on a.id = ap.id_atleta' +
            f'\nwhere p.id_torneio = {tournament_Options.value} ' +
            '\norder by p.id asc;'
        ) # Obtém os dados das partidas do banco de dados
        
        
        games = DataBase().get_DataBase(
            f'select * from partida where id_torneio = {tournament_Options.value} order by id asc;'
        )
        
        print(matchs.loc[0, 'fase'])
        steps = steps[steps.index(matchs.loc[0, 'fase']) :] # Obtém o índice da fase da primeira partida
        steps = [(30, 'Round of 128'), (140, 'Round of 64'), (360, 'Round of 32'), (800, 'Round of 16'), (1700, 'Quartas'), (3500, 'Semifinais'), (0, 'Final')]
        
        Container_Ranking.current.content.controls.clear()
        Container_Ranking.current.content.controls.append(tournament_Options)
        
        Container_Ranking.current.content.controls.append(
            ft.Row(
                controls =
                [
                    ft.Column(
                        controls =[
                            ft.Text(step.upper(), size = 25, weight = ft.FontWeight.BOLD),
                            ft.Column(
                                controls = [
                                    ft.Container(
                                        content = ft.Column(
                                            controls = [
                                                ft.Row(
                                                    controls = [
                                                        ft.Text(
                                                            '   ' if matchs[matchs['id'] == key].empty else matchs.loc[matchs['id'] == key, 'nome_completo'].values[0],
                                                            size = 20,
                                                            color = ft.Colors.BLACK
                                                        ),
                                                        
                                                        ft.Text(
                                                            '   ' if matchs[matchs['id'] == key].empty else matchs.loc[matchs['id'] == key, 'set'].values[0],
                                                            size = 20,
                                                            color = ft.Colors.BLACK
                                                        )
                                                    ],
                                                    alignment = ft.MainAxisAlignment.SPACE_BETWEEN
                                                ),
                                                
                                                
                                                ft.Divider(height=1, thickness=2, color=ft.Colors.GREY),
                                                
                                                
                                                ft.Row(
                                                    controls = [
                                                        ft.Text(
                                                            '   ' if matchs[matchs['id'] == key].empty or matchs[matchs['id'] == key].shape[0] < 2 else matchs.loc[matchs['id'] == key, 'nome_completo'].values[1],
                                                            size = 20,
                                                            color = ft.Colors.BLACK
                                                        ),
                                                        
                                                        ft.Text(
                                                            '   ' if matchs[matchs['id'] == key].empty or matchs[matchs['id'] == key].shape[0] < 2 else matchs.loc[matchs['id'] == key, 'set'].values[1],
                                                            size = 20,
                                                            color = ft.Colors.BLACK
                                                        )
                                                    ],
                                                    alignment = ft.MainAxisAlignment.SPACE_BETWEEN
                                                )
                                            ],
                                            spacing = 0,
                                            alignment = ft.MainAxisAlignment.CENTER
                                        ),
                                        bgcolor = ft.Colors.WHITE,
                                        width = 300,
                                        height = 80,
                                        border_radius = 10,
                                        padding = ft.padding.only(top=10, left=8, right=8),
                                        alignment = ft.alignment.center,
                                        border = ft.border.all(color = ft.Colors.GREY)
                                    )
                                    
                                    for key in games.loc[games['fase'] == step, 'id'].values
                                ],
                                alignment = ft.MainAxisAlignment.SPACE_BETWEEN,
                                spacing = space
                            )
                        ],
                        adaptive = ft.MainAxisAlignment.START,
                        expand = True
                    )
                    
                    for space, step in steps
                ],
                spacing = 20,
                scroll = ft.ScrollMode.AUTO,
                alignment = ft.MainAxisAlignment.START,
            )
        )
        
        
        Container_Ranking.current.update()
        
        
    steps = ['Round of 128', 'Round of 64', 'Round of 32', 'Round of 16', 'Quartas', 'Semifinais', 'Final']
    
    Container_Ranking.current = ft.Container(
        content = ft.Column(
            controls = [
                tournament_Options := ft.Dropdown(
                    value = tournament.loc[0, 'id'],
                    label = 'Torneios: ',
                    hint_text = 'Selecione um torneio',
                    menu_height = 300,
                    color= ft.Colors.ON_SURFACE_VARIANT,
                    options = [
                        ft.dropdown.Option(key, name)
                        for key, name in tournament[['id', 'nome']].values.tolist()
                    ],
                    editable = True,
                    enable_filter = True,
                    on_change = lambda e: upload_layout(),
                    expand = True
                )
            ],
            scroll = ft.ScrollMode.AUTO,
            expand = True
        ),
        expand = True
    )
    
    return Container_Ranking.current
