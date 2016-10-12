import { Component } from '@angular/core';
import { UserService } from './user.service';

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
  selector: 'unlock-btn',
  template: `
    <div class="unlock">
      <button (click)="registerUser(username.value);" class="unlock-btn mi">
        lock_open
      </button>
    </div>
  `,
  styleUrls: ['styles/app.unlock-btn.css']
})
export class UnlockBtn {
  user: User;
  mode = 'Observable';
  constructor (private userService: UserService) {}
  registerUser (name: string) {
    if (!name) { return; }
    this.userService.registerUser(name)
                     .subscribe(
                       user  => this.user = user);
  }
}

@Component({
  selector: 'who-are-you',
  template: `
    <div class="outer">
      <div class="out-circle">
        <div class="in-circle">
          <unlock-btn></unlock-btn>
          <div class="key">
            Hi, <input #username value="{{user.name}}" placeholder="uh... whoever you are!">
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
