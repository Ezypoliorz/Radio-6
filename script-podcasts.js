const draggable = document.getElementById("Curseur");
let isDragging = false;
let offsetY = 0;
let positionY = 0;
let son = 0;
let YindexMin = 250;
let YindexMax = 465;

draggable.addEventListener('mousedown', (event) => {
    
    isDragging = true;
    offsetY = event.clientY - draggable.offsetTop;
    volume = volume + offsetY;
    
});

document.addEventListener('mouseup', () => {
    isDragging = false;
    document.getElementById("Curseur").style.cursor = 'grab';
});

document.addEventListener('mousemove', (event) => {
    
    if (isDragging) {
        if (event.clientY - offsetY >= YindexMin && event.clientY - offsetY <= YindexMax) {
        document.getElementById("Curseur").style.cursor = 'grabbing';
        positionY = event.clientY;
        draggable.style.top = positionY - offsetY + 'px';
        son = event.clientY - offsetY;
        son = Number(son);
        son = (son - YindexMin) / (YindexMax - YindexMin)
        son = 1 - son;
        son = son.toFixed(2);
        if (son > 0.6) {
            document.getElementById("Volume-icone-img").src = "Images/Volume ON.svg"
            const allAudios = document.querySelectorAll('audio');
            allAudios.forEach(audio => {
                audio.volume = son;
            });
        }
        if (son <= 0.6) {
            document.getElementById("Volume-icone-img").src = "Images/Volume MILIEU.svg"
            const allAudios = document.querySelectorAll('audio');
            allAudios.forEach(audio => {
                audio.volume = son;
            });
        }
        if (son <= 0.03) {
            document.getElementById("Volume-icone-img").src = "Images/Volume OFF.svg"
            const allAudios = document.querySelectorAll('audio');
            allAudios.forEach(audio => {
                audio.volume = 0;
            });
            
        }
    }
    }
});


if (navigator.userAgent.match(/iPad|Android|Tablet/i)) { // Si l'utilisateur est sur un iPad, un Android ou une tablette
    document.getElementById("Niveau-sonore").style.display = "none"; // On cache l'élément "Niveau-sonore"
  
  }
  
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

  function pauseOtherAudios(audioElement) {
const allAudios = document.querySelectorAll('audio'); // On récupère tous les éléments audio
allAudios.forEach(audio => { // Pour chaque élément audio
  if (audio !== audioElement) { // Si l'élément audio est différent de l'élément audio actuel
    audio.pause(); // On met en pause l'élément audio
  }
});
}

const audios = document.querySelectorAll('audio'); // On récupère tous les éléments audio
audios.forEach(audio => { // Pour chaque élément audio
audio.addEventListener('play', () => { // On crée un événement au lancement de la lecture
  pauseOtherAudios(audio); // On met en pause les autres éléments audio
});
});


function changeTheme(theme) {
  
  if(theme === "light"){
    document.querySelector(':root').style.setProperty('--main-color', '#fbfbfb');
    document.querySelector(':root').style.setProperty('--secondary-color', 'black');
    document.getElementById("Logo-header").src = "Images/Logo header.png";
    document.getElementsByClassName("infos").src = "Images/Programme.svg";
    document.getElementsByClassName("fermer").src = "Images/Fermer.svg";
  }
  else{
    document.querySelector(':root').style.setProperty('--main-color', '#363636');
    document.querySelector(':root').style.setProperty('--secondary-color', '#fbfbfb');
    document.getElementById("Logo-header").src = "Images/Logo header dark.png";
    document.getElementsByClassName("infos").src = "Images/Programme dark.svg";
    document.getElementsByClassName("fermer").src = "Images/Fermer dark.svg";
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
    changeTheme("dark");
    document.getElementById("Bouton-thème").src = "Images/Thème sombre.png";
} else {
    thème = "clair";
    changeTheme("light");
    document.getElementById("Bouton-thème").src = "Images/Thème clair.png";
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