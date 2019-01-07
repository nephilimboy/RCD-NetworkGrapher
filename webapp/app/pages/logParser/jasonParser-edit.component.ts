import {
    AfterContentInit,
    Compiler,
    Component,
    ComponentFactory,
    ComponentFactoryResolver,
    ComponentRef,
    Input,
    ModuleWithComponentFactories,
    NgModule,
    OnInit,
    ViewChild,
    ViewContainerRef
} from '@angular/core';
import {NbDialogRef} from "@nebular/theme";
import {CustomPattern} from "./customPattern.model";
import {CommonModule} from "@angular/common";
import {FormsModule} from "@angular/forms";
import {JasonParser} from "../../core/utils/jasonParser/jasonParser";
import {JasonParserService} from "./jasonParser.service";

@Component({
    selector: 'app-logParserEdit',
    templateUrl: './jasonParser-edit.component.html',
})
export class JasonParserEditComponent implements OnInit, AfterContentInit {
    @ViewChild('container', {read: ViewContainerRef}) container: ViewContainerRef;

    @Input() customPattern: CustomPattern;
    @Input() isEditData: boolean = false;

    jasonInput: any = '';
    objectsParentsNodeKey: string = '';
    totalInputsNumber: number = 0;
    template: string;
    private componentRef: ComponentRef<{}>;
    private keyPathIndexMap: Map<number, string>;

    constructor(protected ref: NbDialogRef<JasonParserEditComponent>,
                private componentFactoryResolver: ComponentFactoryResolver,
                private compiler: Compiler,
                private jasonParserService: JasonParserService) {
    }

    ngOnInit() {
        this.jasonParserService.jasonDataBetweenDynamicComponentAndParrent.subscribe(message => {
            console.log('heeeee');
            console.log(message)
        });
    }

    ngAfterContentInit(): void {
    }


    dismiss() {
        this.ref.close();
    }

    save() {

    }

    protected onSaveSuccess() {
        this.ref.close('true');
    }

    protected onSaveError() {
        console.log('Log Parser saving error');
    }

    createJson() {
        this.totalInputsNumber = 0;
        this.findJsonKeyPath(JSON.parse(this.jasonInput));
        this.template = '<ul id="json_container" class="json_container" #json_container style="margin: 15px;">\n' + this.json2html(JSON.parse(this.jasonInput), "expanded") + '\n</ul>';
        this.compileTemplate();
    }

    findJsonKeyPath(jsonData) {
        let jasonParser = new JasonParser();
        this.keyPathIndexMap = new Map<number, string>();
        jasonParser.getAllKeys(jsonData).forEach((value: string, key: number) => {
            this.keyPathIndexMap.set(key, jasonParser.getJasonPath(jsonData, value, key));
        });
    }

    json2html(json, expanderClasses) {
        if (json !== '') {
            let html = '';
            for (let key in json) {
                if (!json.hasOwnProperty(key)) {
                    continue;
                }
                let value = json[key], type = typeof json[key];
                html = html + this.createElement(key, value, type, expanderClasses);
            }
            return html;
        }
    }

    createElement(key, value, type, expanderClasses) {

        let klass = 'object',
            open = '{{ "{" }}',
            close = '{{ "}" }}';
        if (value instanceof Array) {
            klass = 'array';
            open = '[';
            close = ']';
        }
        if (value === null) {
            return '<li><span class="key">"' + this.encode(key) + '": </span><span class="null">"' + this.encodeVal(key) + '"</span></li>';
        }

        switch (type) {
            case 'object':
                var object = '<li><span class="' + expanderClasses + '"></span><span class="key">"' + this.encode(key) + '": </span>     <span>' + this.encodeValExeptipns(key) + '</span>      <span class="jsonOpen">' + open + '</span> <ul class="' + klass + '">';
                object = object + this.json2html(value, expanderClasses);
                return object + '</ul><span class="jsonClose">' + close + '</span></li>';
                break;
            // case 'number':
            case 'boolean':
                return '<li><span class="key">"' + this.encode(key) + '": </span><span class="' + type + '">' + this.encodeVal(key) + '</span></li>';
            default:
                return '<li><span class="key">"' + this.encode(key) + '": </span><span class="' + type + '">"' + this.encodeVal(key) + '"</span></li>';
                break;
        }
    }

    encode(value) {
        return value;
    }

    encodeVal(value) {
        ++this.totalInputsNumber;
        let tempVal = "'" + this.keyPathIndexMap.get(this.totalInputsNumber) + "'";
        if (this.objectsParentsNodeKey == '') {
            return '<input type="text" class="form-control" name="model' + String(this.totalInputsNumber) + '" (input)="changeValue(' + tempVal + ',$event)"  placeholder="Parser Name" style="display: inline;width: 121px;font-size: 13px;line-height: 1.2;font-family: monospace;height: 36px;" > ' +
                '<h6 class="jsonAlias" style="font-family: monospace; font-size: 12px"> ' + tempVal + '</h6>';
        } else {
            return '<input type="text" class="form-control" name="model' + String(this.totalInputsNumber) + '" (input)="changeValue(' + tempVal + ',$event)"  placeholder="Parser Name" style="display: inline;width: 121px;font-size: 13px;line-height: 1.2;font-family: monospace;height: 36px;" > ' +
                '<h6 class="jsonAlias" style="font-family: monospace; font-size: 12px"> ' + tempVal + '</h6>';
        }

    }

    encodeValExeptipns(value) {
        if (!isNaN(value)) {
            this.objectsParentsNodeKey = value;
            return '';
        }
        ++this.totalInputsNumber;
        let tempVal = "'" + this.keyPathIndexMap.get(this.totalInputsNumber) + "'";
        if (this.objectsParentsNodeKey == '') {
            return '<input type="text" class="form-control" name="model' + String(this.totalInputsNumber) + '" (input)="changeValue(' + tempVal + ',$event)"  placeholder="Parser Name" style="display: inline;width: 121px;font-size: 13px;line-height: 1.2;font-family: monospace;height: 36px;" > ' +
                '<h6 class="jsonAlias" style="font-family: monospace; font-size: 12px"> ' + tempVal + '</h6>';
        } else {
            return '<input type="text" class="form-control" name="model' + String(this.totalInputsNumber) + '" (input)="changeValue(' + tempVal + ',$event)"  placeholder="Parser Name" style="display: inline;width: 121px;font-size: 13px;line-height: 1.2;font-family: monospace;height: 36px;" > ' +
                '<h6 class="jsonAlias" style="font-family: monospace; font-size: 12px"> ' + tempVal + '</h6>';
        }
    }


    compileTemplate() {

        let metadata = {
            selector: `runtime-component-sample`,
            template: this.template,
        };

        let factory = this.createComponentFactorySync(this.compiler, metadata, null);

        if (this.componentRef) {
            this.componentRef.destroy();
            this.componentRef = null;
        }
        this.componentRef = this.container.createComponent(factory);
    }

    private createComponentFactorySync(compiler: Compiler, metadata: Component, componentClass: any): ComponentFactory<any> {
        // const cmpClass = componentClass || class RuntimeComponent {
        const cmpClass = class RuntimeComponent {
            jasonPathValueMap: Map<string, string> = new Map<string, string>();
            jasonParserService: JasonParserService;

            changeValue(key, evt) {
                this.jasonPathValueMap.set(key.toString(), evt.target.value);
                this.jasonParserService.updateJasonDataBetweenAllSharedComponents(this.jasonPathValueMap);
            }
        };
        const decoratedCmp = Component(metadata)(cmpClass);
        decoratedCmp.prototype.jasonParserService = this.jasonParserService;

        @NgModule({imports: [CommonModule, FormsModule], declarations: [decoratedCmp]})
        class RuntimeComponentModule {
        }

        let module: ModuleWithComponentFactories<any> = compiler.compileModuleAndAllComponentsSync(RuntimeComponentModule);
        return module.componentFactories.find(f => f.componentType === decoratedCmp);
    }


}