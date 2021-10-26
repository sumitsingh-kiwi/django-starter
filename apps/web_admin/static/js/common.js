var successDiv = "success-div";
var errorDiv = "error-div";

function logout(){
    // used to logout the user
    document.forms['logout-form'].submit()
}

function logoutConfirm(){
    // call to show the popup
    $("#confirmation-modal-title").html("Logout");
    $("#confirmation-modal-description").html("Are you sure want to logout?");
    $("#confirmation-modal-yes-button").attr("onClick", "logout()");
    $("#confirmation-modal-yes-button").html("Yes");
    $("#confirmation-modal-no-button").html("Cancel");
    $("#deactivate-customer").modal('show');
}

function timeOut(){
    // used to disappear the success/error msg
    setTimeout(function(){
          var x = document.getElementById(errorDiv);
          if(x){
            x.style.display = "none";
          }
          var y = document.getElementById(successDiv);
          if(y){
            y.style.display = "none";
          }
    }, 4500	);
}

function showLoader(){
    let loaderDiv = '<div class="inner-loader"></div>';
    $(".loader").append(loaderDiv);
}

function hideLoader(){
    $(".loader").remove();
}

function showError(message){
    if(document.getElementById(errorDiv)){
        $(errorDiv).html(message);
        $(errorDiv).css('display', "flex");
    }else{
        var error_div = '<div class="alert-main show"><div class="alert alert-danger" id="error-div"'+
                        ' style="display: flex;">'+message+'</div></div>';
        $(error_div).insertAfter(".body");
    }
    timeOut();
}

function showSuccess(message){
    if(document.getElementById(successDiv)){
        $(successDiv).html(message);
        $(successDiv).css('display', "flex");
    }else{
        var success_div = '<div class="alert-main show"><div class="alert alert-success" id="success-div"'+
                        ' style="display: flex;">'+message+'</div></div>';
        $(success_div).insertAfter(".body");
    }
    timeOut();
}
