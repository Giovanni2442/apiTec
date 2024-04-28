 /*
	#DOCUMENTO DE PRUEBAS CARPETE TEMPDIR/

*/
function pr(){
    const $inpts = document.querySelectorAll(".frm input"),
    $form = document.querySelector(".frm"),
    $btnSend = document.getElementById("request")

    let b1 = 0;
    let url = 'http://127.0.0.1:2000/insert';
    document.addEventListener("submit", async(e) =>{
        let data = e.target;
        //console.log();
        e.preventDefault();
        if(data === $form){
            //console.log(data);
            e.preventDefault();
            $inpts.forEach(el => { if(el.value === '') b1 = 1; });
            if(b1!=0){
                console.log("Falta");
                b1 = 0;
            }else{
                const POST_request = {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({
                        "id" : data.id_ing.value,
                        "ingenieria" : data.name_ing.value,
                        "reticula" : [
                            {
                                "clave" : data.clave.value,
                                "nombre" : data.name_mtr.value,
                                "creditos" : data.creditos.value,
                                "semestre" : data.semestre.value
                            }
                        ]
                    })
                };

                ajax('http://127.0.0.1:2000/insrt');
                
                //console.log();
            }
        }
    });
}

const ajax = async(api_url) =>{
    return fetch(api_url)
    .then(res =>{ if(res.ok){ console.log("send ok!"); return res.json(); } else {Promise.reject() }})
    .catch(err =>{
        let msg = err.statusText || "Ocurrio un error";                     // "||" : Se le conoce como "coalecencia nula" y se aplica al que le sigue de las barras si cumple con : "(undefined, null, false, 0, "" o NaN)"
        return console.log(`Error ${err.message} : ${msg}`);
    })
}

function hola(){
    console.log("Hola");
}
//hola();
pr();
