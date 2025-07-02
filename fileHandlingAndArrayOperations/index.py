import os
import logging
import datetime
from typing import Optional, List, Tuple
import pandas as pd
import numpy as np

import pydicom
from pydicom.errors import InvalidDicomError
from PIL import Image

class FileProcessor:
    
    def __init__(self, base_path: str, log_file: str):
        self.base_path = base_path
        self.log_file = log_file

        self.logger = logging.getLogger("FileProcessorLogger")
        self.logger.setLevel(logging.ERROR)

        # Crea el archivo de log en la ruta base
        log_path = os.path.join(base_path, log_file)
        handler = logging.FileHandler(log_path)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)

        # Evita múltiples que se creen multiples handlers
        if not self.logger.handlers:
            self.logger.addHandler(handler)


    def list_folder_contents(self, folder_name:str, details:bool= False) -> None:
        
        folder_path = os.path.join(self.base_path, folder_name)

        if not os.path.exists(folder_path):
            self.logger.error(f"Carpeta no encontrada: {folder_path}")
            print(f"La carpeta '{folder_name}' no existe.")
            return

        items = os.listdir(folder_path)
        print(f"\n La carpeta '{folder_name}' contiene {len(items)} elementos:\n")

        for item in items:
            full_path = os.path.join(folder_path, item)
            item_type = "Carpeta" if os.path.isdir(full_path) else "Archivo"
            output = f"{item_type}: {item}"

            if details:
                try:
                    size_mb = os.path.getsize(full_path) / (1024 * 1024)
                    modified = datetime.datetime.fromtimestamp(os.path.getmtime(full_path))
                    output += f" | Tamaño: {size_mb:.2f} MB | Modificado: {modified}"
                except Exception as e:
                    self.logger.error(f"Error al obtener detalles de {item}: {str(e)}")
            print(output)


    def read_csv(self, filename: str, report_path: Optional[str] = None, summary: bool = False):
        file_path = os.path.join(self.base_path, filename)

        if not os.path.isfile(file_path):
            self.logger.error(f"Archivo no encontrado: {file_path}")
            print(f"Error: El archivo '{filename}' no existe.")
            return
        
        try:
            df = pd.read_csv(file_path)
        except Exception as e:
            self.logger.error(f"Error al leer el archivo CSV.: {str(e)}")
            print("Error al leer el archivo CSV.")
            return

        print(f"\n Archivo CSV: {filename}")
        print(f"Columnas ({len(df.columns)}): {list(df.columns)}")
        print(f"Total de filas: {len(df)}")

        numeric_df = df.select_dtypes(include=[np.number])
        print("\n Análisis de columnas numéricas:")

        try:
            for col in numeric_df.columns:
                mean = numeric_df[col].mean()
                std = numeric_df[col].std()
                print(f"- {col}: Media = {mean:.2f}, Desv. Estandar = {std:.2f}")
        except Exception as e:
            self.logger.error(f"Error en análisis numérico: {str(e)}")
            print("Error en análisis numérico")


        if report_path:
            try:
                with open(os.path.join(self.base_path, report_path), 'w') as report:
                    report.write(f"Informe de análisis para {filename}\n\n")
                    for col in numeric_df.columns:
                        report.write(f"{col}: Media = {numeric_df[col].mean():.2f}, Desv. Est. = {numeric_df[col].std():.2f}\n")
                print(f"\n Informe guardado en: {report_path}")
            except Exception as e:
                self.logger.error(f"Error al guardar el informe: {str(e)}")
                print("Error al guardar el informe.")


        if summary:
            print("\n Resumen de columnas no numéricas:")
            non_numeric_df = df.select_dtypes(exclude=[np.number])
            for col in non_numeric_df.columns:
                print(f"\n Columna: {col}")
                print(non_numeric_df[col].value_counts())

    def read_dicom(self, filename: str, tags: Optional[List[Tuple[int, int]]] = None, extract_image: bool = False) -> None:
        file_path = os.path.join(self.base_path, filename)
        if not os.path.isfile(file_path):
            self.logger.error(f"Archivo DICOM no existe: {file_path}")
            print(f" El archivo '{filename}' no existe.")
            return
        
        try:
            ds = pydicom.dcmread(file_path)
        except InvalidDicomError as e:
            self.logger.error(f"El archivo no es un DICOM válido: {str(e)}")
            print("El archivo no es un DICOM válido.")
            return
        except Exception as e:
            self.logger.error(f"Error al leer el archivo DICOM: {str(e)}")
            print(" Error al leer el archivo DICOM.")
            return
        
        print(f"\n Archivo DICOM: {filename}")
        print(f" Paciente: {getattr(ds, 'PatientName', 'Desconocido')}")
        print(f" Fecha de estudio: {getattr(ds, 'StudyDate', 'Desconocida')}")
        print(f" Modalidad: {getattr(ds, 'Modality', 'Desconocida')}")

        if tags:
            print("\n🔍 Tags solicitados:")
            for group, element in tags:
                tag = (group << 16) + element
                if tag in ds:
                    print(f"- ({group:04X}, {element:04X}): {ds[tag].value}")
                else:
                    print(f"- ({group:04X}, {element:04X}): No encontrado")

        if extract_image:
            try:
                pixel_array = ds.pixel_array
                img = Image.fromarray(pixel_array)
                img_path = os.path.join(self.base_path, filename.replace(".dcm", ".png"))
                img.save(img_path)
                print(f"\n Imagen extraída y guardada como PNG: {img_path}")
            except Exception as e:
                self.logger.error(f"No se pudo extraer la imagen DICOM: {str(e)}")
                print(" No se pudo extraer la imagen.")

if __name__ == "__main__":
    processor = FileProcessor(base_path=".", log_file="errores.log")

    # Listar el contenido del folder
    processor.list_folder_contents("data")

    # Listar el contenido del folder con detaller
    processor.list_folder_contents("data", details=True)

    # --------------------------------------------------

    # Leer CSV e imprime las columnas y el total de filas
    processor.read_csv("data/sample.csv")

    # Leer CSV y guardar  el análisis (promedios y desviaciones estándar) como archivo TXT.
    processor.read_csv("data/sample.csv", report_path="data/reporte.txt")

    # Leer CSV y imprimir un resumen de las columnas no numéricas, incluyendo valores únicos y sus frecuencias.
    processor.read_csv("data/sample.csv", summary=True)


    # ----------------------------------------------
    
    # Leer archivo DICOM
    processor.read_dicom("data/sample-02-dicom.dcm", tags=[(0x0010, 0x0010)], extract_image=True)