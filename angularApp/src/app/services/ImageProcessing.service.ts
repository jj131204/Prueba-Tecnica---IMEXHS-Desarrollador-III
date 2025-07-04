import { Injectable } from '@angular/core';
import { BehaviorSubject, Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ImageProcessingService {

  private _imageUrl = new BehaviorSubject<string | null>(null);
  public readonly imageUrl$: Observable<string | null> = this._imageUrl.asObservable();
  
  private _imageData = new BehaviorSubject<ImageData | null>(null);
  public readonly imageData$: Observable<ImageData | null> = this._imageData.asObservable();

  constructor() { }

  /**
   * Carga un archivo de imagen, emite su URL como Base64.
   * Una vez cargada la imagen, extrae sus ImageData y las emite.
   * @param file El archivo de imagen (File) a cargar.
   */
  loadImageFile(file: File): void {
    const reader = new FileReader();

    reader.onload = (e: ProgressEvent<FileReader>) => {
      const url = e.target?.result as string;
      this._imageUrl.next(url); // Emite la URL de la imagen

      
      this.getImageDataFromUrl(url)
        .then(imageData => {
          this._imageData.next(imageData); // Emite los ImageData
        })
        .catch(error => {
          console.error('Error al obtener ImageData:', error);
          this._imageData.next(null); // Emitir null en caso de error
        });
    };

    reader.onerror = (e) => {
      console.error('Error al leer el archivo:', e);
      this._imageUrl.next(null);
      this._imageData.next(null);
    };

    reader.readAsDataURL(file);
  }

  /**
   * Carga una imagen desde una URL y devuelve sus ImageData.
   * Esto requiere crear un canvas temporal en memoria.
   * @param url La URL de la imagen (normalmente una data URL Base64).
   * @returns Una promesa que resuelve con el ImageData de la imagen.
   */
  private getImageDataFromUrl(url: string): Promise<ImageData> {
    return new Promise((resolve, reject) => {
      const img = new Image();
      img.onload = () => {
        const tempCanvas = document.createElement('canvas');
        const tempCtx = tempCanvas.getContext('2d');

        if (!tempCtx) {
          reject('No se pudo obtener el contexto 2D para el canvas temporal.');
          return;
        }

        tempCanvas.width = img.width;
        tempCanvas.height = img.height;
        tempCtx.drawImage(img, 0, 0, img.width, img.height);

        const imageData = tempCtx.getImageData(0, 0, img.width, img.height);
        resolve(imageData);
      };
      img.onerror = (error) => reject('Error al cargar la imagen desde URL: ' + error);
      img.src = url;
    });
  }

  /**
   * Reinicia el estado del servicio de procesamiento de imagen.
   */
  resetImageState(): void {
    this._imageUrl.next(null);
    this._imageData.next(null);
  }
}