$(document).ready(function () {
  window.onload = function () {
    $("#add_customer_result").modal("toggle");
  };

  $('#date_of_birth').datetimepicker({
    format: 'DD/MM/YYYY'
  });

  /* validate */
  $("#customer_info").validate({
    validClass: "success",
    required: true,
    rules: {
      phoneNumber: {
        matches: "[0-9]+",
        minlength: 10,
        maxlength: 10
      }
    },
    highlight: function (element) {
      $(element).closest('.form-group').removeClass('has-success').addClass('has-error');
    },
    success: function (element) {
      $(element).closest('.form-group').removeClass('has-error').addClass('has-success');
    },
  });
});