import { CommonModule } from '@angular/common';
import { Component, ElementRef, OnInit, ViewChild } from '@angular/core';

@Component({
  selector: 'app-homeComponent',
  templateUrl: './homeComponent.component.html',
  styleUrls: ['./homeComponent.component.css'],
  imports: [
    CommonModule
  ]
})
export class HomeComponentComponent implements OnInit{


  @ViewChild('imageElement') imageElement!: ElementRef<HTMLImageElement>;
  @ViewChild('imageCanvas') imageCanvas!: ElementRef<HTMLCanvasElement>;

  imageUrl: string | ArrayBuffer | null = null;
  imageWidth: number = 0;
  imageHeight: number = 0;
  estimatedArea: number | null = null;

  showModal: boolean = false;
  modalData = {
    pointsInStain: 0,
    totalPoints: 0,
    totalImageArea: 0,
    estimatedArea: 0
  };

  ngOnInit(): void {
    this.imageUrl = null
    this.imageWidth = 0
    this.imageHeight = 0;
    this.estimatedArea = null;
  }

  onFileSelected(event: Event): void {
    const input = event.target as HTMLInputElement;
    if (input.files && input.files[0]) {
      const reader = new FileReader();

      reader.onload = (e: ProgressEvent<FileReader>) => {
        this.imageUrl = e.target?.result as string;
        
        setTimeout(() => {
          this.loadImageToCanvas();
        }, 0);
      };

      reader.readAsDataURL(input.files[0]);
    }
  }

  loadImageToCanvas(): void {
    const img = this.imageElement.nativeElement;
    const canvas = this.imageCanvas.nativeElement;
    const ctx = canvas.getContext('2d');

    img.onload = () => {
      this.imageWidth = img.width;
      this.imageHeight = img.height;

      canvas.width = this.imageWidth;
      canvas.height = this.imageHeight;

      if (ctx) {
        ctx.drawImage(img, 0, 0, this.imageWidth, this.imageHeight);
      }
    };
  }


  calculateArea(): void {
    if (!this.imageWidth || !this.imageHeight) {
      alert('Por favor, suba una imagen primero.');
      return;
    }

    const n = 100000; // Número de puntos aleatorios a generar
    let pointsInStain = 0;

    const canvas = this.imageCanvas.nativeElement;
    const ctx = canvas.getContext('2d');

    if (!ctx) {
        alert('No se pudo obtener el contexto del canvas.');
        return;
    }

    const imageData = ctx.getImageData(0, 0, this.imageWidth, this.imageHeight);
    const data = imageData.data; // Array de píxeles (RGBA)

    for (let i = 0; i < n; i++) {
        const x = Math.floor(Math.random() * this.imageWidth);
        const y = Math.floor(Math.random() * this.imageHeight);

        // Calcular el índice en el array de píxeles (RGBA)
        // Cada píxel tiene 4 valores: Rojo, Verde, Azul, Alfa
        const index = (y * this.imageWidth + x) * 4;

        // Comprobar si el píxel es blanco (o muy cercano al blanco)
        // En una imagen binaria (blanco y negro), blanco suele ser [255, 255, 255, 255]
        // Se considera blanco si la suma de RGB es alta (ej: > 700) o si R, G, B son > 200
        const isWhite = data[index] > 200 && data[index + 1] > 200 && data[index + 2] > 200;

        if (isWhite) {
            pointsInStain++;
        }
    }
    
    this.estimateArea(pointsInStain, n);
  }

  estimateArea(pointsInStain: number, totalPoints: number): void {
    const totalImageArea = this.imageWidth * this.imageHeight;
    const estimatedArea = totalImageArea * (pointsInStain / totalPoints);

    this.modalData = {
      pointsInStain: pointsInStain,
      totalPoints: totalPoints,
      totalImageArea: totalImageArea,
      estimatedArea: estimatedArea
    };

    this.showModal = true;
  }

  closeModal(): void {
    this.showModal = false;
  }
}
