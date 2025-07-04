import { Routes } from '@angular/router';
import { HomeComponentComponent } from './templates/homeComponent/homeComponent.component';

export const routes: Routes = [
    {
        path: '', component : HomeComponentComponent
    },
    { path: '**', redirectTo: '' }
];
