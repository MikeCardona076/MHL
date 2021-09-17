//How to make a get request from an api  "http://localhost:8000/apis-mhl/Estudios%20y%20Perfiles%20de%20Laboratorio/" 

const Http = new XMLHttpRequest();
const url='http://localhost:8000/apis-mhl/Estudios%20y%20Perfiles%20de%20Laboratorio/';
Http.open("GET", url);
Http.send();


Http.onreadystatechange = (e) => {
  console.log(Http.responseText)
}
