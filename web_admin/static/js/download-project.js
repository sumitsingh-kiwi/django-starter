function formValidation(){
  // Initialize form validation on the registration form.
  // It has the name attribute "registration"
  $("form[name='download-project']").validate({
    // Specify validation rules
    rules: {
      // The key name on the left side is the name attribute
      // of an input field. Validation rules are defined
      // on the right side
      project_name: {required: true, maxlength: 30, projectNameValidation: true},
    },
    messages: {
        project_name: {maxlength: "Not more than 30 Char are allowed"},
    },
    // Specify validation error messages
    highlight: function(element, errorClass, validClass) {
        $(element).parent().addClass("error");
    },
        unhighlight: function(element, errorClass, validClass) {
            $(element).parent().removeClass("error");
//            label.remove();
        },
    // Make sure the form is submitted to the destination defined
    // in the "action" attribute of the form when valid
    submitHandler: function(form, event) {
        form.submit();
    }
  });

  jQuery.validator.addMethod("projectNameValidation", function(value, element){
      if(value.match(/^[^_0-9][a-zA-Z0-9_]+$/)){
        if(!value.match(/[^a-zA-Z0-9_]/)){
            if (isNaN(parseInt(value))) {return true;}
            }
      }
      return false;
  }, "Invalid project name");
}


function timeOut(){
    // used to disappear the success/error msg
    setTimeout(function(){
          var x = document.getElementById("message-div");
          if(x){
            x.style.display = "none";
          }
    }, 4500	);
}

$( document ).ready(function() {

    // added form validations
    formValidation();
    timeOut();

});