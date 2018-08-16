document.addEventListener("DOMContentLoaded", function() {
    var elements = document.getElementsByTagName("INPUT");
    for (var i = 0; i < elements.length; i++) {
        elements[i].oninvalid = function(e) {
            e.target.setCustomValidity("");
            if (!e.target.validity.valid) {
                e.target.setCustomValidity("Por favor rellene este campo.");
            }
        };
        elements[i].oninput = function(e) {
            e.target.setCustomValidity("");
        };
    }
});
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
});
