export class JasonParser {
    constructor(public id?: string,
                public name?: string,
                public jason?: string,
                public jasonAlias?: JasonParserAlias[]
    ) {
        this.id = id ? id : null;
        this.name = name ? name : '';
        this.jason = jason ? jason : '';
        this.jasonAlias = jasonAlias ? jasonAlias : []
    }
}

export class JasonParserAlias {
    constructor(public id?: string,
                public name?: string,
                public path?: string,
    ) {
        this.id = id ? id : null;
        this.name = name ? name : '';
        this.path = path ? path : '';
    }
}
