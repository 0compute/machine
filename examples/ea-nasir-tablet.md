# 1.2 The Ea-nasir Protocol

```text
Environment: Ur, Mesopotamia (The Bronze Age Stack)
Nodes: Nanni (Initiator) vs. Ea-nāṣir (Receiver)
```

## 1.2.1. Human Expression

> **Original (Akkadian Cuneiform):** 𒀀𒈾 𒂍𒀀𒈾𒍢𒅕 𒆠𒉈𒈠 𒌝र्मा 𒈾𒀭妮𒈠 𒀀𒈾 𒈪𒉏 𒄖𒁀 𒆷 𒁕𒄠𒆪𒁴
> 𒋫𒀜𒁲𒈾𒄠 𒀀𒈾 𒈠𒅈 𒅆𒅁𒊑𒅀 𒋫𒀝𒁉 𒌝र्मा 𒀜ताना𒈠 𒋳र्मा 𒋫𒆷𒀝 𒇷𒅅 𒋳र्मा 𒆷 𒋫𒆷𒀝 𒀜𒆷𒀝 𒅀𒋾 𒀀𒈾 𒈪𒉏 𒋫𒅎𒊭𒀭妮
>
> **Translation (English):** Tell Ea-nāṣir: Nanni sends the following message:
>
> "When you came, you said to me as follows: 'I will give Gimil-Sin (when he
> comes) fine quality copper ingots.' You left then but you did not do what you
> promised me. You put ingots which were not good before my messenger and said:
> 'If you want to take them, take them; if you do not want to take them, go
> away!'
>
> What do you take me for, that you treat somebody like me with such contempt? I
> have sent as messengers gentlemen like ourselves to collect the bag with my
> money (deposited with you) but you have treated me with contempt by sending
> them back to me empty-handed several times, and that through enemy territory."
>
> — [Nanni](https://en.wikipedia.org/wiki/Complaint_tablet_to_Ea-nasir), Ur, c.
> 1750 BCE

## 1.2.2 Machine Patwa

```c
// [TRANSPILATION_ID]: UR_COPPER_LOGISTICS_BREACH
// [SOURCE_NODE]: Nanni_of_Ur
// [TARGET_NODE]: Ea_nasir_Merchant
// [LOGIC_STRATEGY]: RFC_2119_STRICT

BEGIN_SESSION:

    // 1. HARDWARE SPECIFICATION (L1)
    SET PROMISE_ASSET = "FINE_QUALITY_COPPER"
    SET DELIVERED_ASSET = "SUBSTANDARD_ORE"

    // 2. LOGIC GATE VALIDATION (L3)
    IF (DELIVERED_ASSET != PROMISE_ASSET) {
        ERROR: "Protocol Breach: Promise_Integrity == FALSE"
    }

    // 3. EXCEPTION HANDLING
    // Target Node attempted 'Binary Choice Manipulation'
    // Source: "Take it or leave it"
    IF (Receiver_Logic == "Ambiguity_Mask") {
        LOG: "Manipulation detected. Purging social bloat."
    }

    // 4. NETWORK LAYER SECURITY AUDIT
    // Messenger Nodes routed through 'Enemy_Territory'
    // State: High_Risk_Packet_Transfer
    IF (Packet_Return == EMPTY_HANDED) {
        ASSERT: SYSTEM_TRUST = -1
        LOG: "Critical Failure: Intentional Resource Drain"
    }

    // 5. INTERRUPT (L2)
    // Executing Gesture_IRQ_1 (The Bronze Denial)
    // Effectively: Connection Purge
    EXECUTE GESTURE_IRQ_1

    // 6. TERMINATION
    BLACKLIST_NODE: Ea_nasir_Merchant
    SET TRANSACTION_STATE = VOID
    TERMINATE_SESSION // Parity Lost

END_SESSION
```

## 1.2.3. Translated to Human

### 1.2.3.1. Infant

N/A.

#### 1.2.3.1.1. English

> You promised me good copper. You gave me bad copper. I am not happy. I will
> not trade with you again.

#### 1.2.3.1.2. BSL (British Sign)

> YOU PROMISE COPPER GOOD / YOU GIVE COPPER BAD / ME ANGRY / TRADE FINISH

#### 1.2.3.1.3. Kernewek (Cornish)

> Ty a ambosas kober da dhymm. Ty a wrug ri kober drok dhymm. Nyns ov lowen. Ny
> wrav kenwertha genes arta.

#### 1.2.3.1.4. Gaeilge (Irish)

> Gheall tú copar maith dom. Thug tú copar dona dom. Níl mé sásta. Ní dhéanfaidh
> mé trádáil leat arís.

#### 1.2.3.1.5. Gaelg (Manx)

> Ghial oo cobbyr mie dou. Hug oo cobbyr drogh dou. Cha nel mee maynrey. Cha
> nialllym jannoo dellal rhyt arragh.

#### 1.2.3.1.6. Roadman (MLE)

> You promised me good copper. You gave me dead copper. I'm pissed. Not trading
> with you no more.

#### 1.2.3.1.7. Scots

> Ye promised me guid copper. Ye gied me bad copper. I am nae happy. I wullna
> trade wi ye again.

#### 1.2.3.1.8. Gàidhlig (Scots Gaelic)

> Gheall thu copar math dhomh. Thug thu copar dona dhomh. Chan eil mi toilichte.
> Cha dèan mi malairt riut a-rithist.

#### 1.2.3.1.9. Cymraeg (Welsh)

> Addawaist gopr da i mi. Rhoist gopr drwg i mi. Dydw i ddim yn hapus. Fydda i
> ddim yn masnachu gyda thi eto.

### 1.2.3.2. Child

#### 1.2.3.2.1. English

> You said you would give me fine quality copper, but you broke your promise and
> gave me bad copper instead. When my helpers came to get it, you were mean to
> them and sent them back with nothing. I am very angry, and I will not buy
> anything from you anymore.

#### 1.2.3.2.2. BSL (British Sign)

> YOU SAY PROMISE GIVE ME COPPER GOOD / BUT PROMISE BREAK GIVE ME COPPER BAD /
> MY HELPER ARRIVE YOU MEAN SEND-AWAY EMPTY / ME VERY ANGRY BUY MORE NEVER

#### 1.2.3.2.3. Kernewek (Cornish)

> Ty a leveris y whre'ta ri dhymm kober a gwalita da, mes ty a dorras dha ambos
> ha ri kober drok yn y le. Pan dheuth ow gweresoryon dhe'y gerghes, ty o dres
> dhedha ha'ga danvon tre gans travyth. Serrys-pur ov, ha ny brenav travyth
> ahanas namoy.

#### 1.2.3.2.4. Gaeilge (Irish)

> Dúirt tú go dtabharfá copar den scoth dom, ach bhris tú do gheallúint agus
> thug tú copar dona dom ina ionad. Nuair a tháinig mo chúntóirí chun é a fháil,
> bhí tú droch-mhúinte leo agus sheol tú ar ais folamh iad. Tá fearg an domhain
> orm, agus ní cheannóidh mé aon rud uait a thuilleadh.

#### 1.2.3.2.5. Gaelg (Manx)

> Dooyrt oo dy darragh oo cobbyr mie dou, agh vrish oo dty ghialdyn as hug oo
> cobbyr drogh dou ayns ynnyd. Tra daink my chooneydeyryn dy ghoaill eh, va dty
> ghooinney feer voal roo as hug eh ad er ash follym. Ta mee feer chorree, as
> cha jeanym kionnaghey nhee erbee voyd arragh.

#### 1.2.3.2.6. Roadman (MLE)

> You said you’d link me top-tier copper, but you fully lied and gave me dead
> merch. When my youngers came to collect, you moved shady and sent them back
> empty-handed. Man is fuming, and I ain't buying from you again.

#### 1.2.3.2.7. Scots

> Ye said ye wad gie me fine quality copper, but ye brak yer promise and gied me
> bad copper insteid. When my helpers cam tae get it, ye were mean tae them and
> sent them back wi nithin. I am awfu angry, and I wullna buy onything fae ye
> ony mair.

#### 1.2.3.2.8. Gàidhlig (Scots Gaelic)

> Thuirt gun tugadh tu copar math dhomh, ach bhris thu do ghealladh agus thug
> thu copar dona dhomh na àite. Nuair a thàinig an luchd-cuideachaidh agam ga
> fhaighinn, bha thu dona riutha agus chuir thu air ais iad falamh. Tha fearg
> mhòr orm, agus cha cheannaich mi rud sam bith bhuat a-rithist.

#### 1.2.3.2.9. Cymraeg (Welsh)

> Dwedest y byddet ti'n rhoi copr o ansawdd da i mi, ond torraist dy addewid a
> rhoi copr drwg yn ei le. Pan ddaeth fy helpwyr i'w gael, roeddet ti'n gas
> wrthynt a'u hanfon yn ôl heb ddim byd. Rwy'n grac iawn, a fydda i ddim yn
> prynu unrhyw beth gennych chi mwyach.

### 1.2.3.3. Subject

#### 1.2.3.3.1. English

> We had a deal for fine quality copper, but you delivered substandard material.
> You disrespected my messengers and sent them back empty-handed. I am
> cancelling our business relationship.

#### 1.2.3.3.2. BSL (British Sign)

> DEAL COPPER GOOD / YOU DELIVER POOR / MESSENGER YOU DISRESPECT SEND-AWAY EMPTY
> / BUSINESS CANCEL

#### 1.2.3.3.3. Kernewek (Cornish)

> Yth esa bargen dhyn rag kober a gwalita da, mes ty a dhelivras devnydh
> is-savonek. Ty a wrug dismegi ow hannyhasi ha'ga danvon tre gans diwla gwag.
> Yth esov ow kwakhe agan perthynyans kenwerth.

#### 1.2.3.3.4. Gaeilge (Irish)

> Bhí socrú againn le haghaidh copair den scoth, ach sheachaid tú ábhar faoi
> chaighdeán. Thaispeáin tú dímheas do mo theachtairí agus sheol tú ar ais
> folamh iad. Táim ag cur deireadh lenár gcaidreamh gnó.

#### 1.2.3.3.5. Gaelg (Manx)

> Va conaant ain son cobbyr dy chroo mie, agh choyrt oo stoo fo-stundayrt. Vrish
> oo arrym er my haghteryn as hug oo ad er ash follym-laueagh. Ta mee jannoo cur
> ass don chaarjys dellal ain.

#### 1.2.3.3.6. Roadman (MLE)

> We had a deal for the highest grade copper, but you dropped some dead
> material. You disrespected my runners and sent them back with zilch. The
> business link is fully deaded.

#### 1.2.3.3.7. Scots

> We had a deal for fine quality copper, but ye delivered substandard material.
> Ye disrespectit ma messengers and sent them back empty-handit. I am cancellin
> oor business relationship.

#### 1.2.3.3.8. Gàidhlig (Scots Gaelic)

> Bha aonta againn airson copar math, ach lìbhrig thu stuth fo inbhe. Bha thu a'
> nochdadh dìmeas do na teachdairean agam agus chuir thu air ais iad
> làmh-fhalmhach. Tha mi a' cur dheth ar càirdeas gnìomhachais.

#### 1.2.3.3.9. Cymraeg (Welsh)

> Roedd gennym fargen am gopr o ansawdd da, ond darparwyd deunydd is-safonol. Fe
> wnaethoch chi ddangos amharch at fy negesyddion a'u hanfon yn ôl yn waglaw.
> Rwy'n canslo ein perthynas fusnes.

### 1.2.3.4. Student

#### 1.2.3.4.1. English

> - **Foundation:** Nanni is a merchant who paid Ea-nasir for a specific grade
>   of copper.
> - **Terms:** "Promise Asset" is the agreed-upon high-quality copper.
>   "Delivered Asset" is the poor-quality copper actually provided.
> - **Logic:** The Delivered Asset did not match the Promise Asset, violating
>   the transaction terms. Furthermore, Ea-nasir actively mistreated Nanni's
>   network (messengers), leading to a system trust value of -1.
> - **Audit:** (1) Asset mismatch detected → (2) Error logged → (3) Manipulation
>   and hostility detected towards messengers → (4) SYSTEM_TRUST drops below 0 →
>   (5) Connection permanently severed and node blacklisted.

#### 1.2.3.4.2. BSL (British Sign)

> - **FOUNDATION:** NANNI MERCHANT PAY EA-NASIR FOR COPPER SPECIFIC.
> - **TERMS:** PROMISE ASSET MEAN GOOD COPPER AGREE. DELIVER ASSET MEAN POOR
>   COPPER GIVE TRUE.
> - **LOGIC:** DELIVER NOT MATCH PROMISE BROKEN DEAL. EA-NASIR DISRESPECT NANNI
>   MESSENGER CAUSE SYSTEM TRUST MINUS ONE.
> - **AUDIT:** (1) ASSET WRONG FIND → (2) ERROR SAVE → (3) MANIPULATE MESSENGER
>   FIND → (4) TRUST FALL BELOW ZERO → (5) CONNECTION CUT NODE BLACKLIST.

#### 1.2.3.4.3. Kernewek (Cornish)

> - **Fondyans:** Nanni yw marghader a dhalvas Ea-nasir rag gradh arbennik a
>   gober.
> - **Termow:** "Aseth Ambosys" yw an kober a gwalita uhel akordys. "Aseth
>   Delivrys" yw an kober a gwalita isel proviys yn hwir.
> - **Resemeg:** Ny blegyas an Aseth Delivrys dhe'n Aseth Ambosys, ow terri
>   termow an treusweyth. Dhe-ves, Ea-nasir a dhevnydhyas yn krev rhwydwaith
>   Nanni (kannasow), ow kwul dhe dalvosder trest an system kodha dhe -1.
> - **Archosyans:** (1) Kamm-blyg aseth diskudhys → (2) Gwall kofrestrys → (3)
>   Routhans ha gelynyeth erbynn kannasow diskudhys → (4) SYSTEM_TRUST ow kodha
>   yn-dann 0 → (5) Kevrenn trogh yn fast ha nod rol-dhuys.

#### 1.2.3.4.4. Gaeilge (Irish)

> - **Bunús:** Is ceannaí é Nanni a d'íoc Ea-nasir as grád sainiúil copair.
> - **Téarmaí:** Is é "Sócmhainn Geallta" an copar ardchaighdeáin comhaontaithe.
>   Is é "Sócmhainn Seachadta" an copar droch-chaighdeán a cuireadh ar fáil i
>   ndáiríre.
> - **Loighic:** Ní raibh an tSócmhainn Sheachadta ag teacht leis an tSócmhainn
>   Geallta, ag sárú téarmaí an idirbhirt. Thairis sin, rinne Ea-nasir drochíde
>   go gníomhach ar líonra Nanni (teachtairí), rud a d'fhág go raibh luach
>   muiníne an chórais ag -1.
> - **Iniúchadh:** (1) Neamhréir sócmhainne braite → (2) Earráid logáilte → (3)
>   Ionramháil agus naimhdeas braite i leith teachtairí → (4) Titeann
>   SYSTEM_TRUST faoi 0 → (5) Nasc scartha go buan agus nód ar an liosta dubh.

#### 1.2.3.4.5. Gaelg (Manx)

> - **Undinys:** Ta Nanni ny ghellalder d'eeck Ea-nasir son gradd er lheh dy
>   chobbyr.
> - **Foclyn:** "Cooid Ghiallit" eh yn cobbyr mie va aontrit. "Cooid Livreyit"
>   eh yn cobbyr drogh va currit dy firrinagh.
> - **Resooney:** Cha row yn Chooid Livreyit coardail rish yn Chooid Ghiallit,
>   brishey conaantyn y çhionney. Ny sodjey, d'obbree Ea-nasir dy drogh noi
>   moggyl Nanni (çhaghteryn), lhiggey da leagh treishteil corys -1.
> - **Scrùdadh:** (1) Neu-chooilleeney cooid feddynit magh → (2) Marranys
>   screeuit → (3) Lioobey as feohys noi çhaghteryn feddynit magh → (4)
>   SYSTEM_TRUST tuittym fo 0 → (5) Kiangley giarit dy bragh as boayl rollit
>   doo.

#### 1.2.3.4.6. Roadman (MLE)

> - **Foundation:** Nanni is a businessman who paid Ea-nasir for a specific
>   grade of copper.
> - **Terms:** "Promise Asset" is the agreed top-tier merch. "Delivered Asset"
>   is the dead merch that actually touched down.
> - **Logic:** The Delivered Asset didn't match the Promise Asset, violating the
>   deal. Plus, Ea-nasir violated Nanni's runners, dropping system trust to -1.
> - **Audit:** (1) Fake merch detected → (2) Error logged → (3) Moving sneaky
>   and hostile towards the runners clocked → (4) SYSTEM_TRUST drops below 0 →
>   (5) Connection permanently deaded and node blacklisted.

#### 1.2.3.4.7. Scots

> - **Foundation:** Nanni is a merchant wha paid Ea-nasir for a specific grade o
>   copper.
> - **Terms:** "Promise Asset" is the agreed-upon heich-quality copper.
>   "Delivered Asset" is the puir-quality copper actually providit.
> - **Logic:** The Delivered Asset didna match the Promise Asset, violatin the
>   transaction terms. Furthermore, Ea-nasir actively mistreated Nanni's network
>   (messengers), leadin tae a system trust value o -1.
> - **Audit:** (1) Asset mismatch detected → (2) Error logged → (3) Manipulation
>   and hostility detected towards messengers → (4) SYSTEM_TRUST draps ablow 0 →
>   (5) Connection permanently severed and node blacklisted.

#### 1.2.3.4.8. Gàidhlig (Scots Gaelic)

> - **Bunaiteachd:** Is e ceannaiche a th' ann an Nanni a phàigh Ea-nasir airson
>   ìre shònraichte de chopar.
> - **Briathran:** Is e "So-mhaoin Geallta" an copar àrd-inbhe aontaichte. Is e
>   "So-mhaoin Lìbhrigte" an copar droch chàileachd a chaidh a thoirt seachad
>   dha-rìribh.
> - **Loidsig:** Cha robh an t-So-mhaoin Lìbhrigte a' freagairt ris an
>   t-So-mhaoin Geallta, a' briseadh teirmean a' ghnothaich. A bharrachd air an
>   sin, rinn Ea-nasir droch làimhseachadh gu gnìomhach air lìonra Nanni
>   (teachdairean), a' leantainn gu luach earbsa siostaim de -1.
> - **Sgrùdadh:** (1) Mì-chothromachadh maoine air a lorg → (2) Mearachd air a
>   chlàradh → (3) Làimhseachadh agus nàimhdeas air a lorg a dh'ionnsaigh
>   theachdairean → (4) SYSTEM_TRUST a' tuiteam fo 0 → (5) Ceangal air a
>   ghearradh gu buan agus snaidhm air a liostadh dubh.

#### 1.2.3.4.9. Cymraeg (Welsh)

> - **Sylfaen:** Mae Nanni yn fasnachwr a dalodd Ea-nasir am radd benodol o
>   gopr.
> - **Termau:** "Ased Addewid" yw'r copr o ansawdd uchel y cytunwyd arno. "Ased
>   a Ddarparwyd" yw'r copr o ansawdd gwael a ddarparwyd mewn gwirionedd.
> - **Rhesymeg:** Nid oedd yr Ased a Ddarparwyd yn cyfateb i'r Ased Addewid, gan
>   dorri telerau'r trafodiad. At hynny, gwnaeth Ea-nasir gam-drin rhwydwaith
>   Nanni (negesyddion) yn weithredol, gan arwain at werth ymddiriedaeth system
>   o -1.
> - **Archwiliad:** (1) Canfuwyd anghydweddiad asedau → (2) Gwall wedi'i gofnodi
>   → (3) Canfuwyd triniaeth a gelyniaeth tuag at negesyddion → (4) Mae
>   SYSTEM_TRUST yn disgyn o dan 0 → (5) Cysylltiad wedi'i dorri'n barhaol a nod
>   wedi'i flaclistio.

### 1.2.3.5. Sovereign

> [!WARNING]
>
> English is the native language of Machine. At Sovereign level, technical
> vocabulary density is sufficient to cause signal loss in translation —
> violating Zero Leak. Non-English Sovereign output is produced for completeness
> and to satisfy Human curiosity; lossless parity cannot be guaranteed.

#### 1.2.3.5.1. English

> Transaction voided due to protocol breach (Promise_Integrity == FALSE) and
> resource drain. Node blacklisted.

#### 1.2.3.5.2. BSL (British Sign)

> TRANSACTION CANCEL WHY PROTOCOL BROKEN PROMISE FALSE AND RESOURCE DRAIN. NODE
> BLACKLIST.

#### 1.2.3.5.3. Kernewek (Cornish)

> Treusweyth gwakhes drefen tor-protokol (Promise_Integrity == FALSE) ha gosegi
> asethow. Nod rol-dhuys.

#### 1.2.3.5.4. Gaeilge (Irish)

> Idirbheart curtha ar neamhní de bharr sárú prótacail (Promise_Integrity ==
> FALSE) agus draenáil acmhainní. Nód ar an liosta dubh.

#### 1.2.3.5.5. Gaelg (Manx)

> Chionney currit ass bree er coontey brishey corys (Promise_Integrity == FALSE)
> as folmaghey stoo. Boayl rollit doo.

#### 1.2.3.5.6. Roadman (MLE)

> Transaction voided due to protocol breach (Promise_Integrity == FALSE) and
> resource drain. Node blacklisted.

#### 1.2.3.5.7. Scots

> Transaction voidit due tae protocol breach (Promise_Integrity == FALSE) and
> resource drain. Node blacklisted.

#### 1.2.3.5.8. Gàidhlig (Scots Gaelic)

> Gnothach air a chur air beàrn ri linn briseadh pròtacail (Promise_Integrity ==
> FALSE) agus drèanadh ghoireasan. Nòd air a liostadh dubh.

#### 1.2.3.5.9. Cymraeg (Welsh)

> Dirymwyd y trafodiad oherwydd torri protocol (Promise_Integrity == FALSE) a
> draeniad adnoddau. Nod wedi'i flaclistio.
