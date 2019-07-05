$input_path = 'ping.txt'
$output_file = 'ip.txt'
$regex = '\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b'
select-string -Path $input_path -Pattern $regex -AllMatches | % { $_.Matches } | % { $_.Value } > $output_file