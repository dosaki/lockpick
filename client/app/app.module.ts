import { NgModule }       from '@angular/core';
import { BrowserModule }  from '@angular/platform-browser';
import { FormsModule }    from '@angular/forms';
import { HttpModule, JsonpModule } from '@angular/http';
import { AppComponent, UnlockBtn }   from './app.component';
@NgModule({
  imports: [
    BrowserModule,
    FormsModule
  ],
  declarations: [
    AppComponent,
    UnlockBtn
  ],
  bootstrap: [ AppComponent ]
})
export class AppModule { }
