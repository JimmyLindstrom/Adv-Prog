package roman_numerals_185;

import java.io.*;
import java.util.*;

/**
 * Created by jimmy on 2016-11-13.
 */
public class Main {
    InputStreamReader isr = null;
    BufferedReader br = null;
    String[] romanNumbers;
    int arabicSum;
    Map<Character, Integer> distinctDigits;
    List<Character> digits;


    // hjälp metod som tar en romersk bokstav som parameter och returnerar dess värde
    public int getArabicValue(char roman) {
        switch (roman){
            case 'M': return 1000;
            case 'D': return 500;
            case 'C': return 100;
            case 'L': return 50;
            case 'X': return 10;
            case 'V': return 5;
            case 'I': return 1;
            default: return 0;
        }
    }

    // tilldelar ett unikt värde mellan 0-9 för varje distinkt bokstav i den romerska summan.
    // Sen kontrolleras ifall de tilldelade värdena ger en korrekt summa. Counter håller reda
    // på antalet korrekta summor, och överstiger det 1 innebär det att det är en tvetydig
    // tolkning. Counter = 1 innebär att det bara finns en korrekt uppsättning värden, och 0
    // innebär att det är en omöjligt att tolka den som en arabiska summa!
    private int checkCombinations() {
        int counter = 0;
        for (int i1 = 0; i1 < 10; i1++) {
            distinctDigits.put(digits.get(0), i1);
            for (int i2 = 0; i2 < 10; i2++) {
                if (i2 == i1)
                    continue;
                if(1 == digits.size()) {
                    counter = checkArabicSum(counter);
                    if(counter > 1)
                        return counter;
                    break;
                }
                distinctDigits.put(digits.get(1), i2);

                for (int i3 = 0; i3 < 10; i3++) {
                    if (i3 == i2 || i3 == i1)
                        continue;
                    if(2 == digits.size()) {
                        counter = checkArabicSum(counter);
                        if(counter > 1)
                            return counter;
                        break;
                    }
                    distinctDigits.put(digits.get(2), i3);

                    for (int i4 = 0; i4 < 10; i4++) {
                        if (i4 == i3 || i4 == i2 || i4 == i1)
                            continue;
                        if(3 == digits.size()) {
                            counter = checkArabicSum(counter);
                            if(counter > 1)
                                return counter;
                            break;
                        }
                        distinctDigits.put(digits.get(3), i4);

                        for (int i5 = 0; i5 < 10; i5++) {
                            if (i5 == i4 || i5 == i3 || i5 == i2 || i5 == i1)
                                continue;
                            if(4 == digits.size()) {
                                counter = checkArabicSum(counter);
                                if(counter > 1)
                                    return counter;
                                break;
                            }
                            distinctDigits.put(digits.get(4), i5);

                            for (int i6 = 0; i6 < 10; i6++) {
                                if (i6 == i5 || i6 == i4 || i6 == i3 || i6 == i2 || i6 == i1)
                                    continue;
                                if(5 == digits.size()) {
                                    counter = checkArabicSum(counter);
                                    if(counter > 1)
                                        return counter;
                                    break;
                                }
                                distinctDigits.put(digits.get(5), i6);

                                for (int i7 = 0; i7 < 10; i7++) {
                                    if (i7 == i6 || i7 == i5 || i7 == i4 || i7 == i3 || i7 == i2 || i7 == i1)
                                        continue;
                                    if(6 == digits.size()) {
                                        counter = checkArabicSum(counter);
                                        if(counter > 1)
                                            return counter;
                                        break;
                                    }
                                    distinctDigits.put(digits.get(6), i7);

                                    counter = checkArabicSum(counter);
                                    if(counter >= 2 ) {
                                        return counter;
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
        return counter;
    }

    // kontrollerar summan med tilldelade värden för varje bokstav
    private int checkArabicSum(int counter) {
        String[] numbers = {"", "", ""};
        for (int i = 0; i < romanNumbers.length; i++) {
            for (int j = 0; j < romanNumbers[i].length(); j++) {
                if(j == 0 && distinctDigits.get(romanNumbers[i].charAt(j)) == 0) {
                    return counter;
                }
                numbers[i] += String.valueOf(distinctDigits.get(romanNumbers[i].charAt(j)));
            }
        }
        // ifall summan blir korrekt öka counter med 1
        if(Integer.parseInt(numbers[0]) + Integer.parseInt(numbers[1]) == Integer.parseInt(numbers[2])){
            counter++;
        }
        return counter;
    }

    // omvandlar de romerska siffrorna till nummer och returnerar dem
    private int[] romanToArabic(String[] romanNumbers) {
        int[] numbers = {0, 0, 0};
        for (int i = 0; i < romanNumbers.length; i++) {
            String tempRoman = romanNumbers[i];
            for (int j = 0; j < tempRoman.length(); j++) {
                int current = getArabicValue(tempRoman.charAt(j));
                if(j < tempRoman.length() - 1 &&
                        current < getArabicValue(tempRoman.charAt(j + 1))) {
                    numbers[i] -= current;
                } else {
                    numbers[i] += current;
                }
            }
        }
        return numbers;
    }

    // metod som läser in romerska summor
    public void run() throws IOException {
        isr = new InputStreamReader(System.in);
// -------------- FOR READING LOCAL FILE -------------
        String path = "roman_numerals_185/input_data.txt";
        isr = new InputStreamReader(new FileInputStream(new File(path)));
// ---------------------------------------------------
        br = new BufferedReader(isr);
        String newSum = br.readLine();
        while(!newSum.equals("#")) {
            romanNumbers = new String[3];
            romanNumbers = newSum.split("\\W");
            // kontrollerar ifall den romerska summan är korrekt
            int[] arabicNumbers = romanToArabic(romanNumbers);
            if(arabicNumbers[0] + arabicNumbers[1] == arabicNumbers[2]) {
                System.out.print("Correct ");
            } else {
                System.out.print("Incorrect ");
            }


            distinctDigits = new HashMap<>();
            digits = new ArrayList<>();
            for(String str: romanNumbers) {
                for (int i = 0; i < str.length(); i++) {
                    if (!distinctDigits.containsKey(str.charAt(i))) {
                        distinctDigits.put(str.charAt(i), -1);
                        digits.add(str.charAt(i));
                    }
                }
            }
            // kontrollerar ifall den romerska summan kan tolkas som en giltig/ogiltig/tvetydig
            // arabisk kodning
            arabicSum = checkCombinations();
            if (arabicSum == 0)
                System.out.println("impossible");
            else if (arabicSum == 1)
                System.out.println("valid");
            else if (arabicSum > 1)
                System.out.println("ambiguous");

            newSum = br.readLine();

        }
    }

    public static void main(String[] args) {
        Main program = new Main();
        try {
            program.run();
        } catch (IOException io) {
            System.out.println(("IOEXCEPTION"));
        }
    }
}
