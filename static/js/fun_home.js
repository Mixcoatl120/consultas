// JavaScript source code
var boton = document.getElementById('r_con');
var con_tipingre = document.getElementById('con_tipingre');
var con_dirgen = document.getElementById('con_dirgen')
var checks = document.querySelectorAll('.form-check-input');
var cadena = "";
boton.addEventListener('click', function () {
    con_tipingre.innerHTML = '';
    checks.forEach((e) => {
        if (e.checked == true) {
            var elem = document.createElement('li');
            elem.className = 'list_g';
            elem.innerHTML = e.value;
            con_tipingre.appendChild(elem);
            if (cadena == "") {
                cadena = cadena + e.value;
            }
            else {
                cadena = cadena + " " + e.value;
            }
        }
    });
    document.getElementById('con').value = cadena;
});