import {AfterContentInit, Component, ElementRef, OnInit, ViewChild} from '@angular/core';
import * as d3 from 'd3';
import {NetworkGrapherService} from "./networkGrapher.service";

@Component({
    selector: 'app-networkGrapher',
    styleUrls: ['./networkGrapher.component.scss'],
    templateUrl: './networkGrapher.component.html',
})
export class NetworkGrapherComponent implements OnInit, AfterContentInit {
    @ViewChild('chart') private chartContainer: ElementRef;
    public margin: any = {top: 0, bottom: 0, left: 0, right: 0};
    public width: any;
    public height: any;
    public svg: any;
    // private nodes: any
    // private links: any
    public nodeElements: any;
    public textElements: any;
    public linkElements: any;
    public imgElements: any;
    public tooltipDiv: any;

    public nodes;
    public links;

    constructor(private networkGrapherService: NetworkGrapherService) {
        this.nodes = [
            {id: "mammal", group: 0, label: "Mammals", level: 1},
            {id: "dog", group: 0, label: "Dogs", level: 2},
            {id: "cat", group: 0, label: "Cats", level: 2},
            {id: "fox", group: 0, label: "Foxes", level: 2},
            {id: "elk", group: 0, label: "Elk", level: 2},
            {id: "insect", group: 1, label: "Insects", level: 1},
            {id: "ant", group: 1, label: "Ants", level: 2},
            {id: "bee", group: 1, label: "Bees", level: 2},
            {id: "fish", group: 2, label: "Fish", level: 1},
            {id: "carp", group: 2, label: "Carp", level: 2},
            {id: "pike", group: 2, label: "Pikes", level: 2}
        ];

        this.links = [
            {target: "mammal", source: "dog", strength: 0.7},
            {target: "mammal", source: "cat", strength: 0.7},
            {target: "mammal", source: "fox", strength: 0.7},
            {target: "mammal", source: "elk", strength: 0.7},
            {target: "insect", source: "ant", strength: 0.7},
            {target: "insect", source: "bee", strength: 0.7},
            {target: "fish", source: "carp", strength: 0.7},
            {target: "fish", source: "pike", strength: 0.7},
            {target: "cat", source: "elk", strength: 0.1},
            {target: "carp", source: "ant", strength: 0.1},
            {target: "elk", source: "bee", strength: 0.1},
            {target: "dog", source: "cat", strength: 0.1},
            {target: "fox", source: "ant", strength: 0.1},
            {target: "pike", source: "cat", strength: 0.1}
        ];
    }

    ngOnInit() {
    }

    ngAfterContentInit(): void {
        this.createDiagram();
    }

    createDiagram() {

        this.networkGrapherService.getDiagram()
            .subscribe(diag => {console.log(4);console.log(diag)});


        const element = this.chartContainer.nativeElement;
        this.width = element.offsetWidth - this.margin.left - this.margin.right;
        this.height = element.offsetHeight - this.margin.top - this.margin.bottom;
        this.svg = d3.select(element).append('svg')
            .attr('width', element.offsetWidth)
            .style('border', "1px solid #00f9a6")
            .style('border-radius', "11px")
            .attr('height', element.offsetHeight);


        this.tooltipDiv = d3.select(element).append("div")
            .attr("class", "tooltip")
            .style("opacity", 0);


        let linkForce = d3
            .forceLink()
            .distance(100)
            .id(function (link) {
                return link.id
            })
            .strength(function (link) {
                return link.strength
            })

        var simulation = d3
            .forceSimulation()
            .force('link', linkForce)
            .force('charge', d3.forceManyBody().strength(-120))
            .force('center', d3.forceCenter(this.width / 2, this.height / 2))


        let dragDrop = d3.drag().on('start', function (node) {
            node.fx = node.x
            node.fy = node.y
        }).on('drag', function (node) {
            simulation.alphaTarget(0.7).restart()
            node.fx = d3.event.x
            node.fy = d3.event.y
        }).on('end', function (node) {
            if (!d3.event.active) {
                simulation.alphaTarget(0)
            }
            node.fx = null
            node.fy = null
        })


        this.linkElements = this.svg.append("g")
            .attr("class", "links")
            .selectAll("line")
            .data(this.links)
            .enter().append("line")
            .attr("stroke-width", 2)
            .attr('stroke', '#159499');
        // .attr("stroke", "rgba(50, 50, 50, 0.2)")


        this.textElements = this.svg.append("g")
            .attr("class", "texts")
            .selectAll("text")
            .data(this.nodes)
            .enter().append("text")
            .text(function (node) {
                return node.label
            })
            .attr("font-size", 15)
            .attr("dx", -20)
            .attr("dy", 40)

        this.imgElements = this.svg.append("g")
            .attr("class", "image")
            .selectAll("image")
            .data(this.nodes)
            .enter().append("image")
            .attr("xlink:href", "https://cdn2.iconfinder.com/data/icons/networking-icons-1/512/networking_icons-09.png")
            .attr("x", -30)
            .attr("y", -30)
            .attr("width", 20)
            .attr("height", 20);

        this.nodeElements = this.svg.append("g")
            .attr("class", "nodes")
            .selectAll("circle")
            .data(this.nodes)
            .enter().append("circle")
            .attr("r", 20)
            .attr("fill", 'transparent')
            .attr('stroke', '#939899')
            .attr("stroke-width", 1)
            .call(dragDrop)
            .on('click', (d) => this.selectNode(d))
            .on("mouseover", (d) => this.mouseOver(d))
            .on("mouseout", (d) => this.mouseOut(d));


        simulation.nodes(this.nodes).on('tick', () => {
            this.nodeElements
                .attr('cx', function (node) {
                    return node.x
                })
                .attr('cy', function (node) {
                    return node.y
                });
            this.textElements
                .attr('x', function (node) {
                    return node.x
                })
                .attr('y', function (node) {
                    return node.y
                });
            this.imgElements
                .attr('x', function (node) {
                    return node.x - 10
                })
                .attr('y', function (node) {
                    return node.y - 10
                });
            this.linkElements
                .attr('x1', function (link) {
                    return link.source.x
                })
                .attr('y1', function (link) {
                    return link.source.y
                })
                .attr('x2', function (link) {
                    return link.target.x
                })
                .attr('y2', function (link) {
                    return link.target.y
                })
        })

        simulation.force("link").links(this.links)

    }

    mouseOver(data) {
        this.tooltipDiv.transition()
            .duration(200)
            .style("opacity", .9);
        this.tooltipDiv.html('amir' + "<br/>" + 'ssss')
            .style("left", (d3.event.pageX) + "px")
            .style("top", (d3.event.pageY - 28) + "px");
    }

    mouseOut(data) {
        this.tooltipDiv.transition()
            .duration(500)
            .style("opacity", 0);
    }

    selectNode(selectedNode) {

        // let neighbors = this.returnNeighbors(selectedNode);
        //
        // // we modify the styles to highlight selected nodes
        // this.nodeElements.attr('fill', node => this.getNodeColor(node, neighbors));
        //
        // this.textElements.attr('fill', node => this.getTextColor(node, neighbors));
        //
        // this.linkElements.attr('stroke', node => this.getLinkColor(node, neighbors));


    }

    returnNeighbors(node): any {
        return this.links.reduce((neighbors, link) => {
                if (link.target.id === node.id) {
                    neighbors.push(link.source.id)
                } else if (link.source.id === node.id) {
                    neighbors.push(link.target.id)
                }
                return neighbors
            },
            [node.id]
        )
    }


    isNeighborLink(node, link) {
        return link.target.id === node.id || link.source.id === node.id
    }

    getNodeColor(node, neighbors) {
        // if (Array.isArray(neighbors) && neighbors.indexOf(node.id) > -1) {
        //     return node.level === 1 ? 'blue' : 'green'
        // }
        //
        // return node.level === 1 ? 'red' : 'gray'
    }

    getLinkColor(node, link) {
        return this.isNeighborLink(node, link) ? 'green' : '#E5E5E5'
    }

    getTextColor(node, neighbors) {
        return Array.isArray(neighbors) && neighbors.indexOf(node.id) > -1 ? 'green' : 'black'
    }

}