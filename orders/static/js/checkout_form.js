var form_fields = document.querySelector(".user-info-form").getElementsByTagName("input");
form_fields[1].placeholder = "First Name";
form_fields[2].placeholder = "Last Name";
form_fields[3].placeholder = "Email";
form_fields[4].placeholder = "Address";
form_fields[5].placeholder = "Postal Code";
form_fields[6].placeholder = "City";

for (var fields in form_fields) {
	form_fields[fields].className += "form-control";
};
