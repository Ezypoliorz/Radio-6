div_programme_background = document.querySelectorAll(".div-programme-background");
div_programme_background.forEach(element => {

  element.style.display = "none";
});

fermer = document.getElementsByClassName("fermer");
for (let i = 0; i < fermer.length; i++) {

  let id_self = fermer[i].id;
  let id_self_number = id_self.match(/\d+/)[0];
  let id_target = "Programme-background" + (id_self_number);
  document.getElementById(id_self).onclick = function() {
  document.getElementById(id_target).style.display = "none";
  }

}

infos = document.getElementsByClassName("infos");
for (let i = 0; i < infos.length; i++) {

  let id_self = infos[i].id;
  let id_self_number = id_self.match(/\d+/)[0];
  let id_target = "Programme-background" + (id_self_number);
  const element = document.getElementById(id_target);
  const style = window.getComputedStyle(element);
  document.getElementById(id_self).onclick = function() {
    if (style.display === 'none') {
      for (let i = 0; i < infos.length; i++) {
        let id_self = infos[i].id;
        let id_self_number = id_self.match(/\d+/)[0];
        let id_target = "Programme-background" + (id_self_number);
        document.getElementById(id_target).style.display = "none";
      
      }
      document.getElementById(id_target).style.display = "block";
    }
    else {
      document.getElementById(id_target).style.display = "none";
    }

  }

}

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
        son = (son - YindexMin) / (YindexMax - YindexMin);
        son = 1 - son;
        son = son.toFixed(2);
        if (son > 0.6) {
            document.getElementById("Volume-icone-img").src = "Images/Volume ON.svg";
            const allAudios = document.querySelectorAll('audio');
            allAudios.forEach(audio => {
                audio.volume = son;
            });
        }
        if (son <= 0.6) {
            document.getElementById("Volume-icone-img").src = "Images/Volume MILIEU.svg";
            const allAudios = document.querySelectorAll('audio');
            allAudios.forEach(audio => {
                audio.volume = son;
            });
        }
        if (son <= 0.03) {
            document.getElementById("Volume-icone-img").src = "Images/Volume OFF.svg";
            const allAudios = document.querySelectorAll('audio');
            allAudios.forEach(audio => {
                audio.volume = 0;
            });
            
        }
    }
    }
});


function pauseOtherAudios(audioElement) {
const allAudios = document.querySelectorAll('audio');
allAudios.forEach(audio => {
  if (audio !== audioElement) {
    audio.pause();
  }
});
}

const audios = document.querySelectorAll('audio');
audios.forEach(audio => {
audio.addEventListener('play', () => {
  pauseOtherAudios(audio);
});
});

if (navigator.userAgent.match(/iPad|Android|Tablet/i)) {
  document.getElementById("Niveau-sonore").style.display = "none";

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



function changeTheme(theme) {
  
  if(theme === "light"){
    document.querySelector(':root').style.setProperty('--main-color', '#fbfbfb');
    document.querySelector(':root').style.setProperty('--secondary-color', 'black');
    document.getElementById("Logo-header").src = "Images/Logo header.png";
    document.querySelectorAll("img.icone-infos").forEach(image_infos => {
      image_infos.src = "Images/Programme.svg";
    });
    document.querySelectorAll("img.icone-fermer").forEach(image_fermer => {
      image_fermer.src = "Images/Fermer.svg";
    });
  }
  else{
    document.querySelector(':root').style.setProperty('--main-color', '#363636');
    document.querySelector(':root').style.setProperty('--secondary-color', '#fbfbfb');
    document.getElementById("Logo-header").src = "Images/Logo header dark.png";
    document.querySelectorAll("img.icone-infos").forEach(image_infos_dark => {
      image_infos_dark.src = "Images/Programme dark.svg";
    });
    document.querySelectorAll("img.icone-fermer").forEach(image_fermer_dark => {
      image_fermer_dark.src = "Images/Fermer dark.svg";
    });
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