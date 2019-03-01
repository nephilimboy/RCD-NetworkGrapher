import {Component, Input} from '@angular/core';
import {NbDialogRef} from "@nebular/theme";
import {GrapherEntities} from "./grapherEntities.model";

@Component({
    selector: 'app-grapherEntitiesEdit',
    templateUrl: './grapherEntities-edit.component.html',
})
export class GrapherEntitiesEditComponent {
    @Input() grapherEntities: GrapherEntities;
    @Input() isEditData: boolean = false;

    constructor(protected ref: NbDialogRef<GrapherEntitiesEditComponent>) {

    }

    save() {

    }

    dismiss() {
        this.ref.close();
    }

}