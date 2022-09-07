var form_fields = document.querySelector(".user-info-form").getElementsByTagName("input");
form_fields[1].placeholder = "Address";
form_fields[2].placeholder = "Country";
form_fields[3].placeholder = "Province";
form_fields[4].placeholder = "City";
form_fields[5].placeholder = "Postal Code";

for (var fields in form_fields) {
	form_fields[fields].className += "form-control";
};
