const root = document.documentElement;
document.documentElement.style.fontSize = '15px';

let paragrafy = [
  "Natenczas Wojski chwycił na taśmie przypięty",
  "Swój róg bawoli, długi, cętkowany, kręty",
  "Jak wąż boa, oburącz do ust go przycisnął",
  "Wzdął policzki jak banię, w oczach krwią zabłysnął",
  "Zasunął wpół powieki, wciągnął w głąb pół brzucha",
  "I do płuc wysłał z niego cały zapas ducha",
  "I zagrał: róg jak wicher, wirowatym dechem",
  "Niesie w puszczę muzykę i podwaja echem.",
  "",
  "Umilkli strzelcy, stali szczwacze zadziwieni",
  "Mocą, czystością, dziwną harmoniją pieni.",
  "Starzec cały kunszt, którym niegdyś w lasach słynął",
  "Jeszcze raz przed uszami myśliwców rozwinął;",
  "Napełnił wnet, ożywił knieje i dąbrowy,",
  "Jakby psiarnię w nie wpuścił i rozpoczął łowy.",
  "",
  "Bo w graniu była łowów historyja krótka:",
  "Zrazu odzew dźwięczący, rześki: to pobudka;",
  "Potem jęki po jękach skomlą: to psów granie;",
  "A gdzieniegdzie ton twardszy jak grzmot: to strzelanie."
];

function Azure(element) {
  element.style.backgroundColor = '#EFF';
  element.style.borderColor = '#A8A8A8';
  element.style.borderStyle = 'solid';
  element.style.paddingLeft = '5%';
}


function setStyles() {
  // Your existing styling code here
  const header = document.querySelector('header');
  const nav = document.querySelector('nav');
  const aside = document.getElementById('aside');
  const footer = document.getElementById('footer');
  const main = document.getElementById('main');

  Azure(header);
  Azure(nav);
  Azure(aside);
  Azure(main);
  Azure(footer);
  header.style.marginBottom = '25px';

  nav.style.width = '10%';

  aside.style.width = '40%';
  aside.style.position = 'absolute';
  aside.style.top = '100px';
  aside.style.left = '745px';

  footer.style.marginTop = '10px';
  footer.style.width = '100%';

  main.style.width = '35%';
  main.style.marginTop = '25px';
  main.style.fontSize = '1,5vw';
}

function deleteStyles() {
  const elementsToReset = document.querySelectorAll('header, nav, #aside, #footer, #main');
  for (let i = 0; i < elementsToReset.length; i++) {
    elementsToReset[i].style = '';
  }
}

function add() {
  if (paragrafy.length > 0) {
    const paragraph = document.createElement('p');
    paragraph.textContent = paragrafy.shift();
    main.appendChild(paragraph);
  } else {
    document.getElementById('addButton').disabled = true;
  }
}


const styleForm = document.getElementById('styleForm');
styleForm.style.position = 'fixed';
styleForm.style.bottom = '20px';
styleForm.style.right = '20px';

document.getElementById('setButton').addEventListener('click', setStyles);
document.getElementById('deleteButton').addEventListener('click', deleteStyles);
document.getElementById('addButton').addEventListener('click', add);