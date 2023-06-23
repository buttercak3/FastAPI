# FastAPI

https://fastapi.hubi.club

https://fastapi.hubi.club/docs

## Create virtual environment:
- press `F1` in VS Code
- search for `Python: Create Environment`
- select interpreter

## Make .ps1 executable:
```powershell
cd 'C:\Users\Sebi\Documents\4tes Semester\Cloud Computing\FastAPI\'
Set-ExecutionPolicy RemoteSigned

Set-ExecutionPolicy Restricted #if Activate.ps1 is no longer needed
```

## Activate venv:
```powershell
#inside: FastAPI folder:
.\.venv\Scripts\Activate.ps1

#inside: FastAPI\my_app\app:
uvicorn main:app #starts uvicorn server
```

## Install python libraries
```powershell
python -m install uvicorn

py -m pip freeze > requirements.txt #save all libs
```