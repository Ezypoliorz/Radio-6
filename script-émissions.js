div_programme_background = document.querySelectorAll(".div-programme-background"); // On récupère tous les éléments de classe "div-programme-background"
div_programme_background.forEach(element => { // Pour chaque élément de la liste

  element.style.display = "none"; // On cache l'élément

});

fermer = document.getElementsByClassName("fermer"); // On récupère tous les éléments de classe "fermer"
for (let i = 0; i < fermer.length; i++) { // Pour chaque élément de la liste

  let id_self = fermer[i].id; // On récupère l'id de l'élément
  let id_self_number = id_self.match(/\d+/)[0]; // On récupère le nombre de l'id
  let id_target = "Programme-background" + (id_self_number); // On crée l'id de l'élément cible
  document.getElementById(id_self).onclick = function() { // On crée un événement au clic
  document.getElementById(id_target).style.display = "none"; // On cache l'élément cible
  }

}

infos = document.getElementsByClassName("infos"); // On récupère tous les éléments de classe "infos"
for (let i = 0; i < infos.length; i++) { // Pour chaque élément de la liste

  let id_self = infos[i].id; // On récupère l'id de l'élément
  let id_self_number = id_self.match(/\d+/)[0]; // On récupère le nombre de l'id
  let id_target = "Programme-background" + (id_self_number); // On crée l'id de l'élément cible
  document.getElementById(id_self).onclick = function() { // On crée un événement au clic
  document.getElementById(id_target).style.display = "block"; // On affiche l'élément cible
  }

}

const draggable = document.getElementById("Curseur");
let isDragging = false;
let offsetY = 0;
let positionY = 0;
let son = 0;
let YindexMin = 200;
let YindexMax = 415;

draggable.addEventListener('mousedown', (event) => { // On crée un événement au clic
    
    isDragging = true; 
    offsetY = event.clientY - draggable.offsetTop; // On récupère la position y du curseur
    volume = volume + offsetY; // On ajoute la position y du curseur à la variable volume
    
});

document.addEventListener('mouseup', () => { // On crée un événement au relâchement du clic
    isDragging = false;
    document.getElementById("Curseur").style.cursor = 'grab'; // On change le curseur
});

document.addEventListener('mousemove', (event) => { // On crée un événement au déplacement de la souris
    
    if (isDragging) { // Si on clique
        if (event.clientY - offsetY >= YindexMin && event.clientY - offsetY <= YindexMax) { // Si la position y du curseur est comprise entre 200 et 415
        document.getElementById("Curseur").style.cursor = 'grabbing';
        positionY = event.clientY; // On récupère la position y de la souris
        draggable.style.top = positionY - offsetY + 'px'; 
        son = event.clientY - offsetY;
        son = Number(son);
        son = (son - YindexMin) / (YindexMax - YindexMin); // On calcule le volume
        son = 1 - son;
        son = son.toFixed(2); // On arrondit le volume à 2 chiffres après la virgule
        if (son > 0.6) { // Si le volume est supérieur à 0.6
            document.getElementById("Volume-icone-img").src = "Images/Volume ON.svg" // On change l'image de l'icône du volume
            const allAudios = document.querySelectorAll('audio');
            allAudios.forEach(audio => {
                audio.volume = son;
            });
        }
        if (son <= 0.6) { // Si le volume est inférieur ou égal à 0.6
            document.getElementById("Volume-icone-img").src = "Images/Volume MILIEU.svg" // On change l'image de l'icône du volume
            const allAudios = document.querySelectorAll('audio');
            allAudios.forEach(audio => {
                audio.volume = son;
            });
        }
        if (son <= 0.03) { // Si le volume est inférieur ou égal à 0.03
            document.getElementById("Volume-icone-img").src = "Images/Volume OFF.svg"  // On change l'image de l'icône du volume
            const allAudios = document.querySelectorAll('audio');
            allAudios.forEach(audio => {
                audio.volume = 0;
            });
            
        }
    }
    }
});


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

if (navigator.userAgent.match(/iPad|Android|Tablet/i)) { // Si l'utilisateur est sur un iPad, un Android ou une tablette
  document.getElementById("Niveau-sonore").style.display = "none"; // On cache l'élément "Niveau-sonore"
}

document.getElementById("Bouton-nav-téléphone").onclick = function() {

  document.getElementById("Conteneur").style.display = "none";
  document.getElementById("Bouton-nav-téléphone").style.display = "none";
  document.getElementById("Div-nav-téléphone").style.display = "block";
  document.getElementById("Body").style.backgroundImage = "Images/Arrière-plan.svg";
  document.getElementById("Body").style.backgroundSize = "cover";
  document.getElementById("Body").style.backgroundRepeat = "no-repeat";
  document.getElementById("Body").style.backgroundPosition = "center";
  document.getElementById("Body").style.backgroundAttachment = "fixed";

}