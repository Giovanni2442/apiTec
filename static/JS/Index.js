function pruebas(){
    const $div = document.querySelector(".cnt-message");
    
    
}

const ajax = ()=>{
    fetch('http://127.0.0.1:2000/getUssers')
        .then(res =>{ return res.ok ? res.json() : Promise.reject()
        })
        .then(json =>{
            console.log(json);
        })
        .catch(err =>{
            let msg = err.statusText || "Ocurrio un error";                     // "||" : Se le conoce como "coalecencia nula" y se aplica al que le sigue de las barras si cumple con : "(undefined, null, false, 0, "" o NaN)"
            return console.log(`Error ${err.message} : ${msg}`);
    });
}

const elements = (json)=>{
    
}


pruebas();