function remove_blanks(string){
    array = string.split(' ')
    string = array.join('')
    console.log(string)
}

// x = 'Pl ayTha tF u nkyM usi c'
// remove_blanks(x)

function get_digits(string){
    array = []
    for(var i = 0; i < string.length; i++){
        if(string[i] >= '0' && string[i] <= '9'){
            array.push(string[i])
        }
    }
    string = array.join('')
    console.log(string)
}

// x = "0s1a3y5w7h9a2t4?6!8?0"
// get_digits(x)

function acronym(string){
    array = string.split(' ')
    array_2 = []
    for (var i = 0; i < array.length; i++){
        array_2.push(array[i][0].toUpperCase())
    }
    string = array_2.join('')
    console.log(string)
}

// x = "there's no free lunch - gotta pay yer way."
// acronym(x)

function count_non_spaces(string){
    array = string.split(' ')
    string = array.join('')
    console.log(string.length)
}

// x = 'Honey pie, you are driving me crazy'
// count_non_spaces(x)

function rem_short_strings(array, length){
    new_array = []
    for (var i = 0; i < array.length; i++){
        if (array[i].length < length){
            new_array.push(array[i])
        }
    }
    console.log(new_array)
}

// x = ['adam', 'tony', 'alexander', 'bob', 'joseph', 'tyrone', 'jessica', 'mary', 'kate', 'lisa']
// rem_short_strings(x, 5)