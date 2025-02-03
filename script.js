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
        if (event.clientY - offsetY >= 200 && event.clientY - offsetY <= 465) {
        document.getElementById("Curseur").style.cursor = 'grabbing';
        positionY = event.clientY;
        draggable.style.top = positionY - offsetY + 'px';
        son = event.clientY - offsetY;
        son = Number(son);
        son = (son - 250) / (515 - 250)
        son = 1 - son;
        son = son.toFixed(2);
        if (son > 0.6) {
            document.getElementById("Volume-icone-img").src = "Images/Volume ON.svg"
            document.getElementById("Audio1").volume = son;
            document.getElementById("Audio2").volume = son;
            document.getElementById("Audio3").volume = son;
            document.getElementById("Audio4").volume = son;
            document.getElementById("Audio5").volume = son;
        }
        if (son <= 0.6) {
            document.getElementById("Volume-icone-img").src = "Images/Volume MILIEU.svg"
            document.getElementById("Audio1").volume = son;
            document.getElementById("Audio2").volume = son;
            document.getElementById("Audio3").volume = son;
            document.getElementById("Audio4").volume = son;
            document.getElementById("Audio5").volume = son;
        }
        if (son <= 0.03) {
            document.getElementById("Volume-icone-img").src = "Images/Volume OFF.svg"
            document.getElementById("Audio1").volume = 0;
            document.getElementById("Audio2").volume = 0;
            document.getElementById("Audio3").volume = 0;
            document.getElementById("Audio4").volume = 0;
            document.getElementById("Audio5").volume = 0;
            
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
