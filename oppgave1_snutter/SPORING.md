Runde	i	total	...	Utskrift
1	I kjører range(1,6) som da skriver ut tallene [1,2,3,4,5]	Total har en start verdi på 0. 
Inne i løkka skriver vi «total = total + i»  Dette tar hvert tall ifra 1 til 5 og plusser den med runden så første runde er 0 + 1 = 1 også bygger det seg opp. 	I if setningen såe det her at hvis ruden er mer en 6 skal veriden endres: 
”total = total - 2”

i totalt = total + i blir resultatet slik 
1	0 + 1 = 	 1
2	1 + 2  =	3
3	3 + 3 = 	6
4	6 + 4 = 	10
5	10 + 5 = 	15

Også kommer if skjekken som sier når runden er kommet til 6 så skal total = total – 2 og da tar vi «15 – 2 = 13» 	11

Her fikk feil.


2	Første variabel er: tekst = «banan»
Andre variabel er: resultat = «» tom streng
Neste er i = len(tekst) – 1
Ok dette tar tekst i en len funksjon som da kalkulerer alle bukstaver i en streng. I vårt tilelle er strengen «banan» og  da kalkulerer den bokstavene og gir et resultat 5. Men vi må ikke glemme «-1» som da fjerner en verdi og veriden blir til 4. 

	Neste som skjer er «while i >= 0:»
Den skjekker om i er større eller lik 0 og hvis den er lik er en bolien verdi på false om den er ulik blir det til true. 

Så er det er «if tekst[i] ! = a»
Er får vi false for a != a bliver false fordi veriden er lik
	
Så er det resultat = resultat = tekst[i]
Så resultat blir da: ”bnan”
Også tilslutt tar i = i - 2
Jeg trur resultat er «bnn »
	nnb

feil igjene
				
				

 


Runde 	Variabeler	Besrkivelse	Print	Utskrift
3	a = [1, 2, 3]
	en array med tall verdier
	Print(a)
[1,2,3,4]	[1, 2, 3, 4]
[1, 2, 3, 4]
[1, 2, 3, 4, 5]
	b = a 
	gir variabelen b veriden i a 
	Print(b)
[1,2,3,4]	
	b.append(4)
	dette legger på enda et tall i array-en, da vil den se slik ut: [1,2,3,4]
		
	 c = a[:]
	Dette lager en kopi 
		
	c.append(5)
	Legger til en ny verdi i listen: [1,2,3,4,5]
	Print(c)
[1,2,3,4, 5]	

