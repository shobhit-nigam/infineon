$From = 'Trainer.Nigam@gmail.com'
$To = 'deepak.hada@infineon.com'
$attach = 'C:\Users\ushan\Desktop\infe\ping.txt'
$sub = 'test mail twice'
$body = 'powershell training going on'
$server = 'smtp.gmail.com'
$port = 587
$secpsswd = ConvertTo-SecureString 'nigam.trainer' -AsPlainText -Force
$username = 'Trainer.Nigam@gmail.com'

$credobj = new-Object System.Management.Automation.PSCredential ($username, $secpsswd)

Send-MailMessage -From $From -to $To -Subject $sub -Body $body -SmtpServer $server -port $port -UseSsl -Credential $credobj -Attachments $attach 
#Send-MailMessage -