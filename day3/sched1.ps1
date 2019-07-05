$users = @()

$sechtasks = Get-ScheduledTask 
foreach ($Task in $sechtasks) {
    $tempUser = $Task.Principal.UserId
    switch ( $Task.Principal.UserId) {
        "NETWORK SERVICE" { $continue = "skip this user"}
        "LOCAL SERVICE" {$continue =  "skip this user"}
        "SYSTEM" { $continue = "skip this user"}
        "$null" {$continue =  "skip this user"}
    default {$continue = "Report User"}
    }
    if ($continue -eq "Report User"){
        $users = $users + $tempUser
        }
 }
 $users.Count
 $users | Get-Unique