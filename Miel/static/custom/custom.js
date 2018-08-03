$(document).ready(function(){
  $("#add-receta-filter").on("keyup", function() {
    var value = $(this).val().toLowerCase();
    $("#add-receta-table tr:not(.table-head)").filter(function() {
      $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
    });
  });
});
