

try {
    10/2
    }
catch 
    {
        Write-Host "exception handled"
        Write-Host $_.Exception.message 

    }
finally 
    {
        Write-Host "fanally this will run"

    }





