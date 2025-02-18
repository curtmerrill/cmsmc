import * as d3 from "d3";

d3.json('/qs/summary/now/').then( (data) => {
  console.log(data);
  d3.select('#recent-battery')
    .append('dd')
    .html(`${data.battery.level}% <small class="light">${data.battery.time}</small>`);

  d3.select('#recent-location')
    .append('dd')
    .text(data.location.place);

  d3.select('#recent-tv')
    .selectAll('dd')
    .data(data.tv)
    .join('dd')
      .html(d => `<i>${d}</i>`)

  d3.select('#recent-movie')
    .selectAll('dd')
    .data(data.movie)
    .join('dd')
      .html(d => `<i>${d}</i>`)

  d3.select('#recent-book')
    .selectAll('dd')
    .data(data.book)
    .join('dd')
      .html(d => `<i>${d.title}</i> by ${d.author}`)
})
