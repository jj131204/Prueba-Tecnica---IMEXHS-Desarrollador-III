// src/app/services/area-calculation.service.ts
import { Injectable } from '@angular/core';

export interface AreaCalculationResult {
  pointsInStain: number;
  totalPoints: number;
  totalImageArea: number;
  estimatedArea: number;
}

@Injectable({
  providedIn: 'root'
})
export class AreaCalculationService {

  constructor() { }

  /**
   * Calcula el área estimada de la mancha en una imagen binaria usando el método Monte Carlo.
   * @param imageData Los datos de píxeles de la imagen (ImageData).
   * @param numberOfPoints El número de puntos aleatorios a generar (n).
   * @returns Un objeto con los resultados del cálculo.
   */
  calculateStainArea(imageData: ImageData, numberOfPoints: number): AreaCalculationResult {
    const data = imageData.data; // Array de píxeles (RGBA)
    const imageWidth = imageData.width;
    const imageHeight = imageData.height;

    let pointsInStain = 0;

    for (let i = 0; i < numberOfPoints; i++) {
      const x = Math.floor(Math.random() * imageWidth);
      const y = Math.floor(Math.random() * imageHeight);

      // Calcular el índice en el array de píxeles (RGBA)
      const index = (y * imageWidth + x) * 4;


      const isBlack = data[index] < 50 && data[index + 1] < 50 && data[index + 2] < 50;

      if (isBlack) { // Si es negro, cuenta como mancha
        pointsInStain++;
      }
    }

    const totalImageArea = imageWidth * imageHeight;
    const estimatedArea = totalImageArea * (pointsInStain / numberOfPoints);

    return {
      pointsInStain: pointsInStain,
      totalPoints: numberOfPoints,
      totalImageArea: totalImageArea,
      estimatedArea: estimatedArea
    };
  }
}