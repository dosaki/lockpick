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
  selector: 'game-submitter',
  template: `
    <div>
      <span>Hi, {{user.name}}!</span>
    </div>
    <div>
      <input value="" placeholder="">
    </div>
  `
})

export class AppComponent {
  title: string = 'Lockpick';
  game: Game = null;
  user: User = {
    id: null,
    name: "Anonymous",
    secret: null
  };
}
