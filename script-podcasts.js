const draggable = document.getElementById("Curseur");
let isDragging = false;
let offsetY = 0;
let positionY = 0;
let son = 0;
let YindexMin = 200;
let YindexMax = 415;

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