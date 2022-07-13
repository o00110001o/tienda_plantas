

let url = "https://pokeapi.co/api/v2/pokemon"
$.get(url, function(respuesta){
    
    console.log(respuesta)
} , "json")