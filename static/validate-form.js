var FormValidation = function () {
    var handleValidation = function (rules, messages) {
        rules = rules || {}
        messages = messages || {}
        var form = $(".admin-form.form-horizontal")
        var error = $('.alert-danger', form)
        var success = $('.alert-success', form);

        form.validate({
            errorElement: 'span',
            errorClass: 'help-block help-block-error',
            focusInvalid: false,
            ignore: "",
            rules: rules,
            messages: messages,
            errorPlacement: function(error, element) {
                error.appendTo(element.parent())
            },
            invalidHandler: function (event, validator) {
                success.hide();
                error.show();
            },
            highlight: function (element) {
                $(element).closest('.control-group').addClass('has-error')
            },
            unhighlight: function (element) {
                $(element).closest('.control-group').removeClass('has-error') 
            },
            success: function (label) {
                label.closest('.control-group').removeClass('has-error')
            },
            submitHandler: function (form) {
                $("input.btn-primary").attr('disabled', 'disabled')
                form.submit()
            }
        })
    }
    return {
        init: function (rules, messages) {
            handleValidation(rules, messages)
        }
    }
}()

export default FormValidation
