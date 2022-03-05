#Detener servicios de la Computadora
$Path = Read-Host "Introduzca el la ubicacion del TXT"
Get-ChildItem -Path $Path -Force
#Obtenemos el status de los servicios
Get-Content -Path $Path | Get-Service
#Iniciamos todos los servicios dedl del txt
Get-Content -Path $Path | Get-Service | Start-Service
