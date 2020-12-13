class CndcePie{
    width = 500;
    height = 500;
    // left, top, right, down
    margin = [50, 50, 50, 50]

    svg;
    pie;
    arc;
    arcLabel;

    constructor(){
        this.__initD3()
    }


    __initD3(){
        CNDCE.loadCheckins.then((checkins) => {
            this.svg = d3.select('.cndce-checkin-pie')
                .append('svg')
                .attr('viewBox', [-this.width/2 - this.margin[0], -this.height/2 - this.margin[1], this.width + this.margin[0] + this.margin[2], this.height + this.margin[1]+ this.margin[3]])


            this.pie = d3.pie()
                .sort(null)
                .value( d => d.hours );

            this.arc = d3.arc()
                .innerRadius(50)
                .outerRadius(Math.min(this.width, this.height) / 2 - 1)
                .cornerRadius(15)

            const radius = Math.min(this.width, this.height) / 2 * 0.8;
            this.arcLabel = d3.arc()
                .innerRadius(radius)
                .outerRadius(radius)

            this.svg.append('g')
                .attr('stroke', 'white')
                .attr('class', 'cndce-pie-g')

            this.svg.append('g')
                .attr('class', 'cndce-pie-labels-g')

            this.updateD3()

        })
    }

    updateD3(){
        const __data = CNDCE.groupedBy.tag;

        // Convert to array
        const data = Object.keys(__data).map((key)=>__data[key])

        const arcs = this.pie(data);

        const arcsG = this.svg
            .select('.cndce-pie-g')
            .selectAll('path')

        const pathG = arcsG.data(arcs)
            .enter()
            .append('g')
            .attr('class', 'cndce-pie-arcs')
            .attr('fill', (d, i) => d3.schemePaired[i])

        pathG.append('path')
            .attr('d', this.arc)
            .append('title')
            .text(d => d.data.tag.name)

        pathG.append('text')
            .attr('class', 'cndce-pie-label')
            .attr('transform', d => `translate(${this.arc.centroid(d)})`)
            .call(text => (
                text.append('tspan')
                    .attr('y', '-0.4em')
                    .attr('font-weight', 'bold')
                    .text(d => d.data.tag.name)
            ))
            .call(text => text.filter(d => (d.endAngle - d.startAngle) > 0.25).append("tspan")
                .attr("x", 0)
                .attr("y", "1rem")
                .attr("fill-opacity", 0.7)
                .text(d => `Total: ${d.data.hours.toFixed(2)} hours`));

        arcsG.exit().remove()

            
        
    }


    
}





$(()=>{
    new CndcePie();
})