
# 🧠 FileProcessor

`FileProcessor` es una clase en Python que permite realizar operaciones útiles sobre archivos y carpetas, incluyendo análisis de archivos CSV y lectura de imágenes médicas en formato DICOM.

---

## 📁 Estructura del proyecto

```
recursionAndColors/
│
├── data/sample.csv         # Archivo CSV de ejemplo
├── data/sample.dcm         # Archivo DICOM de ejemplo
├── errores.log               # Archivo de registro (generado automáticamente)
├── index.py              # Script principal con la clase FileProcessor
└── README.md                 # Documentación del proyecto
```

---

## 🚀 Cómo usar

### 1. Clona el repositorio.

### 2. Ejecuta el script principal:

```bash
python index.py
```

Asegúrate de tener instalado:

```bash
pip install pandas numpy pydicom Pillow
```

---

## 🔧 Clase `FileProcessor`

### Constructor

```python
FileProcessor(base_path: str, log_file: str)
```

- `base_path`: Ruta raíz desde donde se realizarán las operaciones.
- `log_file`: Nombre del archivo de log donde se guardarán los errores.

---

## 📂 Métodos disponibles

### `list_folder_contents(folder_name: str, details: bool = False)`

Lista los elementos dentro de una carpeta.

- Muestra si son archivos o carpetas.
- Si `details=True`, también muestra tamaño (MB) y fecha de modificación.
- Registra errores si la carpeta no existe.

---

### `read_csv(filename: str, report_path: Optional[str] = None, summary: bool = False)`

Lee un archivo CSV y muestra:

- Número de columnas y filas.
- Media y desviación estándar de columnas numéricas.
- Si `report_path` se indica, guarda el análisis en un archivo TXT.
- Si `summary=True`, muestra un resumen de valores únicos por columna no numérica.
- Registra errores si el archivo no existe o hay columnas no numéricas mal interpretadas.

---

### `read_dicom(filename: str, tags: Optional[List[Tuple[int, int]]] = None, extract_image: bool = False)`

Lee un archivo DICOM e imprime:

- Nombre del paciente.
- Fecha del estudio.
- Modalidad de imagen.
- Si se pasan tags, muestra los valores correspondientes.
- Si `extract_image=True`, guarda la imagen como PNG en la ruta base.
- Registra errores si el archivo es inválido, no existe o no se puede leer la imagen.

---

## 🧪 Ejemplo de uso

```python
processor = FileProcessor(base_path=".", log_file="errores.log")

# Ver contenido de una carpeta
processor.list_folder_contents("data", details=True)

# Leer archivo CSV
processor.read_csv("ejemplo_datos.csv", report_path="reporte.txt", summary=True)

# Leer archivo DICOM
processor.read_dicom("ejemplo_dicom.dcm", tags=[(0x0010, 0x0020)], extract_image=True)
```

---

## 📦 Requisitos

- Python 3.7 o superior
- pandas
- numpy
- pydicom
- Pillow

---

## 🧠 Autor

Juan José Arteta  
Desarrollador Front-End / Python  
2025
