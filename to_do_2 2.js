function reverse(array){
    for(var i = 0; i < array.length / 2; i++){
        temp = array[i]
        array[i] = array[array.length - 1 - i]
        array[array.length - 1 - i] = temp
    }
    console.log(array)
}

// x = [1,2,3,4,5,6]
// reverse(x)

function rotate(array, shift){
    if(shift >= 0){
        for(var j = 0; j < shift; j++){
            for(var i = array.length - 1; i >= 0; i--){
                array[i + 1] = array[i]
            }
            array[0] = array[array.length - 1]
            array.pop()
        }
    }
    else{
        for(var j = 0; j > shift; j--){
            temp = array[0]
            for(var i = 1; i < array.length; i++){
                array[i - 1] = array[i]
            }
            array[array.length - 1] = temp
        }
    }
    console.log(array)
}

// x = [1,2,3,4,5,6,7,8,9,10]
// rotate(x, -3)

function filter_range(array, min, max){
    for(var i = 0; i < array.length; i++){
        if(array[i] < min || array[i] > max){
            for(var j = i; j < array.length; j++){
                array[j] = array[j + 1]
            }
            array.pop()
            i--
        }
    }
    console.log(array)
}

// x = [1,2,3,4,5,6,7,8,9]
// filter_range(x, 4, 7)

function concat(array_1, array_2){
    arr_1_len = array_1.length
    for(var i = 0; i < array_2.length; i++){
        array_1[arr_1_len + i] = array_2[i]
    }
    console.log(array_1)
}

x = [1,2,3,4]
y = [5,6,7,8]
concat(x, y)

