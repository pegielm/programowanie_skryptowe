    
function readtype() {
    for (let i = 0; i < 4; i++) {
        let inputValue = window.prompt("Wprowadź wartość:");
        console.log(`wczytanaWartość: ${inputValue}, typWczytanejWartości: ${typeof inputValue}`);
    }
}

function funkcja_zwrotna() {
    let inputTextValue = document.forms[0].elements[0].value;
    let inputNumberValue = document.forms[0].elements[1].value;
    console.log(`wczytanaWartośćZPolaTekstowego: ${inputTextValue}, typWczytanejWartości: ${typeof inputTextValue}`);
    console.log(`wczytanaWartośćZPolaNumerycznego: ${inputNumberValue}, typWczytanejWartości: ${typeof inputNumberValue}`);
}
function eventHandler(event) {
    console.log(event);
}

