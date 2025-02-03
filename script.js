document.getElementById("Programme-background1").style.display = "none";

var fermer = document.getElementById("Close1");
fermer.onclick = function() {
  document.getElementById("Programme-background1").style.display = "none";

};

var fermer = document.getElementById("Infos1");
fermer.onclick = function() {
  document.getElementById("Programme-background1").style.display = "block";

};

const draggable = document.getElementById("Curseur");
let isDragging = false;
let offsetY = 0;
let positionY = 0;
let son = 0;
let YindexMin = 250;
let YindexMax = 515;

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
