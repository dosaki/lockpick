import { Component } from '@angular/core';

export class User {
  id: number;
  name: string;
  secret: string;
}

export class Game {
  id: number;
  name: string;
  owner: User;
}

export class Lock {
  id: number;
  key: string;
  clue: string;
  treasure: string;
  game: Game;
}

export class UserProgress {
  id: number;
  user: User;
  game: Game;
}

@Component({
  selector: 'who-are-you',
  template: `
    <div class="outer">
      <div class="out-circle">
        <div class="in-circle">
          <div class="key">
            Hi, <input value="{{user.name}}" placeholder="uh... whoever you are!">
          </div>
          <div class="key-ends">
            <span class="end"></span>
            <span class="end"></span>
            <span class="end"></span>
          </div>
        </div>
      </div>
    </div>
  `,
  styleUrls: ['styles/app.who-are-you.css']
})

export class AppComponent {
  title: string = 'Lockpick';
  game: Game = null;
  user: User = {
    id: null,
    name: null,
    secret: null
  };
}
