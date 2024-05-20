# Praca inżynierska 2024/2025
System kontroli tożsamości opiekunów dzieci w przedszkolach

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