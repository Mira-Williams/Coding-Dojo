function push_front(array, val){
    for(var i = array.length - 1; i >= 0; i--){
        array[i + 1] = array[i];
    }
    array[0] = val;
    return array;
}

// x = push_front([1,2,3,4,5], 10);
// console.log(x);

function pop_front(array){
    x = array[0];
    for(var i = 1; i < array.length; i++){
        array[i-1] = array[i];
    }
    array.pop();
    return x;
}

// x = [1,2,3,4,5];
// y = pop_front(x);
// console.log(y);

function insert_at(array, index, val){
    for(var i = array.length - 1; i >= index; i--){
        array[i+1] = array[i];
    }
    array[index] = val
    console.log(array);
}

// x = [1,2,3,4,5]
// insert_at(x, 1, 0)

function remove_at(array, index){
    val = array[index]
    for(var i = index + 1; i < array.length; i++){
        array[i-1] = array[i];
    }
    array.pop()
    console.log(array)
    return val
}

// x = [1,2,3,4,5]
// remove_at(x, 3)

function swap_pairs(array){
    for(var i = 0; i < array.length - 1; i+=2){
        temp = array[i]
        array[i] = array[i + 1]
        array[i + 1] = temp
    }
    console.log(array)
}

// x = [1,2,3,4,5]
// swap_pairs(x)

function rem_dup(array){
    var i = 0
    while(i < array.length){
        if(array[i] == array[i + 1]){
            for(j = i + 1; j < array.length; j++){
                array[j] = array[j+1]
            }
            array.pop()
        }
        if(array[i] == array[i + 1]){
            continue
        }
        else{
            i++
        }
    }
    console.log(array)
}

// x = [1,2,2,3,3,3,4,5,5,5,5]
// rem_dup(x)