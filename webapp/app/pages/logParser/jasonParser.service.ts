import {Injectable} from '@angular/core';
import {HttpClient, HttpHeaders, HttpResponse} from '@angular/common/http';
import {BehaviorSubject, Observable} from "rxjs";
import {CustomPattern} from "./customPattern.model";

type EntityResponseType = HttpResponse<CustomPattern>;
type EntityArrayResponseType = HttpResponse<CustomPattern[]>;

@Injectable({providedIn: 'root'})
export class JasonParserService {
    resourceUrl = 'http://127.0.0.1:8000/api/v1/jasonParser/';
    // httpHeader = new HttpHeaders({'content-type': 'application/json', "Access-Control-Allow-Methods":"GET, POST"});
    httpHeader = new HttpHeaders({'content-type': 'application/json', 'Access-Control-Allow-Origin': '*' ,"Access-Control-Allow-Methods":"GET, POST"});

    private messageSource = new BehaviorSubject(new Map<string, string>());
    public jasonDataBetweenDynamicComponentAndParrent = this.messageSource.asObservable();


    constructor(private http: HttpClient) {
    }

    query(): Observable<EntityArrayResponseType> {
        return this.http.get<CustomPattern[]>(this.resourceUrl, {headers: this.httpHeader, observe: 'response'});
    }

    create(customPattern: CustomPattern): Observable<EntityResponseType> {
        return this.http.post<CustomPattern>(this.resourceUrl, customPattern, {observe: 'response'});
    }

    update(customPattern: CustomPattern): Observable<EntityResponseType> {
        return this.http.put<CustomPattern>(this.resourceUrl + customPattern.id + '/', customPattern, {observe: 'response'});
    }

    delete(id: number): Observable<HttpResponse<any>> {
        return this.http.delete<any>(this.resourceUrl + id + '/', {observe: 'response'});
    }

    updateJasonDataBetweenAllSharedComponents(message: Map<string, string>) {
        this.messageSource.next(message)
    }

}