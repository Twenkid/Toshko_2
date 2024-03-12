# Toshko_2
Тошко 2 - Bulgarian Text-to-Speech Synthesizer - Синтезатор на българска реч и малко английски

Виж папка: Versions

**Новини:** 

* 13.3.2024: Напоследък внедрявам система за разпознаване на реч и си мисля да има "Тошко 3", който да бъде с нея, а може и да задвижа старите идеи още от 2004 г. за обучаващо се разпознаване и синтез "по моя начин", или просто да внедря невронен както се прави сега с клонира на гласове, "Voice Cloning" - използвах една такава система в два от дийпфейк филмите на Twenkid Studio.
* 13.3.2024: Може би ще публикувам магистърската ми дипломна работа "Глас 2", която съдържаше планове за развитие на Глас 2004 още от създаването на първия синтезатор - част от тях осъществени в "Тошко 2", но не и най-интересните, обучаващи се, които вече са разрешени чрез невронни мрежи.


* 18.2.2024: Toshko 2.076: Parameter Int 69; no save after each segmentation to a temporary debug file; more words with accents: extract the acc_ files to data2076.7z to /data folder.
2.076 - no writing to _release-debug-segment.txt & more accents in the dictionary

* 12.2023: Оправен изпълнимия файл на 2.075, беше качена някаква неработеща версия. Компилиран е с VS 2019 x86, така че може да е нужно да се изтеглят съответните "Redistributable" files. https://learn.microsoft.com/en-us/cpp/windows/latest-supported-vc-redist?view=msvc-170

https://learn.microsoft.com/en-us/cpp/windows/latest-supported-vc-redist?view=msvc-170#visual-studio-2015-2017-2019-and-2022

X86	https://aka.ms/vs/17/release/vc_redist.x86.exe	Permalink for latest supported x86 version

## Глас 2004: Първата версия на Тошко 2.

Глас 07.05.2004	Синтезатор на българска реч. Прочети повече и следи за най-новите кръпки от същото място.	170 КБ	| 12.5.2004
https://www.oocities.org/todprog/bgr/glas-07052004.zip

![image](https://github.com/Twenkid/Toshko_2/assets/23367640/96bf7622-0186-40d9-a70e-61b9136dba9f)

https://www.oocities.org/todprog/

https://www.oocities.org/todprog/bgr/glas.htm

https://www.oocities.org/todprog/pisar/pisar.htm

### Тошко 2: "официален сайт"

http://twenkid.com/software/toshko2/

https://artificial-mind.blogspot.com/search?q=%D0%A2%D0%BE%D1%88%D0%BA%D0%BE

![image](https://user-images.githubusercontent.com/23367640/153290810-ef9e4e83-067e-48ec-b782-8e947632b7a0.png)

"Тошко 2.055" демо:

https://www.youtube.com/watch?v=cn2Sl9OqvWY

## 2.075 

5.4.2021

Работи и без връзка с Интернет. (Досега при зареждане изискваше свързване със сървър, така беше в началото - с  логване; - после логването беше само за статистика, но поради неоправен бъг забиваше при липса на връзка.)  

Download lame mp3 dll for encoding WAV to mp3: https://lame.sourceforge.io/download.php
Lame binaries 32-bit x86 Windows ... 
https://lame-binaries-for-windows.en.uptodown.com/windows/download
Поставете lame_enc.dll  при exe-то:

![image](https://github.com/Twenkid/Toshko_2/assets/23367640/916abf89-f697-48ea-acb1-1a671fa59004)



## 2.070 - Изговор през уеб сървър

И получаване на изговорения запис като mp3-файл, примерен код на Python и PHP.

Чрез съобщението WM_COPYDATA. Виж scripts.


## Статистика

Приложението е пуснато на около 227 различни конфигурации процесор/тактова честота и около 175 ако не се брои честотата. 
Intel: 143+24 = 167, AMD: 26, 2 - неизвестни
AMD: 14.9 %

...

See also: 
https://github.com/Twenkid/NLP-Computational-Linguistics/
https://github.com/Twenkid/Vsy

