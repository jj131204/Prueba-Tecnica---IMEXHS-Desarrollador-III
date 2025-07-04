# Estimador de Área de Manchas en Imágenes Binarias

Este proyecto es una aplicación web simple desarrollada con Angular que permite a los usuarios cargar una imagen binaria (blanco y negro) y estimar el área de las "manchas" (píxeles negros) utilizando el método de muestreo aleatorio (Monte Carlo). Los resultados del cálculo se muestran en una ventana modal.

## 🚀 Características

* **Carga de Imagen:** Sube fácilmente imágenes binarias (PNG, JPG, etc.).
* **Estimación de Área:** Calcula el área de las manchas (píxeles negros) utilizando el método de Monte Carlo.
* **Número de Puntos Configurable:** Slider para ajustar la cantidad de puntos aleatorios utilizados en el cálculo, permitiendo variar la precisión.
* **Resultados Claros:** Visualización de los resultados del cálculo en una ventana modal intuitiva.
* **Interfaz Moderna:** Estilizado con **Tailwind CSS** para una experiencia de usuario limpia y responsiva.
* **Arquitectura Modular:** Lógica separada en servicios de Angular para mejorar la mantenibilidad y la escalabilidad (con Observables de RxJS para gestión de estado).

## 🛠️ Tecnologías Utilizadas

* **Angular CLI** (versión recomendada: 17.x o superior)
* **TypeScript**
* **HTML5**
* **CSS3** (con **Tailwind CSS** para utilidades)
* **RxJS** (para gestión de estado reactiva en servicios)



## ⚙️ Instalación y Ejecución

Para poner en marcha el proyecto en tu máquina local, sigue estos pasos:

### Prerrequisitos

Asegúrate de tener instalado lo siguiente:

* **Node.js**: [Descargar e instalar Node.js](https://nodejs.org/en/download/) (incluye npm).
* **Angular CLI**: Instálalo globalmente ejecutando:
    ```bash
    npm install -g @angular/cli
    ```

### Pasos

1.  **Clona el repositorio:**
    ```bash
    git clone <URL_DE_TU_REPOSITORIO>
    cd <nombre-de-tu-carpeta-de-proyecto>
    ```

2.  **Instala las dependencias:**
    ```bash
    npm install
    ```
    Si usas `yarn`:
    ```bash
    yarn install
    ```

3.  **Inicia el servidor de desarrollo:**
    ```bash
    ng serve
    ```
    Esto compilará la aplicación y la iniciará en un servidor local. Podrás acceder a ella abriendo tu navegador en `http://localhost:4200/`. La aplicación se recargará automáticamente si cambias alguno de los archivos fuente.

## 📝 Uso

1.  **Cargar Imagen:** Haz clic en el área "Insertar imagen" o en el botón "Cambiar imagen" si ya hay una cargada. Selecciona una imagen binaria (con manchas negras sobre fondo blanco preferiblemente, o viceversa si el código se ajusta).
2.  **Ajustar Puntos:** Usa el slider para seleccionar la cantidad de puntos aleatorios a utilizar en el cálculo (cuantos más puntos, mayor precisión, pero más tiempo de cálculo).
3.  **Calcular Área:** Haz clic en el botón "Calcular".
4.  **Ver Resultados:** Aparecerá una ventana modal con los resultados de la estimación del área de la mancha.
