import * as d3 from "d3";

d3.json('/qs/summary/now/').then( (data) => {

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
      .html(d => `<i>${d}</i>`);

  d3.select('#recent-movie')
    .selectAll('dd')
    .data(data.movie)
    .join('dd')
      .html(d => `<i>${d}</i>`);

  d3.select('#recent-book')
    .selectAll('dd')
    .data(data.book)
    .join('dd')
      .html(d => `<i>${d.title}</i> by ${d.author}`);

  d3.select('#recent-planes')
      .append('dd')
      .html(`${data.planes.count} <small class="light"><a href="https://www.flightaware.com/adsb/stats/user/scmerrill">${data.planes.time}</a></small>`);

})
