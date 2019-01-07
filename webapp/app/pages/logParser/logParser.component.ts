import {AfterContentInit, Component, ElementRef, OnInit, ViewChild} from '@angular/core';
import {LocalDataSource} from "ng2-smart-table";
import {NbDialogService} from '@nebular/theme';
import {LogParserEditComponent} from "./logParser-edit.component";
import {LogParser} from "./logParser.model";
import {LogParserService} from "./logParser.service";
import {HttpErrorResponse, HttpResponse} from "@angular/common/http";
import {CustomPatternService} from "./customPattern.service";
import {CustomPattern} from "./customPattern.model";
import {CustomPatternEditComponent} from "./customPattern-edit.component";
import {JasonParserEditComponent} from "./jasonParser-edit.component";

@Component({
    selector: 'app-logParser',
    templateUrl: './logParser.component.html',
})
export class LogParserComponent implements OnInit, AfterContentInit {


    logParser_table_settings = {
        hideSubHeader: true,
        mode: 'external',
        add: {
            addButtonContent: '<i class="nb-plus"></i>',
            createButtonContent: '<i class="nb-checkmark"></i>',
            cancelButtonContent: '<i class="nb-close"></i>',
        },
        edit: {
            editButtonContent: '<i class="nb-edit"></i>',
            saveButtonContent: '<i class="nb-checkmark"></i>',
            cancelButtonContent: '<i class="nb-close"></i>',
        },
        delete: {
            deleteButtonContent: '<i class="nb-trash"></i>',
            confirmDelete: true,
        },
        columns: {
            name: {
                title: 'Name',
                type: 'string',
            },
            pattern: {
                title: 'Pattern',
                type: 'string',
            },
        },
    };

    customPatter_table_settings = {
        hideSubHeader: true,
        mode: 'external',
        add: {
            addButtonContent: '<i class="nb-plus"></i>',
            createButtonContent: '<i class="nb-checkmark"></i>',
            cancelButtonContent: '<i class="nb-close"></i>',
        },
        edit: {
            editButtonContent: '<i class="nb-edit"></i>',
            saveButtonContent: '<i class="nb-checkmark"></i>',
            cancelButtonContent: '<i class="nb-close"></i>',
        },
        delete: {
            deleteButtonContent: '<i class="nb-trash"></i>',
            confirmDelete: true,
        },
        columns: {
            name: {
                title: 'Name',
                type: 'string',
            },
            pattern: {
                title: 'Pattern',
                type: 'string',
            },
        },
    };

    sourceLogParser: LocalDataSource = new LocalDataSource();
    logParsers: LogParser[];
    sourceCustomPattern: LocalDataSource = new LocalDataSource();
    customPattern: CustomPattern[];

    constructor(private dialogService: NbDialogService,
                private lopParserService: LogParserService,
                private customPatternService: CustomPatternService) {
        // const data = this.service.getData();
    }

    onDeleteConfirmLogParser(event): void {
        if (window.confirm('Are you sure you want to delete?')) {
            event.confirm.resolve();
        } else {
            event.confirm.reject();
        }
    }

    onDeleteConfirmCustomPattern(event): void {
        console.log('hhd');
    }

    ngOnInit() {
        this.loadAllLogParser();

        this.loadAllCustomPattern();

        // this.createJson('');
    }

    ngAfterContentInit(): void {
    }

    loadAllLogParser() {
        this.lopParserService.query().subscribe(
            (res: HttpResponse<LogParser[]>) => {
                this.logParsers = res.body;
                this.sourceLogParser.load(this.logParsers);
            },
            (res: HttpErrorResponse) => console.log('error')
        );
    }

    loadAllCustomPattern() {
        this.customPatternService.query().subscribe(
            (res: HttpResponse<CustomPattern[]>) => {
                this.customPattern = res.body;
                this.sourceCustomPattern.load(this.customPattern);
            },
            (res: HttpErrorResponse) => console.log('error')
        );
    }

    createNew() {

        this.dialogService
            .open(LogParserEditComponent, {
                closeOnBackdropClick: false,
                context: {
                    customPattern: this.customPattern
                },
            })
            .onClose.subscribe((res) => this.loadAllLogParser());
    }

    createNewCustomPattern() {
        this.dialogService
            .open(CustomPatternEditComponent, {
                closeOnBackdropClick: false,
                context: {
                    customPattern: new CustomPattern(),
                    isEditData: false
                },
            })
            .onClose.subscribe((res) => this.loadAllCustomPattern());
    }

    createNewJasonParser(){
        this.dialogService
            .open(JasonParserEditComponent, {
                closeOnBackdropClick: false,
                context: {

                },
            })
            .onClose.subscribe();
    }

    onEditCustomPattern(evt) {
        this.dialogService
            .open(CustomPatternEditComponent, {
                closeOnBackdropClick: false,
                context: {
                    customPattern: evt.data,
                    isEditData: true
                },
            })
            .onClose.subscribe((res) => this.loadAllCustomPattern());
    }

    onDeleteCustomPattern(evt) {
        console.log(evt);
        this.customPatternService.delete(parseInt(evt.data.id)).subscribe((response) => {
            this.loadAllCustomPattern();
        }, (res) => console.log('res'));
    }

    onEditDataLogParser(evt) {
        console.log(evt)
    }

    onEditDataCustomPattern(evt) {
        console.log(evt)
    }


}