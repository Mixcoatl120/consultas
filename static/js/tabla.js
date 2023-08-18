$(document).ready(function(){
    $('#example').DataTable({
        ajax: '/api/data',
        scrollY: 200,
        deferRender: true,
        scroller: true
    });
});
