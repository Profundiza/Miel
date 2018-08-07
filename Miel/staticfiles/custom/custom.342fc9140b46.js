$(document).ready(function(){
  $("#recetas").hide();
  $("#ingredientes").show();
  $("#add-receta-filter").on("keyup", function() {
    var value = $(this).val().toLowerCase();
    $("#add-receta-table tr:not(.table-head)").filter(function() {
      $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
    });
  });
  $(".nav-link").click(function() {
    $(this).addClass('active');
    $(".nav-link").not(this).removeClass('active');
    $($(this).attr('href')).show();
    $(".tab-pane").not($(this).attr('href')).hide();
  });
  //$(".form-group input").addClass('form-control');
  //$(".form-group label").addClass('bmd-label-floating');
/*  $(".rec-edit-modal").click(function(ev) {
    ev.preventDefault();
    var url = $(this).data("form");
    $("#modal").load(url, function() {
      $(this).modal.show();
    });
    return false;
  })*/
});
