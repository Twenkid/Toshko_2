<html><body>
<?php 
/* 
Извикване на микрофонемния синтезатор на реч Тошко 2.070 през браузър и уеб сървър.

Author: Todor "Tosh/Twenkid" Arnaudov

В тази версия настройките за изговора се задават само от работещото копие на приложението.

Участват три системи и платформи: PHP, Python и Win32 (С++)).

PHP say1.php --> Python2.7 toshko.py --> C++/Win32 Toshko2 --> mp3-запис в двоична форма -->
 --> toshko.py го чете и връща обратно на --> say2.php --> изсвирва

1. Скриптът на PHP праща POST заявка към уеб сървър на Python, слушащ на порт 8079.
2. Сървърът праща съобщение WM_COPYDATA към приложението на Win32.
3. Настолното приложение записва WAV-файл, който прекодира в MP3.
4. Уеб сървърът връща mp3-файла като отговор на POST-заявката, кодиран като низ в BASE64.
5. Скриптът декодира низа до двоичен вид и го записва във файл.
6. Файлът се просвирва през уеб плеър.

http://twenkid.com/software/toshko2/
http://artificial-mind.blogspot.bg

*/
?>

<!-- Send to POST server... -->
<?php
//main --> post2 --> httpPost ... localhost:8079
function httpPost($url, $data)
{
    $curl = curl_init($url);	
    curl_setopt($curl, CURLOPT_POST, true);	    
	curl_setopt($curl, CURLOPT_POSTFIELDS,
	http_build_query($data));	
    curl_setopt($curl, CURLOPT_RETURNTRANSFER, true);
    $response = curl_exec($curl);
    curl_close($curl);
    return $response;
}

function post2($text)   #12-4-2016
{
 $data = array( '@say'=>$text,
				'@vowels'=>'2.0',
				'@consonants'=>'0.5',
				'@speed'=>'1.0');
				
 $re = httpPost("localhost:8079", $data);
 $decoded = base64_decode($re);

 $rn = rand(0,9999999);
 $f = fopen("spoken".$rn.".mp3", "wb");
 $fname = "spoken".$rn.".mp3";

 fwrite($f, $decoded);
 fclose($f);

 $player = "<audio controls autoplay>  <source src=\"$fname\" type=\"audio/mpeg\"/><embed height=\"50\" width=\"100\" src=\"".$fname."\"/></audio>";

 print($player);
}

function main()
{
    $say = $_POST['say'];
    $path = "http://twenkid.com/software/toshko2";
	echo "<div style=\"width:800px; padding: 20px; border: 3px solid\">";
    echo "<span style=\"font-family: Arial; font-size: 150%; background-color: #f0f0f0\"><b>"."<a href=".$path.">"."Тошко 2.070 - синтезатор на реч</b></span><br><br>";
    echo "<span style=\"font-family: Arial; font-size: 24px;\">";
	print("<br><br><b><a href=\"say0.php\">Кажи друго...</a></b></span><hr>"); 
    
    #header("Location: http://localhost/web/play.php");
   
    echo "<span style=\"font-family: Arial; font-size: 12px\">";
    echo "<br><br><b>".$say."</b>";
    echo "</span>";
    echo "<p></p><br><br>";
    
    post2($say);
    
	echo "</div>";	
}
    main();
?>
</body></html>