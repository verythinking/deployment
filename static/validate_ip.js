import FormValidation from "./validate-form.js";

function validateIP(ip) {
    var re = /^(\d{1,2}|1\d\d|2[0-4]\d|25[0-5])\.(\d{1,2}|1\d\d|2[0-4]\d|25[0-5])\.(\d{1,2}|1\d\d|2[0-4]\d|25[0-5])\.(\d{1,2}|1\d\d|2[0-4]\d|25[0-5])$/;
    return re.test(ip);
}

$.validator.addMethod("validateIP", function (value) {
    console.log(value)
    if (value) {
        return validateIP(value);
    }
    return true;
})

$.extend($.validator.messages, {
    required: "字段不能为空",
    validateIP: "IP地址格式不正确"
})

$(function () {
    FormValidation.init(
        {
            name : {required: true},
            ip : {
                required: true,
                validateIP: true,
            }
        }
    )
})
