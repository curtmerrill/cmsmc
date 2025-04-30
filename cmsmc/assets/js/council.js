import * as d3 from "d3";

const config = {
  'width': 960,
  'height': 120,
  'margins': {
    'top': 5,
    'right': 10,
    'bottom': 34,
    'left': 10
  }
}
let minValue, maxValue;
let chartData;
let dataByMember;

const chartContainer = d3.select('#charts');

d3.csv('https://static.curtmerrill.com/2025/attendance.csv').then((data) => {
  chartData = data.filter((d) => d.minutes_late != 'na').map((d) => {
    d.minutes_late = +d.minutes_late;
    return d;
  });
  dataByMember = d3.flatGroup(chartData, (d) => d.name).filter((g) => g[1].length >= 25);

  minValue = d3.min(chartData, (c) => c.minutes_late);
  maxValue = d3.max(chartData, (c) => c.minutes_late);

  drawAll();

  d3.select(window).on('resize', drawAll);
});

function drawAll() {
  chartContainer.html('');
  draw('All attendees', chartData);

  dataByMember.forEach((m) => {
    draw(m[0], m[1]);
  })
}

function draw(label, data) {
  config.width = chartContainer.node().getBoundingClientRect().width;

  const meetingCount = data.length;
  const onTimePct = data.filter(d => d.minutes_late < 0).length / data.length;
  const meanArrival = d3.mean(data, d => d.minutes_late);

  const chartHeight = config.height - config.margins.top - config.margins.bottom;

  let yMax = label == 'All attendees' ? 500 : 50;

  const bins = d3.bin()
    .thresholds([minValue, -30, -15, 0, 5, 10, 15, 30, 60])
    .domain([minValue, maxValue])
    .value(d => parseInt(d.minutes_late))(data);

  const x = d3.scaleBand()
    .domain(d3.range(bins.length))
    .range([0, config.width])
    .paddingOuter(0)

  const y = d3.scaleLinear()
    .domain([0, yMax])
    .range([chartHeight, 0]);

  const xAxis = d3.axisBottom(x)
    .tickSize(0)
    .tickFormat('');

  const yAxis = d3.axisLeft(y)
    .tickSize(-config.width)
    .ticks(3);

  let thisChart = chartContainer.append('div')
    .attr('class', 'single-chart');

  thisChart.append('h3')
    .attr('class', 'chart-title')
    .html( () =>
      label != 'All attendees' ? `${label}<span>, ${data[0].position}</span>` : label
    );

  thisChart.append('p')
    .attr('class', 'annotation')
    .text(`${d3.format(',')(meetingCount)} meeting arrivals`)
  thisChart.append('p')
    .attr('class', 'annotation')
    .text(`${d3.format('.0%')(onTimePct)} on time`)
  thisChart.append('p')
    .attr('class', 'annotation')
    .text(`Average arrival: ${d3.format('.0~f')(Math.abs(meanArrival))} minutes ${meanArrival < 0 ? 'early' : 'late'}`)

  const svg = thisChart.append('svg')
    .attr('width', config.width)
    .attr('height', config.height)
    .attr('viewBox', [0, 0, config.width, config.height]);


  svg.append('g')
      .attr('class', 'axis y')
      .attr('transform', `translate(0, ${config.margins.top} )`)
      .call(yAxis);


    svg.selectAll('path.domain').remove();
    svg.selectAll('.tick text')
      .attr('text-anchor', 'start')
      .attr('x', 1)
      .attr('dy', -4)
      .text( (d, i, j) => {
        if (d == 0) { return '' }
        if (i == j.length-1) { return `${d} arrivals`}
        return d
      })


  const bar = svg.selectAll('g.bar')
    .data(bins)
    .join('g')
      .attr('class', 'bar')
      .attr('transform', (d,i) => `translate(${x(i)}, ${config.margins.top})`);

  bar.append('rect')
    .attr('width', x.bandwidth() - 1)
    .attr('height', d => chartHeight - y(d.length))
    .attr('class', d => d.x0 < 0 ? 'green' : 'orange')
    .attr('transform', d => `translate(0, ${y(d.length)})`);

  bar.append('text')
    .attr('class', 'x-axis')
    .attr('y', chartHeight+15)
    .attr('x', x.bandwidth() / 2)
    .text( (d,i) => {
      if (i == 0) { return '30+' }
      if (i == bins.length-1 ) { return '60+' }
      if (d.x0 < 0) { return `${Math.abs(d.x1)}–${Math.abs(d.x0)}`}
      return `${d.x0}–${d.x1}`
    });


  svg.append('text')
    .attr('class', 'x-axis')
    .attr('x', x(2))
    .attr('y', config.height - 4)
    .text('← minutes early')

  svg.append('text')
    .attr('class', 'x-axis')
    .attr('x', x(4))
    .attr('y', config.height - 4)
    .attr('text-anchor', 'end')
    .text('minutes late →')
}

