import {NgModule} from '@angular/core';

import {PagesComponent} from './pages.component';
import {DashboardModule} from './dashboard/dashboard.module';
import {PagesRoutingModule} from './pages-routing.module';
import {ThemeModule} from '../theme/theme.module';
import {NetworkGrapherModule} from "./networkGrapher/networkGrapher.module";
import {LogParserModule} from "./logParser/logParser.module";
import {GrapherEntitiesModule} from "./grapherEntities/grapherEntities.module";

const PAGES_COMPONENTS = [
  PagesComponent,
];

@NgModule({
  imports: [
    PagesRoutingModule,
    ThemeModule,
    DashboardModule,
    NetworkGrapherModule,
    LogParserModule,
    GrapherEntitiesModule,
  ],
  declarations: [
    ...PAGES_COMPONENTS,
  ],
})
export class PagesModule {
}
