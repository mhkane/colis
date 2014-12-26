<?php
    $name = $_POST['name'];
    $email = $_POST['email'];
    $message = $_POST['message'];
    $from = 'From: customer@airspress.com';
    $replyto = 'Reply-To: $email';
    $to = 'team@airspress.com'; 
    $subject = 'Contact via AirSpress.com';

    $body = "From: $name\n E-Mail: $email\n Message:\n $message";
?>

<?php
if ($_POST['submit']) {
    if (mail ($to, $subject, $body, $from, $replyto)) { 
        echo '<p>Thank you for your email!</p>';
    } else { 
        echo '<p>Oops! An error occurred. Try sending your message again.</p>'; 
    }
}
?>