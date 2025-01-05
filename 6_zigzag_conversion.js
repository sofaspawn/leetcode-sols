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
    * for i in 0..s.len()
    *   grid[x][y] = s[i]
    *   y += 1
    *   if y == numRows
*/

var convert = function(s, numRows) {
    grid = Array(numRows).fill().map(() => Array(s.length).fill('_'));

    let x = 0;
    let y = 0;

    let progression = "D";

    for (let i = 0; i<s.length; i++) {
        grid[x][y] = s[i];
        if (progression==="D"){
            y+=1;
        }
    }

    renderGrid(grid);
};

var renderGrid = function(grid) {
    for (let i = 0; i < grid.length; i++) {
        for (let j=0; j < grid[i].length; j++) {
            process.stdout.write(grid[i][j]);
        }
        console.log("");
    }
}

let s = "PAYPALISHIRING";
let numRows = 3;
convert(s, numRows);
