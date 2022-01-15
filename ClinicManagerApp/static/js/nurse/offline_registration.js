window.onload = function () {
  $("#add_customer_result").modal("toggle");
};

$(document).ready(function () {

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

  // reset regist
  $('#reset').click(function () {
    $('#id_card').val('')
    $('#last_name').val('')
    $('#first_name').val('')
    $('#date_of_birth').val('')
    $('#email').val('')
    $('#address').val('')
    $('#phone_number').val('')
    $("#male").prop("checked", true);
  });
});