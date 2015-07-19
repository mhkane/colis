// Require and initialize the Twilio module with your credentials
var client = require('twilio')('ACaf4280d3ec4f919c4e6615071a051620', '95b47b527b742f7cb9ef16ea051e57b9' );


Parse.Cloud.define("sms", function(request, response) {
// Require and initialize the Twilio module with your credentials
var client = require('twilio')('ACCOUNT_SID', 'AUTH_TOKEN');

// Send an SMS message
client.sendSms({
    to: request.params.to_number, 
    from: '+15615940299', 
    body: request.params.sms_body 
  }, function(err, responseData) { 
    if (err) {
      console.log(err);
    } else { 
      console.log(responseData.from); 
      console.log(responseData.body);
    }
  }
);
});
