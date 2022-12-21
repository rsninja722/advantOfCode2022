function main(input) {
    input = input.split("\n");
    var sum = 0;
    // for (var i = 0; i < input.length; i++) {
    //     l = findCommon(input[i]);
    //     l = l.charCodeAt(0);
    //     if(l > 96) {
    //         l -= 96;
    //     } else if(l > 64) {
    //         l -= 38;
    //     }
    //     sum += l;
    // }
    for (var i = 0; i < input.length; i+=3) {
        l = findCommon3(input[i],input[i+1],input[i+2]);
        l = l.charCodeAt(0);
        if(l > 96) {
            l -= 96;
        } else if(l > 64) {
            l -= 38;
        }
        sum += l;
    }

    return sum;
}

function findCommon(s) {
    secondHalf = s.slice(s.length / 2);
    for(var i = 0; i < s.length/2; i++) {
        var c = s.charAt(i);
        if(secondHalf.indexOf(c) > -1) {
            return c;
        }
    }
}

function findCommon3(a,b,c) {
    for(var i = 0; i < a.length; i++) {
        var cc = a.charAt(i);
        if(b.indexOf(cc) > -1 && c.indexOf(cc) > -1) {
            return cc;
        }
    }
}


main(``);