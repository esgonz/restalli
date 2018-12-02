// Call the dataTables jQuery plugin
//$(document).ready(function() {
//	
//  $('#dataTable').DataTable({
//  	"lengthMenu": [[5, 10, 25, 50, -1], [5, 10, 25,50,  "Todos"]]
//  });
//});

  $(document).ready(function() {
  
    $('#dataTable').DataTable({
      "lengthMenu": [[5, 10, 25, 50, -1], [5, 10, 25,50,  "Todos"]],
      "language": {
          search: "_INPUT_",
          searchPlaceholder: "Buscar...",
      "decimal":        "",
      "emptyTable":     "Sin informacion disponible para la tabla",
      "info":           "Ver _START_ hasta _END_ de _TOTAL_ registros",
      "infoEmpty":      "Mostrando 0 hasta 0 de 0 registros",
      "infoFiltered":   "(Filtrado de _MAX_ registros totales)",
      "infoPostFix":    "",
      "thousands":      ",",
      "lengthMenu":     "Mostrar _MENU_ Entradas",
      "loadingRecords": "Cargando...",
      "processing":     "Procesando...",

      "zeroRecords":    "No se encontro nada",
      "paginate": {
          "first":      "Primera",
          "last":       "Última",
          "next":       "Próxima",
          "previous":   "Anterior"
      },
      "aria": {
          "sortAscending":  ": activate to sort column ascending",
          "sortDescending": ": activate to sort column descending"
      }


          }
    });
  });