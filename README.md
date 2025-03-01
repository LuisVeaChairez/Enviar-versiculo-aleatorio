# Enviar un versículo aleatorio de la biblia a los números seleccionados!

## Instalando dependencias
### Debes abrir la consola, preferiblemente en la ruta en la que se encuentra el código, y, si tienes python instalado escribir:
#### pip install -r requirements.txt
### En caso de no tener python se debe instalar

### Para utilizar este código se debe añadir un archivo data.py en la carpeta src y agregar números de teléfono
#### phone1 = '+196303213'
### Y dentro del script.py cambiar el import en base a los números que agregaste
#### from src.data import phone1, phone2....
### Y ya por último hay que cambiar los parámetros dentro de las llamadas a la función sendMessage
#### sendMessage(phone1, versiculos)
#### sendMessage(phone2, versiculos)
#### .......
## Y para utilizarlo simplemente hay que ejecutar el archivo script.py
