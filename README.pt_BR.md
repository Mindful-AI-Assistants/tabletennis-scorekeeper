
<br>

\[**[🇧🇷Português](README.pt_BR.md)**\] \[[🇺🇸English](README.md)\]

  <!--  START HEADER  -->

<br>


  <!--  START HEADER  -->
## <p align = "center" > 🏓 SmartPing: Aplicativo de Assistente de Placar e Torneio de Tênis de Mesa 
#### <p align = "center" > Aplicativo de Pontuação de Tênis de Mesa; Um aplicativo inteligente para gerenciar os placares de tênis de mesa e as classificações dos jogadores. Construído como um projeto final para o curso de NoSQL (PUC-SP).


 
  <br><br>

#### <p align="center"> [![Sponsor Mindful AI Assistants](https://img.shields.io/badge/Sponsor-Mindful%20AI%20%20Assistants-brightgreen?logo=GitHub)](https://github.com/sponsors/Mindful-AI-Assistants)

<br><br>



# Trabalho Final - Atividade Extensionista  
### Disciplina: NoSQL  
### Curso: Ciência de Dados e Humanistic AI - PUC-SP  
### Data de Entrega: 27 de Junho de 2025

---

## Sumário

1. [Briefing](#1-briefing)  
2. [Explicação do Projeto](#2-explicação-do-projeto)  
3. [Participantes do Grupo](#3-participantes-do-grupo)  
4. [Principais Códigos do Projeto](#4-principais-códigos-do-projeto)  
   4.1 [Signup.py - Tela de Cadastro](#41-signuppy---tela-de-cadastro)  
   4.2 [main.py - Controle do App](#42-mainpy---controle-do-app)  
   4.3 [Exemplo de Container lateral (left_screen)](#43-exemplo-de-container-lateral-left_screen)  
5. [Modelos Conceitual e Lógico](#5-modelos-conceitual-e-lógico)  
6. [Queries e Perguntas para o Banco de Dados](#6-queries-e-perguntas-para-o-banco-de-dados)  
7. [Próximos Passos / Possibilidades Futuras](#7-próximos-passos--possibilidades-futuras)  
8. [Referências e Ferramentas Utilizadas](#8-referências-e-ferramentas-utilizadas)  

---

## 1. Briefing

Este trabalho final integra a atividade extensionista prevista na Unidade Curricular CEAPI - Banco de Dados (BD).  

**Objetivos do trabalho:**  
- Identificação dos atores envolvidos (Personas)  
- Criação do Modelo Conceitual da proposta  
- Criação do Modelo Lógico da proposta  
- Popular o Banco de Dados com pelo menos 5 registros  
- Desenvolvimento do Modelo Físico da proposta  
- Criação de 10 perguntas e suas queries correspondentes para o banco de dados  
- Desenvolvimento de aplicativo(s) para uso da base e consulta  

**O que deve ser entregue:**  
1. Relatório da atividade extensionista conforme modelo  
2. Apresentação do projeto da UC  
3. Modelos (Conceitual, Lógico e Físico)  
4. Execução das queries  

---

## 2. Explicação do Projeto

O aplicativo desenvolvido tem como finalidade facilitar o controle da pontuação em partidas de Tênis de Mesa. Ele elimina a necessidade de placares físicos e automatiza o processo de classificação dos jogadores para as próximas etapas dos torneios.  

Embora o sistema atual seja um protótipo, há potencial para automatizar 100% da pontuação usando sensores na mesa e na bolinha, para registrar automaticamente os pontos. Porém, devido a possíveis erros, a presença de um juiz ainda é essencial para validar a pontuação.  

O projeto visa:  
- Facilitar a contabilização dos pontos nas partidas;  
- Permitir a criação e gestão de equipes;  
- Futuramente, possibilitar a criação e controle de torneios;  
- Otimizar a classificação dos jogadores, tornando o trabalho dos organizadores mais simples e eficiente.

---

## 3. Participantes do Grupo

| Nome Completo                | Contato                  |
|-----------------------------|--------------------------|
| João Silva                  | joao.silva@email.com     |
| Maria Oliveira              | maria.oliveira@email.com |
| Lucas Fernandes             | lucas.fernandes@email.com|
| Ana Paula Santos            | ana.santos@email.com     |
| Fabiana Rotella Campanari   | fabiana.campanari@email.com |

---

## 4. Principais Códigos do Projeto

### 4.1 Signup.py - Tela de Cadastro

```python
import flet as ft
from DataBase import DataBase

def Signup(page: ft.Page, conn: DataBase) -> ft.Ref[ft.Column]:
    Accound_Confirmation = False
    Container_SignUp = ft.Ref[ft.Column]()
    
    def Accound_Verification() -> None:
        nonlocal Accound_Confirmation
        # Validações dos campos de cadastro para Atleta e Time
        # Configura mensagens de erro e ajusta layout dinamicamente
        # Se tudo correto, seta Accound_Confirmation = True e atualiza layout
        
    def update_layout() -> None:
        nonlocal Container_SignUp, Accound_Confirmation
        # Atualiza layout conforme estado de confirmação de cadastro
        # Insere dados no banco ao confirmar
    
    # Construção inicial do layout de cadastro, com dropdown para tipo e campos correspondentes
    
    update_layout()
    return Container_SignUp.current
























































<br><br><br><br>


#### <p align="center">  🛸๋ My Contacts [Hub](https://linktr.ee/fabianacampanari)


<br>

### <p align="center"> <img src="https://github.com/user-attachments/assets/517fc573-7607-4c5d-82a7-38383cc0537d" />


<br><br>

<p align="center">  ────────────── ⊹🔭๋ ──────────────

<br>

<p align="center"> ➣➢➤ <a href="#top">Back to Top </a>
  

  
#
 
##### <p align="center">Copyright 2025 Mindful-AI-Assistants. Code released under the  [MIT license.]( https://github.com/Mindful-AI-Assistants/.github/blob/ad6948fdec771e022d49cd96f99024fcc7f1106a/LICENSE)

