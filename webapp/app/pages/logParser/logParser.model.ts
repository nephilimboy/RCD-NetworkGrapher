export class LogParser {
    constructor(public id?: string,
                public name?: string,
                public pattern?: string,
                public logParserCrudFormCustomPattern?: LogParserCrudFormCustomPattern[],
                public logParserCrudFormStaticPattern?: LogParserCrudFormStaticPattern[],
    ) {
        this.id = id ? id : null;
        this.name = name ? name : '';
        this.pattern = pattern ? pattern : '';
        this.logParserCrudFormCustomPattern = logParserCrudFormCustomPattern ? logParserCrudFormCustomPattern : [];
        this.logParserCrudFormStaticPattern = logParserCrudFormStaticPattern ? logParserCrudFormStaticPattern : [];
    }
}

export class LogParserCrudFormCustomPattern {
    constructor(public id?: string,
                public order?: string,
                public parserType?: string,
                public name?: string,
                public patternType?: string,
                public customPatternName?: string,
    ) {
        this.id = id ? id : null;
        this.order = order ? order : '';
        this.parserType = parserType ? parserType : '';
        this.name = name ? name : '';
        this.patternType = patternType ? patternType : '';
        this.customPatternName = customPatternName ? customPatternName : '';
    }
}

export class LogParserCrudFormStaticPattern {
    constructor(public id?: string,
                public order?: string,
                public parserType?: string,
                public text?: string,
    ) {
        this.id = id ? id : null;
        this.order = order ? order : '';
        this.parserType = parserType ? parserType : '';
        this.text = text ? text : '';
    }
}
