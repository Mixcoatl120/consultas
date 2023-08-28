// JavaScript source code
var boton = document.getElementById('r_con');
var checks = document.querySelectorAll('.form-check-input');
var tip_asunto = "";
var tip_dir_gen = "";
boton.addEventListener('click', function () {
    con_tipingre.innerHTML = '';
    checks.forEach((e) => {
        if (e.checked == true) {
            if (e.value == "tipoingreso = 'ASUNTO'" || e.value == "tipoingreso = 'TRAMITE'") {
                if (tip_asunto = "") {
                    tip_asunto = "and " + e.value;
                }
                else {
                    tip_asunto = tip_asunto + " or " + e.value;
                }
            }
            if()
        }
    });
});