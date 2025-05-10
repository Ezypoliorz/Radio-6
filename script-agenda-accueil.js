async function GetLastProgram() {
    try {
      const response = await fetch('https://ezypoliorz.github.io/Radio-6/émissions.html');
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
      const html = await response.text();
      const parser = new DOMParser();
      const doc = parser.parseFromString(html, 'text/html');
      const Titre = doc.querySelector(`.${"titre-émission"}`);
      const Date = doc.querySelector(`.${"date-émission"}`);
      const Infos = [Titre, Date];
      return Infos

    } catch (error) {
      return [error, ""];
    }
  }

async function GetNextProgram() {
  try {
    const response = await fetch('https://ezypoliorz.github.io/Radio-6/calendar.json');
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    const data = await response.json()
    const Titre = data.titre;
    const Date = data.date;
    const Description = data.description;
    const Image = data.image;
    const Infos = [Titre, Date, Description, Image]
    return Infos

  } catch (error) {
    return [error, "", "", "", ""];
  }
}

function convertLink(texte) {
  const urlRegex = /(https?:\/\/|www\.)[^\s]+/gi;
  return texte.replace(urlRegex, (url) => {
    const href = url.startsWith('http') ? url : 'http://' + url;
    return `<a href="${href}" target="_blank">${url}</a>`;
  });
}

async function main() {

const infos1 = await GetLastProgram();
const TitreEmisison1 = infos1[0]?.textContent;
const DateEmission1 = infos1[1]?.textContent;
document.getElementById("Infos-dernière-émission").textContent = TitreEmisison1 + " - " + DateEmission1

const infos = await GetNextProgram();
const TitreEmisison = infos[0];
const DateEmission = infos[1];
const DescriptionEmission = infos[2];
const ImageEmission = infos[3];
document.getElementById("Titre-prochaine-émission").textContent = TitreEmisison;
document.getElementById("Date-heure-prochaine-émission").textContent = DateEmission;
document.getElementById("Description-prochaine-émission").innerHTML = convertLink(DescriptionEmission);
document.getElementById("Image-prochaine-émission").src = ImageEmission;

}
main();