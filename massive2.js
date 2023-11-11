import http from 'k6/http';
import { parseHTML } from 'k6/html';
import { sleep } from 'k6';

export const options = {
  vus: 100,
  duration: '20s',
};

export default function () {
  const res = http.get('http://localhost:5000/');
  const doc = parseHTML(res.body); // equivalent to res.html()
  const pageArray = doc.find('h1').text();
  console.log(pageArray);
  sleep(1);
}
