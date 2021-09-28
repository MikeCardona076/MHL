const request = "http://172.16.2.83:8000/apis-mhl/Estudios%20y%20Perfiles%20de%20Laboratorio/";



fetch(request, {mode: 'no-cors'})
.then(function(response) {
//print json
console.log(response);
})
.catch(function(error) {
console.log(error);
}
);