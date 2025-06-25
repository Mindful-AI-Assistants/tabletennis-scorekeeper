
<br>

 \[[🇧🇷 Português](README.pt_BR.md)\] \[**[🇺🇸 English](README.md)**\]

<br>


  <!--  START HEADER  -->
## <p align="center">  🏓 SmartPing: Table Tennis Score and Tournament Assistant App
#### <p align="center">  Table Tennis Scoring App; A smart app to manage table tennis scores and player rankings. Built as a final project for the NoSQL course (PUC-SP).

 
  <br><br>

#### <p align="center"> [![Sponsor Mindful AI Assistants](https://img.shields.io/badge/Sponsor-Mindful%20AI%20%20Assistants-brightgreen?logo=GitHub)](https://github.com/sponsors/Mindful-AI-Assistants)


<br><br>

 <p align="center">
<img src="https://github.com/user-attachments/assets/5001ffb7-9bc1-4228-a38f-af5f1e2d6677"/>

<br><br>




Currently, the project is in the prototype stage, with the potential to achieve full automation of scoring and player ranking through the implementation of sensors on the table and the ball. These sensors would enable automatic point counting, although human supervision (referee) remains essential to ensure accuracy and prevent errors.

The focus is on simplifying and making the work of sports event organizers more efficient, providing a modern and reliable digital environment for competition management.

The system allows:
- Facilitate point counting in matches;  
- Allow team creation and management;  
- In the future, enable tournament creation and control;  
- Optimize player ranking, making organizers' work simpler and more efficient.
- Dynamic viewing and updating of athlete rankings.

<br>

## 3. Extension Activity

To fulfill the Curricular Unit, we completed the following stages:

| Stage                               | Description                                                                                 |
|-------------------------------------|---------------------------------------------------------------------------------------------|
| Actor Identification (Personas)     | Defined system user profiles: players, referees, organizers, and audience.                 |
| Conceptual Model                    | Construction of entity-relationship diagram defining main entities and relationships.       |
| Logical Model                       | Translation from conceptual to logical model (relational/NoSQL) for database structuring.   |
| Database Population                 | Insertion of at least 5 real records for system testing and validation.                    |
| Physical Model                      | Definition of physical database model (storage, indexes, partitioning).                    |
| Question and Query Creation         | Development of 10 key database questions with corresponding query implementations.         |
| App Development                     | Application construction for database interaction (registration, scoring, visualization).    |


<br>

## 4. Personas (Involved Actors)

| Persona          | Description                                                                                 |
|------------------|---------------------------------------------------------------------------------------------|
| Player           | Athlete participating in matches, needs to register data, scores, and check rankings.      |
| Referee          | Responsible for match supervision and automated scoring validation.                         |
| Organizer        | Manages tournaments, creates teams/matches, controls game flow.                            |
| Spectator        | Follows matches/rankings with access to public tournament info.                            |
| Administrator    | Privileged user managing sensitive data, validating users, and administrative codes.        |



<br>


## 5. Developed Models

### 5.1 Conceptual Model  
Entity-Relationship Diagram (ER) including:  
- Entities: Player, Team, Match, Tournament, Score, Referee.  
- Relationships: Player belongs to Team, Match involves Players, Tournament contains Matches, Referee supervises Match, Score assigned to Player in Match.

### 5.2 Logical Model  
Conversion of ER model to document-oriented NoSQL structures, storing players, teams, matches, and results in specific collections.  

### 5.3 Physical Model  
Physical implementation in chosen NoSQL database (e.g., MongoDB), with index definition for fast querying by player/matches/tournaments, plus version control and data auditing structures.


<br>

## 6. Database Population

- Initial records inserted for 5 players, teams, and sample matches for system testing/validation.


<br>
## 7. Created Queries
Development of 10 essential database operation questions, such as:  
- Who are the players in a specific tournament?  
- What is the current player ranking?  
- Which matches have been completed?  
- What is a player's match history?  
- How many points did each player score in a specific match?  
- Which teams are registered and their members?  
- Who was the referee for a match?  
- Which players have no team?  
- Which players have equal scores?  
- Which matches are scheduled for next week?

All questions have corresponding queries implemented for fast, efficient access.

<BR>

## 8. Application

The app features an intuitive GUI built with Flet, enabling:  

- Player/team/tournament registration;  
- Match selection and real-time scoring control;  
- Detailed athlete ranking visualization;  
- Light/dark theme toggling;  
- Secure password access for players/administrators.

<br>

## 9. Final Considerations

This project combines modern NoSQL database technologies and application development to solve a real-world sports management problem. The database-app integration delivers a robust, functional experience expandable through future improvements like full sensor automation and IoT device integration.

<br>

## 10. 🧑🏼‍🚀 [Team Members]()

| Name                    | Role                                             |
|-------------------------|--------------------------------------------------|
| **Andson Ribeiro**       | [Github](https://github.com/andsonandreribeiro09) - [Contact]() |
| **Fabiana 🧬 Campanari** | [Github](https://github.com/FabianaCampanari) - [Contact Hub](https://linktr.ee/fabianacampanari)   |
| **Gabriel Moraes**       | [Github]()  - [Contact]() |
| **Leonardo X Fernandes** | [Github](https://github.com/LeonardoXF)  - [Contact]()  |
| **Pedro Vyctor Almeida** | [Github](https://github.com/ppvyctor) - [Contact]()    |
<br>

## 11. References

- Official MongoDB Documentation  
- Flet Library Documentation  
- PUC-SP - CDIA Course Material - NoSQL Databases  

<br>

**Developed by:**  
PUC-SP Team - Data Science and Humanistic AI - CDIA - NoSQL Databases

































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

