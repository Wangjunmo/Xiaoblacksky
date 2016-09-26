var friends = {};
friends.bill = {
    firstName: 'Bill',
    lastName: 'Gates',
    number: 10,
    address : ['Microsoft.Inc']
    };
friends.steve = {
    firstName: 'Steve',
    lastName: 'Jobs',
    number: 10,
    address: ['Apple.Inc']
    };

var list = function(ob){
    for(var key in ob){
        console.log(key);
    }
}
var search = function(name){
    for(var key in friends){
        if(friends[key].firstName === name){
            console.log(friends[key]);
            return friends[key];
        }
    }
}
