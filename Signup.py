import flet as ft
import pandas as pd
from DataBase import DataBase # Importando a classe DataBase para manipulação do DataBase



def Signup(page: ft.Page, conn: DataBase) -> ft.Ref[ft.Column]:
    Accound_Confirmation = False
    Container_SignUp = ft.Ref[ft.Column]()
    
    
    def Accound_Verification() -> None:
        nonlocal Accound_Confirmation, TextField_First_Name, TextField_Last_Name
        TextField_First_Name.value = TextField_First_Name.value.strip()
        TextField_Last_Name.value = TextField_Last_Name.value.strip()
        
        
        
        if option_SignUp.value == 'Atleta':
            TextField_First_Name.error = False
            TextField_First_Name.error_text = ""
            
            TextField_Sexo.error = False
            TextField_Sexo.error_text = ""
            
            TextField_Contry.error = False
            TextField_Contry.error_text = ""
            
            TextField_New_Password.error = False
            TextField_New_Password.error_text = ""
            
            TextField_Confirm_New_Password.error = False
            TextField_Confirm_New_Password.error_text = ""
            
            TextField_ADM_Code.error = False
            TextField_ADM_Code.error_text = ""
            
            Container_SignUp.current.height = 520
            Container_SignUp.current.controls[1].height = 520
            
            
            # Check if the username is valid
            if TextField_First_Name.value == '':
                TextField_First_Name.error = True
                TextField_First_Name.error_text = "* Campo obrigatório"
                Container_SignUp.current.height += 20
                Container_SignUp.current.controls[1].height += 20


            if TextField_Sexo.value == '':
                TextField_Sexo.error = True
                TextField_Sexo.error_text = "* Campo obrigatório"
                Container_SignUp.current.height += 20
                Container_SignUp.current.controls[1].height += 20
            
            
            if TextField_Contry.value == '':
                TextField_Contry.error = True
                TextField_Contry.error_text = "* Campo obrigatório"
                Container_SignUp.current.height += 20
                Container_SignUp.current.controls[1].height += 20


            # Check if the password is valid
            if TextField_New_Password.value == '':
                TextField_New_Password.error = True
                TextField_New_Password.error_text = "* Campo obrigatório"
                Container_SignUp.current.height += 20
                Container_SignUp.current.controls[1].height += 20
                
            
            if TextField_Confirm_New_Password.value == '':
                TextField_Confirm_New_Password.error = True
                TextField_Confirm_New_Password.error_text = "* Campo obrigatório"
                Container_SignUp.current.height += 20
                Container_SignUp.current.controls[1].height += 20
                
            
            if TextField_New_Password.value != TextField_Confirm_New_Password.value:
                TextField_New_Password.error = True
                TextField_New_Password.error_text = "* As senhas não coincidem"
                Container_SignUp.current.height += 20
                Container_SignUp.current.controls[1].height += 20
                
                TextField_Confirm_New_Password.error = True
                TextField_Confirm_New_Password.error_text = "* As senhas não coincidem"
                Container_SignUp.current.height += 20
                Container_SignUp.current.controls[1].height += 20
                
            
            # Check if the ADM code is valid
            if TextField_ADM_Code.value == '':
                TextField_ADM_Code.error = True
                TextField_ADM_Code.error_text = "* Campo obrigatório"
                Container_SignUp.current.height += 20
                Container_SignUp.current.controls[1].height += 20 
            
            elif TextField_ADM_Code.value != 'Adm123':
                TextField_ADM_Code.error = True
                TextField_ADM_Code.error_text = "* Código inválido"
                Container_SignUp.current.height += 20
                Container_SignUp.current.controls[1].height += 20


            if not (((((TextField_First_Name.error or TextField_New_Password.error) or TextField_Confirm_New_Password.error) or TextField_ADM_Code.error) or TextField_Sexo.error) or TextField_Contry.error):
                Accound_Confirmation = True
                update_layout()
        
        else:
            TextField_Team_Name.error = False
            TextField_Team_Name.error_text = ""
            Container_SignUp.current.height = 250
            Container_SignUp.current.controls[1].height = 250
            
            if TextField_Team_Name.value == '':
                TextField_Team_Name.error = True
                TextField_Team_Name.error_text = "* Campo obrigatório"
                Container_SignUp.current.height += 20
                Container_SignUp.current.controls[1].height += 20
            
            elif TextField_Team_Name.value.strip().lower() in [team.lower() for team in database_Team['nome'].values]:
                TextField_Team_Name.error = True
                TextField_Team_Name.error_text = "* Este nome de time já está em uso."
                Container_SignUp.current.height += 20
                Container_SignUp.current.controls[1].height += 20
            
            
            if not TextField_Team_Name.error:
                Accound_Confirmation = True
                update_layout()
            
            
        page.update()
    
    
    def new_signup() -> None:
        nonlocal Accound_Confirmation, Container_SignUp, option_SignUp

        Container_SignUp.current.height = 520
        option_SignUp.value = 'Atleta'
        
        Accound_Confirmation = False
        update_layout()
        
        page.update()
    
    
    def update_layout() -> None:
        nonlocal Container_SignUp, Accound_Confirmation, TextField_Confirm_New_Password
        
        if Accound_Confirmation:
            Container_SignUp.current.controls.clear()
            Container_SignUp.current.controls.append(
                ft.Column(
                    controls = [
                        ft.Container(
                            content = ft.Column(
                                controls = [
                                    ft.Row(
                                        controls = [
                                            ft.Icon(
                                                name = ft.Icons.AUTORENEW,
                                                color = ft.Colors.BLACK,
                                                weight = 'bold',
                                                size = 25
                                            ),
                                            
                                            ft.Text(
                                            "Cadastrando jogador!!" if option_SignUp.value == 'Atleta' else "Cadastrando time!!",
                                                size = 25,
                                                weight = 'bold',
                                                color = ft.Colors.BLACK
                                            )
                                        ]
                                    )
                                ],
                                alignment = ft.MainAxisAlignment.CENTER,
                                horizontal_alignment = ft.CrossAxisAlignment.CENTER
                            ),
                            width = 450,
                            height = 240,
                            bgcolor = ft.Colors.WHITE,
                            border_radius = 10,
                            padding = ft.padding.only(top=10, left=8, right=8)
                        )
                    ],
                    expand = True,
                    alignment = ft.MainAxisAlignment.CENTER,
                    horizontal_alignment = ft.CrossAxisAlignment.CENTER
                )
            )
            page.update()
            
            
            try:
                conn = DataBase()
                
                if option_SignUp.value == 'Atleta':
                    conn.insert_Player(
                        'atleta', 
                        '(nome, sobrenome, id_time, "id_país", sexo, senha)',
                        (
                            TextField_First_Name.value.strip(),
                            TextField_Last_Name.value.strip() if TextField_Last_Name.value != '' else None,
                            int(TextField_Team.value) if TextField_Team.value != '' else None,
                            int(TextField_Contry.value),
                            TextField_Sexo.value,
                            TextField_New_Password.value
                        )
                    )
                
                else:
                    conn.insert_Player(
                        'time', 
                        '(nome)',
                        (TextField_Team_Name.value.strip(),)
                    )
                
                conn.close()
                
                Container_SignUp.current.controls.clear()
                Container_SignUp.current.controls.append(
                    ft.Column(
                        controls = [
                            ft.Container(
                                content = ft.Column(
                                    controls = [
                                        ft.Row(
                                            controls = [
                                                ft.Icon(
                                                    name = ft.Icons.CHECK,
                                                    color = ft.Colors.GREEN,
                                                    weight = 'bold',
                                                    size = 25
                                                ),
                                                
                                                ft.Text(
                                                "Cadastro realizado com sucesso!!",
                                                    size = 25,
                                                    weight = 'bold',
                                                    color = ft.Colors.GREEN
                                                )
                                            ]
                                        ),
                                        
                                        ft.Text(
                                            '\n',
                                            size = 15
                                        ),
                                        
                                        ft.FloatingActionButton(
                                            content = ft.Text("Novo Cadastro", color = ft.Colors.WHITE, weight = 'bold', size = 20),
                                            bgcolor = ft.Colors.BLUE,
                                            width = 340,
                                            height = 40,
                                            on_click = lambda e: new_signup()
                                        )
                                    ],
                                    alignment = ft.MainAxisAlignment.CENTER,
                                    horizontal_alignment = ft.CrossAxisAlignment.CENTER
                                ),
                                width = 450,
                                height = 240,
                                bgcolor = ft.Colors.WHITE,
                                border_radius = 10,
                                padding = ft.padding.only(top=10, left=8, right=8)
                            )
                        ],
                        expand = True,
                        alignment = ft.MainAxisAlignment.CENTER,
                        horizontal_alignment = ft.CrossAxisAlignment.CENTER
                    )
                )
            
            except:
                Container_SignUp.current.controls.clear()
                Container_SignUp.current.controls.append(
                    ft.Column(
                        controls = [
                            ft.Container(
                                content = ft.Column(
                                    controls = [
                                        ft.Row(
                                            controls = [
                                                ft.Icon(
                                                    name = ft.Icons.CLOSE,
                                                    color = ft.Colors.RED,
                                                    weight = 'bold',
                                                    size = 25
                                                ),
                                                
                                                ft.Text(
                                                "Falha no cadastro, por favor tente novamente!!",
                                                    size = 25,
                                                    weight = 'bold',
                                                    color = ft.Colors.RED
                                                )
                                            ]
                                        ),
                                        
                                        ft.Text(
                                            '\n',
                                            size = 15
                                        ),
                                        
                                        ft.FloatingActionButton(
                                            content = ft.Text("Novo Cadastro", color = ft.Colors.WHITE, weight = 'bold', size = 20),
                                            bgcolor = ft.Colors.BLUE,
                                            width = 340,
                                            height = 40,
                                            on_click = lambda e: new_signup()
                                        )
                                    ],
                                    alignment = ft.MainAxisAlignment.CENTER,
                                    horizontal_alignment = ft.CrossAxisAlignment.CENTER
                                ),
                                width = 450,
                                height = 240,
                                bgcolor = ft.Colors.WHITE,
                                border_radius = 10,
                                padding = ft.padding.only(top=10, left=8, right=8)
                            )
                        ],
                        expand = True,
                        alignment = ft.MainAxisAlignment.CENTER,
                        horizontal_alignment = ft.CrossAxisAlignment.CENTER
                    )
                )
            
            TextField_First_Name.value = ''
            TextField_Last_Name.value = ''
            TextField_Team.value = ''
            TextField_Team_Name.value = ''
            TextField_Sexo.value = ''
            TextField_Contry.value = ''
            TextField_New_Password.value = ''
            TextField_Confirm_New_Password.value = ''
            TextField_ADM_Code.value = ''


        else:
            Container_SignUp.current.controls.clear()

            Container_SignUp.current.controls.append(option_SignUp)
            Container_SignUp.current.controls.append(
                atleta if option_SignUp.value == 'Atleta' else team
            )


        page.update()


    def UsernameOn_Autofocus_Next():
        nonlocal TextField_New_Password
        TextField_New_Password.focus()
        page.update()


    def PasswordOn_Autofocus_Next():
        nonlocal TextField_Confirm_New_Password
        TextField_Confirm_New_Password.focus()
        page.update()


    def Confirm_PasswordOn_Autofocus_Next():
        nonlocal TextField_ADM_Code
        TextField_ADM_Code.focus()
        page.update()


    database_Team = conn.get_DataBase("SELECT * FROM time ORDER BY nome ASC")
    database_Contry = conn.get_DataBase('SELECT * FROM "país" ORDER BY nome ASC')
    
    
    atleta = ft.Container(
        content = ft.Column(
            controls = [
                ft.Text(
                    "Cadastro Atleta",
                    size = 25,
                    weight = 'bold',
                    color = ft.Colors.BLACK
                ),
                
                
                TextField_First_Name := ft.TextField(
                    label = "Nome: ",
                    hint_text = "Digite o seu primeiro nome",
                    max_length = 50,
                    prefix_icon = ft.Icons.PERSON,
                    border = ft.InputBorder.UNDERLINE,
                    color = ft.Colors.BLACK,
                    keyboard_type = ft.KeyboardType.TEXT,
                    input_filter = ft.InputFilter(
                        regex_string = r"[0-9!@#$%&=*/+{}()?|\\ªº~^]*$",
                        allow = False
                    ),
                    on_submit = lambda e: UsernameOn_Autofocus_Next(),
                    autofocus = True
                ),
                
                
                TextField_Last_Name := ft.TextField(
                    value = '',
                    label = "Sobrenome: ",
                    hint_text = "Digite o seu sobrenome",
                    max_length = 50,
                    prefix_icon = ft.Icons.PERSON,
                    border = ft.InputBorder.UNDERLINE,
                    color = ft.Colors.BLACK,
                    keyboard_type = ft.KeyboardType.TEXT,
                    input_filter = ft.InputFilter(
                        regex_string = r"[0-9!@#$%&=*/+{}()?|\\ªº~^]*$",
                        allow = False
                    ),
                    on_submit = lambda e: UsernameOn_Autofocus_Next(),
                    autofocus = True
                ),


                ft.Row(
                    controls = [
                        TextField_Sexo := ft.Dropdown(
                            value = '',
                            label = 'Sexo: ',
                            hint_text = 'Selecione o seu sexo',
                            color= ft.Colors.BLACK,
                            options = [
                                ft.dropdown.Option('M', 'Masculino'),
                                ft.dropdown.Option('F', 'Feminino')
                            ],
                            expand = True,
                        ),
                        
                        TextField_Team := ft.Dropdown(
                            value = '',
                            label = 'Equipe: ',
                            hint_text = 'Selecione a sua equipe',
                            menu_height = 300,
                            color= ft.Colors.BLACK,
                            options = [ft.dropdown.Option('', 'Sem time')] + [
                                ft.dropdown.Option(str(ident), team) for ident, team in database_Team.values
                            ],
                            editable = True,
                            enable_filter = True,
                            expand = True
                        )
                    ],
                    expand = True
                ),
                
                
                TextField_Contry := ft.Dropdown(
                    value = '',
                    label = 'País: ',
                    hint_text = 'Selecione o país de origem',
                    color= ft.Colors.BLACK,
                    menu_height = 300,
                    options = [
                        ft.dropdown.Option(str(ident), contry) for ident, contry in database_Contry.values
                    ],
                    editable = True,
                    enable_search = True,
                    expand = True,
                ),


                TextField_New_Password := ft.TextField(
                    label = "Senha: ",
                    hint_text = "Digite sua Senha",
                    max_length = 100,
                    prefix_icon = ft.Icons.LOCK,
                    keyboard_type = ft.KeyboardType.VISIBLE_PASSWORD,
                    color = ft.Colors.BLACK,
                    password = True,
                    can_reveal_password = True,
                    border = ft.InputBorder.UNDERLINE,
                    input_filter = ft.InputFilter(
                        regex_string = r'^[a-zA-Z0-9_@$!%*?&#]*$',
                        allow = False
                    ),
                    on_submit = lambda e: PasswordOn_Autofocus_Next()
                ),


                TextField_Confirm_New_Password := ft.TextField(
                    label = "Confirme sua senha: ",
                    hint_text = "Digite sua senha",
                    max_length = 100,
                    prefix_icon = ft.Icons.LOCK_OUTLINE,
                    keyboard_type = ft.KeyboardType.VISIBLE_PASSWORD,
                    color = ft.Colors.BLACK,
                    password = True,
                    can_reveal_password = True,
                    border = ft.InputBorder.UNDERLINE,
                    input_filter = ft.InputFilter(
                        regex_string = r'^[a-zA-Z0-9_@$!%*?&#]*$',
                        allow = False
                    ),
                    on_submit = lambda e: Confirm_PasswordOn_Autofocus_Next()
                ),

                
                TextField_ADM_Code := ft.TextField(
                    label = "Código do Administrador: ",
                    hint_text = "Digite a senha do Administrador",
                    max_length = 100,
                    prefix_icon = ft.Icons.KEY_OUTLINED,
                    keyboard_type = ft.KeyboardType.VISIBLE_PASSWORD,
                    color = ft.Colors.BLACK,
                    password = True,
                    can_reveal_password = True,
                    border = ft.InputBorder.UNDERLINE,
                    input_filter = ft.InputFilter(
                        regex_string = r'^[a-zA-Z0-9_@$!%*?&#]*$',
                        allow = False
                    ),
                    on_submit = lambda e: Accound_Verification()
                ),


                ft.FloatingActionButton(
                    content = ft.Text("Cadastrar", color = ft.Colors.WHITE, weight = 'bold', size = 20),
                    bgcolor = ft.Colors.BLUE,
                    width = 340,
                    height = 40,
                    on_click = lambda e: Accound_Verification()
                )
            ],
            alignment = ft.MainAxisAlignment.CENTER
        ),
                
        
        width = 340,
        height = 520,
        bgcolor = ft.Colors.WHITE,
        border_radius = 10,
        padding = ft.padding.only(top=10, left=8, right=8)
    )
    
    
    team = ft.Container(
        content = ft.Column(
            controls = [
                ft.Text(
                    "Cadastro Time",
                    size = 25,
                    weight = 'bold',
                    color = ft.Colors.BLACK
                ),


                TextField_Team_Name := ft.TextField(
                    label = "Nome do Time: ",
                    hint_text = "Digite nome do time",
                    max_length = 50,
                    prefix_icon = ft.Icons.GROUP_ADD,
                    border = ft.InputBorder.UNDERLINE,
                    color = ft.Colors.BLACK,
                    keyboard_type = ft.KeyboardType.TEXT,
                    input_filter = ft.InputFilter(
                        regex_string = r"^[a-zA-Z\u00C0-\u00FF ]*$",
                        allow = False
                    ),
                    autofocus = True,
                    on_submit = lambda e: Accound_Verification()
                ),


                ft.FloatingActionButton(
                    content = ft.Text("Cadastrar", color = ft.Colors.WHITE, weight = 'bold', size = 20),
                    bgcolor = ft.Colors.BLUE,
                    width = 340,
                    height = 40,
                    on_click = lambda e: Accound_Verification()
                )
            ],
            alignment = ft.MainAxisAlignment.CENTER
        ),
                
        
        width = 340,
        height = 250,
        bgcolor = ft.Colors.WHITE,
        border_radius = 10,
        padding = ft.padding.only(top=10, left=8, right=8)
    )
    
    
    Container_SignUp.current = ft.Column(
        controls = [
            option_SignUp := ft.Dropdown(
                value = 'Atleta',
                label = 'Tipo de Cadastro: ',
                hint_text = 'Selecione o tipo de cadastro',
                border_color = ft.Colors.ON_SURFACE_VARIANT,
                
                options = [
                    ft.dropdown.Option('Atleta', 'Atleta'),
                    ft.dropdown.Option('Time', 'Time'),
                ],
                on_change = lambda e: update_layout(),
                width = 340
            )
        ],
        expand = True,
        alignment = ft.MainAxisAlignment.CENTER,
        horizontal_alignment = ft.CrossAxisAlignment.CENTER
    )
    
    
    update_layout()
    
    return Container_SignUp.current
