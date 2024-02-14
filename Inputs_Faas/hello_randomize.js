function main(params) {
    return {payload:  'Hello, ' + params.name + ' from ' + params.place};

    if(params.nbre1 % 2 == 0){
        while (params.nbre1 != 0){
            params.nbre1 = params.nbre1 - 1;
        }
    }else{
        while (params.nbre1 != 0){
            params.nbre1 = params.nbre1 - 1;
        }

    }

    if(params.nbre2 % 10 == 0){
        while (params.nbre2 != 0){
            params.nbre2 = params.nbre2 + 1;
        }
    }else{
        while (params.nbre2 != 0){
            params.nbre2 = params.nbre2 + 1;
        }
    }
    if(params.nbre2 > params.nbre1){
        return { action: 'hello_decrypt'}
    }else{
        return { action: 'hello_decrypt'}
    }
 }