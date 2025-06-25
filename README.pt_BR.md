
<br>

\[**[🇧🇷Português](README.pt_BR.md)**\] \[[🇺🇸English](README.md)\]

  <!--  START HEADER  -->

<br>


  <!--  START HEADER  -->
## <p align = "center" > 🏓 SmartPing: Aplicativo de Assistente de Placar e Torneio de Tênis de Mesa 
#### <p align = "center" > Aplicativo de Pontuação de Tênis de Mesa; Um aplicativo inteligente para gerenciar os placares de tênis de mesa e as classificações dos jogadores. Construído como um projeto final de Atividade Extensionista  para o curso de NoSQL da graduação em Ciência de Dados e Humanistic AI - PUC-SP  


 
  <br><br>

#### <p align="center"> [![Sponsor Mindful AI Assistants](https://img.shields.io/badge/Sponsor-Mindful%20AI%20%20Assistants-brightgreen?logo=GitHub)](https://github.com/sponsors/Mindful-AI-Assistants)




<br><br>

 <p align="center">
<img src="https://github.com/user-attachments/assets/5001ffb7-9bc1-4228-a38f-af5f1e2d6677"/>

<br><br>





# Trabalho Final - 
### Disciplina: NoSQL  
### Curso: 
### Data de Entrega: 27 de Junho de 2025

<br>

## Table of Contents

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

<br>

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

<br>

## 2. Explicação do Projeto

O aplicativo desenvolvido tem como finalidade facilitar o controle da pontuação em partidas de Tênis de Mesa. Ele elimina a necessidade de placares físicos e automatiza o processo de classificação dos jogadores para as próximas etapas dos torneios.  

Atualmente, o projeto encontra-se em estágio protótipo, com potencial para alcançar automação total da pontuação e classificação dos jogadores por meio da implementação de sensores na mesa e na bolinha. Esses sensores possibilitariam a contagem automática dos pontos marcados, embora a supervisão humana (juiz) permaneça essencial para garantir a correção e prevenir erros.


O foco está em simplificar e tornar mais eficiente o trabalho dos organizadores de eventos esportivos, proporcionando um ambiente digital moderno e confiável para o gerenciamento das competições.

O sistema permite:

- Facilitar a contabilização dos pontos nas partidas;  
- Permitir a criação e gestão de equipes;  
- Futuramente, possibilitar a criação e controle de torneios;  
- Otimizar a classificação dos jogadores, tornando o trabalho dos organizadores mais simples e eficiente.
- Visualização e atualização dinâmica do ranking dos atletas.

<br>

## 3. Atividade Extensionista

Para contemplar a Unidade Curricular, realizamos as seguintes etapas:

| Etapa                                | Descrição                                                                                  |
|-------------------------------------|--------------------------------------------------------------------------------------------|
| Identificação dos atores (Personas) | Definimos perfis dos usuários do sistema: jogadores, juízes, organizadores e público.      |
| Modelo Conceitual                   | Construção do diagrama entidade-relacionamento que define as principais entidades e relações.|
| Modelo Lógico                      | Tradução do modelo conceitual para modelo lógico (relacional/NoSQL) para estruturação do banco.|
| Popular o Banco de Dados            | Inserção de pelo menos 5 registros reais para teste e validação do sistema.                |
| Modelo Físico                     | Definição do modelo físico da base, como armazenamento, índices e particionamento.          |
| Criação de Perguntas e Queries     | Desenvolvimento de 10 perguntas chave para o banco e implementação das queries correspondentes.|
| Desenvolvimento do App             | Construção do aplicativo para interagir com o banco, incluindo cadastro, controle de pontuação e visualização. |


<br>

## 4. Personas (Atores Envolvidos)

| Persona          | Descrição                                                                                   |
|------------------|---------------------------------------------------------------------------------------------|
| Jogador          | Atleta participante das partidas, precisa registrar seus dados, pontuação e consultar rankings.|
| Juiz             | Responsável pela supervisão das partidas e validação da pontuação automática.               |
| Organizador      | Gerencia torneios, cria equipes, partidas e controla o fluxo de jogos.                      |
| Espectador       | Acompanha as partidas e rankings, tem acesso às informações públicas do torneio.           |
| Administrador    | Usuário com privilégios para gerenciar dados sensíveis, validar usuários e códigos administrativos.|



<br>


## 5. Modelos Desenvolvidos

### 5.1 Modelo Conceitual  
Diagrama Entidade-Relacionamento (ER) contemplando:  
- Entidades: Jogador, Equipe, Partida, Torneio, Pontuação, Juiz.  
- Relacionamentos: Jogador pertence a Equipe, Partida envolve Jogadores, Torneio contém Partidas, Juiz supervisiona Partida, Pontuação atribuída a Jogador em Partida.

### 5.2 Modelo Lógico  
Conversão do modelo ER para estruturas NoSQL orientadas a documentos, armazenando jogadores, equipes, partidas e resultados em coleções específicas.  

### 5.3 Modelo Físico  
Implementação física no banco NoSQL escolhido (ex: MongoDB), com definição de índices para consulta rápida por jogador, partidas e torneios, além de estrutura para controle de versões e auditoria dos dados.


<br>

## 6. População do Banco de Dados

- Inseridos registros iniciais para 5 jogadores, equipes e partidas de exemplo, permitindo teste e validação do sistema.


<br>

## 7. Consultas Criadas

Elaboração de 10 perguntas essenciais para a operação do banco, tais como:

- Quem são os jogadores participantes de determinado torneio?  
- Qual o ranking atual dos jogadores?  
- Quais partidas já foram finalizadas?  
- Qual o histórico de partidas de um jogador?  
- Quantos pontos cada jogador marcou em uma partida específica?  
- Quais equipes estão cadastradas e seus membros?  
- Quem foi o juiz responsável por uma partida?  
- Quais jogadores estão sem equipe?  
- Quais jogadores têm pontuações iguais?  
- Quais partidas estão agendadas para a próxima semana?

Todas as perguntas possuem suas queries correspondentes implementadas para acesso rápido e eficiente.

<BR>

## 8. Aplicativo

O aplicativo é desenvolvido com interface gráfica intuitiva usando Flet, permitindo:  

- Cadastro de jogadores, equipes e torneios;  
- Seleção de partidas e controle de pontuação em tempo real;  
- Visualização detalhada do ranking dos atletas;  
- Alternância entre temas claro e escuro;  
- Segurança no acesso via senhas para jogadores e administradores.

<br>

## 9. Considerações Finais

Este projeto alia tecnologias modernas de bancos de dados NoSQL e desenvolvimento de aplicações para resolver um problema real e prático no âmbito esportivo. A integração entre o banco e o app proporciona uma experiência robusta e funcional que pode ser expandida com futuras melhorias, como automação total por sensores e integração com dispositivos IoT.

<br>

## 10. 🧑🏼‍🚀 [Team Members]():

| Name                    | Role                                             |
|-------------------------|--------------------------------------------------|
| **Andson Ribeiro**       | [Github](https://github.com/andsonandreribeiro09) - [Contact]() |
| **Fabiana 🧬 Campanari** | [Github](https://github.com/FabianaCampanari) - [Contact Hub](https://linktr.ee/fabianacampanari)   |
| **Gabriel Moraes         | [Github]()  - [Contact]()
| **Leonardo X Fernandes** |   [Github](https://github.com/LeonardoXF)  - [Contact]()  |
|  **Pedro Vyctor Almeida** |  [Github](https://github.com/ppvyctor) - [Contact]()    |

<br>

## 11. Referências

- Documentação oficial do MongoDB  
- Documentação da biblioteca Flet  
- PUC-SP - Material didático CDIA - Banco de Dados NoSQL  

<br>

**Desenvolvido por:**  
Equipe PUC-SP - Ciência de Dados e Humanistic AI - CDIA - Banco de Dados NoSQL  





































































<br><br><br><br>

<br>


## 💌 [Let the data flow... Ping Me !](mailto:fabicampanari@proton.me)

<br>


#### <p align="center">  🛸๋ My Contacts [Hub](https://linktr.ee/fabianacampanari)


<br>

### <p align="center"> <img src="https://github.com/user-attachments/assets/517fc573-7607-4c5d-82a7-38383cc0537d" />


<br><br>

<p align="center">  ────────────── ⊹🔭๋ ──────────────

<!--
<p align="center">  ────────────── 🛸๋*ੈ✩* 🔭*ੈ₊ ──────────────
-->

<br>

<p align="center"> ➣➢➤ <a href="#top">Back to Top </a>
  

#
 
##### <p align="center">Copyright 2025 Mindful-AI-Assistants. Code released under the  [MIT license.]( https://github.com/Mindful-AI-Assistants/.github/blob/ad6948fdec771e022d49cd96f99024fcc7f1106a/LICENSE)

