$From = 'Trainer.Nigam@gmail.com'
$To = 'deepak.hada@infineon.com'
$attach = 'C:\Users\ushan\Desktop\infe\ping.txt'
$sub = 'test mail'
$body = 'powershell training'
$server = 'smtp.gmail.com'
$port = 587
Send-MailMessage -From $From -to $To -Subject $sub -Body $body -SmtpServer $server -port $port -UseSsl -Credential (Get-Credential) -Attachments $attach
#Send-MailMessage -