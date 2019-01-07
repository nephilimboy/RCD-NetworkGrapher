import { Injectable } from '@angular/core';
import {HttpClient, HttpHeaders, HttpResponse} from '@angular/common/http';
import {Observable} from "rxjs";
import { catchError } from 'rxjs/operators';
import { map } from 'rxjs/operators';

@Injectable({ providedIn: 'root' })
export class NetworkGrapherService {
    configUrl = 'http://127.0.0.1:8000/api/v1/companies/';
    httpHeader = new HttpHeaders({'content-type': 'application/json'})
    // private handleError: HandleError;
    constructor(private http: HttpClient) {
        // this.handleError = httpErrorHandler.createHandleError('HeroesService');
    }

    getDiagram (): Observable<HttpResponse<any>> {
        return this.http.get<any>(this.configUrl, {headers: this.httpHeader});
    }



}