package unidirectional_tsp_116;

import java.io.*;
import java.util.*;


/**
 * Created by jimmy on 2016-11-03.
 */
public class Main {
    InputStreamReader isr = null;
    BufferedReader br = null;

    public void run() throws IOException {
        isr = new InputStreamReader(System.in);
// -------------- FOR READING LOCAL FILE -------------
        String path = "unidirectional_tsp_116/input_data.txt";
        isr = new InputStreamReader(new FileInputStream(new File(path)));
// ---------------------------------------------------
        br = new BufferedReader(isr);
        String rowsCols = br.readLine();
        int rows = Integer.parseInt(rowsCols.split(" ")[0]);
        int cols = Integer.parseInt(rowsCols.split(" ")[1]);
        boolean running = true;
        while (running) {
            int[][] matrix = new int[rows][cols];
            long[][] dist = new long[rows][cols];
            int[][] next = new int[rows][cols];
            int[] dir = new int[3];

            // Building the matrix and arrays for distance/neighbor
            int row = 0;
            int col = 0;
            int count = 0;
            while (count < rows * cols) {
                String[] newRow = br.readLine().split(" ");
//                int newRowLength = newRow.length;
//                if(newRow[newRow.length - 1] == " ") {
//                    newRowLength--;
//                }
                int countInput = 0;
                while (countInput < newRow.length) {
                    matrix[row][col] = Integer.parseInt(newRow[countInput]);
                    dist[row][col] = Long.MAX_VALUE;
                    next[row][col] = -1;
                    if (col == cols - 1) {
                        dist[row][col] = matrix[row][col];
                        row++;
                    }
                    count++;
                    countInput++;
                    col = (col + 1) % cols;
                }
            }

            for (int c = cols - 2; c >= 0; c--) {
                for (int r = 0; r < rows; r++) {
                    // 3 variables for the different movements allowed
                    // from each index in matrix
                    int rowUp = r == 0 ? rows - 1 : r - 1; // diagonal up
                    int rowDown = (r + 1) % rows; // diagonal down
                    int nextCol = c + 1; //
                    //finding "closest" neighbor and updating distance array
                    long min_weight = Math.min(Math.min(dist[rowUp][nextCol], dist[r][nextCol]), dist[rowDown][nextCol]);
                    dist[r][c] = matrix[r][c] + min_weight;

                    // Updating next array with index to it's closest neighbor
                    next[r][c] = Integer.MAX_VALUE;
                    int[] rowsToTry = {rowUp, r, rowDown};
                    // Sorts the rowsToTry so we automatically get min weight AND
                    // minimum index som it will be lexicographically smallest
                    Arrays.sort(rowsToTry);
                    for(int nextRow: rowsToTry) {
                        if (next[r][c] == Integer.MAX_VALUE ||
                                (dist[nextRow][nextCol] == min_weight &&
                                 dist[nextRow][nextCol] < dist[next[r][c]][nextCol])){
                            next[r][c] = nextRow;
                        }
                    }
                }
            }

            // getting shortest path and total minimum distance of path
            int start = 1000;
            long min_value = Long.MAX_VALUE;
            // Getting the start index
            for(int i = 0; i < rows; i++){
                if(min_value > dist[i][0]){
                    min_value = dist[i][0];
                    start = i;
                }
            }
            String min_path = String.valueOf(start + 1);
            long distance = dist[start][0];
            for(int i = 0; i < cols - 1; i++) {
                min_path += " " + (next[start][i] + 1);
                start = next[start][i];
            }
            //Print result
            System.out.println(min_path);
            System.out.println(distance);

            // Check if there are more lines or not!
            try {
                rowsCols = br.readLine();
                rows = Integer.parseInt(rowsCols.split(" ")[0]);
                cols = Integer.parseInt(rowsCols.split(" ")[1]);
            } catch (NullPointerException eof){
                break;
            }
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
