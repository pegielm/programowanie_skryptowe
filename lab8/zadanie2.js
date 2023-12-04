// Plik: zadanie2.js

// Funkcja obliczająca sumę liczb w tablicy napisów
function sum_strings(a) {
    // Inicjalizacja zmiennej przechowującej sumę
    let sum = 0;
  
    // Iteracja po każdym napisie w tablicy
    for (let i = 0; i < a.length; i++) {
      // Sprawdzenie, czy napis można przekształcić na liczbę
      const num = parseFloat(a[i]);
      
      // Jeśli przekształcenie było możliwe, dodaj do sumy
      if (!isNaN(num)) {
        sum += num;
      }
    }
  
    // Zwróć obliczoną sumę
    return sum;
  }
  
  // Funkcja obliczająca sumę cyfr nieparzystych i parzystych w napisie
  function digits(s) {
    // Inicjalizacja zmiennych przechowujących sumy
    let oddSum = 0;
    let evenSum = 0;
  
    // Iteracja po każdym znaku w napisie
    for (let i = 0; i < s.length; i++) {
      // Sprawdzenie, czy znak jest cyfrą
      if (!isNaN(parseInt(s[i]))) {
        // Jeśli cyfra jest nieparzysta, dodaj do sumy liczb nieparzystych
        if (parseInt(s[i]) % 2 !== 0) {
          oddSum += parseInt(s[i]);
        }
        // W przeciwnym razie dodaj do sumy liczb parzystych
        else {
          evenSum += parseInt(s[i]);
        }
      }
    }
  
    // Zwróć wynik w postaci tablicy
    return [oddSum, evenSum];
  }
  
  // Funkcja obliczająca ilość małych i dużych liter w napisie
  function letters(s) {
    // Inicjalizacja zmiennych przechowujących ilość małych i dużych liter
    let lowercaseCount = 0;
    let uppercaseCount = 0;
  
    // Iteracja po każdym znaku w napisie
    for (let i = 0; i < s.length; i++) {
      // Sprawdzenie, czy znak jest literą
      if (/[a-zA-Z]/.test(s[i])) {
        // Jeśli litera jest mała, zwiększ ilość małych liter
        if (s[i] === s[i].toLowerCase()) {
          lowercaseCount++;
        }
        // W przeciwnym razie zwiększ ilość dużych liter
        else {
          uppercaseCount++;
        }
      }
    }
  
    // Zwróć wynik w postaci tablicy
    return [lowercaseCount, uppercaseCount];
  }
  /*
  console.log(sum_strings(["123", "146a2B", "", "b3345a", "\t"]));
  var pierwsza = "123";
  var druga = "146a2B";
  var trzecia = "b3345a";
  console.log(digits(pierwsza));
  console.log(digits(druga));
  console.log(digits(trzecia));
  console.log(letters(pierwsza));
  console.log(letters(druga));
  console.log(letters(trzecia));
 */