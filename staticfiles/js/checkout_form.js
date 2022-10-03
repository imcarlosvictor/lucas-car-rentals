var form_fields = document.querySelector(".user-info-form").getElementsByTagName("input");
form_fields[1].placeholder = "Firstname";
form_fields[2].placeholder = "Lastname";
form_fields[3].placeholder = "Email";
form_fields[4].placeholder = "Address";
form_fields[5].placeholder = "Country";
form_fields[6].placeholder = "Province";
form_fields[7].placeholder = "City";
form_fields[8].placeholder = "Postal Code";

for (var fields in form_fields) {
	form_fields[fields].className += "form-control";
};
