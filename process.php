<?php
$birth = escapeshellarg($_POST['birth']);
$word = escapeshellarg($_POST['word']);

$command = escapeshellcmd("python3 process.py $birth $word");

$output = shell_exec($command);

echo "$output";
?>