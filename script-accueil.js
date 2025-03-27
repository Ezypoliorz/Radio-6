if (navigator.userAgent.match(/iPad|Android|Tablet/i)) { // Si l'utilisateur est sur un iPad, un Android ou une tablette
  document.getElementById("Niveau-sonore").style.display = "none"; // On cache l'élément "Niveau-sonore"

}

document.getElementById("Bouton-nav-téléphone").onclick = function() {

  document.getElementById("Div-nav-téléphone").style.display = "block";
  document.getElementById("Conteneur").style.display = "none";
  document.getElementById("Bouton-nav-téléphone").style.display = "none";

}