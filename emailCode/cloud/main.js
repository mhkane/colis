
// Use Parse.Cloud.define to define as many cloud functions as you want.
// For example:
Parse.Cloud.define("hello", function(request, response) {
  response.success("Hello world!");
});

Parse.Cloud.define("email", function(request, response) {
var Mandrill = require('mandrill');
Mandrill.initialize('t6vxQc9QlFi6FzsjMjQiAQ');
Mandrill.sendEmail({
    message: {
        text: request.params.text,
        subject: request.params.subject,
        from_email: request.params.from_email,
        from_name: request.params.from_name,
        to: [
            {
                email: request.params.email,
                name: request.params.to_name,
            }
        ]
    },
    async: true
},{
    success: function(httpResponse) {
        response.success("email sent");
    },
    error: function(httpResponse) {

    }
}
);
});
