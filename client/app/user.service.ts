import { Injectable } from '@angular/core';
import { Http, Response, Headers, RequestOptions } from '@angular/http';
import { Observable } from 'rxjs/Observable';
import { User } from './app.component';

@Injectable()
export class UserService {
  private userUrl = '/user/';  // URL to web API
  constructor (private http: Http) {}
  getUser (username: string): Observable<User> {
    return this.http.get(this.userUrl+"/"+username)
                    .map(this.extractData)
                    .catch(this.handleError);
  }
  getPrivateUser (username: string, password: string): Observable<User> {
    let body = JSON.stringify({ 'secret':password });
    let headers = new Headers({ 'Content-Type': 'application/json' });
    let options = new RequestOptions({ headers: headers });
    return this.http.post(this.userUrl+"/"+username, body, options)
                    .map(this.extractData)
                    .catch(this.handleError);
  }
  registerUser(username: string): Observable<User> {
    let body = JSON.stringify({});
    let headers = new Headers({ 'Content-Type': 'application/json' });
    let options = new RequestOptions({ headers: headers });
    return this.http.put(this.userUrl+"/"+username, body, options)
                    .map(this.extractData)
                    .catch(this.handleError);
  }
  private extractData(res: Response) {
    let body = res.json();
    return body.data || { };
  }
  private handleError (error: any) {
    // In a real world app, we might use a remote logging infrastructure
    // We'd also dig deeper into the error to get a better message
    let errMsg = (error.message) ? error.message :
      error.status ? `${error.status} - ${error.statusText}` : 'Server error';
    console.error(errMsg); // log to console instead
    return Observable.throw(errMsg);
  }
}
