'use strict';

function node(value){
    var value, left, right;

    var self =  {
        value : value,
        left : left,
        right : right
    };

    return self;
};

function create_tree(totalnodes){    

    var current, root;

    for(var i = 0; i < totalnodes; i++){
        if(current === undefined){
            current = root = node(i);
            continue;
        }        
        if(current.left === undefined){
            current.left = node(i); 
            continue;
        }
        if(current.right === undefined){
            current.right = node(i);
            continue;
        }

        if(1 % 2 == 0){
            current = current.left;
        }else{
            current = current.right;
        }
    }

    return root;
}

var root = create_tree(10);

console.log(JSON.stringify(root, null, 2));
