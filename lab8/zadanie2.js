
function sum_strings(a) {

    let sum = 0;
  
    for (let i = 0; i < a.length; i++) {
      // Sprawdzenie, czy napis można przekształcić na liczbę
      const num = parseFloat(a[i]);
      
      if (!isNaN(num)) {
        sum += num;
      }
    }
  
    // Zwróć obliczoną sumę
    return sum;
  }
  
  function digits(s) {
    let oddSum = 0;
    let evenSum = 0;
  
    for (let i = 0; i < s.length; i++) {
      if (!isNaN(parseInt(s[i]))) {
        if (parseInt(s[i]) % 2 !== 0) {
          oddSum += parseInt(s[i]);
        }
        else {
          evenSum += parseInt(s[i]);
        }
      }
    }
  
    return [oddSum, evenSum];
  }
  
  function letters(s) {
    let lowercaseCount = 0;
    let uppercaseCount = 0;
  
    for (let i = 0; i < s.length; i++) {
      if (/[a-zA-Z]/.test(s[i])) {
        if (s[i] === s[i].toLowerCase()) {
          lowercaseCount++;
        }
        else {
          uppercaseCount++;
        }
      }
    }
  
    return [lowercaseCount, uppercaseCount];
  }
