import {AfterContentInit, Component, Input, OnInit} from '@angular/core';
import {NbDialogRef} from "@nebular/theme";
import {FormArray, FormBuilder, FormGroup} from "@angular/forms";
import {LogParser} from "./logParser.model";
import {LogParserService} from "./logParser.service";
import {HttpErrorResponse, HttpResponse} from "@angular/common/http";
import {CustomPattern} from "./customPattern.model";

@Component({
    selector: 'app-logParserEdit',
    templateUrl: './logParser-edit.component.html',
})
export class LogParserEditComponent implements OnInit, AfterContentInit {
    @Input() customPattern: CustomPattern[];
    selectedType: string;
    textAreaFinalOutput: string = '';
    logParserRows: FormGroup;
    logParserName: string;

    constructor(protected ref: NbDialogRef<LogParserEditComponent>,
                private formBuilder: FormBuilder,
                private lopParserService: LogParserService) {
    }

    ngOnInit() {
        this.logParserRows = this.formBuilder.group({
            itemRows: this.formBuilder.array([this.initItemRows()])
        });
    }

    ngAfterContentInit(): void {
    }

    initItemRows() {
        return this.formBuilder.group({
            itemParserType: ['pattern'],
            itemName: [''],
            itemPatternType: ['custom'],
            itemCustomPattern: [''],
            itemStaticText: ['']
        });
    }

    addNewRow() {
        const control = <FormArray>this.logParserRows.controls['itemRows'];
        control.push(this.initItemRows());
        this.finalOutputHandler();
    }

    deleteRow(index: number) {
        const control = <FormArray>this.logParserRows.controls['itemRows'];
        control.removeAt(index);
        this.finalOutputHandler();
    }

    finalOutputHandler() {
        this.textAreaFinalOutput = '';
        this.logParserRows.value.itemRows.forEach((element, i) => {
            if (element.itemParserType == 'pattern') {
                if (element.itemPatternType != 'custom') {
                    this.textAreaFinalOutput = this.textAreaFinalOutput + '%{' + element.itemPatternType + ':' + element.itemName + '}'
                } else {
                    this.textAreaFinalOutput = this.textAreaFinalOutput + '%{' + element.itemCustomPattern + ':' + element.itemName + '}'
                }
            } else {
                this.textAreaFinalOutput = this.textAreaFinalOutput + element.itemStaticText;
            }

            // %{WORD:name} is %{WORD:gender}, %{NUMBER:age} years old and weighs %{NUMBER:weight} kilograms
        })
    }

    moveUp(index: number) {
        const control = <FormArray>this.logParserRows.controls['itemRows'];
        if (control.at(index - 1)) {
            const extras = control.value;
            const newExtras = this.arraySwap(extras, index - 1, index);
            control.setValue(newExtras);
            this.finalOutputHandler();
        }

    }

    moveDown(index: number) {
        const control = <FormArray>this.logParserRows.controls['itemRows'];
        const extras = control.value;
        if (index < extras.length - 1) {
            const newExtras = this.arraySwap(extras, index, index + 1);
            control.setValue(newExtras);
            this.finalOutputHandler();
        }
    }

    arraySwap(arr: any[], index1: number, index2: number): any[] {
        arr = [...arr];
        const temp = arr[index1];
        arr[index1] = arr[index2];
        arr[index2] = temp;
        return arr;
    }


    dismiss() {
        this.ref.close();
    }

    save() {
        let logParser: LogParser = new LogParser();
        logParser.name = this.logParserName;
        logParser.pattern = this.textAreaFinalOutput;
        logParser.id = null;
        this.lopParserService.create(logParser)
            .subscribe((res: HttpResponse<LogParser>) => this.onSaveSuccess(), (res: HttpErrorResponse) => this.onSaveError());

    }

    protected onSaveSuccess() {
        this.ref.close('true');
    }

    protected onSaveError() {
        console.log('Log Parser saving error');
    }

}