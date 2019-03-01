import {NgModule} from '@angular/core';
import {ThemeModule} from "../../theme/theme.module";
import {NbDialogModule} from "@nebular/theme";
import {Ng2SmartTableModule} from "ng2-smart-table";
import {GrapherEntitiesComponent} from "./grapherEntities.component";
import {GrapherEntitiesRoutingModule} from "./grapherEntities-routing.module";


@NgModule({
  imports: [
    ThemeModule,
    Ng2SmartTableModule,
    NbDialogModule.forChild(),
    GrapherEntitiesRoutingModule,

  ],
  declarations: [
      GrapherEntitiesComponent
  ],
  providers:[
    // LogParserService,
  ],
  entryComponents:[
    // LogParserEditComponent,
  ]
})
export class GrapherEntitiesModule {
}
