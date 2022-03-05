#Sacar el area de un triangulo  
[int]$Base = Read-Host "Introduzca el valor de la Base"
while($Base -lt 0)
{
    $Base++
    Write-host "Introduzca un valor mayor que 0"
    Read-Host $Base
}
[int]$Altura = Read-Host "Introduzca el valor de la Altura"
while($Altura -lt 0)
{
    $Altura++
    Write-host "Introduzca un valor mayor que 0"
    Read-Host $Altura
}
$Area = $Base * $Altura/2
Write-host $Area
