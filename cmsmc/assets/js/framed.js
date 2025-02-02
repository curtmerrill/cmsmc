import * as d3 from "d3";

d3.json('/qs/summary/framed/').then( (data) => {
  let lastUpdate = new Date(data['lastUpdate']);
  let games = data['data'];

  let correct = games.filter((g) => g.correct_guess > 0);
  let incorrect = games.filter((g) => g.correct_guess < 0);
  let seen = games.filter((g) => g.seen == 'Yes');
  let unseen = games.filter((g) => g.seen == 'No');

  d3.select('#framed-timestamp').text(`Data as of ${d3.timeFormat("%B %-d, %Y")(lastUpdate)}`);

  // Top-level figs
  d3.select('#game-count').text(d3.format(',')(games.length));
  d3.select('#correct-count').text(d3.format(',')(correct.length));
  d3.select('#unseen-correct-count').text(d3.format(',')(correct.filter((g) => g.seen == 'No').length));

  // Table figs
  d3.select('#seen-correct').text(d3.format(',')(correct.filter((g) => g.seen == 'Yes').length));
  d3.select('#not-seen-correct').text(d3.format(',')(correct.filter((g) => g.seen == 'No').length));
  d3.select('#total-correct').text(d3.format(',')(correct.length));
  d3.select('#seen-incorrect').text(d3.format(',')(incorrect.filter((g) => g.seen == 'Yes').length));
  d3.select('#not-seen-incorrect').text(d3.format(',')(incorrect.filter((g) => g.seen == 'No').length));
  d3.select('#total-incorrect').text(d3.format(',')(incorrect.length));
  d3.select('#seen-all').text(d3.format(',')(seen.length));
  d3.select('#not-seen-all').text(d3.format(',')(unseen.length));
  d3.select('#total').text(d3.format(',')(games.length));

  d3.select('#average-guesses').text(d3.format('.1f')(d3.mean(correct, (c) => c.correct_guess)));

  drawHistogram(correct);

  firstGuesses(correct);

})

function drawHistogram(data) {
  const container = d3.select('#framed-histogram');

  const width = container.node().clientWidth;

  const height = 280;
  const marginTop = 20;
  const marginBottom = 20;
  const marginLeft = 20;
  const marginRight = 20;

  const bins = d3.bin()
    .thresholds(6)
    .value((d) => d.correct_guess)(data);

  const x = d3.scaleLinear()
    .domain([0, d3.max(bins, (d) => d.length)])
    .range([marginLeft, width-marginRight]);

  const y = d3.scaleBand()
    .domain([1, 2, 3, 4, 5, 6])
    .range([marginTop, height-marginBottom])
    .paddingInner(.3)
    .align(.5)
    .round(true);

  const chartContainer = d3.select('#framed-histogram');

  chartContainer.append('h3')
    .attr('class', 'chart-title')
    .text('Guess distribution for correctly identified movies')

  const chart = chartContainer.append('svg')
    .attr('width', width)
    .attr('height', height)
    .attr('viewBox', [0, 0, width, height])
    .attr('style', 'max-width: 100%; height: auto');

  chart.append('g').selectAll()
    .data(bins)
    .join('rect')
      .attr('x', x(0))
      .attr('width', (d) => x(d.length))
      .attr('y', (d) => y(d[0].correct_guess))
      .attr('height', y.bandwidth());

  let axisY = chart.append('g')
      .attr('class', 'axis y')
      .attr('transform', `translate(${marginLeft-5}, 0)`)
      .call(d3.axisLeft(y).tickValues([1,2,3,4,5,6]).tickFormat(d3.format('.0r')).tickSize(0))
      .call((g) => g.select('.domain').remove());

}

function firstGuesses(correct) {
  let firstFrames = correct.filter((g) => g.correct_guess == 1);
  let frame = d3.select('#first-guesses').selectAll('li')
    .data(firstFrames)
    .join('li')
    .html(d => `<a href="https://framed.wtf/archive?day=${d.id}">${d.id}</a>`);
}
