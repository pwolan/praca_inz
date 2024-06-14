# Praca inżynierska 2024/2025
System kontroli tożsamości opiekunów dzieci w przedszkolach
https://docs.google.com/document/d/129ivr-Cifjc3LthBoJADm0ipba0X7vGCPr46uz0X5L0/edit?usp=sharing

# Development

## Dev containers
0. Instalacja Docker Desktop
1. Instalacja wtyczki Dev Containers do VS Code
2. Ctrl+Shift+P -> Dev Containers: Reopen and Rebuild in container
3. W osobnych terminalach
    * python backend/manage.py runserver
    * cd frontend && npm start
4. Aplikacja będzie dostępna pod adresem 127.0.0.1:3000 

Zaletą dev containers jest to samo środowisko dla każdego oraz postawiony server postgres.

## Lokalnie
1. pip install -r requirements
2. cd frontend && npm install
3. W osobnych terminalach
    * python backend/manage.py runserver
    * cd frontend && npm start
4. Aplikacja będzie dostępna pod adresem 127.0.0.1:3000 