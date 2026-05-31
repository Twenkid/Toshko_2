# Glas 2004 an Toshko 2
## Speech Synthesizer by Todor Arnaudov - Tosh/Twenkid

osnova_glas.cfg

```
0 1
1 data/paket.dll
0
0 data/paket.dll
15
-1
-0.03
0 0.5	
25000 3000000
data/vhod.dll
data/fonemi0.txt
1 data/leleta.dll
1 data/kusidulgi.dll
1 data/slivane.dll
1 data/bezzvuk.dll
1 data/nizove.dll
0 0.7
0
2
ръчно ruchno.txt ruch.dll 0 1
слово text.txt _z.dll 1 1
...
```

```
0 1   
1 data/paket.dll   // read microphonemes waves from data/paket.dll
0                  // 
0 data/paket.dll   // do not save to a new packet file
...

   fscanf(fc, "%d%f", &Da_Napravi_Tembre, &Tembre_Koeficient);
    printf("\nTembre=%f\n", Tembre_Koeficient);

    fscanf(fc, "%d%s", &Da_Prochete_Paket, Paket_Prochete_Niz);
    fscanf(fc, "%d", &Da_Zaredi_Paket);
    printf("\nDa_Zaredi = %d",Da_Zaredi_Paket);
    fscanf(fc, "%d%s", &Da_Zapishe_Paket, Paket_Zapis_Niz);

    fscanf(fc, "%d", &Buf_Min_Len);
    fscanf(fc, "%d", &Neizmenni_Periodi);
    fscanf(fc, "%f", &Neizmenen_Koeficient_Na_Prehod);
    fscanf(fc, "%d%f", &Da_Promeni_Prehod, &Po_Koeficient_Na_Prehod);
    fscanf(fc, "%d%d", &Trans_Space, &Record_Space);
    fscanf(fc, "%s%s", Zapisi_Niz, Fonemi_Niz);
    fscanf(fc, "%d%s", &Da_Napravi_Lele, Lele_Niz);
    fscanf(fc, "%d%s", &Da_Napravi_Kusi_Dulgi, Kusi_Dulgi_Niz);
    fscanf(fc, "%d%s", &Da_Napravi_Slivane, Slivane_Niz);
    fscanf(fc, "%d%s", &Da_Napravi_Bezzvuk, Bezzvuk_Niz);
    fscanf(fc, "%d%s", &Da_Napravi_Nizove, Nizove_Niz);
    fscanf(fc, "%d%f", &Da_Promeni_Skorost, &Zabavyane);
    fscanf(fc, "%d", &Da_Ne_Prehod);

