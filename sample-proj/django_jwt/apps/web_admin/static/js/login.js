function loginFormValidation(){
  // Initialize form validation on the registration form.
  // It has the name attribute "registration"
  $("form[name='login_form']").validate({
    // Specify validation rules
    rules: {
      email: {required: true, email: true},
      password: {required: true},
    },
    highlight: function(element, errCls, validClass) {
        $(element).parent().addClass("error");
    },
    unhighlight: function(element, errCls, validClass) {
        $(element).parent().removeClass("error");
    },
    // Make sure the form is submitted to the destination defined
    // in the "action" attribute of the form when valid
    submitHandler: function(formElement) {
        formElement.submit();
    }
  });
}

$( document ).ready(function() {

    // added form validations
    loginFormValidation();
    timeOut();
});
