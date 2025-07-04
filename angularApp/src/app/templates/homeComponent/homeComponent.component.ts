import { Component, ElementRef, OnInit, ViewChild, OnDestroy } from '@angular/core';
import { CommonModule } from '@angular/common';
import { Observable, Subscription } from 'rxjs';
import { ImageProcessingService } from '../../services/ImageProcessing.service';
import { AreaCalculationResult, AreaCalculationService } from '../../services/AreaCalculation.service';

@Component({
  selector: 'app-homeComponent',
  templateUrl: './homeComponent.component.html',
  styleUrls: ['./homeComponent.component.css'],
  imports: [
    CommonModule 
  ]
})
export class HomeComponentComponent implements OnInit, OnDestroy {

  @ViewChild('imageCanvas') imageCanvas!: ElementRef<HTMLCanvasElement>;
  @ViewChild('imageElement') imageElement!: ElementRef<HTMLImageElement>;

  imageUrl: string | null = null;
  currentImageData: ImageData | null = null;
  imageWidth: number = 0;
  imageHeight: number = 0;

  showModal: boolean = false;
  modalData: AreaCalculationResult | null = null;

  pointsSelected: number = 0;

  private subscriptions: Subscription = new Subscription(); 

  constructor(
    private imageProcessingService: ImageProcessingService,
    private areaCalculationService: AreaCalculationService
  ) {}

  ngOnInit(): void {
    this.pointsSelected = 0;
    // Suscribirse al imageUrl$ del servicio
    this.subscriptions.add(
      this.imageProcessingService.imageUrl$.subscribe(url => {
        this.imageUrl = url;
        if (!url) {
          this.clearCanvas();
        }
      })
    );

    // Suscribirse al imageData$ del servicio
    this.subscriptions.add(
      this.imageProcessingService.imageData$.subscribe(imageData => {
        this.currentImageData = imageData;
        if (imageData) {
          this.imageWidth = imageData.width;
          this.imageHeight = imageData.height;
          
          this.drawImageDataOnCanvas(imageData);
        } else {
          this.imageWidth = 0;
          this.imageHeight = 0;
          this.clearCanvas();
        }
      })
    );

    this.imageProcessingService.resetImageState();
    this.closeModal();
  }

  
  ngOnDestroy(): void {
    this.subscriptions.unsubscribe();
  }

  onFileSelected(event: Event): void {
    const input = event.target as HTMLInputElement;
    if (input.files && input.files[0]) {
      // Se llama al servicio para cargar la imagen
      this.imageProcessingService.loadImageFile(input.files[0]);
    }
  }

  
  drawImageDataOnCanvas(imageData: ImageData): void {
    const canvas = this.imageCanvas.nativeElement;
    const ctx = canvas.getContext('2d');

    if (!ctx) {
      console.error('No se pudo obtener el contexto del canvas para dibujar imageData.');
      return;
    }

    const maxWidth = 450;
    const maxHeight = 450;
    let displayWidth = imageData.width;
    let displayHeight = imageData.height;

    if (displayWidth > maxWidth || displayHeight > maxHeight) {
        const ratio = Math.min(maxWidth / displayWidth, maxHeight / displayHeight);
        displayWidth *= ratio;
        displayHeight *= ratio;
    }

    canvas.width = displayWidth;
    canvas.height = displayHeight;

    ctx.clearRect(0, 0, canvas.width, canvas.height);
    
    const tempCanvasForDisplay = document.createElement('canvas');
    const tempCtxForDisplay = tempCanvasForDisplay.getContext('2d');
    if (tempCtxForDisplay) {
      tempCanvasForDisplay.width = imageData.width;
      tempCanvasForDisplay.height = imageData.height;
      tempCtxForDisplay.putImageData(imageData, 0, 0);

      ctx.drawImage(tempCanvasForDisplay, 0, 0, displayWidth, displayHeight);
    }
  }
  
  clearCanvas(): void {
    const canvas = this.imageCanvas.nativeElement;
    const ctx = canvas.getContext('2d');
    if (ctx) {
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      canvas.width = 0; 
      canvas.height = 0;
    }
  }


  calculateArea(): void {
    if (!this.currentImageData) {
      alert('Por favor, suba una imagen primero.');
      return;
    }

    const results = this.areaCalculationService.calculateStainArea(this.currentImageData, this.pointsSelected);

    this.modalData = results;
    this.modalData.totalPoints = this.pointsSelected;

    this.showModal = true;
  }

  closeModal(): void {
    this.showModal = false;
  }


  onPointsSliderChange(event: Event): void {
    const value = (event.target as HTMLInputElement).value;
    this.pointsSelected = parseInt(value, 10);
  }
}