/**
 * @param {string} s
 * @param {number} numRows
 * @return {string}
 */

/*
    * P   A   H   N
    * A P L S I I G
    * Y   I   R
    *
    * P     I    N
    * A   L S  I G
    * Y A   H R
    * P     I
    *
    * grid = [[""*numCols]*numRows]
    * x = 0
    * y = 0
    *
    * progression = "D"
    *
    * for i in 0..s.len()
    *   grid[x][y] = s[i]
    *   switch progression:
    *       case "D":
    *         y+=1
    *         break
    *       case "UDIA":
    *         x+=1
    *         y-=1
    *         break
    *       default:
    *         break
    *   if y==numRows
    *     progression = "UDIA"
    *   else if y==-1
    *     progression = "D"
*/

var convert = function(s, numRows) {
    grid = Array(numRows).fill().map(() => Array(s.length).fill(' '));

    let x = 0;
    let y = 0;

    let downProgression = true;

    for (let i = 0; i<s.length; i++) {
        if (y >= numRows) {
            x++;
            y = numRows-2;
            downProgression = false;
        } else if (y < 0) {
            downProgression = true;
            y = 1;
            x-=1;
        }

        grid[y][x] = s[i];

        if(downProgression){
            y+=1;
        } else {
            x+=1;
            y-=1;
        }
    }

    let result = "";
    for (let i = 0; i < grid.length; i++) {
        for (let j=0; j < grid[i].length; j++) {
            if (grid[i][j] != ' ') {
                result += grid[i][j];
            }
        }
    }
    return result;
};

var renderGrid = function(grid) {
    for (let i = 0; i < grid.length; i++) {
        for (let j=0; j < grid[i].length; j++) {
            process.stdout.write(grid[i][j]);
            process.stdout.write(" ");
        }
        console.log("");
    }
}

let s = "PAYPALISHIRING";
let numRows = 3;
convert(s, numRows);
