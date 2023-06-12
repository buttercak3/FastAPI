# FastAPI

https://fastapi.hubi.club

https://fastapi.hubi.club/docs

## Virtual environment erstellen:
- in VS Code `F1` drücken
- nach `Python: Create Environment` suchen
- interpreter auswählen

## Virtual environment Datei ausführbar machen:
```powershell
cd 'C:\Users\Sebi\Documents\4tes Semester\Cloud Computing\FastAPI\'
Set-ExecutionPolicy RemoteSigned

Set-ExecutionPolicy Restricted #zum sperren
```

## Virtual environment aktivieren:
```powershell
.\.venv\Scripts\Activate.ps1

uvicorn main:app #startet uvicorn server
```

## Python library installieren
```powershell
python -m install uvicorn

py -m pip freeze > dependencies.txt #alle libs speichern
```
