

try {
    $null.ToString()
    }
catch 
    {
        Write-Host "exception handled"
        Write-Host $_.Exception.message 

    }




