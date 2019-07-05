$users = @()

$sechtasks = Get-ScheduledTask 
foreach ($Task in $sechtasks) {
    $tempUser = $Task.Principal.UserId
        $users = $users + $tempUser
 }
 $users.Count
 $users | Get-Unique