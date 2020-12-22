function min_to_front(array){
    var min = array[0]
    var index = 0
    for(var i = 0; i < array.length; i++){
        if(array[i] < min){
            min = array[i]
            index = i
        }
    }
    for(var i = index; i >= 1; i--){
        array[i] = array[i - 1]
    }
    array[0] = min
    console.log(array)
}

x = [2,3,4,1,5,6,7]
min_to_front(x)
