const xmlhttp = new XMLHttpRequest();


xmlhttp.onload = function() {

  const myObj = JSON.parse(this.responseText);
  let text = "<select class='form-control' id='ddlRegion' onchange='CargarComuna()'>"
  for (let x in myObj) {
      text += "<option value='"+ myObj[x].codigo + "'>"+ myObj[x].nombre +"</option>"
  }
  text += "</select>"    
  document.getElementById("region").innerHTML = text;
  
}

xmlhttp.open("GET", "https://apis.digital.gob.cl/dpa/regiones/",true);
xmlhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
xmlhttp.send();

    function CargarComuna()
{
var seleccion=document.getElementById('ddlRegion');


const xmlhttp = new XMLHttpRequest();
xmlhttp.onload = function() {
  const myObj = JSON.parse(this.responseText);
  let text = "<select class='form-control' id='ddlComuna' onchange='CargarCouma()' >"
  for (let x in myObj) {
      text += "<option value='"+ myObj[x].codigo_padre + "'>"+ myObj[x].nombre +"</option>"
  }
  text += "</select>"    
  document.getElementById("comuna").innerHTML = text;
}
xmlhttp.open("GET", "https://apis.digital.gob.cl/dpa/regiones/"+seleccion.options[seleccion.selectedIndex].value+"/comunas" )
xmlhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
xmlhttp.send();

}