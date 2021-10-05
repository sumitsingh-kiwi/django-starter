[![GitHub Super-Linter](https://github.com/sumitsingh-kiwi/django-starter/workflows/Lint%20Code%20Base/badge.svg)](https://github.com/marketplace/actions/super-linter)

# ready to use Django Project

## Steps to use this project:

* create a python3.8 environment and activate it
* inside the main directory, create a .env file as follow and then edit the value according to the need
    > cp .env.sample .env
* install all the requirements 
    > pip install -r requirements.txt
* Please look into the accounts > models > auth.py , Please do the required changes as per 
  your project requirements, and then do the migrations
    > python manage.py makemigrations
* and now time to migrate the changes
    > python manage.py migrate
* then run the server
    > python manage.py runserver


####There are some other features also that you can use:

* If you want to show the tool-tip error messages in web-admin panel, use the **showError("error message")** 
  function in js.

* If you want to show the tool-tip success messages in web-admin panel, use the **showSuccess("success message")** 
  function in js.

* There is a preLoaded **confirmation-modal** in the templates > common > confirmation-modal.html.<br>
  just include that file in your html file and use it as follows:

  > $("#confirmation-modal-title").html("Logout");<br>
  > $("#confirmation-modal-description").html("Are you sure want to logout?");<br>
  > $("#confirmation-modal-yes-button").attr("onClick", "logout()");<br>
  > $("#confirmation-modal-yes-button").html("Yes");<br>
  > $("#confirmation-modal-no-button").html("Cancel");<br>
  > $("#deactivate-customer").modal('show');<br>
                
* To show the loader, use **showLoader();**<br>
  To hide the loader, use **hideLoader();**
  
* To hide the **success/error** tooltips, use preLoaded function **timeOut()**; <br>
  The default timeout is 4500 you can change it in apps > web_admin > static > js > common.js > timeOut()
