# Sharing Smile

Nota: Antes de ejecutar el proyecto, edite el archivo .env con sus datos locales.<br>
Debe configurar las credenciales proporcionadas para los usuarios admin y profesional.

## Instrucciones de Instalaciónn

1. Requisitos
  Python 3.x
  pip (gestor de paquetes de Python)

2. Crear entorno virtual
```
python -m venv venv
```
3. Activar entorno virtual
Windows:

```
venv/Scripts/activate
```
4.Instalar dependencias

```
pip install -r requirements.txt
```

5. Instalación del plugin de Allure<br>
Primero, necesitas instalar el plugin de Pytest que permite generar los archivos de reporte de Allure.

```
pip install allure-pytest
```

6. Instalación de Allure Commandline<br>
Para generar los reportes HTML, necesitas tener la herramienta de línea de comandos de Allure instalada en tu sistema.

En Windows (usando PowerShell y Scoop):<br>
Si no tienes Scoop, primero instálalo con los siguientes comandos:

PowerShell
```
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
irm get.scoop.sh | iex
```

Luego, instala Allure:

```
scoop install allure
```

Puedes verificar la instalación ejecutando:

```
allure --version
```

7. Ejecución de pruebas y generación de reportes<br>
Una vez que el plugin y la herramienta de Allure están instalados, puedes ejecutar tus pruebas y generar el reporte.

Ejecuta tus pruebas con Pytest, indicando la carpeta donde se guardarán los resultados. La bandera --alluredir es obligatoria.

```
pytest
```
Esto creará una carpeta llamada reports (puedes nombrarla como quieras) con los archivos de resultados.

Genera y visualiza el reporte HTML. Este comando tomará los archivos de la carpeta reports y creará un reporte visual que se abrirá automáticamente en tu navegador.

```
allure serve reports
```

### Comandos para ejecutar pruebas

#### Feature

* Login
  ```
  pytest tests/Login
  ```
* Paciente
   ```
  pytest tests/Patient
  ```
* Profesional
  ```
  pytest tests/Professional
  ```
* End to End
   ```
  pytest tests/e2e
  ```
#### Tipo de Prueba

* Smoke
  ```
  pytest -m "smoke"
  ```
* Negative
   ```
  pytest -m "negative"
  ```
* Positive
  ```
  pytest -m "positive"
  ```
* Regression
   ```
  pytest -m "regression"
  ```      
* Flujos
   ```
  pytest -m "e2e"
  ```      