# Sharing Smile – Framework de Pruebas Automatizadas Rest Api

📑 Nota: Antes de ejecutar el proyecto, edite el archivo .env con sus datos locales.<br>
Debe configurar las credenciales proporcionadas para los usuarios admin y profesional.

### Precondiciones
Antes de comenzar, asegúrate de tener instalado en tu máquina local:
- **Git**
- **Python 3.13.4** o superior
- **Visual Studio Code (VS Code)** o su editor de codigo de preferencia

## ⚙️ Instalación

Para generar los reportes HTML, necesitas instalar la herramienta de línea de comandos **Allure**.

#### En Windows (PowerShell + Scoop)
1. Si no tienes **Scoop**, instálalo con:
   ```powershell
   Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
   irm get.scoop.sh | iex
2. Instala Allure:
   ```powershell
   scoop install allure
4. Verifica la instalación
   ```powershell
   allure --version
## 📥 Descargar el proyecto

Clona el repositorio y accede al directorio:
```bash
git clone https://github.com/Perzival5/Framework-Sharing-Smile.git
cd Framework-Sharing-Smile
```

---

## 🛠️ Configuración del entorno

### Crear entorno virtual
```bash
python -m venv venv
```

### Activar entorno virtual
- **Windows**:
  ```bash
  source venv/Scripts/activate
  ```
- **macOS/Linux**:
  ```bash
  source venv/bin/activate
  ```

### Instalar dependencias
```bash
pip install -r requirements.txt
```

---

## 🚀 Ejecución de pruebas

### Ejecución general
```bash
pytest
```
Esto ejecuta todas las pruebas y genera resultados en la carpeta `reports/`.

### Generar reporte HTML con Allure
```bash
allure serve reports
```
Este comando abre automáticamente un reporte visual en tu navegador.

---

### Ejecución por módulo (Feature)
- **Login**  
  ```bash
  pytest tests/Login
  ```
- **Paciente**  
  ```bash
  pytest tests/Patient
  ```
- **Profesional**  
  ```bash
  pytest tests/Professional
  ```
- **End to End**  
  ```bash
  pytest tests/e2e
  ```

---

### Ejecución por tipo de prueba (Marcadores)
- **Smoke**  
  ```bash
  pytest -m "smoke"
  ```
- **Negative**  
  ```bash
  pytest -m "negative"
  ```
- **Positive**  
  ```bash
  pytest -m "positive"
  ```
- **Regression**  
  ```bash
  pytest -m "regression"
  ```
- **Flujos (E2E)**  
  ```bash
  pytest -m "e2e"
  ```

---
