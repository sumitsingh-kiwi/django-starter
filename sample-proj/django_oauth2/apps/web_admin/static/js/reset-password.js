function formValidation(){
  // Initialize form validation on the registration form.
  // It has the name attribute "registration"
  $("form[name='reset-password']").validate({
    // Specify validation rules
    rules: {
      // The key name on the left side is the name attribute
      // of an input field. Validation rules are defined
      // on the right side
      new_password: {required: true, maxlength: 30, minlength: 8},
      confirm_password: {required: true, maxlength: 30, minlength: 8},
    },
    // Specify validation error messages
    highlight: function(element, errorClass, validClass) {
        $(element).parent().addClass("error");
    },
    unhighlight: function(element, errorClass, validClass) {
        $(element).parent().removeClass("error");
    },
    // Make sure the form is submitted to the destination defined
    // in the "action" attribute of the form when valid
    submitHandler: function(form, event) {
        event.preventDefault();
        if($("#new-password").val() !== $("#confirm-password").val()){
            showError("New Password & conform password should be equal");
            return false;
        }else{
            form.submit();
        }
        return true;
    }
  });

}

$( document ).ready(function() {

    // added form validations
    formValidation();
    timeOut();
});
