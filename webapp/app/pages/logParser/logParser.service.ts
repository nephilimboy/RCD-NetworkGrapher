import { Injectable } from '@angular/core';
import {HttpClient, HttpHeaders, HttpResponse} from '@angular/common/http';
import {Observable} from "rxjs";
import { catchError } from 'rxjs/operators';
import { map } from 'rxjs/operators';
import {LogParser} from "./logParser.model";

type EntityResponseType = HttpResponse<LogParser>;
type EntityArrayResponseType = HttpResponse<LogParser[]>;

@Injectable({ providedIn: 'root' })
export class LogParserService {
    resourceUrl = 'http://127.0.0.1:8000/api/v1/univstud/';
    httpHeader = new HttpHeaders({'content-type': 'application/json'})
    // private handleError: HandleError;
    constructor(private http: HttpClient) {
        // this.handleError = httpErrorHandler.createHandleError('HeroesService');
    }

    query (): Observable<EntityArrayResponseType> {
        return this.http.get<LogParser[]>(this.resourceUrl, {headers: this.httpHeader, observe: 'response'});
    }

    create(logParser: LogParser): Observable<EntityResponseType> {
        return this.http.post<LogParser>(this.resourceUrl, logParser, { observe: 'response' });
    }

    update(logParser: LogParser): Observable<EntityResponseType> {
        return this.http.put<LogParser>(this.resourceUrl, logParser, { observe: 'response' });
    }

    delete(id: number): Observable<HttpResponse<any>> {
        return this.http.delete<any>(this.resourceUrl + id + '/', { observe: 'response' });
    }

}