$(document).ready(function() {
    $("#recetas").hide();
    $("#ingredientes").show();
    $("#add-receta-filter").on("keyup", function () {
        var value = $(this).val().toLowerCase();
        $("#add-receta-table tr:not(.table-head)").filter(function () {
            $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
        });
    });
    $(".nav-link").click(function () {
        $(this).addClass('active');
        $(".nav-link").not(this).removeClass('active');
        $($(this).attr('href')).show();
        $(".tab-pane").not($(this).attr('href')).hide();
    });
    $(".bmd-label-static").removeClass("bmd-label-static").addClass("bmd-label-floating");
    $("label").not(".bmd-label-floating").addClass("bmd-label-floating");
});
