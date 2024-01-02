import http from "node:http";
import { URL } from "node:url";
import fs from "node:fs";
import path from "node:path";

const filePath = path.join("src/guestbook.txt");

function formatEntry(name, content) {
  return `${name}:${content}\n`;
}

function parseEntry(entry) {
  const [name, content] = entry.split(":");
  return `<div><h1>${name}</h1><p>${content}</p></div>`;
}

function requestListener(request, response) {
  console.log("url: ", request.url , " method: ", request.method);

  const url = new URL(request.url, `http://${request.headers.host}`);

  if (request.method === "GET" && url.pathname === "/") {
    // odczyt pliku
    const entriesRaw = fs.readFileSync(filePath, "utf-8");
    const entries = entriesRaw
      .split("\n")
      .filter(entry => entry.trim() !== "")  // usuwanie pustych wierszy
      .map(parseEntry)
      .join('');
    
      response.writeHead(200, { "Content-Type": "text/html; charset=utf-8" });
      fs.readFile('src/index.html', 'utf8', (err, data) => {
        if (err) {
          console.error('Błąd odczytu pliku:', err);
          response.end('Błąd serwera');
          return;
        }
        const html = data.replace('<!--entries-->', entries);
        response.end(html);
      });
  } else if (request.method === "POST") {
    let postData = "";
    request.on("data", (chunk) => {
      postData += chunk;
    });

    request.on("end", () => {
      const formData = new URLSearchParams(postData);
      const name = formData.get("name");
      const content = formData.get("content");

      // zapis do pliku
      const entry = formatEntry(name, content);
      fs.appendFileSync(filePath, entry);

      // przekierowanie do strony głównej
      response.writeHead(302, { Location: "/" });
      response.end();
    });
  } else {
    response.writeHead(501, { "Content-Type": "text/plain; charset=utf-8" });
    response.write("Błąd 501: Niezaimplementowane");
    response.end();
  }
}

const server = http.createServer(requestListener);
server.listen(8000);
console.log("Serwer został uruchomiony na porcie 8000");
console.log('Aby zatrzymać serwer, naciśnij "CTRL + C"');
