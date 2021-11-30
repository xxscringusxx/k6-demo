import http from "k6/http";
import { check, sleep } from 'k6';

export const options = {
  stages: [
    { duration: "30s", target: 25 },
    { duration: "1m", target: 50 },
    { duration: "20s", target: 0 },
  ],
  thresholds: {
    http_req_duration: ["p(90)<200", "p(95)<300"],
    "http_req_duration{what:home}": [{
      thresholds: "p(95)<100",
      abortOnFail: true,
      delayAbortEval: "5s",
    }],
  }
};

export default function () {
  const pages = [
    "/posts/youtube/",
    "/posts/catalog/",
    "/this-does-not-exist/",
  ]
  for (const page of pages) {
    const resHome = http.get(
      "https://www.devopstoolkitseries.com" + page,
      {tags: {what: "home"}
    });
    const resPage = http.get("https://www.devopstoolkitseries.com" + page);
    check(resPage, {
      "status was 200": (r) => r.status == 200,
    });
    sleep(1);
  }
}
