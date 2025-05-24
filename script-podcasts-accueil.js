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
function changeTheme(theme) {
  if(theme === "light"){
    document.querySelector(':root').style.setProperty('--main-color', '#fbfbfb');
    document.querySelector(':root').style.setProperty('--secondary-color', 'black');
    document.getElementById("logo-header-podcast").src = "Images/Logo header.png";
    document.getElementById("Icone-portraits").src = "Images/Icone portraits.svg";
    document.getElementById("Icone-chroniques-culturelles").src = "Images/Icone chronique culturelle.svg";
    document.getElementById("Icone-chroniques-scientifiques").src = "Images/Icone chronique scientifique.svg";
    document.getElementById("Icone-chroniques-touristiques").src = "Images/Icone chronique touristique.svg";
  }
  else{
    document.querySelector(':root').style.setProperty('--main-color', '#363636');
    document.querySelector(':root').style.setProperty('--secondary-color', '#fbfbfb');
    document.getElementById("logo-header-podcast").src = "Images/Logo header dark.png";
    document.getElementById("Icone-portraits").src = "Images/Icone portraits dark.svg";
    document.getElementById("Icone-chroniques-culturelles").src = "Images/Icone chronique culturelle dark.svg";
    document.getElementById("Icone-chroniques-scientifiques").src = "Images/Icone chronique scientifique dark.svg";
    document.getElementById("Icone-chroniques-touristiques").src = "Images/Icone chronique touristique dark.svg";

  }

}

let thème = ""

document.addEventListener('DOMContentLoaded', function() {
document.getElementById("Bouton-thème").src = "Images/Thème sombre.png";
document.getElementById("Bouton-thème").src = "Images/Thème sombre mouvement.png";
document.getElementById("Bouton-thème").src = "Images/Thème clair mouvement.png";
document.getElementById("Bouton-thème").src = "Images/Thème clair.png";

const prefersDarkScheme = window.matchMedia('(prefers-color-scheme: dark)');

if (prefersDarkScheme.matches) {
    thème = "sombre";
    document.getElementById("Bouton-thème").src = "Images/Thème sombre.png";
    changeTheme("dark");
} else {
    thème = "clair";
    document.getElementById("Bouton-thème").src = "Images/Thème clair.png";
    changeTheme("light");
}
});

document.getElementById("Bouton-thème").onclick = function(){

  if(thème === "clair"){
    document.getElementById("Bouton-thème").src = "Images/Thème clair mouvement.png";
      setTimeout(() => {
        document.getElementById("Bouton-thème").src = "Images/Thème sombre mouvement.png";
            setTimeout(() => {
              document.getElementById("Bouton-thème").src = "Images/Thème sombre.png";
            }, 21);
        }, 21);
    thème = "sombre"
    changeTheme("dark");
  }

  else{
    document.getElementById("Bouton-thème").src = "Images/Thème sombre mouvement.png";
      setTimeout(() => {
        document.getElementById("Bouton-thème").src = "Images/Thème clair mouvement.png";
            setTimeout(() => {
              document.getElementById("Bouton-thème").src = "Images/Thème clair.png";
            }, 21);
        }, 21);
    thème = "clair"
    changeTheme("light");
  }

}