<html><head>
<!-- <meta encoding="utf-8"> -->
<?php
/*
Извикване на микрофонемния синтезатор на реч Тошко 2.070 през браузър и уеб сървър.

Author: Todor "Tosh/Twenkid" Arnaudov

В тази версия настройките за изговора се задават само от работещото копие на приложението.

Участват три системи и платформи: PHP, Python и Win32 (С++)).

PHP say1.php --> Python2 t81.py --> C++/Win32 Toshko2 --> say1.php --> say2.php --> say1.php

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
</head>
<body>
<?php
    echo "<div style=\"width:800px; padding: 20px;\">";
    echo '<form action="say1.php" method="post" id="speak">';
	echo '<table with=480 border=1>';
	echo '<tr><td colspan=2><font size=4 face="Arial"><span style="background-color:#f1f1f1"><b>&nbsp; <b>Тошко 2</b></b></span></br></td></tr>';
	?>
	<tr><td>
    <textarea name="say" form="speak" rows=10 cols=60>Сладкопойна..... И2ска3м да изка2жа не2що ху2ба3во3...</textarea>
	</td></tr>       
    <?php	
	echo "</td></tr>";
	echo '<tr><td>&nbsp <input type="submit" name="send" value="ИЗГОВОР ....    " action="post5.php"></td><td></td></tr>';
	echo '</form></table>'; 
    echo "</div>";	
?>
<div style="width: 480px; border: 3px solid gray; font-family: Arial; padding: left;  padding: 10px; margin: 20px; background-color: #f0f0f0"><li> Влючен ли е Тошко 2.070+? <li> Включен ли е Python-сървъра toshko.py?
<!--<li>Тествай и с клиентския скрипт t80_4.py
<li>R:\python27\python s:\code\python\t80_4.py
<li>R:\python27\python s:\code\python\wmcopydata.py
-->
</div>
<?php
?>
</body>	
</html>