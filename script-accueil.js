document.getElementById("Bouton-nav-téléphone").onclick = function() {
  const element = document.getElementById("Conteneur");
  const style = window.getComputedStyle(element);
  if (style.display === 'none') {
    document.getElementById("Div-nav-téléphone").style.display = "none";
    document.getElementById("Conteneur").style.display = "block";
  }

  else{
    document.getElementById("Div-nav-téléphone").style.display = "block";
    document.getElementById("Conteneur").style.display = "none";
  }


}