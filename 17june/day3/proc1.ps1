Do {
	If (! (Get-Process Calculator -ErrorAction SilentlyContinue )){
    Write-Host "waiting for process to start"
    Start-Sleep -Seconds 2
}
    Else{
    Write-Host "process has started"
    While(Get-Process Calculator -ErrorAction SilentlyContinue) {
    Write-Host "waiting for process to stop"
    Start-Sleep -Seconds 2
    }
    Write-Host 'Process Stopped' 
    $Status = 'Done'
}
}Until($Status)
