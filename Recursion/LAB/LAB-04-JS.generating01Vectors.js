const generate = (n) => {
    let vector = new Array(n).fill(0);

    function gen01(startIdx, vector) {
        if (startIdx >= vector.length){
            console.log(vector);
            return
        }
        for (let i = 0; i < 2; i++) {
            vector[startIdx] = i;
            gen01(startIdx + 1, vector);
        }
    }

    gen01(0, vector);
};

generate(5);
