<?php


$url = "http://172.16.2.83:8000/apis-mhl/Estudios%20y%20Perfiles%20de%20Laboratorio/";
$result = file_get_contents($url);
echo $result;



