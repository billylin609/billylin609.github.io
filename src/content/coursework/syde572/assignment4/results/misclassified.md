# Misclassified test reviews

464 of 2383 test reviews are wrong, grouped by true class. Within each class, sorted by margin = log P(doc, predicted) - log P(doc, true), largest (most confidently wrong) first.

| true class | predicted | wrong | of | error rate |
|---|---|---|---|---|
| pos | neg | 266 | 1200 | 22.2% |
| neg | pos | 198 | 1183 | 16.7% |

Errors per topic category:

| category | true pos | true neg |
|---|---|---|
| books | 38 | 46 |
| camera | 30 | 36 |
| dvd | 43 | 38 |
| health | 47 | 21 |
| music | 36 | 50 |
| software | 72 | 7 |

# True pos, predicted neg (266 reviews)

## pos 1. music 384.txt

margin 42.95, 1209 words

> i 've always written how the american now compilations do not even come close to the british ones , and my opinion has not since changed . now 20 's track list , however , is solid and pretty good for the american series . it has mostly good rap songs ( which can be sometimes rare in this series ) , great rock songs , and not an overload of mediocrities . i 'll go in depth . 1. missy elliott feat . ciara & fatman scoop - lose control...a a great rap song - missy elliott has a great style and her lyrics are actually understandable and enjoyable . ciara is a nice addition to the song . fatman scoop 's random screaming in the background was n't essential , but it at least adds some energy to the track . the music 's actually interesting and something different from everything else . 2. black eyed peas - do n't phunk with my heart...c+ their first album was stellar , and their second is as well . but this was one of the worst tracks on " monkey business " and did not deserve to become a single . annoying , but not horrible . 3. pussycat dolls feat . busta rhymes - do n't cha...a - a really good rap song - busta 's rapping is a good addition to the song , making this radio remix better than the original on the pussycat dolls ' album , " pcd " . a dangerously catchy chorus elevates this song to a pretty high grade . 4. rihanna - pon de replay...b+ pretty catchy , and a good party song . but it gets pretty irritating after a while . and the " dip it low and you pick it up slow " from the first verse directly copies from christina milian 's " dip it low " . that 's so unoriginal , rihanna ! 5. ludacris feat . bobby valentino - pimpin ' all over the world...b good music , but it 's not much without the video , which was , by the way , partly shot in africa . 6. bow wow feat . ciara - like you...b bow wow 's returning to the rap scene was really unneeded , but ciara 's chorus makes this song better than mediocre . 7. dem franchize boys feat . jermaine dupri , da brat & bow wow - i think they like me ( remix ) ...c this song does not deserve the publicity , and i 'm stunned why people like this . it 's worse than mediocre , it 's horribly irritating . and much of the song is bleeped out because the original is so dirty . rap just is n't rap when it 's edited , and this song is proof . but even without the editing i do n't think this song has a chance . annoying " yep " s in the background and mediocre rapping...just skip it already . 8. destiny 's child - cater 2u...b - mediocre for destiny 's child . actually pretty boring . but they have great voices . 9. lyfe jennings - must be nice...c+ mediocre . 10. natasha bedingfield - these words...a a great " new " artist who actually found success with this song a year earlier the us . great songwriting about bad songwriting ( if that makes any sense at all ) and a good voice . now i 'm just wondering when her brother daniel 's going to release another " if you 're not the one " . 11. kelly clarkson - behind these hazel eyes...a - the only american idol who earned over twenty minutes of success , kelly 's finding massive success with her second album , and for a reason - she 's got an awesome voice , and pulls off rock quite well . this song was brutally murdered by the radio , but that 's why i 've moved onto the remixes ( not on this album ) . 12. d.h.t. - listen to your heart ( unplugged version ) ...a though furios f.ez 's hard trance remix of this song is a lot better than this unplugged piano version , this amazing cover of the roxette track deserved all the fame it got . edmee 's got a fantastic voice and this is a perfect song for her . beautiful song also . 13. backstreet boys - just want you to know...a - the backstreet boys ' newest album must have been the #1 most unwanted comeback of all time ( let 's just hope n*sync does n't follow...*cringe* justin timberlake ) , but this is their best song . and this comes from someone hard to impress by the backstreet boys , but they pull off this rock song pretty well . 14. click 5 - just the girl...a a really good rock song which many can relate to . 15. franz ferdinand - do you want to...b atonal , but franz ferdinand has a good reputation , so i 'll let it slide . but this is definitely evidence of a sophomore slump . 16. weezer - beverly hills...a+ unfortunately it was flattened , torn apart , and buried alive by the radios , so i will review it as it was still last summer when i first heard it . this song is amazing and the chorus is way too catchy to believe . but i do n't need to write this , as most people already know . 17. fall out boy - sugar we 're going down...a an amazing song , but it 's only good if you can put up with songs where you ca n't understand what they 're saying . seriously , it took approximately six times looking up the lyrics to actually realize what 's being said here . but the music is great , and this song overall is a pretty good rock track . 18. lifehouse - you & me...a - an instant classic . 19. coldplay - fix you...a+ i 've read mixed reviews about this song , but personally , i think its amazing . following a vaguely similar buildup as led zeppelin 's " stairway to heaven " , this song just keeps you listening until the end . the rockout part at the end is magical . 20. keith urban - you 'll think of me...b it 's somewhat annoying that keith 's been on now albums consistently for a while but his songs are n't as popular as , say , gretchen wilson . i 'm starting to think keith 's been put on these albums not for popular songs but just so a default country artist could be there . a good song , but it could 've been replaced with something better in the country department . so overall , this is a great selection of songs , some amazing , some decent , and some mediocre to bad . i 'd suggest you buy this , as it 's a good list of tracks . overall , this album gets a b+.

## pos 2. dvd 10.txt

margin 31.62, 193 words

> i tried to rent this dvd from an online service about a week ago . unfortunately , the dvd was damaged and unplayable , but not in the usual way i 've seen before ( like a disc cracked all the way through ) . it looked like someone had turned the playable side face-up and tapped a small nail with a hammer on it . the cracks had that kind of splintery pattern like a broken window . anyway , i returned the copy and ordered another , which i received today . again , this one is also unplayable and is cracked in an odd way . i just reported this problem online to the dvd rental company and ordered a replacement copy . however , i let them know that they may want to check their inventory of this dvd as someone may be intentionally destroying the dvds . if i get another one that is cracked or unplayable in any way , i 'm going to just buy a copy because the movie must really have gotten under someone 's skin for them to do something like that .

## pos 3. software 334.txt

margin 27.01, 351 words

> after going insane with the new version of norton systemworks 2005 , which does n't even install , i decided to finally swear off all symantec products . i have used zone alarm pro for some time . it 's not perfect , but it certainly will protect your computer . i took the plunge and went with the full security suite this week , and i 've been relatively happy . on the plus side , the software works really well . the personal firewall is better than any you can find , and the virus protection found a phishing app that norton had not ( before i had unstalled it ) . on the minus side , the firewall can be problematic . i 've had page load issues on ebay and on my own site which has a cgi script to keep my images and files from being hotlinked ( bandwidth theft ) . when i visit my site or any other that has a similar anti-theft cgi script , the images simply wo n't come up . ebay gets all messed up as well . i have n't been able to figure out a setting that works , so i have to turn off the firewall on ebay and a few other sites , which kind of defeats the purpose of a firewall . this does n't happen a lot though , so it 's not annoying enough to get my dander up . all in all it 's been a far better investment than symantec products , so despite its limitations i would recommend this program . it does have a lot of options to set , but they are pretty easy to get through if you are computer literate . if you decide to go with this program and you currently have norton antivirus , you will need to uninstall norton before this program will run . if you were to ask me if i preferred symantec systemworks or zone alarm security suite , there would be absolutely no hesitation in recommending zone alarm .

## pos 4. software 934.txt

margin 21.12, 156 words

> it was a relief for me to be able to keep and upgrade word and excel , and to get virtual pc ( for access ) as well . i used them a lot on my pc a few years ago , and when i first switched to mac , could n't find software that did what they did . i had no trouble installing the upgrade on my imac g5 , nor did i have trouble installing virtual pc . the only thing that was disappointing was that i could n't find out whether accessing the internet from virtual pc would open me up to pc-type viruses , or if mac 's unix system would protect me there , too . i continue to be disappointed that the mac version of this software is not as rich as the pc version . but the upgrade itself worked well for what it was meant to do

## pos 5. software 805.txt

margin 21.08, 290 words

> for years i used powerquest 's drive image 7 for backups . it 's rock solid and totally dependable . when symantec aquired powerquest they rolled the underlying technology of drive image 7 into norton ghost . the result is a very capable and reliable package that can backup partitions or entire drives and also provides support for incremental backups . most importantly , like drive image 7 , it provides for emergency recovery of your system . just boot from the ghost cd and restore the backup ( restore point ) that you select . i 've tested this process by making both full system backups and subsequent incremental backups , and then restoring the system from those backups . the process works flawlessly . if you need to restore to a different physical drive ( replaced a failed drive , etc ) , the process requires a few extra selections , but is still very straightforward . just take the time to read the manual . i 've seen acronis true image recommended by some both here and elsewhere . i 've tried acronis and find it lacking in one major respect : it simply is not reliable . during trials , i made backups with acronis . acronis indicated that the backups were successful but , when attempting to make a system recovery just minutes later , acronis indicated that the backups were corrupted and could not be used . the backups were worthless . when purchasing backup software remember that bells and whistles do n't count for anything . the only thing that counts is reliability . it must be able to reliably restore your system . norton ghost passes that test with flying colors .

## pos 6. software 776.txt

margin 19.63, 214 words

> i 'm currently learning how to use this product ; however , one of the first things i noticed was that the only way to do my payroll with it was to use a service . now of course , this service was n't free and with only 4 employees , the last thing i wanted to do was expend $20 a month on a service . was n't that the point of getting quickbooks - so i could do it myself ? now i can understand that tax codes , percentages , etc can vary from state to state , but would it have been so difficult for them to just set up a section with the generalized accounts and have the user input the amounts for each account needed on their payroll checks . see , i 'm not even asking them to have the computer calculate the amounts . simple would have been fine with me . as for the rest of the program , it looks as though it will be fairly easy to use after i figure out the best way to set it up for my particular business . i 'm disappointed that a business program designed for the small businessman would omit something as vital as payroll

## pos 7. software 706.txt

margin 19.43, 328 words

> first i would like to state that sooner or later every computer user will come in contact with some problem with an internet security program . they are human made and not 100% fault proof . i study and work in the it field and was first introduced to pc-cillin through trend micro 's product housecall . soon after i tried out the trial and have finally bought the product . i love it ! i have used several of the other " major " anti-virus suites available and have had tons of problems with them . mcafee after one uninstall had bedded itself so far into the computer that i had to completely reformat the pc to gain functionality again . norton to say was n't much better . if you are installing on a " clean " pc where these other software suites have not been , i have not had a problem . i have installed / uninstalled pc-cillin many times each time running smoothly . the software has been a valuable asset protecting my pcs by alerting me to virus threats and even hacking threats that were not even on my network but on my isps network . as well as protecting my network from one single computer that received a virus by shutting off traffic to that pc . i can understand where some of the other problems reported with this software may occur if the person a beginning user or just unfamiliar with the framework of the software . but if you already have some experience in how to set this type of software up i really do recommend you give pc-cillin a try . it is a sleak program , easy to install , easy to customize , and really goes above and beyond with alerting you to possible risks and threats . with all its competitors out there i would choose pc-cillin over the rest any day of the week

## pos 8. camera 130.txt

margin 19.32, 590 words

> this is one of the best bargains that i 've seen , " essentially " you get 3 filters for the price of one . the image quality with these filters is great , the 812 ( warming ) filter is by far a favorite giving back the color richness that flash photography so often washes out , that is unless you have the patience for constantly tweaking your flash power . aside from the 812 the uv protector is basically a clear protective filter . while it obviously has advantages over clear glass , i tend not to think of it as any different . this too is a great filter which i use about half the time because it does n't affect color hues or change f stop values too greatly while it takes the worry out of carrying the camera around ready for any candid shots that may occur . finally included is the circular polarizer . this filter adjusts the amount of uv light entering the camera by spinning the filter to the direction the uv rays are entering ( or turning the thingy till things look better ) . this lens is great for sunny days and will take surface glare off lakes and glass making them transparent again . it also makes colors more crisp in general when photographing buildings and other large " reflective " man-made things . so things sound great so far , but now to why i only give this item 4 stars . while tiffen is known to be one of the best at photo and video filters , they have quality control issues that do no live up to thier reputation . in my case the 812 filter arrived with a discoloration in the glass . while it was did n't hurt image quality , with the flaw being towards the edge of the filter , i none the less did n't want to find a situation in which the flaw would diminish quality . seeing as it was not amazon 's fault my first e-mail went to tiffen for a replacement which they said they would gladly do , but only after i send them the filter and they recieve it would they ship my replacement ( not an option in my circumstances ) . instead amazon 's wonderful customer service shown through again , and within 3 days they had replaced the entire set . the second set arrivided without flaw but since my other two filters were in perfect condition i traded just the 812. i hav n't had any other issues and i 'm very satisfied with my filters . the only other word of warning would be to that of the circular polorizer . while i recieved 2 that were flawless occassionally i have read in reviews customers have received ones that were assembled backwards making the lens useless . a quick way to check to see if your cp is working correctly is to hold it , thread facing yourself , and look at an lcd monitor or tv and spin it until the picture dissapears ( obviously working correctly ) . i still would n't pass up this deal knowing what i do now , chances are everything will show up perfectly but none the less if you 're concerned order it before you need it and check everything over carefully . amazon is always the best for returns and will often ship a replacement the next day with overnight shipping

## pos 9. music 65.txt

margin 17.63, 107 words

> okay bryce nickelback yells not screams big difference and wtf sum 41 your kiding right sum 41 does not scream at all and you say " i like music " well you dont know any thing about music and another thing you poser is that limp bizkit is not metal they rap so how can you say that they scream all the time...limp bizkit is the worst band out their they give a bad name to music itself and as for you dont write anymore reviews until you know more about music wich with the information i just got from you that will take a long tim

## pos 10. health 593.txt

margin 17.60, 407 words

> i have a preemie who 's temperature needs to be monitored pretty much constantly . at every diaper change we were taking axial temps with one of those standard digital thermometers . torture ! took forever and baby screamed her head off the whole time . then my sister got this thermometer for us and it is fabulous . what we like : 1. when baby is screaming , the light blinks and then goes solid when temp is done , great when you ca n't hear the beep . 2. it truly does take a second unless baby is thrashing about . 3. produces a long beep when you are taking your own temperature , no guesswork about when it 's finished which is an improvement over earlier models . what we do n't like : 1. preemies have tiny ear holes . so we have had to wait till our baby 's ear was big enough to be able to use this thing . 2. the lens covers are a pain to switch out and keep on hand , it would be nice if there were a way to just sanitize the lens after each use . 3. we see a discrepancy of almost one degree between the left and right ear which makes us question the accuracy somewhat . the enclosed brochure explains various causes of this , but that does n't help when trying to determine what exactly your baby 's temperature is . we have done both the axial and ear temp and found that the right ear on our baby corresponds with the digital thermometer 's reading on her armpit . however , the enclosed chart shows the variances between oral , rectal , axial , and ear temperatures which make it somewhat confusing . so we alternate between the digital and the ear thermometer just to be sure . i personally would recommend this thermometer for older babies and kids , just be sure that you test it out when kids are healthy to figure out your baseline and what is normal . it takes some investigation to develop your method based on what your needs are , but it is a nice , quick to use product and my family loves using it for adult temperature readings . we think we will be happier with it when baby is bigger and we are using it for sick readings only

## pos 11. books 19.txt

margin 16.29, 249 words

> i must say my first reaction was to be surprised at how much better hawking is at explaining modern physics than my college instructors were . heisenberg 's uncertainty principle was just an equation i learned . hawking made it seem like common sense . hawking tries a little too hard to be witty at times ( and punctuates all of his jokes with exclamation points ! just in case you missed them ! ) , but all-in-all , this was a quite readable account of what 's presently known about cosmology . i use the term " presently " guardedly , as just recently there was some big finding about dark matter ( it exists ! ) , but from now on , when there are new findings in physics , i want hawking to explain them to me , because i feel like then i might understand them . that 's why you should read this book . the reason you should not read this book is because you have no interest in wrestling with abstractions with which you will never interact in daily life , and would rather read about global warming or darfur or something a bit more topical and practical . this was still a hard read , and i feel like i grasped maybe 80% of it . for you to decide , but for a former engineering student , this was something i wish i had read when i was taking physics

## pos 12. health 130.txt

margin 15.45, 309 words

> i rate ( green tea fat burner ) 5 star . because i bot another called lipoxinol 70.00 ) and i bot another one called ( green tea fat furner ) and it was better in quality wise and its only 14.99 at costco . lipoxinol is very good as well but more expesive . bot off amazon.it sais its ( made canada ) derctions say to take 4 pills in am & 4pills pm . and man there great . the ( green tea fat burners ) in comparison dictions say take 2 pillsam & 2pills pm . i over rall i think ( green tea fat burner ) makes me a little bit more hyper . the more hyper the more stuff i do , that means the more excerise i get , , , , , you will see lipoxinal on amazon . its 4 star , this one has less rating for some reason , not many people said much about it , wierd , americans like to pay more money when , this one can work just as great , not all work tho , but like i said this one was great for me in wise , i bot both , dont go off telling every one u are taking weight loss pills because people will get worryed , like theres no problem , people drink coffee every day of there life , i told my mom and she thot i was crazy , but what dose my mom know , she never tryed weight loss pills , i tryed ntoher one from the natral food store call mini skiny fat burner and i felt like i just shot my self with cocane , so be carfull , earbs have been used for thousand of years and can make u drug crazy ,

## pos 13. software 732.txt

margin 15.25, 236 words

> i 've used turbotax ( or macintax in the early days ) for over 15 years to do my taxes . most of those years included some form of business income , requiring a schedule c to be filed . turbotax home and business is a terrific product , taking you from gathering documents , to educating you about the tax code and recent changes , to data entry , to electronic filing . it 's the whole package . one year , we used an accountant to prepare our taxes , because of a particularly unusual income situation with complicated tax implications . in the amount of time that it took me to write down by hand all the information requested on the accountant 's form , i could have typed everything into turbotax and had my taxes filed . plus , turbotax is less than the $250 average tax preparation bill . and that year i really missed the tax education i usually get by going step-by-step through turbotax , giving me tax saving strategies for the following year . faster . cheaper . plus tax strategy education . that 's why i 'm using turbotax again this year . p.s. there 's no income tax for my state , so getting the federal only version is saving me $10. thank you , intuit , for splitting that apart and giving me the option

## pos 14. software 967.txt

margin 14.46, 183 words

> this software came with a scanner i recently purchased and i decided to upgrade from the " se " ( striped edition ? ) that was bundled with the device . considering the cost and what the software can do it is an amazing value . by simply using this software to re-create documents instead of retyping them is saving me more an hour or two a day . i was hesitant to puchse it based upon all the recent negative reviews , but decided with the 30 day refund policy i could try it risk free . i 'm glad i did . the software worked flawlessly for me - even on 5th and 6th generation copies that were hard to read with my naked eye ( and i do n't need or wear glasses ) . i 'm not sure what those people that were scanning books were trying to accomplish , but when i scanned some pages from an encyclopedia for my son the ocr worked great ! try it and if it does n't work then return it .

## pos 15. camera 843.txt

margin 14.10, 372 words

> i see a lot of people have had trouble tracking baseballs with this thing . i 've owned one for 3 years and it works pretty well . i will give some tips on it : ! ! ! if you throw at a respectable speed , and do n't follow the correct procedure it will not work - there will be no reading ! ! 1 ) do n't stand behind a metal fence . the chain links with the plastic coating over them will work , but for whatever reason exposed metal interferes with the signal . 2 ) the focus beam of the radar gun is very narrow . the whole idea is to keep the beam on the ball as long as possible . just having the ball pass through the radar beam is not enough . you need to keep the beam on the ball for practically the whole pitch . 3 ) use rechargable batteries.. . and this is n't to save money . some of the better energizer rechargable are high amperage , 1350 ma and up . the gun tends to respond better to this , as its pretty power hungry . you will get more consistant readings with better batteries . non-rechargable batteries cannot provide the same level of current ( usually 850 ma or less ) , which seem to effect the gun . so , how would you properly use the gun ? one way is to stand behind the mound as the pitcher throws . forget about using it during a game , behind the backstop . it wont work . try line up the pitchers release point and the plate , then situate your gun so that it fires on this imaginary line ( connecting pitchers hand and the target . you may have to slightly change the angle of the gun to track the pitch , which can be slightly tricky . follow the ball with the gun as long as you can . for a sure fire way to clock a throw , get a cheap net and stand behind it . you will register it every time . you will also have the most accurate reading

## pos 16. software 287.txt

margin 13.72, 177 words

> i have used this anti-virus since 2000 , i liked it then , and i love it now . if your the type of user that does not want to worry about your computer on the internet , this is for you . it can be a pain on older computers that have less ram , but it still gets the job done . now the cons , i had 3 experiences with customer service , and 2 were postitive , and 1 was negative . i 'm not throwing the baby out with the bath water , although i wanted too . the woman was extremely rude , to the point that i contacted the corporate office . in the end i did renew my subscription . i had no idea how easy it is for exe programs , and the such to change settings on your computer allowing attacks . this software lets you know when your settings have changed as soon as they get changed . for 20.00 how can you go wrong !

## pos 17. camera 566.txt

margin 13.16, 254 words

> i have the sony battery that came with the camera and bought an additional sony battery that allowed for 2-4 hours . however , i wanted a battery that i could count on for the better part of an " all day " event and i found it in the qm91d . i was asked to photograph a wedding from getting ready ( hair dresser at 0830 , until the end of the reception at 11:30pm ) the qm91d held strong . i did not constantly video tape , but with my digital recorder i had 6 sony 120 tapes ( 60 min digital ) - - 5 were captured using the qm91d . i did switch some of the tapes before they were completely used to make sure i did n't miss important events ... so i never actually used up " all " of the qm91d battery . this battery was used again during the evacuation from houston ( secondary to hurricane rita ) - - i used it entirely and it did not faulter ... it lasted throughout the trip and i had no need to change to the smaller batteries . the size of the battery did not really bother me - - i was aware that it would be larger than the others and it did not hamper the use of the camera . read the manufacturer information on battery life , charging time etc ... for this battery it is valid . i would recommend this battery .

## pos 18. music 736.txt

margin 12.82, 235 words

> this is one of my favorites of 2004. you got a seasoned vet of an mc rockin over some of the illest producers in underground hip hops beats ( madlib , j-zone , dangermouse ) and some pretty nice guest appearances . i have a couple of complaints on this album though , like the song " love thang " , the hook is wack and the beat is corny , another wack hook comes thru on the title track where you got prince po sounding like tonto from lone ranger chanting some indian ish , and on top of that in his rhyme he says some sh*t like " and if the girl farts then she 's a pooter " ? ? ? thats dumb . one last complaint then i 'm done hatin , but the chorus on bump bump is terrible , and i 'm embarrased to bump bump that ish when i 'm in my car because it sounds so wack , but raekwon 's verse takes me back to when wu tang was the untouchable squad they were back in the mid 90 's , which more than makes up for the lackluster chorus . aside from those complaints you got a dope album , j-zone hit this up with some of best beats i 've ever heard from him . so pick this up its definitely a good purchase

## pos 19. software 986.txt

margin 12.65, 125 words

> purchased this edition of taxcut last week . on win xp2 the software installed cleanly and it downloaded the updates without any issues . i imported last year 's data in less than a minute and i had my return completed in less than 1 hour . this includes capital gains / losses , dividends , and amt calculations . it does n't get much easier than this . yes , you have to download updates . the irs is still making changes to the tax codes long after this software has to be packaged and sent to the stores . the alternative would be to download the whole package online when you buy it , but would n't that take at least as long

## pos 20. software 880.txt

margin 12.26, 88 words

> the product of windows xp - professional is just what i was looking for with many updated features and i am looking forward in using it daily . it was shipped exacting when they had told me to expect it . but most of all , service was " top knotch " . i could not have asked to better service on any questions or problems i may have had . customer service is a plus . i would not hesitate to purchase another product from this seller

## pos 21. software 278.txt

margin 12.13, 152 words

> i tested numerous anti-virus programs after getting fed-up with previous norton anti-virus , which would always " hang " my incoming email , causing me to redownload larger files and sometimes make it impossible to retrieve them at all . ( incidentally , this had nothing to do with the " time-out " settings . ) after testing other top rated anti-virus programs , the only one that would n't " hang " large email files , was kaspersky . even though i have my " time-out " set to only 1 minute , kaspersky never stumbles and lets go , even if it takes much more than 1 minute to download . i also like the easy to use " pause protection " when i 'm doing file clean-ups , because there 's no sense passing temporary files through a second time , and it speeds the clean-up 5 times faster

## pos 22. software 500.txt

margin 11.90, 151 words

> i have windows xp which came with mcafee . i used both norton and mcafee but lately mcafee 's updates seem to have giving other users a lot of trouble . rather than updating the anti-virus definitions , etc. , i decided to try zone alarm where many users seem to like it . i must say that from the moment i installed it the only problem i ran was that you have to completely unistall your current antivirus , firewall , etc. if zonealarm is to work . to date the software has worked beautifully . actually , i believe that my computer runs smoother and slightly faster . i definately would upgrade or buy this product again . check some of the sellers for the bargain prices . i bought mine for 19.99 , which is a big savings from the zonealarm website . it is worth every penny

## pos 23. camera 890.txt

margin 11.80, 254 words

> i have had several digital cameras and this tops them all ! ! ! ! everything they say about it , is true . i love not even having to think about batteries , i did n't believe what people said about the battery life , and i was just happy i did n't need to think about batteries , but i just got married and my 13 year old daughter took more than 100 pictures with this camera and her pictures are almost as good as the photographer i hired and yes the camera battery lasted all day and thru the next 4 days on our honeymoon with another 200 pictures taken , no low battery light ! ! ! ! ! i even going to buy my parents one . also , one more note i love how fast you can take pictures , no wait 4 seconds between shots . i had a kodak digital before only 1 1 / 2 years old and hated it , i hated the download procedure , it did n't put your pictures onto your hard drive , but in it 's own little cubbyhole and trying to attach them to your email was absolutely a nightmare , you 'd have to identify the picture copy it to your desktop , remember what you called it and then attach it your email . this is the main reason why i purchased this camera . i will never own anything else , especially a kodak .

## pos 24. dvd 355.txt

margin 11.54, 148 words

> i purchased this dvd because it said it was an easier pilates video to do ; basically anyone , even beginners , could do it . i have to disagree . i started this video and tried to do all of the 5 , ten minute sections . it was n't completely hard , but definitely challenging . i am not the most fit person , but also not the most unfit . i had a harder time because i am just not as limber as you should be to use this pilates video . i am not saying i would n't suggest it , i am just saying it 's not definitely for beginners . however , the instructions are clear and since it 's broken up into the five-ten minute sections it gets even lazy people like me to get off the couch and do it

## pos 25. health 380.txt

margin 11.14, 233 words

> had i read these reviews before buying this , i probably would n't have purchased it . but i had been looking at the much more expensive sonicare toothbrushes after my dentist recommended sonicare after i asked . i did n't ask if there was a certain model that he recommended , so i assumed i 'd have to pay from $40- $150 for a sonicare . when i saw this one for $30 at target , i figured i did n't have much to lose . i 've had no problems with any of the other problems mentioned and have been happy with how it makes my teeth feel super clean and has even cleaned this spot that even my dental hygienist could n't get . it turns off automatically after 2 minutes , so i know that i 'm brushing my teeth longer . one thing that takes getting used to is not removing it while it 's going...you 'll splatter toothpaste all over yourself ! :d another plus is not having your tummy jiggle like it does with a manual toothbrush ! ! the only negative is that it goes thru 2 aa batteries about once a month , but the directions said that it lasts about 60 brushes per battery change and that 's about right . i 've started using rechargable batteries and have had no problems .

## pos 26. software 506.txt

margin 11.06, 431 words

> tiger is simply the most advanced personal operational system on earth ! i am an advanced used . i have used all sorts of operational systems in the last decades : irix ( unix from silicon graphics ) , sunos ( unix from sun ) , linux , and also the bad written windows . everytime i used windoze in the last 20 years , i had to deal with crashes , hanging , lost of data and hours of configurations , tuning , adjusts , cleaning , etc. even today , everytime i shutdown windoze , it hangs , due to some program crashing . it 's a true joke ! ! ! on february 2005 i decided to buy a mac and give it a try . i bought a mac mini and started using it . what i have to say is that i am using it for more than an year without an issue , without a crash . system is solid as rock . some bad written programs eventually crash , but never the system . and i am the kind of guy who works with several heavy programs with heavy documents opened at the same time . mac never crashed . i am about to suggest apple a way to make it crash , so we can rest a little bit , instead of working all the time . so much trouble i had in the past with windoze that even today , while i am using the mac , i feel like it will crash at any time . fortunately it never crashed . beyond those functions advertised by apple , you will see that macos is a superb gold mine for those who want to explore under the hood . filled with thousands of powerfull unix commands and programs , you will be able to perform miracles . microsoft is copying everything it can from tiger and advertising it as revolutionary features of up comming windows ( hasta la ) vista . i cannot see a single revolutionary function on vista , as everything already exists on tiger . the most amazing is some sites on the web comparing vista ( a vaporware not yet launched ) with tiger ( an actual product ) . the only thing gates forgot is that one month after vista is released , apple will launch leopard that will take the crown from tiger . what i can say you is that for the first time on years i have joy of using a personal computer .

## pos 27. software 386.txt

margin 10.94, 157 words

> ok i gave it 4 stars just for the fact that you cant actually hold them in your hands and read them . i do have them on my laptop so i guess that kinda works . whats great about it is the price . 30 bucks for 40 years of comics.....get real ! ! ! i did have some install problems at first like others have but when i took the disc out and reloaded it it fixed itself . i think it was a adobe update but it did it for me so no biggie . my only problem now is when am i going to find time to read all of the issues . oh and one more thing you can save the disc to your hard drive so you can save it at work and read at lunch without having to bring the disc with you . highly recomended if you love comics

## pos 28. software 903.txt

margin 10.82, 126 words

> maybe it 's because i was upgrading from an older version - - 2002 - - but i found the new features to be very good . for example.. . the junk mail feature works better than any other i have used . it was catching junk from the very beginning , and has missed very few things . i have only had one thing put in the junk folder that was not junk email . also the security features are far superior to the 2002 version . and the calendar is more flexible and easier to use . installation was seemless . i think it might be a little overpriced , but considering how long i will keep it , it 's not too bad

## pos 29. books 672.txt

margin 10.76, 153 words

> i was very excited to get my hands on this book . i have been ordering this series from amazon.co as they are released as i can get them several months ahead on their american counter parts . i must say that i was disappointed with the beginning of the book . first - hem is not the character that i wanted to read about . second - the start is slow and the plot drags a little . but - all is forgiven after 100 pages . i warmed up to hem . i actually think that the authors writting style has improved each book and this book just feels right . i was done reading way before i wanted to be done . the ending is nothing but action . i put the book down entertained and wanting more . what else can you ask for in a work of fictio

## pos 30. software 700.txt

margin 10.40, 222 words

> the lawsuit mentioned in mr john matlock " gunny " review has nothing to do with the quality or legality of documents created using quicken willmaker plus software . instead , it concerns the actions of an insurance agent who was found to have practiced law without a license . he used will-making software ( not quicken willmaker plus ) to write a will for an elderly client . the trouble arose because he created the will outside of her presence and arranged for her to sign it while she was hospitalized . apparently she never reviewed the will . in other words , he acted too much like a lawyer . while the " unauthorized practice of law " is a vague concept , had the insurance agent merely recorded the woman 's wishes and entered them verbatim into the software , there would almost certainly have been no problem . there is no problem with using software to prepare a will for your self . nor is there a problem with using it to create a will for someone else if you merely type in that person 's answers at their direction . the main way to run afoul of unauthorized-practice-of-law rules is to give legal advice to or prepare documents for others without their express , detailed instructions .

## pos 31. dvd 762.txt

margin 10.27, 222 words

> ok , i rounded up to 4 stars . this really is n't bad , though . it 's an idiom that most american viewers wo n't be familiar with . the major characters are kuan yin , confucius , and a flock of other gods , godlings , immortals , buddhas , figures from myth , and other well-known figures and stereotypes from the chinese pantheon . there are the flying heroes , improbable weapons , and acting at least on a par with the dr. who series . in other words , lots of viewers will see it as alien , disconnected , and amateurish , as well as being filled overly convenient miracles . but it 's not in the western idiom , so parts of it have to be taken in their own terms . and it has the look of a low-budget film , so you wo n't see effects on the star wars scale . and it is a bit cheesy and over-the-top , which is part of the appeal . the fights are bloodless , the romance is chaste , and all but the youngest kids will understand the characters . if you do n't take it or yourself too seriously , there 's a lot of fun in this one . / / wiredweir

## pos 32. dvd 864.txt

margin 10.21, 243 words

> it is almost ashame that north amercian culture needs bill maher . after all , should n't honest yet entertaining social commentary be a little bit more available then it currently is ? on victory begins at home , maher creates entertainment by basically speaking his mind . maher 's central premise that the war on terrorism can be aided by what people do in the united states really is almost a common sense arguement . yet maher is so uniquely unapologetic about what he says and how he presents it , the commentary and comedy bristle with an energy that few comedians can match . maher does this by not pretending he is n't politically opinated , in fact that is what bases his comedy completely on , the rarity of straight-forward unabashed opinion . on victory begins at home he is more democrat then republican , but he openly sides with neither . instead , he rails at all presenting himself as a full person , neither liberal nor conservative , right-wing or left-wing . the end result is an engaging and unique look at culture that seems unfiltered . there is no spin here , what maher realizes is that no spin is funny in a world full of it . with all the spin that is normally doled out by the news media , political columnists and special interest groups , know wonder we need him so much .

## pos 33. software 155.txt

margin 10.11, 220 words

> i have been using microsoft operating systems for a very long time , and , i still say that this is the best system out there , for many reasons . an increasing amount of linux and mac users have made the claim that they are more compatible with programs , and are less vulnerable to virus and hacks . in response to linux users - stay away from linux , linux is free for a reason . it is compatible with very very few programs as it is , and that number will only decrease . for gamers - rarley do i see a linux compatible game . just stay away from this system . for mac users - mac 's also have a lesser amount of compatible programs . fewer and fewer programs can run on them , and like linux , that number will only decrease . the only thing keeping macintosh alive is itunes . which is compatible with windows . besides , when direct x 10 comes out , it will only be available for windows , making macintosh 's un-usable for new games when the next windows os comes out ( microsoft vista ) . the computers are also generally more expensive than windows . btw - you can get viruses on mac 's

## pos 34. camera 985.txt

margin 10.04, 468 words

> after reading the reviews here and at [...] on this baby , i was a little cocerned about its low-light and indoor performance . let me be the first to say that my fears were largely unfounded . yes , if you film in very low light , it will darken many colors . but we 're talking 60 lux , which is the roughly equivalent to the light put off from the candles of a birthday cake . just keep the lights on when your kid blows out the candles , and viola ! seriously , i have had absolutely no problems with it filming too dark indoors , outdoors , or even when i film local bands playing in dark bars . the reason i wanted to try this camera was because it is the only flash-based camera that is receiving even mildly positive reviews . i do not want a tape mechanism that will break , nor a fragile hard drive that cannot be used in many film-worthy conditions ( think snow skiing , as the drive mechanism will freeze up on you in very cold weather ) . as i said , i was skeptical when i purchased it , but no more . the videos are far better than any other camcorder i 've owned . my last was a canon zr 50 mini dv , and this camera takes vastly superior videos than that one . the four stars is only because of the mpeg2 format this records to . i have a mac , so editting requires that i convert to dv with streamclip so that imovie can import the movies . mainly , i just do n't edit my home videos so that has n't been a problem . but if would have been nice for it to be an easier option , and it could have been if they encoded to mpeg4 with h264 and mp3 / aac , which appears to be the next standard . if that concerns you , or if you want hd , you might wait until the panasonic sd1 is available because it records in avhdc which is a form of mpeg4. of course , imovie does n't yet support that either , so you may have to wait until ilife 07 to really use it . in parting , i will also mention that the size of this unit is absolutely fabulous . i no longer dread lugging around even my smallish mini dv camera . this thing literally fits in my jacket pocket , so i end up filming a lot more than i did with previous cameras . if you 're looking for small , flash-based , and good quality video , get this camera , you 'll love it

## pos 35. software 636.txt

margin 9.91, 223 words

> high fives to paperport 11 pro ! being in a business where i am constantly told to print this and print that off of one website and another , a product like paperport professional 11 has really come to my rescue . the product has given the opportunity to do something with a document , picture , or file other than printing now when i select the document or file and hit my print option button , i now can print it to a multi-page pdf , if i choose to do so . files that i download , scan , save , or archive are no longer just random clutter on my hard drive , i can retrieve the information from them effortlessly using the product 's powerful search engine . i was thrilled to find that its all-in-one search engine was able to work with files generated in many ms office applications . all i needed to do was remember some of the content text and the pp pro 11 would find the file for me . now i 'm stacking individual ms office files into logically-named pdf groups or using the product to search the web and retrieve information of interest , i find pp pro 11 to be well worth the money and my time to use it .

## pos 36. music 725.txt

margin 9.89, 300 words

> i bought this cd before going to see mmw ( with john scofield ) for the first time at first avenue in minneapolis dec 7 , 2006. i had never heard of them before and liked the clip on the venue 's website . so i bought a ticket and wanted to get " out louder " , which i knew they were going to play , to familiarize myself , but the store i was at was out of it . so i bought " end of the world " instead . while some of it was a little too spacey for my liking at first , i still liked the overall funkiness of it all . then....i saw them play . you must see them play ! ! i did n't ever want it to end ! i immediately wanted to see them again ! it 's less than a week later and i have 2 more cd 's ( " out louder " and scofield 's " a-go-go " which they " back " him on ) and 4 more on the way from amazon as i 'm writing this . i 'm like an addict now ! i have to have them on in the car and in the house . i get back in the car after having been in a store or whatever and they 're on and all is right with my world again . i must say i like " out louder " and even " a-go-go " better than " end of the world " , but only slightly . it is trippy with the synth and the other guest players , and i do like it better after a few listens . i just prefer mmw with less guest musicians

## pos 37. books 950.txt

margin 9.70, 114 words

> the trilogy just stunned me and i worked at trying to understand its complexities . then i read this book , and everything made sense . at first i declared that the trilogy was better than ' the lord of the rings ' but could not explain why . this book nails it . it will be wonderful if you read the trilogy , read this book , and share everything with your children . remember when ' expanding your consciousness ' was all the rage ? no ? that 's ok . all these books do it with a basis in science . buy the darn books . buy them for your friends

## pos 38. dvd 264.txt

margin 9.47, 132 words

> leather wing would only buy this if he ran out of toilet paper , because , you know , a dvd makes good toilet paper ( maybe it 's why he 's so grumpy ) . i would suggest purchasing it and watching it . michael moore may be more to the left than some , but god , has n't anyone ever considered watching everything with a speculative eye ? it 's less biased than the news is - he reports , you decide , and most of it is things that should have been covered by the news in some fashion , but weren't . michael moore is far more honest than the republican talking heads ( rush , coulter , hannity ) . watch , enjoy , investigate further

## pos 39. dvd 559.txt

margin 9.33, 198 words

> the movie starts out with our hero , izo , being gruesomly crucified . because of his rage towards the ones who crucified him , he travels through time to present day to wreak his vengence on them . then a bunch of stuff happens that has no relevance to the plot really , including : having sex with mother nature , a woman pulling a sword out of her vagina then izo throwing a rock at her face , being killed several times , a very trippy scene where he is sucked underwater and comes up on the other side of some wedding where he kills the groom and bride then is sucked back , killing little children , killing a group of mothers in the hallway , vampires , being attacked by a swat team , and a random guy singing while playing an out of tune guitar . while he does all this he turns into a demon then finally kills the ones that were responsible for his crucifixion . this movie gets 5 stars because it is so random and has made me mentally insane since watching it and other japanese films like it

## pos 40. music 217.txt

margin 9.29, 124 words

> buy it . now . stop reading . are you still reading ? ? ? ? okay , so i 'll tell you my reason why . reason ( s ) why . 5.1 sound . dts . different ( some versions better to my ears / psyche ) than the cd . flavor . beautiful production . did i mention dts - you gotta hear this in dts . and she and her band deserve and have earned every penny you could spend on her ( gratuitously inciting flaming ) . i am just hoping that she will give us the opportunity to have dvd 's covering her ' girl in the other room ' and her ' from this moment on' .

## pos 41. camera 635.txt

margin 9.05, 118 words

> we just got this camera after much research . the camera is easy to use and we like it but frustrated that it does n't do some of what was advertised . for the most part tho for the price and all it is fine . just read all the directions and do n't be to disappointed if it does n't play your old 8 mm tapes and a few other things like that . i wrote to sony and they said that this model does n't do a few things . so main point here is read and read and know what it is . i liked the service we received thru amazon . no problems ther

## pos 42. camera 990.txt

margin 8.87, 89 words

> i went the ( thinking it was cheaper ) ebay route - for about $10 more i got a new one here and it works . ebay is nice , but when it comes to stuff like this i learned my lesson . i 've never gone wrong ordering from amazon , in fact i just ordered an oem nb-3l battery for my sd500 ; tried the radio slop route and it wo n't go over 20 pictures . again , shame on me for trying to go cheap

## pos 43. books 416.txt

margin 8.80, 161 words

> private investigator kinsey millhone is back again in this fourth installment of sue grafton 's alphabet series . this time she is offered a fee to give a $25 , 000 cashier 's check to a young man named tony gahan . the check for the fee bounces and kinsey is now looking for the man who gave it to her , plus the young man she is to give the cashier 's check to . everything she finds out about her client is bad . he is a drunk , who has killed several people in a car wreck , and appears to be a bigamist . when he is found dead , kinsey has plenty of suspects including survivors of the dead motorists and two angry wives . this book is written in grafton 's usual breezy style , and kinsey becomes more independent and more likeable with each book . i would recommend the whole series to mystery-lovers

## pos 44. music 172.txt

margin 8.78, 210 words

> recorded 2001 - 2002. it has become all too common that few are taken to task for saying or doing stupid things . what 's worse is that no one seems to care . this is the kind of thing that pisses lewis black off . the angrier he gets the funnier he is . i first came to appreciate mr. black on the comedy central 's " daily show . " i always felt that there should have been more time devoted to lewis black . i wanted more - i needed more - i had to have more ! so i went to my " mental health club , " amazon.com and bought every title available . the end of the universe , rules of engagement and luther burbank preforming arts center blues - ( i had already purchased the white album ) which one is the best ? all of them ! as i write this review - i realize that i still want more - so i am buying the dvd's . there is nothing dated about this material . in 2006 it is just as - if not funnier than when first released . please lewis keep recording it still is not enough ! casl

## pos 45. software 457.txt

margin 8.29, 49 words

> over the last two years , i have found h&r block 's tax cut software to be simple to use to process an otherwise complex tax return . i would recommend it to anyone who wants a reliable tax preparation source without having to pay the accountant 's fees

## pos 46. software 690.txt

margin 8.29, 107 words

> do n't get confused by the licensing mumbo jumbo that comes on the package . it is the full version ready to be installed . do n't forget to plan out your disk partitioning strategy before you start . so far , i have not noticed a dime 's worth of difference from the pro version . it is working great . however , the vista coupon shipped with my package expired on march 15 , 2007. additionally , the coupon only applied to new systems purchased between october 26 , 2006 and march 15 , 2007 , so do n't let the vista thing induce you

## pos 47. health 129.txt

margin 8.22, 148 words

> i love this product . in combination with diet and exercise i have lost about 5 pounds , and i was n't heavy to begin with ( all i wanted to do was tone up ) . instead of taking the recommended dosage of 2 capsules twice a day , i am taking 1 twice a day . i figured i 'd take it slow before i get too jittery . but it definitely curbs my appetite . i literally eat half of my usual intake . it gives me energy without making me feel like i 'm wired and i have n't had any shaking hands . i only had headaches for the first 2 days i took this , but now they are completely gone . i will continue to take this even after i reach my goal weight . it 's a great product .

## pos 48. software 717.txt

margin 7.98, 132 words

> ( review written by my wife , the user . ) i 've happily used the quicken checkbook program for many years . when we changed operating systems from windows xp to windows vista , i was unable to get the quicken 2002 version to work in vista , so i purchased quicken basic 2007 and am totally pleased with the program . the only feature i use is the checkbook program and as far as i 'm concerned , it 's perfect . i 've never used the download from bank option because i prefer to review all posted transactions when the bank statement arrives . i use edit preferences feature to tailor the program to my liking and i could n't be happier . the price is reasonable , too

## pos 49. dvd 856.txt

margin 7.93, 183 words

> i stumbled across this movie on cable a couple of years ago , having nothing better to do i watched it . my first impression was that it would be just another stoner movie were nothing really happens . i was suprised though because not only does it have a plot it has a interesting plot . you do n't have to be stoned , or even a stoner to enjoy this movie . one reveiwer said somthing along the lines of it looking like grade school kids made it . well it is true it was an independent film made on the cheep but think it actualy adds something to the over all feel of the film , like your actualy there , scrapping through life with the characters . i guess i can understand why some people wouldnt get this movie , not enough bells and whisels , but if your up for something differnt give it a try . by the way , the movie was based on a book of the same name , also very good and differnt

## pos 50. dvd 153.txt

margin 7.90, 356 words

> 2 fast 2 furious is one of those sequels that comes around every so often that does n't require you to have seen the original . i saw this movie for the first time not too long after it came out , and having never seen the original , i thought i would be lost and would n't enjoy myself as much as other people , but on the contrary - i left the experience much happier than when i came in . this film is full of quick one-liners that deserve a laugh . the special effects and the car races will leave your mouth gaping open . i have heard and read that people did n't appreciate this film as much because it seemed to focus more on a plot than the first film did rather than focus more on the races , but overall , i think the balance works well . even thinking of the plot that we are left with , i really ca n't see another time when a race would even be appropriate . and as for people saying that this film is worse than the original , i would have to disagree...why ? frankly , i have always been a firm believer than vin diesel is entirely overrated as an actor . ( i mean , c'mon - have you seen the pacifier ? ) he 's nothing more than a meat head who , while able to do pretty good fight scenes , should leave the dialogue to someone else . yes , this film is for the younger crowd , and there are numerous occasions when unbelievable events take place ( take the boat jumping as an example ) , but there is no saying that an older person would n't enjoy it as well...the only thing that i will say is that you really should n't go into this film expecting an oscar worthy performance , or else you will be disappointed . if you sit back and take this as the fun romp that it is , however , you will thoroughly enjoy yourself

## pos 51. music 246.txt

margin 7.87, 175 words

> i bought this cd after i 'd watched the movie the first three times . the music is wonderful . i bought it specifically for the song they sing in the church scene - " i do n't care to stay here long " and i want it played at my own funeral way out there in " someday " . you ca n't hear it without smiling and the words are much easier to understand on the cd than in the movie . but just in case , here 's the first foot-stompin ' verse : fare - - well , vain world ! i 'm going home . my savior smiles and bids me come and i do n't care to stay here long . bright angels beckon me away to sing god 's praise in endless day and i do n't care to stay here long . right up yonder ! christians , away up yon-der . oh , yes my lord , for i do n't care to stay here long

## pos 52. health 930.txt

margin 7.84, 128 words

> i 'm a black male and everytime i would shave normally i would get irritated skin and ingrown hairs . at first i 'd feel a little itch throughout the day and by the end of the day i 'd see these tiny little bumps with white heads ( about 10-20 of them ) . that was before . now after i apply the product i do n't have the itch nor do the tiny bumps come up anymore . it just feels like i never had any hair on my face in the first place . the only bad thing about this product is that it burns slightly but i do n't really care i mean it 's not like the product claims to be painless .

## pos 53. books 814.txt

margin 7.84, 97 words

> this book started off very slowly for me . i got pretty tired of the gender bending deception - how could she be so stupid as to think he was stupid enough to believe his charade for that long in that close of company ? ? ? once the air was cleared , the book picked up speed and ended quite well . i give the book 4 stars because it did cause me to shed a few tears at one point . all in all , a very enjoyable read . past about the halfway point

## pos 54. health 17.txt

margin 7.73, 118 words

> i originally ordered a tanita scale and it stopped working within two weeks . ( amazon , of course , took it back with no problems . ) i was so glad when the omron scale arrived . it costs less than the tanita but the quality is much higher . the numbers on it are very large and easy to read . also , it is much easier to place your feet properly than on the tanita . i ca n't wait to try all the features . by the way , i weighed myself over and over and my weight only varied .2 lbs . as promised . great deal for the money ! ! !

## pos 55. software 615.txt

margin 7.55, 117 words

> this is a cool game in a lot of ways . i was jazzed about it because of the era it represents . but the complexity and inscrutability of the setup menus is somewhat offputting . the huge disapointment , however , is this : the online registration code is missing . utterly missing . and there is no resource available on the net to help . the u.s.a. help number is disconnected . you will not be able to play online . period . the developer 's forums are full of posts about this problem . no resolution... . beware . demand more of the makers of the products you purchase . this is extremely bad

## pos 56. camera 734.txt

margin 7.48, 181 words

> the picture is fine at this price . i bought the panasonic vdr-d100 for my daughter because she usually does n't want to do anything with the computer like edit video . when we gave it to her the first thing she asked was , " can i edit the movies ? " i did a quick test to make sure the dvds would finalize and work on another dvd player with success on 3 computers and 3 dvd players . i did n't find anything the disc would n't play on . then i started up vegas movie studio platinum which i use to edit my minidv movies . i selected import from dvd and it went straight to the minidvd and loaded in the files where i was able to edit and add titles , music , sound effects and a voice over if i wanted to . since i already bought dvd-r / w discs she will be able to reuse them if she ever edits the movies because you can unfinalize the discs and reformat them .

## pos 57. dvd 130.txt

margin 7.42, 350 words

> this is kl 's reveiw this was a very good movie but the plot was a little on the strange side . mitchel musso did a great job , well we all know he always does a great job.okay i 'll stop drooling over him and get back to the movie . this movie is about a cranky old man that dos n't like people to set one foot on his lawn , and a teenage boy that lives across the street that documents every toy the old man takes because it touched his lawn , what time it was when it accured , and takes pictures.but then when a tragic incident happens to the old man and every one asumes him dead well at least the boys do . the teenager dj and his friend chouder discover that the house is even stranger than the old man and that the house seems to be possessed by the old man , well thats what the boys think . then when a arogant girl named jenny selling holloween candy goes up to the house dj and chouder come to her rescue and she ends up helping them find out more about the house . their plan is to put out the fire or the heart of the house . but when thay finally get inside of the house they discover a very strange thing which i 'm not going to say because your going to have to just watch it for your self.but before they get to the heart , they get up chucked , lol.and then a horrable thing comes to their minds its holloween and every kid that goes to that house is going to get eaten ! but i 'm geting too close to the ending or am i ? well if you have n't seen it you would n't know so you 'll just have to watch it because i 'm not giving any more of the movie away ! hope you like it and by the way mitchel musso 's mine ! ! ! ! !

## pos 58. health 460.txt

margin 7.08, 120 words

> i 've tried for literally the last 6 years to find a way to straighten my hair ( and have it stay straight ) ! i am happy to say that i 've finally found something that works ! i 've had many different straighteners , and this one is by far the best . i have long curly hair , and this straightener gets it done in about 20 minutes . much better than the hour i 'm used to . plus , the straightening lasts . my hair stays completely flat all day , instead of curling up on the ends like it did with my other straightener . you simply ca n't get better than this !

## pos 59. software 125.txt

margin 7.02, 85 words

> i am very happy with it but it does n't live up to my expectations . i also have the reg . plus for xp and i really do n't think the extra money is worth it . if i were to do over i would still have bought the plus superpack for xp but not the regular plus just because i do have a media center pc . if i did n't have that the regular plus for xp would have been just fine

## pos 60. dvd 819.txt

margin 6.74, 121 words

> they do't make musicals like this anymore . well , they do n't really make musicals anymore , do they ? they used to make them , made them well and they came out like " down argentine way . " the plot is just enough to keep your interest but the music is bright , costumes lavish and not a few laughts . the major players - betty grable and don ameche - are as engaging as usual.carmen miranda makes her us film debut and sings , dances and mispronounces her way to stardom . the 20th century fox role players appear ( charlotte greenwood , j . carrol naish , henry stephenson ) and add to the fun .

## pos 61. music 170.txt

margin 6.71, 122 words

> a friend of mine gave me this cd about a year ago , i listened to a few minutes of it and was like " what is this crap ? " and i shelved it for a couple months . i then picked it back up and gave it another listen . to my surprise it was really catchy to me . the music ( and lyrics ) are simple , but thats what i like about them . theyre simple ! this is a great college-rock cd . i plan on checking out more teenage fanclub , and i suggest you do the same . notable tracks are sidewinder , what you do to me , and is this music ?

## pos 62. software 430.txt

margin 6.70, 183 words

> i currently have version 1.0 on my pc . it does everything it claims to and does it flawlessly . it cleans internet cache , history , cookies and more ! i 've tried another internet privacy program , but it failed to clean up the tracks that this program successfully cleaned . i especially like the fact that it cleans the autocomplete entries in my internet search and internet browser . others can use my pc , and wo n't be able to see what documents i 've recently opened , which programs i 've recently run , or what i 've searched for and what sites i 've visited online . and that 's the way it should be ! this program can be set to clean up this information securely ( can be set to wipe not just delete the info ) . another plus , it can clean usage tracks for all users on a pc . the program i tried on my other pc only worked with administrator accounts ( and not very well may i ad )

## pos 63. music 304.txt

margin 6.66, 41 words

> please do yourself a favor and buy this cd ! whatever you do , dont listen to it in your car though . no kidding aside , i almost ran my car off the road because i was laughing so hard

## pos 64. software 156.txt

margin 6.47, 144 words

> i have been running xp for a few days and so far so good . i was running win98se and decided to upgrade after microsoft announced that they no longer support win98. my software is now obsolete ? yikes ! well , i 'm glad i upgraded . installation went smooth as silk and i have not experienced any problems at all . i had to find a couple of new drivers for hardware but that 's been it . and for home edition versus pro , i think i can be quite happy with the home edition . i will say that win98se had been a headache for a long time so the stability that i see so far with xp home is a relief . good features , good reliability . a very decent upgrade . i recommend it . four stars

## pos 65. dvd 78.txt

margin 6.43, 64 words

> outstanding ! i new a remastered version of ran was a must have , but i did not expect to enjoy madadayo as much as i did . while i agree the packaging does not protect the disks well , i got lucky and had no damage . i wonder how they will handle this issue if they truly only made 5 , 000

## pos 66. software 346.txt

margin 6.35, 54 words

> i upgraded form office 2000 to office 2007 , expecting to see major improvements . i was disappointed . office 2007 has some enhancements , but it also has some glitches . if i had been able to try it first , i probably would have just stuck with my old version of office

## pos 67. software 654.txt

margin 6.25, 46 words

> some existing programs , such as norton system works , are not compatible with vista and norton insists that you pay for an upgrade to the 2007 version . other than the compatibility issue , windows vista home basic works fine for me . larry leika

## pos 68. music 802.txt

margin 6.25, 257 words

> i 'm not sure about all that other nonsense the reviewer before me is talking about ( sounds like someone with an axe to grind ) but this album is a stunning piece of workmanship . the music is inspired , the melodies transcending , and the emotion - deep and meaningful . as far as " copying yanni " goes , well - i do n't agree , in fact , yanni is far more generic and less inspired . the sound samples the cranky reviewer alludes to are in fact not the same nor , are they yanni 's creation . i write this review to commend mr farish on his work , and to take to task the idiot who misinformed others and could n't resist his own urge to see his " critique " in print . ryans music is distinctly his own , no question - and any similarities are tonal , and not compositional - which the reveiwer would be well advised to take note of . as far as i 'm concerned , you be the judge - and let cranky wannabe music critics continue to wallow in their own self hate as they surf store shelve 's and websites for music to criticize - and well , make themselves feel a little better . personally , i would recommend this album to anyone who likes strong songs with great production and uplifting energy . all the other stuff is for hacks ! enjoy this music ! i do .

## pos 69. music 961.txt

margin 6.24, 108 words

> i just purchased this album , my first misfits album and every song on it rocks ( i especially like where eagles dare ) . i just bought two more albums , walk among us and static age and i wish they would hurry up and get here in the mail because i cant wait . my only complain is the sound quality . it sounds like they put a dollar store tape recorder in the corner and started rocking...but i guess that makes it sound more real too . metallica covered a couple of their albums on their garage album but it just isnt the same .

## pos 70. dvd 94.txt

margin 6.17, 173 words

> james , you wrote : " ben is weak , immature , a stalker , lazy , has bad taste in women and at 21 is unable to tell his parents no when they ask him to wear a scuba suit for their family friends . wow ! revolutionary film-making...not ! " yes , ben was weak , immature , and had bad taste in women . his learning to overcome his weakness , immaturity , bad taste in women , and then defy his family and elaine 's family was his coming of age story . that was the point of the movie . it went right over your head ! the acting was dead on and the subject matter was shocker when it came out ! how could you not love this movie ? maybe you need to grow up a little to see the value . watch it again in a few years . i think you will change your low opinion of this great classic movie over time .

## pos 71. dvd 488.txt

margin 6.08, 60 words

> i thought.. . what the heck , i 'll watch it . so i did . i loved it . i was so surprised none of the critics liked it . it was well made and the characters are all rather believable . i was surprised at how many bad reviews it got . i thought it was rather good

## pos 72. software 942.txt

margin 6.02, 95 words

> in my opionion , act ! is clearly still the best contact manager on the market . i am not talking about a complex crm solution , but it is a fine contact manager . i am not using the outlook and palm interfaces and i do n't have any complains other than it is slow if you are running many programs at the same time . the built in email features are okay , seach features are excellent . just give it a 30 day trial and compare to goldmine , maximizer and others

## pos 73. dvd 325.txt

margin 6.01, 95 words

> i did not have any of the original trilogy on dvd . i am happy to have the theatrical releases as i am not a fan of the se 's , particularly jedi . i was nervous due to bad reviews , but they look and sound great . if you like star wars and want the original releases i highly recommend these . if you already happily own the se 's or are feeling cheated or robbed in some way by repeated releases of the same movie , then do n't buy these .

## pos 74. books 889.txt

margin 5.95, 663 words

> the story , walk across the sea , by susan fletcher , takes place at a town near the ocean . white people thought themselves superior to others , especially the chinese . chinese were often looked down upon and shunned , mainly because of their religious beliefs . the lighthouse keeper 's daughter , however , was different from other white people . believing her father 's talks about chinese people in the beginning of the story , the girl , eliza jane , meets a chinese boy around her age . after the chinese boy saves her goat , eliza becomes interested in the boy 's behavior . soon , she learns that everyone may not be as they seemed . this story was rather interesting in a way . the time of the story show how the characters act and think . the story also shows how different some characters are , such as eliza 's father and mother . ( " something moved inside me , like a sudden shift in the wind . " ) eliza was also , in a way , different from other white people . she befriended and showed kindness toward the chinese boy . ( " ` you 'll do him no harm ? i have your word on it ? ' " ) i was also amazed by the twist of the story when the story reveals that the father truly worries about the chinese boy . of all of the stories i have read , i have never found one that was perfect . this story is no different . when the chinese people were driven out of the village by angry white people , i could feel the same shock and anger eliza felt . the story , however , has a few more bad parts . one boy , amos , accidentally broke eliza jane 's nose while trying to find the chinese boy . afraid that he might get in trouble , the boy lied to his father about breaking eliza 's nose . to make matters worse , amos blames the fault on the chinese boy ! ( " i had a mind to shout at him , to tell him to put her down.. . " ) on the other hand , i did not like how eliza acted toward the chinese boy when they first met . when the boy yelled a warning , eliza thought he was trying to scare her off so he could steal her goat . therefore , when the boy was holding the goat , eliza thought that he was taking the goat from her , when what really happened was that the boy saved the goat from a wave . even so , that was not the worst part of the story . ( " ` get you from me , ' he said . ` i ca n't be near you now . get out of my sight ! ' " ) as a father , eliza 's father was expected by me to listen and talk to eliza about her chinese friend , and maybe even understand why she was protecting him . as a result , i was shocked and disappointed in her father when he told her that he did not even want to talk to her ! thankfully , there was nothing worse than this part of the story . ( " terrible things can happen in this world-things you ca n't explain away . it 's not safe here , andrew john . i ca n't promise you 'll be safe . but there are miracles , too-like you . and love . and glories well beyond our knowing . " ) the ending , where eliza talks to her baby brother about life and the chinese boy was my favorite part . it ties everything together and concludes the story about friendship

## pos 75. dvd 163.txt

margin 5.95, 466 words

> awhile ago i was having a conversation with someone about musical tastes where we vastly disagreed on what was simply awesome bands and which ones were purely based around taste , such as people who love r&b and rap to people who prefer dance . in a way , texas chainsaw massacre , as well as the exorcist and the shining are like the beatles and led zeppelin of horror movies : you must love them and say anything different and you 're going to get lynched . so i will agree that the film is definately refreshing considering the latest crop of so-called " horror movies " , yet at the same time i wonder why it did n't hit me that much . 5 kids are travelling through the country and hear of a couple of houses . they decide to check it out only no one 's home...seemingly at first . pretty soon they meet leatherface , a man in a burlap sac mask who wields a big fat chainsaw . pretty soon , the kids start going one by one and we find a family seriously depraved and having to escape alive . it 's odd how i ca n't say any more about the plot ; not because of spoilers but because there 's not a lot else to say . like many a filmgoer , i ca n't stand the latest releases in horror . instead of using atmosphere , pacing and mood to creep people out , they go for broke and show some of the more violent scenes . this film is n't even gory at all . in fact , the film 's goriest scene , where one of the kids meets a chainsaw , is n't even shown onscreen . your mind fills in what went on which can probably be even more disturbing . adding to the realism is that it 's shot in a kind of documentary-like style . one problem i had with the film was that the dread did n't feel there . there was pre-mtv style editing and extreme-closeups of eyeballs and maybe i 've just seen it before but it did n't creep me out like it should 've ( and having a woman scream for 20 minutes does n't help ) . if i saw this in 1974 , i mostly likely would 've been creeped out of my wits but seeing it 32 years later , it 's more like " yeah it was alright although i better not say so cause then everybody will bug me about it " . if you 're a fan , go ahead and buy it because it 's probably the best release of the film but personally , i 'm not

## pos 76. dvd 365.txt

margin 5.89, 144 words

> all of these bad reviews confuse a movie they did n't like with a badly made movie . this is a very well made movie , with perfectly competent performances . the tone is quite serious , and the ending wo n't cheer anyone up . but then there are many people who loved titanic , which i found utterly depressing . more to the point , though , who cares about the problems of these rich kids ? not me . the real reason to watch this is to see molly ringwald at her most beautiful . and if you enjoy this film , check out less than zero , another gloomy but solid ( & underrated ) ' 80s film . the worst ' 80s film is bright lights , big city - do n't say i did n't warn you !

## pos 77. software 491.txt

margin 5.88, 106 words

> purchased this a while ago and recieved it yesterday . reason ? my computer was moving much slower than it used to . mcafee scans my computer everyday , and does n't find anything , yet it was fully updated . i had a feeling it was n't working . when i installed this thing , i scanned it right away . this is what it found : viruses : 67 spyware : 312 adware : 51 after the scan , everything was deleted and my computer ran like new again . i am very pleased with panda 's software and will purchase again if needed

## pos 78. software 105.txt

margin 5.82, 245 words

> i bought version 5 of this software a few years ago and was very pleased with the many features . a tech at my isp ( bellsouth ) recommended this software to me . i recently purchased version 6 for my new laptop which is running windows xp pro . installation was a snap . updates are frequent and install quickly with my dsl connection . the software suite has in my opinion more and better features than norton pro which i use on my desktop . i really like the registry cleaner ( fixer ) and the defrag tools . ( they use trend micro for virus protection ) the program allows simple maintenance or for more experienced users indepth tools that allow you to maintain and tweak your system . there is a lot of extra programs that come with this software that i did not install after reading some reviews and warnings about using them . however , my personal experience after installing just the system suit 6 professional has really been good for me . i bought my copy from walmart and filled out the rebate following the instructions carefully and i received my rebate after about 6 weeks . i hope if anyone buys this software because of my recommendation will have similar results . i would rate my knowledge of computers as above average , which may be why i did not have any problems with the software .

## pos 79. software 182.txt

margin 5.68, 94 words

> i liked how you could go underwater and try to find things . i also liked how you had to bake cookies and make sundaes . another really cool thing was that you could buy stuff for minette and yourself . i did n't like how the tea was so hard , though.i could n't figure it out , but finally i got it.i liked that you had to fight minette , too.it was funny that she had an alien tatoo on her face.over all , danger by design was a fun game .

## pos 80. dvd 564.txt

margin 5.64, 149 words

> i first saw this movie around 1980 , when the cold war was still on . i had been inundated with propaganda from birth , that all russians talked about was political , that they did n't do " normal " things or live a normal life . all politics you know . well , here was this movie about the lives and loves of three women . it was very well acted , and basically , just a long soap ! i loved it- -and not one word about lenin , marx , or anti-americanisms . i recently saw it again , and liked it just as much . for those who say it is unrealistic- -well , how do you know ? do you think that all russians lived the exact same life ? or because american cold war propaganda stated that all russians were totally miserable

## pos 81. books 201.txt

margin 5.57, 140 words

> the cover of this book compares it to the kite runner , so it caught my attention . i honestly could not stop reading as " yasmina khadra " does an amazing job of making believable and likeable characters . he weaves a tale of how terrible situations eat away at people 's humanity . my only nit is the ending was a bit predictable . that said , it was still a very good ending that rings true . spoiler : if you wonder why she did n't come back , consider that she would not forget the face of the man that bumped into her on the street , which led to them being stopped , which ultimately resulted in her husband 's death . i honestly ca n't wait to read more by " yasmina khadra "

## pos 82. health 424.txt

margin 5.52, 76 words

> i have had this heating pad for over a year and am very pleased with it . the auto shut off is annoying when i forget to reset the pad and it goes completely cool but otherwise , very pleased . just ordered one for my grandma and she is thrilled with the soft cover and the fact that it does n't " rattle " like the old fashioned ones . great improvment and larger size

## pos 83. software 441.txt

margin 5.49, 112 words

> h&r block 2006 works well like it always has . i 've used and liked h&r since the turbotax activation debacle , to the extent that i can like doing income tax ! what is great is the media the software comes on . install the program and then have a nice flash drive to use elsewhere . maybe flash drives will be like floppies someday , with piles of used drives in a box , but for now it 's a super handy way to store and move a few files . 256 megs makes for a big floppy but a small flash drive . no matter- -the price it right

## pos 84. books 933.txt

margin 5.42, 154 words

> this was a book that finally answered my wife 's questions . she is a theologian ( main stream , liberal . evolution is ok ) and deals with science and religion frequently . she kept asking me of my biochemical research " is it predictive ? " . what she was asking was from my studies in protein structure could i predict the taj mahal ? i mumbled a great deal during those conversations . in this book mayr give voice and coherence to the chaos that is biology . it is not the science of physics , where one equation rules all . choices , and accidents happen , and they shape future development . that is who we are . i recommend this book to anyone really interested in what biology is , and what is can say about how it has arrived in this place and time . duke ou

## pos 85. software 963.txt

margin 5.38, 92 words

> turbo tax deluxe is an excellent product but they should make it easier for you to back up without having to go thorugh the whole category to get to one item . also they should make it easier to make adjustments to your state return . it 's very annoying to find and adjust the state return once you have gone back into your federal return . i think it is a very good product but they should make it much easier to navigate to other areas especially for the state return

## pos 86. software 889.txt

margin 5.37, 73 words

> coreldraw x3 is a fine product . it has added some nice features from v-11. coreldraw came with a rebate and i must say amazon failed big time in helping me apply for it...on line was a joke replied by e-mail 3 time never got a reponse...talked to reps 2 times they did not help....yes i got the product in 5 days....but if you have a small problem....amazon aint gunna get r done

## pos 87. music 60.txt

margin 5.36, 251 words

> attell is one of the few decent comics out there right now . i was n't that big of a fan until i saw this in a record store and decided to give it a shot . i 'm running out of comedy albums , there 's not that many good ones out there . so i bought it and i was impressed . the audience is obviously drunken college kids who were very familiar with the show " insomniac " . they would laugh and scream if just slammed the microphone into his forehead the whole night . he has very good timing and delivery though and his jokes have very unpredictable punchlines for the first time you are hearing them . you never see the punchline coming a mile away . he is vulgar so if you are sensitive in any way to graphic sexual scenarios and profanity , stay away . he is one of the few that i enjoy now , tragically mitch hedberg died in march because he was another . the increasingly popular dane cook does n't do it for me . cook 's retaliation cd has broken all sorts of records for a comedy album . i think cook is very marketable to the college , 20something crowd , guys like him because he 's the loud obnoxious drinking buddy from the frat , chicks think he 's cute . i recommomend attell myself , he is vulgar but is just a better comedian

## pos 88. music 799.txt

margin 5.27, 59 words

> i bought this cd yesterday and i immediatly knew it was going to rock ! after hearing the title track , go ! , i knew this cd was going to be different then the spice girls cds. it is better . my favorite songs are never be the same again , ga ga , and goin down .

## pos 89. software 825.txt

margin 5.15, 146 words

> good product amazon had a great price . even though people say it is high priced i paid $44 after discounts . i tried the beta version and i liked it . beta version does not give you all of the features but enough to get the idea . easy to install worked at the get go . intuitive enough to figure it out . you may have to go through things a few times to understand what it means . did n't have a manual with the beta version and still figured it out . manual does provide information , works great . did n't need any help . had mcafee before did n't find any new virus . it works as good as mcafee but it is a lot faster when you start up . both kaspersky and mcafee have features i like .

## pos 90. software 826.txt

margin 5.00, 116 words

> i 've been using this for several years without ever having a problem . i like this new version even better than the last version by having everything in one control panel makes it easier than before . it uses less system resources than norton plus i know people that have gotten viruses using norton & mcafee . kaspersky always rates in the top three . the only drawback is there is no anti spyware but i do n't feel that is an issue . let them worry about viruses & such & i 'll continue using webroot 's spysweeper to control spyware . together , they make a great combo to keep my computer clean

## pos 91. music 586.txt

margin 4.91, 188 words

> if you like beatles , monkees and the who , then you will like the group that is better than all of them ; the rascals ! " lonely too long " is a sad rock pop painful staple in your 60 's elbow...it hurts...then theres all this other good sh*** here...and i do n't mean groovin ! the harmonys and the killer keyboards and tight drumming in these little pop angry yet cheerful nuggets is where its at ! ...i can remember listening to the rascals intermitently with black sabbath and the stooges...and i realised that above all...i liked my rascals record the most back in 1987 up in that cold lonely bel air gardening cabode ! also known at times as ' the young rascals ' but to me...this band will always be the one from way back in childhood that got me listening to queen and the who later on........its hard to say that they are underrated since in any given conversation , you realise the rascals get tone of respect and people will take over and talk about them ; five stars...buy this thing

## pos 92. software 847.txt

margin 4.87, 385 words

> i 've had this pc remove for 1 year and i have used it everyday that i am home and i have not yet changed the remote batteries . my pc has suddenly become more entertaining and useful . with this remote , the time i spend sitting in front of the monitor is reduced . in my 860 sq ft apt , the farthest point away from my pc is about 50 ft . the remote has always worked from anywhere in the apt thru 2 walls . i was surprised to get this much range . i have not yet found a spot from which it does n't work . to get the best range be sure to position the usb rf receiver near the computer as directed . with my pc , i 'm always playing music . i also play digital video files that were either taken with my camera or were rented digitally from the internet . i have a good graphics card with s-video tv out . i got a 50 ft s-video / out cable ; this connects my pc and tv which are in different rooms . with this remote , i now can play ( and control ) my entire digital music collection on my home stereo ( which is connected to the tv ) without being at my pc or be in the same room as my pc . also , with this remote , any video that can be played on my pc , ( online streaming or local ) i can watch and control it ( pause , rewind , slow motion , next , fwd ) on my tv . my pc / tv has effectively become a powerful media center- -media center pc not needed . there is so much more.. . with the remote , i use the mouse from far away ( lying in bed or on the couch ) ; there a numerous ways to get creative with this . i wish the remote was lighted . still , the keys are arranged for " touch typing " so to speak . another negative , i 've noticed that windows media player sometimes crashes when video is launched from within the software that comes with the remote .

## pos 93. music 154.txt

margin 4.82, 418 words

> ah , yes , it 's nirvana 's " nevermind " cd , released in 1991. i listen to all 80 's pop-metal , or hair metal ( whitesnake , winger , van halen , y&t , dokken ) i could go on forever on 80 's bands . ( of course there is rick springfield , and john cougar mellencamp ) . i am a true rocker here , i know all the true bands out there , i know everything about them . i have reasons for this . but here 's the bottom line . nirvana was a breakthough along with soundgarden and pearl jam back in the early 90's . millions of people bought those cds . and yes , there were hair bands still alive back then , like poison , and firehouse , etc. firehouse and poison had alot of success , eventhough it was n't the 80 's anymore . as i can see , alot of my fellow rockers do n't really like nirvana , or pearl jam , or soundgarden . to be completely honest , i like their music , i just do n't prefer the music , because i do n't like the hard sound . i really like the glam-hair band style . people say : " nirvana and those other grunge bands killed glam-metal " . yes , i agree that they killed the 80 's hair bands , but it 's not necessarly their fault . it 's a mix between the bands , and the people listenting to the music . because of grundge music , today 's music is quite horrifying , with emo and other types of music that would 've been a nightmare back in those days . nirvana has a great cd here , but i just do n't prefer it . if you are a real rocker , you 'll listen to all the types of music back then . do n't judge unless you have actually heard it , because you may actually like it . to all rockers - do n't listen to modern music . it 's poisoning our people , and no one really understands the true meaning of " the guitar " in today 's music . most of you will understand what i mean , so listen to the classics . classic rock , and hair bands forever , and even grunge . keep the classic alive . ~the sicilian axe ma

## pos 94. health 857.txt

margin 4.78, 61 words

> i 'm not sure how well since i have never used anything like this before , but my bath water feel a whole lot better and i do not itch for an hour afterwards . i probably should have rated a 5 star , but i really have no base for comparing . i will definitely buy this product again .

## pos 95. software 280.txt

margin 4.68, 77 words

> i have got a virus that cause files " comment.htt " appeared in many folders and my previous antivirus can detect them but can not destroy that virus . i tried to use another 2 antiviruses but not effective . so i try kav and it works ! also kav does not slow my computer like some big-named antivirus . autoupdate feature is cool . we do not have to click anything and the prize is reasonable

## pos 96. camera 854.txt

margin 4.64, 194 words

> we love this camcorder ! we bought it because our other bulky , digital video that uses tapes , which we would have to copy onto vhs / dvd , stopped working . we did n't want to spend a lot of money . we loved the idea that it was easier to carry in my purse and you could download it straight to the computer or burn it ( which is very simple to do , and you do not have to download any software . ) i have to admit i was a little reluctant that the quality of the picture would be less than great , and only 60 minutes concerned me , but the pictures is great and i have n't ran out of time yet . we have used this indoors , outdoors and have no problems . we have recorded our son 's basketball games and it worked great . we read where the batteries did n't last very long , but we have been using rechargeable batteries and have been impressed with lifetime they have . this is a must for those who have children or grandchildren

## pos 97. music 658.txt

margin 4.61, 124 words

> hands down , a 5 star , two thumbs up , classic joint . after it dropped , puba reigned supreeeme . disregard the amazon reviewer , there are no " gaffes " in this one , period.. . these guys were true to their beliefs . they were n't packaging a product for " pop " consumption , they were telling a generation what they thought . check it out and the music will speak for itself . the best track in my opinion was " wake up " , but the whole album was great . as someone else mentioned , fast tracks put it in the 90 's but most of the tracks are relevant sound as good as ever .

## pos 98. dvd 577.txt

margin 4.47, 194 words

> although tomorrow is yesterday is an okay episode , it is not one to rave about.it is certainly not one of the original series ' best . however , return of the archons is one of the best and one of my favourites.kirk , spock and mccoy investigate a planet where the inhabitants appear to be in a drug-induced state then rapidly change from walking peacefully and amiably along the streets into violent and looting maniacs that seem to lose all inhibitions . a mob attacks kirk and crew and they are forced to defend themselves with their phasers . it seems the planet is run by a man named landru , who advocates peace and tranquility to the extent that you get " absorbed " .a kind of brainwash conditioning into thinking only of harmony and serenity.later it is discovered that landru is a computor projection ; the edict of landru who died 5 , 000 years ago has been continued by a computer i just read a review saying the solution to the landru mystery wo n't surprise anyone , it sure surprised me . i did n't see that one coming

## pos 99. books 661.txt

margin 4.44, 162 words

> i have read all of the karen rose books and i continue to love every one of them . the other reviews go into great depth explaining the plot so i won't . the best review i can give an author is when i can honestly say " i ca n't put it down ! " when i fall asleep at work due to reading all night i can tell you it was a karen rose book . " nothing to fear " did not diappoint me yet thrilled me with more suspense and visual images than most of karens books . i honestly can say that i wish she wrote 10 times faster so i would n't have to wait so long for another book to get published . when i meet a friend or stranger reading romance i ca n't help but recommend a karen rose book . this is my latest favorite of hers . keep writing karen !

## pos 100. software 424.txt

margin 4.43, 95 words

> i seriously do n't get why people are having problems installing and using windows vista . i had no problems installing it and no problems using it . it runs smoothly and responsively . no problems . current specs : 3.0ghz intel pentium 4 ht 800fsb 1mb l2 cache 1.5gb ddr pc3200 667mhz ram 200gb sata 7200rpm 8mb cache 256mb ati radeon x600 realtek integrated hd audio intel 915g motherboard 22 " viewsonic vx2235wm hd digital monitor 1680x1050 optical drive 1 : dvd+ / - rw dl optical drive 2 : dvd-rom no problemo .

## pos 101. software 866.txt

margin 4.32, 51 words

> this anti-virus ( and everything else ) software was highly recommended by my company 's network tech . for stand-alone computer home use , it is significantly better than any others ( especially norton ) because it is not a memory hog , so does n't slow your machine down .

## pos 102. health 769.txt

margin 4.21, 213 words

> i do n't know why most of the reviews are so negative . mine works perfectly , it does not flip-flop , does not drop down and you can remove those thingies inside to make the water pressure higher for a more soothing shower experience . reason i gave it 4 stars is because i have what is called a " diverter valve " attached to my shower head . the waterpik is meant to be installed directly onto the shower head itself . i could not do that , because i have a portable " wand " that is moveable via hose connected to the valve and noticed that the threading is too short for the waterpik to latch on to . went to home depot and got an extension and a coupling , kind of ingenious and used lots of pipe tape to " interface " the waterpik via the extension , via the coupling onto the diverter valve.... . wow ! no leaks ! works perfectly . for those of you out there that has a diverter valve for more then one showerhead option , go to home depot , lowe 's or a hardware store and what i wrote above will work as it did for me . enjoy

## pos 103. software 383.txt

margin 4.20, 37 words

> the content gives you 40 years of comic reading for a fraction of the price . however , some of the years ca n't be opened . tried contacting the seller but to no avail . :

## pos 104. books 162.txt

margin 4.17, 157 words

> so many books on the market about pregnancy focus on the medical aspect of what is growing in your wife 's little belly , and not how that little thing is changing your wife and life forever ! this book describes to a ' t ' how this life changing event reeks havoc on everyone involved in the process , and it does it in a way that is bust-a-gut funny . before i read this book , i was like " what the heck is wrong with my wife ? " after reading this book , i was more like " ohhh , i know why she just ripped my head off.. . she hates the smell of carrots ! " great book , fast and fun read , a must read for a new dad . i 've bought it for every father to be , and they in turn have done the same .

## pos 105. music 878.txt

margin 4.12, 48 words

> this album has morse code on it , what more can you say.. . ...well some of that morse code actually sounds like that ua6 you just worked on 40 metres , complete with t6 buzz and slow drift . and the music is pretty good too .

## pos 106. camera 636.txt

margin 4.05, 25 words

> i purchased the videocamera thinking i could watch my old tapes also . this videocam does not do that . i had to return it

## pos 107. dvd 249.txt

margin 4.03, 139 words

> " the incredibles " , together with " finding nemo " , " shrek 1 & 2 " , " madagascar " and the " spy kids " series , certainly mark a turning point in terms of animated moviemaking . particularly the incredibles is a movie no kid ( or adult as well ) will ever get tired of watching . as for the plot.. . it is just plainly great . things have been kind of boring for superheroes since they have been forced to give up their superpowers and adopt a conventional lifestyle . but everything will change for mr. incredible and his family when an interesting business proposal will ultimately make him wear his superhero suit again for an exciting new job . my kids just love this movie ( and so do i !

## pos 108. health 371.txt

margin 4.02, 93 words

> its a freakin wet nap , what else can i say ? not much to critique here . i live in a small town & their kind of hard to find so amazon to the rescue . pros : 1. style ( square ) 2. looks . it does n't shout " hey i 'm a wet nap " 3. shape . it stays put in my truck & does n't roll around . 4. does a great job of what its intended to do , nothiing more . cons : 1. non

## pos 109. dvd 11.txt

margin 4.00, 62 words

> this movie is a scream ! i laughed until i thought i was going to die . comedy does n't get any better than this . the characters are incredible . it 's amazing the actors could keep straight faces while making this movie ! do yourself a favor and watch this movie ! it 's even better the second time around

## pos 110. health 212.txt

margin 3.99, 52 words

> when i found out that contradiction was no longer going to be sold in the us i thought i would never find this again . it 's my boyfriend 's favorite cologne and i was determined to find it . thanks to amazon , he has his sexy scent back . lo

## pos 111. dvd 95.txt

margin 3.99, 69 words

> moving , intelligent , realistic , not overly acted ( as could quite easily have been the case ) . about a 20 year old who has gone off the rails to come back onto them again...you see why this has happened , feel sympathy , and just want him to do well when the film ends . a story about hope , in a world with little. .

## pos 112. software 641.txt

margin 3.96, 77 words

> i read horror storied about 7.0 nero so i upgraded to 6.6 from 5.5 by going to the amazon new & used market . this is a good program that does all you need for dvd 's and cd's . it gets good reviews . i ca n't imagine what happened to 7.0 but they may have gotten carried away with " user friendly-ness " - i see a little of that in 6.6 compared to 5.5

## pos 113. books 777.txt

margin 3.92, 61 words

> this is a great book . i could n't wait to see what was going to happen next and how all the mixups would be straightened out ! it is a very funny and delightful book , i hope there will be a sequel , we need to know what happens to these people , i feel like i know them

## pos 114. camera 715.txt

margin 3.90, 15 words

> i canceled this order because shipment was n't going to arrive in time for christmas

## pos 115. music 191.txt

margin 3.89, 97 words

> if you think yer gonna puke everytime you have to suffer through a " country " song from nashville these days , and you happen to like classic rock , you would probably appreciate what shooter 's trying to do here . folks , this is the real deal . i do n't mean real country or real rock - this is a hybrid - i mean he 's making music that is honest and down to earth . a flash in the pan , he 's not . he 's going to be around for awhile

## pos 116. health 99.txt

margin 3.82, 180 words

> my wife had high bp , so we got this model . the reasons for choosing this model were that : 1. the upper arm monitors are supposed to be more accurate 2. it was cheaper than the fully automatic models 3. omron seems to be one of the better / best brands . 4. supposedly , the pumps on the fully automatic models are prone to breaking . the unit appears well built ( including the hand pump ) . it is easy to operate , and it seems very accurate . we checked its readings with an fully manual unit that we have at home , and the automatic unit at the drug store . we find it takes very accurate and consistent readings . people with physical limitations might find the hand pump inconvenient . also , people with a big arm might need to buy the larger cuff . i 'm overweight right now , so the cuff barely fits my arm , but fits my wife 's nicely ( it was bought for her )

## pos 117. health 22.txt

margin 3.82, 180 words

> my wife had high bp , so we got this model . the reasons for choosing this model were that : 1. the upper arm monitors are supposed to be more accurate 2. it was cheaper than the fully automatic models 3. omron seems to be one of the better / best brands . 4. supposedly , the pumps on the fully automatic models are prone to breaking . the unit appears well built ( including the hand pump ) . it is easy to operate , and it seems very accurate . we checked its readings with an fully manual unit that we have at home , and the automatic unit at the drug store . we find it takes very accurate and consistent readings . people with physical limitations might find the hand pump inconvenient . also , people with a big arm might need to buy the larger cuff . i 'm overweight right now , so the cuff barely fits my arm , but fits my wife 's nicely ( it was bought for her )

## pos 118. software 435.txt

margin 3.76, 166 words

> i initially purchased creator 9 to do the same thing this software does , but the only thing is it didnt hang my computer when it came down to burn the dvd . this software is pretty much easy to use , comes with two ( bibles ) manuals , plenty of information in there to creat some good videos . i recommend buying this or you can always buy creator 9 have it crash your system and then spend a few days trying to review other products out there that have gotten good reviews such as this one . you will be happy with the videos you make . you can make a video containing still images ( pictures ) , video from camcorder camera or from your computer , add text in the movies , add background music , its awesome . i must say again it wont hang your system . please get it , your family and yourself wont be disappointed .

## pos 119. books 153.txt

margin 3.69, 169 words

> this was one of the first books that i picked up after my divorce 17 plus years ago . i knew that i was giving these men all my love , but even with all the love i was giving them they were treating me like i did not matter . knowing there is a problem is the first step and what a huge step that is . after reading this book the light bulb went on with a bang and it has never gone off . i have struggled with relationhsip issues , but at least i know what is going on and with each relationship i got better and better until i got it right . i learned i had to read the signs that i chose to ignore for some many years . i have been in a healthy relationship now for 8 years with a man that shows me his love ( along with telling me ) and treats me the way i deserve .

## pos 120. dvd 69.txt

margin 3.64, 112 words

> i watched this dvd in one of my classes and it left me feeling hoplessly hopeless ! i really dont know what to think about the whole presentation . the presence of chomsky makes it look reputable but who knows , he might have been taken out of context although it seemed not . if what they claim about corporations is true , then we are getting ready to implode in one way or another.i 'll keep away from political lines and just suggest that you watch it and decide.. . i had given it a rating of 3 but just changed it to 4. the material is more plausible than otherwise

## pos 121. health 455.txt

margin 3.61, 41 words

> good product - the pressure could be a little stronger with the sponge head . it has a nice scent , and when the crystals had leaked upon arrival i had excellent customer service from the company to replace it .

## pos 122. music 962.txt

margin 3.60, 104 words

> i usually do n't do album reviews but i gotta say this was tight from beginning to end and i was shook that this was given a low reading by a magazine i call & quot ; the sauce&quot ; so many of yall need to stop reading magazine ratings and come to sites likes this and read your own peers ratings . word of mouth is bliss . a-g-2-a-ke who came out on rap-a-lot has n't come out with a cd since this classic . i 'm salty they did n't & quot ; make it&quot ; because this was heavily slept on

## pos 123. health 599.txt

margin 3.58, 127 words

> i 'm not a sucker for advertising and i 'm definitely not an impulse buyer . but i did purchase a schick quattro razor some time ago to replace my old , tired blade . and i 've been satisfied thoroughly with it . however , after needing some refills , i bought these titanium coated blades . wow . i did n't believe it at first but i actually took a new titanium blade and the regular schick blades and ( i ca n't believe i 'm about to confess this.. . ) did one of those hokey " side-by-side " tests . this blade is excellent . it is an upgrade above their standard blade and , to me , worth the difference in price

## pos 124. software 480.txt

margin 3.53, 52 words

> i made the mistake of ordering this product and microsoft office 2007 which i did n't realize that it was also offered in office 2007 which i did n't need 2 of them so i gave the other one to my sister who just loves to keep all her records in the

## pos 125. health 746.txt

margin 3.46, 93 words

> not a bad product . irritates the skin a little , but does remove your hair . the only things i do n't like is that the buffers wear out quickly and your hair grows back with in 2 weeks . it does a nice job of exfoliating the skin and is great for hard to reach places . not a bad product ; however , i hope someone soon comes up with something that can take hair away permanently or for a longer period of time . i would recommend this product

## pos 126. music 5.txt

margin 3.42, 132 words

> ok good cd . im not suprised . ok jaheim may not have the b best voice but his music is good and it goes will with the voice that he has . yes yall this album does use profanity but the songs actually have meanings . i like that daddy thing song , and like a dj . this album looks at issues from a mans point of view . ya know we 've heard the angry woman and how the man did t his and that now jaheim looks at it from a males view . ok yall i know he is not the first one to do this but he did it well . also this is a break from that [...] that is played on the radio .

## pos 127. dvd 787.txt

margin 3.42, 58 words

> it 's just like the hit tv show ! in fact they probably got the idea for the tv show from this movie . actually i thought it was more of a comedy than anything . i saw it on the " we " network . it 's worth the price if you feel like buying it .

## pos 128. software 900.txt

margin 3.36, 105 words

> i think this is the best version to come out yet . i would have a high end pc if i was to upgrade only software . i would just wait and buy a new pc . its alot easyer then learning a new operating system and if you enable the adminstrator account and only use your standard accounts to surf the web then it give you some security . the firewall is good in the business versions and there is some good virus software out there . its got alot more features and run 's good's . device drivers are easyier to load -scott

## pos 129. camera 183.txt

margin 3.35, 35 words

> works great on my s2is , clicked on silver on main page but switched to black on order form , did n't notice this but i like the black anyway . looks good with acc

## pos 130. dvd 337.txt

margin 3.35, 187 words

> i have been following the laughing man fansubs , so i 've covered all this material before . i 'm acquiring the dvds as they come out to have legit copies . the desc says 2 collectibles toys , it 's actually 3. there is batou on the plate like motoko from vol 3. in fact , the base plates fit together , which makes me belive that vol 5 will have another piece that will fit together to complete a composite set . the other two toys are the chinese assassin with the gun-arm and the old robot unit from the organ-farming business ( with the fake southern accent ) . these are easier to put together , i had problems with the tachikoma from the last set , it broke when i tried to put the legs on . have n't gotten around to the super-glue session yet . the product itself : stand alone complex - 2nd gig continues some of the best animation and smartest television ever produced . buy it , share it with those persons worthy / capable of appreciating it

## pos 131. dvd 551.txt

margin 3.34, 55 words

> one of the best new sitcoms in recent years.. . up until i got the dvd i had no idea bob saget was the narrator.. . neil patrick harris is very funny as barney ( who names thier kid that these days ? ) and basically makes the show what it is...... . legendary !

## pos 132. music 135.txt

margin 3.24, 36 words

> i like every song but 1 on this cd . they 're the same ones that 're on the movie and if you do n't like the movie , you probably would n't like the cd

## pos 133. software 704.txt

margin 3.16, 42 words

> absolutely no trouble installing on 2 computers , ( i use windows xp ) ! ! total protection , plus you can block many websites very easy , which is great for the computer the kids use . came with 3 licenses

## pos 134. dvd 206.txt

margin 3.15, 154 words

> i saw this movie for one reason : i wanted to see gerard butler in something other than phantom of the opera just to see how he played a " normal " role . i 've never been a big fan of " chick flicks " ( for instance , my friend and i watched a walk to remember awhile ago , and the only thing that kept us from laughing throughout was the constant threat of being slapped by one of the girls in the room ) . that said , dear frankie is a thoroughly entertaining film that has a surprisingly deep plot and keeps going at a fast enough pace that you never get bored . initially i had trouble understanding what the actors were saying ( they all have thick accents ) , but once i got used to it i had no problems through the rest of the movie

## pos 135. health 32.txt

margin 3.15, 82 words

> this is a great drink . i wanted to try something that was different , and this definately fit in . it isnt carbonated , and tastes really good . what i really wanted to know though , was how it worked . there is no caffeine or taurine , and the ingredients list didnt really show anything out of the ordinary . it worked well though , and i was able to stay focused for a long time after drinking it

## pos 136. books 393.txt

margin 3.13, 331 words

> a surprisingly tiny book . ( the picture in the upper-left corner is nearly actual size . ) after receiving it , i immediately looked up its dimensions in the description on this page . it says 4.7 x 3.3 x 0.6. i had not noticed that before i ordered it . the book seems much smaller than that . not that that is a problem ; it was just somewhat of a shock to find such a minuscule book when i opened the box . i believe it is intended to be carried with you in your pocket or glove box or the locket around your neck so you 'll have a chance to pick out a few choice topics of conversation before you enter a party or whatever . it certainly is not intended as bathroom reading . for one thing , the pages are much too small for emergency tp use . not that i am complaining , mind you . this is a gem of a book with over 200 interesting bits of trivia listed more or less alphabetically from " the amish " to " zero " . ( this is not to imply that the title of each page has much to do with the text , but who cares - the book is fun . ) each page has its stated " fact " and a follow-up paragraph to expound on the subject . also , there are a number of pages randomly strewn through the book with three " instant personalities " each - little tidbits of info about famous people . ( although , thomas jefferson got his own page , as did alfred hitchcock . ) and unlike another trivia book i purchased recently ( bla bla ) , the information here is actually correct . will and mangesh research their topics , not just publish un-provable " facts " gathered from the internet . use the contents with confidence .

## pos 137. books 618.txt

margin 3.11, 85 words

> i liked the book but you also have to consider the end killer.. . is that logical at all ? ? the senator is in his late fifties and so how old is his father ? if he had the senator when he was twenty he 'd have to be 77. is it really reasonable that he 's running around killing people , and setting houses on fire . it was a very unlikely twist to the end . it still was a good book

## pos 138. software 946.txt

margin 3.08, 117 words

> i think this is actually a very good os . there are a lot of new features and home premium appears to be the best vista os for the money . i purhased a new pc with this os and have really found no compelling reason to upgrade to ultimate for $150. only legitimate gripe concerns drivers for non-microsoft products . not excatly sure why this is microsoft 's problem though . regardless , this os is the smart choice for a new pc for home use . accept a minimum required graphics and audio card until suppliers catch up with this new os . then upgrade . otherwise , wait till you need a new pc

## pos 139. dvd 597.txt

margin 3.08, 68 words

> i loved this movie...it was a little hard to follow because of the commercial break timings in it . this did not make the movie any less great it just made the movie a little hard to follow because it kept repeating the intro . at the time that the commercial breaks should have been because of it being a tv show that was made into a movie

## pos 140. books 414.txt

margin 3.03, 103 words

> i am so passionate about this book . it has answered all the life questions i have ever held . although many people i have recommended it to have reported that they have not been able to " get into it " - for me , i would say it is the best book i have ever read . this is about the 5th copy i have purchased because when i lend it out , somehow it is not returned and i want to have a copy to re-read every now and then . ( i will not be lending this one again

## pos 141. software 999.txt

margin 2.96, 166 words

> if you want a simple to use program to manage personal finances quicken is for you . i have found it very useful for keeping track of my checking and savings accounts . you can also make automatic posts to your accounts . which is nice feature if you use automatic online bill pay with your bank . the program makes charts , graphs and reports showing where your money is going and coming from . it also does a nice job showing you if where you are meeting your budget and where you are spending too much money . quicken makes keeps track of loans easy . it calculates how much money is going to interest and principle . i have been having a hard time and have been unsuccessful at setting up the program to track my 403b account . overall , i think quicken is a good program and recommend it to anyone to anyone who does not have a similar product already

## pos 142. music 412.txt

margin 2.92, 154 words

> wow ! i love this spykids movie way better than the first one . i think of the first one as an introduction for the characters and the sequel is the big adventure for all the cortezes and even more characters , like the giggleses . we met donnagon in the first movie , and he was the reason for the cortez parents to go on the mission . now we see that he has kids and we relize that he has bigger plans for the oss . and what about alexandra , the preisidants daughter ? she is the main reason we know about the transmooker device , right ? also grandma and grandpa cortez are joining us in this movie . i think robert rodregiuz did an execallent job on the sequel , spy kids 2 : the island of lost dreams . ... the sequel is awesome ! ! ! !

## pos 143. camera 793.txt

margin 2.91, 59 words

> i had a previous generic charger that did not work . well if you go with this one , you wo n't have to worry about that . this one works like a charm and seems to charge pretty fast too . i 've had this for a while now , and never had any problems with it .

## pos 144. dvd 623.txt

margin 2.91, 50 words

> this movie was one of the most honest , accurate portrayals of how to play the dating " game " i have ever seen . i liked it so much i bought it for my 15 year old son to give him pointers . ignore the tacked on hollywood ending

## pos 145. camera 215.txt

margin 2.86, 84 words

> this is a great camera . plenty of resolution . excellent shot speed . sturdy frame . the kit lense does n't do the camera justice . buy the body separate and add a better lense . on the bad side , i had a small glitch with the camera 's firmware soon after purchase and had to return it for a fix . it was two months before the camera was returned . sorry , canon.. . you lose a star for that

## pos 146. software 51.txt

margin 2.85, 23 words

> this was used to upgrade my operating system at work . it went fairly well . actually much better than i had hoped

## pos 147. software 157.txt

margin 2.85, 23 words

> this was used to upgrade my operating system at work . it went fairly well . actually much better than i had hoped

## pos 148. health 517.txt

margin 2.84, 78 words

> i took " my " unit to a monthly meeting for seniors . their machine broke & i took mine as a replacement . they liked it so well , they had me buy this unit for the monthly meetings . they like all the different aspects of the machine . a suggestions could be to include a card that you could carry in your wallet & write down the date & the numbers from the machine ?

## pos 149. music 56.txt

margin 2.76, 125 words

> it 's sometimes hard to think there are really anymore pleasing melodies out there , but thank halstead & co . for proving me wrong . i am happily pleased with their latest , and very eagerly awaited , effort . instead of the depths of melancholia and loveliness on , say , out of tune , they give us 41+ minutes of what seems like basically " it 's good , everything 's going just way ok.. . " it 's happy . maybe i 'll hear a lyric later that says something else , but for those for whom music is the priority , you ca n't go wrong with this considered and experienced and artful pop . four and a half stars

## pos 150. software 713.txt

margin 2.76, 20 words

> it would be nice if the contents were listed , with all of microsoft 's versions , it gets confusing

## pos 151. software 151.txt

margin 2.73, 36 words

> this program does what it says . it does limit you to only 3 loadings of the product on your computer , so if you have more than 3 computers you have to buy another program

## pos 152. camera 10.txt

margin 2.73, 37 words

> i enjoy the tc80n3.you may think it 's costly , but the features are out standing.i think it was worth the buy.the only disappointment i have is there is no " on , off " power switch

## pos 153. software 220.txt

margin 2.62, 114 words

> i have a question about this . i 'm wondering if i can hook my guitar into my computer and record it and then like add drums and loops an stuff onto it . is that possible on this program ? cause my friend has acid pro 4.0 and that is really awesome but it 's like $400 and i dont have that kinda money . wut i liked about acid pro 4.0 is that you could hook up ur guitar to the computer and stuff like that , so im wondering if you can do that on this program . if u have an answer for me , e-mail me at peepilott@aol.com .

## pos 154. health 966.txt

margin 2.60, 81 words

> i got this bed topper a couple weeks ago to place on my older matress . it was pretty pungent , but it felt so good the first time i layed in it . after a couple days it appeared to lose it 's memory and start to dent and crease , but eventually it got back to full expansion . the customer service with this item was fantastic ! we 'll see how long the matress keeps up its memory

## pos 155. music 58.txt

margin 2.58, 32 words

> you definetely gotta own this . after an 11 years break from the music scene , seger 's back full-force . already 400.000 copies sold . more info on bob at [...

## pos 156. books 787.txt

margin 2.53, 116 words

> i like this author 's work so much that i actually bought the hard cover since i could n't wait for the pb to be issued . however , p . d . james ' view of life as expressed by her characters can be very pessimistic at times ( a contrast to her autobiography ) . in this one , there is still the feeling that the characters are going through the motions of living , never really feeling any joy- -or often even happiness . however , when adam and emma come together at the end , there was a ray of hope . please , ms. james give us a new book asap

## pos 157. music 421.txt

margin 2.51, 170 words

> this movie was a favorite in our household and my daughters always enjoyed the karaoke a the end of the dvd , so we searched for the soundtrack . i actually chose this volume over volume 1 for two reasons...it contains the favorite from the movie , " i want to grow old with you " actually sung by adam sandler and secondly , because volume 1 contains the song that adam sandler sings about his ex-girlfriend , which contains quite a bit of profanity , so i did n't want to get it for my kids . i would have given it five stars , but we find the introduction by billy idol at the start of the last track , " i want to grow old with you , " which is dialog from the movie , to be distracting and it gets tiring to have to listen to over and over when you just want to hear the song , which i mentioned was the absolute favorite

## pos 158. dvd 531.txt

margin 2.51, 66 words

> english humor is famous for it 's eccentricities but with the exception of selected monty python you need the english pedigree to really like it . the young ones pick up where monty left off . outrageous , yet real , there is a plot line but it does n't get in the way . it 's a shame there were n't more episodes made... .

## pos 159. dvd 600.txt

margin 2.49, 16 words

> exactly what i thought i was purchasing . shipped quickly . definately would recommend this seller

## pos 160. software 324.txt

margin 2.45, 46 words

> i had the software in just a couple days and it was exactly as i ordered . along with it came an information sheet on what to do and who to contact if there were any problems . great job . would order from them again

## pos 161. music 680.txt

margin 2.44, 25 words

> three six mafia has out done there self with this new guy chrome about every song is decent which is hard to find these days

## pos 162. health 890.txt

margin 2.39, 202 words

> nearly two years of ownership and it has been a great purchase . i have no shame dorking up my drinking . use to ensure legal driving or for ill advised contests . also determine what at what bac memory gets spotty ( what point is there exceeding that ? ) . fun to call out big talkers who do n't suspect you are packing a lie detector of sorts . also useful to get people off your back who think you are too drunk to drive . pros precision to third decimal place . rare at this price at time of my purchase very repeatable with consistant deep breath small enough to take to bars in jacket pocket or cargo pockets . light for its size . cons innaccurate if sips have been taken within 10 minutes or so . true for all breathalyzers . drunk idiots have tough time getting it through their heads warm up / calibration time ~45 sec . another let down at parties but perhaps key to accuracy would be nice if it was more pocket sized chirps at you alarm clock style if above .08 " i know i 'm drunk , shut up !

## pos 163. music 4.txt

margin 2.37, 91 words

> like i said i would , i finally got around to purchasing this cd . i especially like tracks 9-12. cheap trick is solid as always . i have been a long time fan and enjoy all their releases . if i do have any criticism at all , it is the fact that some songs sound like recycled trick riffs . i guess it 's hard to create new stuff after 30+ years . anyway , there are some great tunes on this . buy it like i did !

## pos 164. software 670.txt

margin 2.35, 56 words

> quickbooks lives up to it 's reputation of being the one-size-fits-all small business book keeping software . it does what you want it to do . i like the feature of being able to easily sent e-mail invoices . if you need the software right away it is just as cheap at the office supply stores

## pos 165. software 245.txt

margin 2.27, 101 words

> if you have used ms streets & trips , then you 'll know your way around autoroute . we are using this to plan a trip to europe next may . based on my knowledge of locations in britian , the software appears to be pretty accurate . if you want to use this with a gps that does not come bundled with the package , expect some frustration . i still have not figured out how to get it to talk to my usb based garmin unit . i think it is possible , just do not know how .

## pos 166. books 422.txt

margin 2.27, 248 words

> great book ; it get 's you thinking . my kids arre almost out of the nest and they are all i could ask for . yes , i worked . but not until they were in school , almost always part time and i did not use ' working ' as an excuse to not volunteer at school , sports , and generally be in my kids lives . the point is really about your priorities . do you instinctively put your kids needs first ? it 's been interesting to see how things have worked out with families in our area . we have a large group of kids who have been together since kindergarten ; now they are seniors . you can instantly tell which parents were connected , involved and had their priorities straight . not all of them stayed home the whole time . on and off i used to listen to dr. laura , frequently agreeing , but many times not . what i love is that she has an unpopular point of view and she 's not going to let social , financial , or industry pressure dilute her message . yes , she 's frequently abrasive ; so were many people who have made an impact in the course of events in this world . if you are a parent with young children read the book at least it will give you important ideas to agree or disagree with .

## pos 167. dvd 925.txt

margin 2.20, 226 words

> i was blown away by the wonderful acting of juliet lewis and giovanni ribisi who played the retarded young adults . this was a very compassionate film about the realities of living with a disability . disabled people desire and deserve to have the same opportunities as everyone else . it was wonderful to see the love " carla " ' s siblings and parents had for her . there were 2 reasons i did n't give this movie 5 stars . one was that diane keaton 's character of the overly controlling mother was annoying . obviously she was supposed to be annoying , but i think she overacted a bit and she needed better lines , she seemed to say the same stuff over and over again . another reason i did n't love this film was because hollywood once again compels right wing nut jobs to write reviews that portray themselves as normal and good . sorry , hollywood , but there will always be those of us who still believe god 's word to be true . being a right wing nut job is n't considered normal or ok in the bible . god never created it . look it up . you are not helping people who struggle with it to be set free from that addiction and lonely lifestyle .

## pos 168. health 617.txt

margin 2.16, 64 words

> i used the huggies overnite diapers on my son at night until we started potty training . i used to put absorbent inserts inside his pull-ups to get him through the night without leaks , but even that did n't work very well . finally , huggies came out with an overnight pull-up - and it really works well ! ! ! excellent product

## pos 169. software 388.txt

margin 2.13, 174 words

> we purchased this for my 6 year old son and 7 year old daughter since both children have been asking me to help teach them how to play chess the last several months . while i have been able to get them started , i find that approach used in this software to introduce the game pieces and concepts has allowed their understanding of the game to grow . both kids enjoy using this software and , if i would let them , would spend hours at a time using the software . my biggest issue with the software is the sound and animation . we continually have issues with the sound / animation not being in sync or the audio cutting in and out . we run this on a computer with plenty of processing power , memory , disk space , etc. it does not bother this kids too much , but i find it annoying . all in all , a great tool to help my children learn the game .

## pos 170. books 451.txt

margin 2.09, 104 words

> " i have shooting pains in my upper left arm . " said the pilot to brian . brian is the main character in the book hatchet . this book would be for someone who likes survival in the wilderness or even just survival . i like this book because i am into this type of writing . i think gary paulson is a very intelegant man because.....who could have thought of a book about a boy who his plain crashes into the canadian wilderness and.............do you think he survived the wilderness ? .........he does survive the wilderness ! submitted by : peanut !

## pos 171. health 187.txt

margin 2.08, 29 words

> shaving cream in a tube is just about impossible to buy at retail outlets . this is a great product and i will continue to buy it through amazon

## pos 172. dvd 380.txt

margin 2.07, 34 words

> you gotta get the whole series....you ca n't just get one or two dvds...you need the whole thing , trust me . once you start you gotta go all the way to the end

## pos 173. books 795.txt

margin 2.04, 89 words

> after getting and reading primary target as a gift , i immediately began picking up other joe weber books . defcon one , his first , was absolutely terrific . great plot line and characters . the action is continuous throughout . my suggestion is not to pick up this book to read up before going to bed because you 'll never put it down . looking forward to reading his next - shadow flight . my hat 's off to joe weber . keep up the great work

## pos 174. music 216.txt

margin 2.00, 199 words

> i have loved the swans since my danceteria days in early 80s new york . but its a fitful , frustrating love . you get the sense from ' incandesent ' that the swans forgot to stop partying . that they never took the time to put together more than a handful of songs . oh , but what songs they were . this collection is for completists and aging post-punker ( like myself ) who wished they 'd shared a pint with the boys back when simply getting stoned was a subversive act . its a nice collection of beautiful , quirky oddities here . but a few gems are missing " holy holy " , " 1982 " , " world of milk and blood " come to mind . maybe on an ' ashes ' reissue . in the meantime , scoop this up . simpson & company deserve the attention . if you really care about the band , buy it directly from their label , renascent . that way the company ( and the band ) can make a few pennies . maybe enough to mine the crates for a second hits collection .

## pos 175. music 567.txt

margin 1.99, 78 words

> plain and simple...cage is one of the best underground rappers around.....and soon after hell 's winter drops i think he will be accepted into mainstream......this cd is cage at his craziest , the beats are hott , the rhymes are hot...buy this cd....and if you like this cd buy some of his other cds , weatherproof , night hawks , smut peddler 's : porn again , the leak brothers : water world , and hell 's winter

## pos 176. camera 51.txt

margin 1.97, 72 words

> this is a good tool , does the job well , and serves the purpose , but is a little overpriced and canon keeps changing connectors , forcing us to buy new accessories which is a wrong practice against the consumer . i give a 4 star because of canon , not because of the product . if you are willing to pay for it , it 's a good product .

## pos 177. health 575.txt

margin 1.94, 251 words

> compared to the conair 1 , 600w i have used for the past seven years or so it sounded incredibly loud and high-pitched when i first turned it on , but you may have a high-pitched blow dryer now- -compared to my old conair- -and wo n't notice a difference . it does n't have a cold air feature , which many women use regularly to either finish off their styling or to cause less damage to the hair ; or like me , in the summer when the option of switching from hot to cold is preferable . these two drawbacks , especially having only the hot at high or low setting , is why i give it four out of five , instead of five out of five star rating . pluses : price- -for $13 it ca n't be beat for the frugal shopper ; efficiency- -it blowdries my hair a bit faster than the conair did though i do n't understand the science behind that ; appearance- -it 's cute and compact ; weight- -a toddler could wield this blow-dryer with ease ; carrying ease- -small enough to fit neatly in just about any drawer or a crammed gym bag , under the sink , et cetera . i have n't had this long enough to rate how durable it is , so i hope someone who 's owned one for at least a year comes on to write , " it 's still going strong .

## pos 178. software 281.txt

margin 1.82, 136 words

> this is one program that in my opinion you get more than what you pay for i have several immaging programs that i use for several different things . this one is a delight to use and does a great job taking most of the work off the user . its a microsoft program that is very user friendly and easy to use . however you do have to be some what computer savy , ( like know where to turn on the computer kind of thing ) not like some of the 1 star comments that were made here by other folks . i would recomend it to all people that need a simple to use program . its not what you pay for something its what you do with it after you get it

## pos 179. software 644.txt

margin 1.77, 58 words

> how can doing taxes get any easier ? this is my fifth year using turbo tax and i think each year gets easier and faster . i love the way my information from the previous year is brought forward and the ability to e-file is just a click away . i ca n't imagine using any other program

## pos 180. dvd 774.txt

margin 1.68, 47 words

> about time urban works brings back " the cosby show " , but i wonder , what happened to " a different world " after the release cancellation of season 2 ? if any worker of urban works reads this , please reply ! ! ! !

## pos 181. books 498.txt

margin 1.68, 39 words

> the book is complete brand new and i got it very quickly after the order even with the free shipping service . in addition , the price is pretty good for the book with such a good condition .

## pos 182. books 472.txt

margin 1.66, 68 words

> for the first quarter of the book , i thought eugenia was ( to be polite ) a witch . she slowly became likeable . all of poor cyrus 's choices in clothing were so tacky . the story had a good blend of romance and mystery . after reading this book and all the talk of glass , i have a serious interest in collecting glass art

## pos 183. dvd 308.txt

margin 1.65, 56 words

> this is a typical ( semi slapstick ) gaiday film . it is corny , well produced , and will please anyone who enjoys the upper crust of silly comedy . the subtitles are just fine . you do not have to understand any russian to laugh at this movie . buy it , and enjoy

## pos 184. camera 40.txt

margin 1.65, 36 words

> i do not trust any batteries except canon for my canon cameras . i have found " compatible " batteries do not always charge in canon charger , and do not last as long on camera

## pos 185. dvd 654.txt

margin 1.59, 76 words

> my 11 year old saw this movie at school and would n't stop talking about it or asking for it . since we could n't find it at any store we amazoned it and there it was ! ! . part of his christmas present , he loves it . this movie is very inspiring and from what he says it makes him have hope in other people and what we can do to help others

## pos 186. books 942.txt

margin 1.57, 90 words

> having attended the fictitious " grove school " bingham describes in this book , i am confident in saying that it is all true . we are all indeed messed up and destined for the ivy league . in any event , the fictitious " fairfield academy " does also exist . i frequent the grove house of pizza and i highly recommend the chicken cutlet sub . bingham has written a fine text and i only wish he were alive to read these reviews now . hip hip hooray

## pos 187. dvd 327.txt

margin 1.57, 94 words

> i was fourteen years old when i attended the new york premier of this movie at the rivoli theater . i have the original premier book from the theater ; which is not for sale . i immediately fell in love with the beautiful ingrid bergman . so did millions of other young men . this movie did not win the award of the year ; it was overshadowed by " casablanca " ; which in my estimation , was of inferior quality , compared to for whom the bell tolls . bob richard

## pos 188. dvd 279.txt

margin 1.55, 72 words

> ...if the writers intended to have a reset-style ending all along , or if they were forced to compress and compromise their original vision . would be very interested to hear about the " original " ending envisioned ( and i do n't mean that of ep 26 ) by the writers.. . nonetheless , after viewing the rest of wr , one ca n't avoid watching these last 4 eps. .

## pos 189. camera 770.txt

margin 1.54, 39 words

> thes item is gretes item i used befoer for these prise ! ! yes is true is very clear optics , you can see in total darknes about 350 m it 's agood rand , price and qulity .

## pos 190. books 350.txt

margin 1.50, 80 words

> there is a reason this book has sold over 180 , 000 copies . it gets right to the point . it accompanies each strategy with a visual aid so you can get a mental picture in your head . further , its section on analyzing stocks and commentary on the state of financial statements and the financial market are right on the money . if your just starting out in options , this book really is a must .

## pos 191. camera 565.txt

margin 1.50, 99 words

> i was amazed on how well this battery has performed . i did make sure when i got it i did a complete charge and complete discharge and it has not let me down since . i can shoot well over two hours without needing to change to the very meek battery that came with my camcorder ( sony hdr-hc1 ) . it is thicker and sticks off the back a little bit more so you can not get your eye up to the eyepiece but i use the lcd when shooting anyway , and almost always on tripod

## pos 192. health 569.txt

margin 1.50, 69 words

> i have pergo and cannot get it too wet or the floor will bubble . the swiffer wet cloths are the perfect solution . they 're so incredibly easy to use and there are no water spills to watch out for once you 're done . i hate that i 'm consuming a product that is so disposable , but at the same time , it works so well

## pos 193. music 727.txt

margin 1.47, 21 words

> hell rell did his job , i was n't expecting anything as good as this . hell rell outdid himself .

## pos 194. camera 539.txt

margin 1.47, 52 words

> the case is beautiful leather . seems sturdy and well made . would have been more functional if the belt holder was open ended , i thought . i ordered it for my son , but found it very feminine when it arrived . i had to give it to someone else

## pos 195. health 641.txt

margin 1.42, 29 words

> love it ! love it ! love it ! it 's like a high pressure car wash . ( i do n't sound like a high pressure salesman ?

## pos 196. health 580.txt

margin 1.40, 71 words

> i have used the unit for about two weeks , with nimh rechargable batteries installed , and it performs as advertised . there is , in my opinion , a design flaw : the start / stop button acts as the power on{off function , and is easily depressed at unwanted times , e.g. putting into or removing from the case . they could / should have included an ac adapter

## pos 197. camera 545.txt

margin 1.39, 68 words

> worked like a charm in my panasonic ag-dv30 video camera ! having 5+ hours of battery life really helps when you 're on vacation and do n't want to mess with charging batteries or being " selective " in your shooting . this gives you the freedom to tape what you want and edit out the boring stuff later . worth the money and a good deal here

## pos 198. camera 741.txt

margin 1.34, 44 words

> i was a little skeptical on this product because of the cheap price and the lack of reviews . but it is just what it says it is , and i am really happy with my purchase . i would definitely buy this again

## pos 199. books 387.txt

margin 1.33, 76 words

> i enjoyed this book , but then again i always enjoy sue miller 's novels.she has this way of making me feel close to her main characters . so anyway sue , is lottie ok ? has she found contentment in life ? please write me at babz@aol.com . i am about to read & quot ; the distinguished guest&quot ; - -i heard it was really great ! i 'll let you know . bar

## pos 200. health 333.txt

margin 1.28, 124 words

> now i finally have the look and feel of a celebrity . the best product on earth period ! i 've tried all ingrown hair product 's since 1985 beleive me ive ' spent thousand of dollars , nothing comes close to it " forget about it " saliylic acid is history in my book . sorry dermatologist their is a cure . i bought 1 bottle before christmas 2006. since the new year 2007 started i 've already bought 2 bottle 's and i 'm spreading the word . do n't delay a smooth and perfect face is just a few days away . thanks to all who have complimented my slick and smooth face . j . diaz aka ( papi rico

## pos 201. books 112.txt

margin 1.20, 55 words

> having spent five years trying to establish an open-source software platform standard , in retrospect it would have been awfully nice to have had this book . if you 're going to compete with the big commercial firms you have to be comparable to or better than they are in as many areas as possible

## pos 202. health 197.txt

margin 1.16, 24 words

> that 's the only way i can rate this product . if it taste great , then it gets a high rating from me

## pos 203. software 680.txt

margin 1.15, 76 words

> i have been using printmaster platinun for several years and love it . i scrapbook constantly using all of the features . i have printed thousands of items with this program . if people have problems with the program it is because it uses alot of memory and the problem is their computer . i have gotten rid of 10 scrapbook , photo programs and only use printmaster . there is no better program . ann

## pos 204. software 771.txt

margin 1.14, 64 words

> actually , comic book creator lets you use your content in a million different ways , including reselling of your work . the only limitation is that you ca n't sell comics created around branded content- -like images from marvel , paramount , tokyopop , etc.- -because they do n't allow that . it 's all in the user agreement . check it out

## pos 205. books 528.txt

margin 1.13, 41 words

> this is a very interesting book , particularly on the early restrictionists . it gave me a new perspective on why americans restricted immigration in the early 20th century , and gave me historical insight into today 's immigration policy crisis

## pos 206. health 8.txt

margin 1.13, 54 words

> i was really enjoying my oregon scientific pedometer , i found it easy to use and accurate ; however , after 1 month it accidentally fell on the floor , and that was it , it no longer works...i will probably buy another one , but it needs to be treated with kid-gloves .

## pos 207. camera 982.txt

margin 1.04, 107 words

> i ordered this hoping that it would fit my camera and accessories and it did . i have a stylus 750 plus a pop up screen shade , an extra battery , and an extra picture card . there are two slots specifically designed to fit two picture cards on the inside cover . in the main compartment , a small slit will fit an extra battery or two plus a creit card and perhaps a bit of paper money . ( it wo n't fit much more than that , though . ) it 's compact , stylish and functional- -i 'm glad i bought it

## pos 208. health 728.txt

margin 1.02, 113 words

> i am 100% satisfied with this product and it has already earned me what i paid for . i am able to trim my front portion of hair with this on my own , where as for a complete trim , i do need my wife 's assistance . if you trim on a regular basis , ie . , when the hair 's not over grown , you will definitely find the job more easier.i recommend it to everyone who wants to save on their haircuts . the price is a good deal too if you buy from amazon , else one may perhaps ahve to wait for the thanks giving sale

## pos 209. music 826.txt

margin 1.00, 70 words

> quem não gosta de samba , bom sujeito não é , é ruim da cabeça ou doente do pé...essa letra desse samba serve para definir melhor o cd da marisa monte . quem não gostar dele , é doente da cabeça , do ouvido , do corpo , etc. É um trabalho dedicado , na medida certa para esta cantora , verdadeira diva da mpb . recomendo a todos .

## pos 210. health 47.txt

margin 0.99, 44 words

> they do n't seem small at all . i would agree that it 's like a size 3 , if you 're talking about toddler clothing , but the diaper size is different . my daughter wears 3t clothes , size 5 easy ups

## pos 211. music 472.txt

margin 0.97, 119 words

> i bought this because i thought this cd would be nice to listen to in the car while on out and about . i love that our 2 1 / 2 year old daughter who is from china loves this cd and will request it " chinese flute " please . this is just one way to keep her heritage alive and expose her to different kinds of music beyond the wiggles & lilo & stitch cd . i would have liked to have had more information on the songs like what province of china . but not having this information really does not lessen the rating of 5 stars ! our family thinks this is an excellent cd

## pos 212. software 631.txt

margin 0.97, 56 words

> i upgraded from the 2003 version with no major problems . the 2007 version is a bit easier to use and works just fine for my small business . the security , however , is not great for a mid-sized company . since my accountant fully supports the product , they are always available for support

## pos 213. health 829.txt

margin 0.96, 59 words

> i have had this model for years ! and i cut my hair with it 3-4 times a month between me & my sons . it is the best clipper set i have ever owned . most clippers i buy only last 1-2 years . i have had this one i think 5-6 years ! well worth the money

## pos 214. health 753.txt

margin 0.94, 40 words

> received my pack of 4 in 2 days with the free ship option . shop-rite sells individual box for 8.99 , so even the regular price of $32 beat that . the $10 additional promotion was icing on the cake

## pos 215. books 44.txt

margin 0.93, 49 words

> very topical . easy read . hope people in the know read this and give serious thought to the potential for something like this happening . gives good reason why border control should be taken more serious by everybody . looking forward to reading other books by mr. bell

## pos 216. music 342.txt

margin 0.92, 52 words

> so , incubus rocks no matter who you are or which of their albums is your favorite . plainly put , this album was not my favorite of theirs . it 's good . it 's really good . but if you 're expecting incubus good , you 'll be slightly disappointed

## pos 217. software 862.txt

margin 0.85, 70 words

> i upgraded to this version from money 2000. the interface looks cleaner , and the reports and budgeting options are better . i do find it a little less intuitive than the older version that i am used to . overall , i 'm happy with this product and there is room for me to get to know it better . i think it will last me for several years

## pos 218. software 405.txt

margin 0.83, 298 words

> i do n't know what other people are complaining about . i just installed vista ultimate a few days ago and i absolutely love it . no interface lag or any other lag at all . maybe the people complaining have weak or outdated hardware . those people need to turn down their settings if their not going to keep their computers on the cutting edge or at least near it . i 'm glad microsoft is n't waiting for people to catch up and are on the cutting edge . i 'd rather be the one catching up than the other way around . i have a core 2 duo e6300 overclocked to 2.5ghz , 2 gigs of ram , a geforce 7600gt and a western digital raptor 150g hd and vista ultimate works flawlessly on my computer . it 's not the best computer but it runs flawlessly , i built it myself and all the parts cost me about $850 off the net . i play world of warcraft among some other games and i have n't seen any problems yet with any games or any of the major software i use as of yet . i 've only encountered one problem and that was with my old soundblaster live ! 5.1 sound card which has discontinued support . no big deal , it was about time to get a better one anyway . vista is awesome , i love everything about it . it 's very futuristic and it is not a simple interface makeover at all like some clueless dummies proclaim . by the way , i only paid $110 for vista ultimate upgrade off ebay , check there first if you already have an existing os and want to save some dough

## pos 219. software 140.txt

margin 0.81, 48 words

> the software does a lot of great things . you can start basic and work your way up to the more difficult tasks . the system does run a bit slow and takes a long time to shut off but other than that , it is great software

## pos 220. camera 486.txt

margin 0.80, 38 words

> kodak door strains to shut with this battery . nice idea but , too bad for kodak owners . i have great success though with energizer lithium batteries . they last me a long time and fit perfectly

## pos 221. books 237.txt

margin 0.79, 65 words

> this book does what it says . it lists low or no cost campgrounds , they may not be where you want to go or fit your mega motorhome , that 's what commercial parks are for . i do n't know if it is all-inclusive but it certainly has most of the campgrounds that i know of in areas in which i am familiar

## pos 222. health 10.txt

margin 0.78, 55 words

> i bought this product because i had a borderline high reading at my doctor 's office . rather than having the hassle of going to his office and paying a cop-pay just to have it monitored , we purchased this unit . it works wonderful . very simple and gives more information than i expected

## pos 223. health 171.txt

margin 0.74, 59 words

> it is not one of the stain removers , which instantly gets rid of the stain . so when you spill over something over your t-shirt , you got to spill this tide stain remover on it as well so it does make sure that your cloth wouldnt be clogged with stain but its not an immedieate relief solution

## pos 224. music 916.txt

margin 0.73, 128 words

> i do n't see how they can compare these guys to the mars volta or coheed and cambria . i can hear the prog elements but it 's more of a rush kind of prog rock , shorter 3 minute songs compared to 12 minute epics . they are missing the one thing that would make them a true prog rock band : the songs just are n't as epic as a tmv or a c&amp ; c song . i think reviewers liken brazil to these other bands because their singer has a high pitched singing voice . this is still an amazing album that is well worth your time . go into it expecting sparta rather than the mars volta and you wo n't be disappointed

## pos 225. books 363.txt

margin 0.71, 26 words

> this book is loaded with the most recent medical findings and is organized as a referenced book , although i read it cover to cover .

## pos 226. camera 953.txt

margin 0.71, 28 words

> camera arrived earlier than i expected , and was just what i wanted . very small , but versitle . large screen . very satified with my purchase

## pos 227. dvd 53.txt

margin 0.67, 49 words

> this movie is pure fun . my whole family loved it . it 's corny and the acting leaves you feeling like it 's amatuer hour , but its fun to watch . we made popcorn and laughed our way through the whole thing . watch it and enjoy

## pos 228. software 887.txt

margin 0.61, 21 words

> very good it does what i want and more . now to get more training on doing more with this produc

## pos 229. books 752.txt

margin 0.61, 41 words

> i have read this book daily for almost 20 years . the original book , given to me in 1979 is somewhat worn and now i require a replacement . it has been and will remain my first reading each day

## pos 230. health 193.txt

margin 0.59, 22 words

> i ordered these disposable pampers for my son . they are great . i ordered them and recieved free 2 day shipping

## pos 231. camera 440.txt

margin 0.58, 29 words

> i am a photographer and i am always running down my batteries.. . i have n't found one so cheap as i did here . thank you amazon. .

## pos 232. books 691.txt

margin 0.56, 157 words

> i have many robot books and this is the best and most informative book of all . it is easy to understand and read ; i personally could n't put it down . i wish it was twice as long while still marinating the high info density.. . most authors just babble and every few pages actually tell you something ; this is not the case with this book ! the programming of a robot is everything.. . and behavior based programming is the only way to go . this book provides a very good intro into that very subject . the only complaint i have is not about the book but his robot simulation program on is website which is referred to in the text . it seems to be rather slow and over taxing for the pc , but being a java app it 's not that surprising . highly recommended to anyone building robots

## pos 233. software 677.txt

margin 0.53, 16 words

> seems to do the trick . i do n't use it personally but mom likes it

## pos 234. dvd 253.txt

margin 0.52, 80 words

> this boxed set is beautiful . everything from the box itself to the discs . i have every individual season box , and the show is the most amazing show on earth . but , i really wa n't this box set . so tell me , since it was originally a limited edition box set , why does it keep popping up here again ? is it not limited anymore ? i hope it isn't . does anyone know

## pos 235. books 517.txt

margin 0.52, 12 words

> you will never look at these birds the same again - fansinating

## pos 236. health 836.txt

margin 0.51, 55 words

> i love the idea of the glasses always being where i can find them . the only problem is they need to also be adjustable for how wide the band is . every time i look up the magnets pop apart . if they fix that , i 'd give them 5 stars ! !

## pos 237. books 951.txt

margin 0.51, 98 words

> i found this book to be very helpful . it does n't just give you the steps to do little tasks like some of the other books i looked at ; it explains the features and why you would use them , and shows you how to do things from start to finish . it also has a lot of helpful hints that are n't related to the exercises- -last night my husband installed vista business edition and could n't find a feature he wanted , and i was able to find the solution immediately in this book

## pos 238. books 781.txt

margin 0.48, 84 words

> the author not only argues for feminism , but she does so in a unique manner , and innovative approach by arguing for feminism across borders . she compares and defines literary and national borders . this book is extremely thorough on all aspects of chicana feminist writing available , by engaging historical theories as well as contemporary notions . to really grasp the experience , the author has certainly covered her basis in terms of depth , substance , truth and validity .

## pos 239. health 279.txt

margin 0.47, 105 words

> i bought this product because i had one from years ago that i use when i go to the gym but lost . it 's great at drying me off while i 'm working out and yet the towel is n't wet . i am conflicted though . i bought this one when i lost the one i already had . it 's a bit thinner and not the same deminsion as the original , but i still like it for what it does . i also like the little bag that it comes in , which i did n't have with the original one

## pos 240. camera 495.txt

margin 0.47, 69 words

> for those wishing to purchase this product , and who also want accessory filters to protect the lens , or to add special effects , although not mentioned , the size of the filter is 30mm . ( not the 37 mm mentioned at other locations , which caused me to order the wrong size which now must be returned . ) remember , 30 ( thirty ) mm

## pos 241. health 299.txt

margin 0.42, 35 words

> i 've tried several lumbar cushions from amazon and this one is the most comfortable , despite being so inexpensive . i only wish it did n't have the " wings " on the side

## pos 242. software 264.txt

margin 0.41, 65 words

> thanks for office . i bought a new h / p desktop that only had a 60-day office trial - - and literally had to pay the price . thanks to you , i 'm glad i did n't have to pay full retail . installed like a charm - - downloading sure has gotten a heck of a lot smoother . bless your hearts

## pos 243. health 805.txt

margin 0.40, 156 words

> omgosh i cannot tell you how much i love this straightener . it makes my hair so soft its like baby bottom soft or when u sand wood for a really really long time . i love it . i use it everymorning. . at night i use the wet setting to dry off my hair and then in the mroning i finish it off with the dry settting . but i also use sunsilk pink bottle 24 / 7 creme . its an absolute must-have . to the person who gave it one star. . maybe yours was a defect . im sure everyone else who has rated it so far loved it . did you straighten it section by section ? it doesnt work if you do it all at once . i recommend this straightener ! its not that expensive and also makes a great christmas gift . looks nice too . enjoy

## pos 244. software 518.txt

margin 0.39, 26 words

> easy to install and navigate . automatic incremental backups are completed randomly . sometimes they work , other times they abort . ca n't determine why

## pos 245. books 910.txt

margin 0.37, 31 words

> a great read for anyone interested in cards . i managed to pretend to my friends that i knew nothing about cards before cleaning them out after reading this book. .

## pos 246. health 955.txt

margin 0.37, 8 words

> works great , no problems after 4 months

## pos 247. dvd 545.txt

margin 0.36, 25 words

> yeah . it 's true . this movie is awesome . i think i watched it four times in the first week i had it

## pos 248. health 755.txt

margin 0.35, 26 words

> this has an average scent . i have bought other brands of reed diffusers that i like alot more . i would not buy this again

## pos 249. books 433.txt

margin 0.32, 36 words

> i bought this book in the 80 's and it did wonders for me ! it helped me to get control of " me " again.. . and i went forward with my son from there

## pos 250. dvd 280.txt

margin 0.30, 46 words

> stoners , music , girls . 80 's high school times in cali . it takes you back to when vans were cool and the girls had way to much hairspray . everytime i watch this movie im ready to hit the beach . good movie

## pos 251. health 948.txt

margin 0.29, 47 words

> i find this product to be very good for calfs & one of the best foot massagers i 've ever tried . the one drawback is that it tends to slide away from you when you are using it on your feet . i would reccommend it

## pos 252. health 100.txt

margin 0.22, 15 words

> it is really good enough for my need . i have no problems so far

## pos 253. health 103.txt

margin 0.20, 24 words

> i bought this one for my wife and she was really happy about the product . she personally like the product and really good

## pos 254. music 32.txt

margin 0.19, 12 words

> nice cd cool beats songs like welcome to atlanta pick it u

## pos 255. health 474.txt

margin 0.15, 29 words

> this is really fun to do with a friend its so spa like i love it ! but it has so many warnings im afraid to do something wrong

## pos 256. camera 951.txt

margin 0.15, 45 words

> i bought this product almost a month ago , its sleek , its reliable and has all good features a good digital camera should . worth the money for a sony camera , this camera has the usualy seen high quality for a sony product

## pos 257. software 846.txt

margin 0.15, 213 words

> i 've used the ati all-in-wonder remote with a make-shift media center solution before and it 's been sluggish , and sometimes non-responsive . not so for the firefly . quick , responsive and adaptive . i also tried the cyberlink media remote . not even suitable to prop-up a bird-food tray . you 'll find cyberlink 's tech support is positively absurd . their primary focus is to ask you tons of questions till you run out of patience , or till they find an excuse to tell you they ca n't help you . the firefly really rocks . controls several programs and tools and even provides a mouse interface incase you ca n't get things just right with the application and pre-defined buttons . if you have a pc and want media-center performance on it - i 'd recommend this guy . sadly the data is rf for this remote ; not ir . i was hoping to ' absorb ' all the functions of this remote into my harmony 688 but they do n't talk the same . i think snapstream offers another product to talk ir for the same purposes , but i 'm not there yet . still getting my sea-legs with the firefly 's abilities .

## pos 258. camera 622.txt

margin 0.14, 222 words

> i mainly use the camcorder for recording my kids . i bought this camcorder a couple of weeks ago . i had the sony hc-7 before for a couple of weeks which i returned to buy the canon camcorder . the high light performance of both camcorders are excellent . with the sony camcorder , i felt that the best color performance can be achieved by reducing the color intensity . the low light performance when recording 1080i is similar for the two camcorders but much better with canon when recording in 24p format . this is the main reason that i prefer the canon . the 24p recording is more sensitive to motion which can be a problem if recording motion . the still images from canon are lower resolution but to me they looked better than sony . this is especially true when taking flash pictures . the sony seems a little better built . the hdmi cover on canon is poorly built . i liked the controls on canon better than sony . the auto focus and automatic white balance worked better in canon than in sony . the auto white balance in sony worked poorly in indoor light . sony has supershot infrared recording and canon does not . sony has more manual controls than canon . [...

## pos 259. music 290.txt

margin 0.13, 85 words

> hot hot heat is one of the few new bands to pique my interest . their first release was decent , but " elevator " is even better . great tunes , drums and guitars - and , of course , steve bays ' yelping vocals . there 's only three songs i really do n't care for - " pickin ' it up " , " soldier in a box " and " shame on you " . looking forward to the next cd

## pos 260. software 969.txt

margin 0.12, 599 words

> the very early years of optical character recognition ( ocr ) were quite the challenge . programs cost thousands of dollars , as did the scanners . none of them worked very well . it would take longer to " clean up " the document after scanning than it would for the secretary to have typed it in from scratch . all of that has of course now changed , and omnipage 15 pro takes the art and craft to a new level . i have been using the omnipage product for the last seven years or so . i use it my law office ( along with a number of the other scansoft , now nuance , suite of products ) on a daily basis , many times through out the day . we use it to chew up everything from court pleadings , to 100 page plus contracts , to real estate property descriptions , which must be accurate down to the comma and semicolon . our needs are fairly simple - get the text into the word processor so we can respond on behalf of our client as fast as possible . op15pro offers a significant performance increase over its predecessor version 14. it is faster ( very much faster ) and more accurate . work flow is straight forward . there is of course the ability to manually set or readjust recognition zones , recognize and format as spreadsheets . this new version easily handles text in relation to graphic elements and does a good job of keeping them all together in their right places . like most everything else , and especially with computers and software , nothing is perfect and there are times that op15 misses a mark . it is however , for the most part , very accurate and efficient , but remember , the old rule of " garbage in equals garbage out " still applies . we have recently started taking pen scanner images of documents in the books at the local registries of deeds . these are 200 dpi scans of documents that themselves are old photocopies of text placed on paper with ibm selectrics or worse . in other words , stuff from the dark ages of the 1970 's and before . we were pleasantly surprised at how well op15pro performed . with these very old images there is a need to clean them up , but nowhere near what it used to be . i will comment only briefly about the company 's tech support . there has always been enough information provided to get the software up and running . the key , of course , is to read and follow the directions . a task that is sometimes difficult in this " i want it now world . " the one " free call " is not just for installation problems , but can come months or even years after the product is purchased . i have also found on occasion that tech support will often answer the simple and obvious questions without first asking for the credit card . solving technical problems can be frustrating and time consuming . considering what the software is attempting to do , there fact that it accomplishes it at all seems at times to be just short of a miracle . lastly , the company 's knowledge base is filled problem solving information . there is also a tremendously large user base that supports the product through usenet and other forums . norm michaels , esq

## pos 261. software 444.txt

margin 0.11, 51 words

> not a bad typing program for kids . it keeps my kids interested for about 15-20 minutes a day . they complain about all the practice pages for the games...but , hey ! it 's a typing instructor ! you gotta pratice ! once they start playing , they have fun

## pos 262. camera 616.txt

margin 0.09, 56 words

> solid construction , good optics , nice sound . as mentioned by others , the output for the usb transfer is found in the handycam console and not the camera itself...a minor annoyance . all in all , this is a good camera that is touch pricy but you do get what you pay for... .

## pos 263. books 196.txt

margin 0.04, 57 words

> first book i 've read from sandra brown and it was really great . it was a page turner from beginning to end . i found the book interesting and easy reading . a well written mystery suspense that keeps you guessing until the very end . will not be the last sandra brown novel for me

## pos 264. books 577.txt

margin 0.04, 98 words

> a wonderful book . you will meet many charming cats on your jounrey here that will stay with you forever . although this book is only 150 pages , it took me a long time to read it . while many things made me smile or laugh out loud , far too many things made me cry and i had to stop reading and set it aside for awhile . i often wondered if i could even finish it , but i am glad that i did . it is a book that truly touches the heart .

## pos 265. dvd 866.txt

margin 0.04, 83 words

> stay tuned is about roy and helen knable . roy gets a new tv from mr. spike . the new tv has 666 channels that 's filled with shows such as " facts of life support " , " 30 something to life " , " sadistic hidden videoes " , " murder , she likes " and commerical parodies . roy and helen has 24 hours to live through hell 's channels . will they make it out alive ? stay tuned

## pos 266. dvd 67.txt

margin 0.03, 54 words

> i thought the movie was great ! nothing like the gospel to me ! ! do n't compare ! billoah is sexy baby ! he played zulu ! ! ( pretty eyes ) the movie was very funny also and taught a lesson in love ! ! ! 5 star movie ! ! ****

# True neg, predicted pos (198 reviews)

## neg 1. books 145.txt

margin 43.51, 5965 words

> ` ` people say again and again that philosophy does n't really progress ,  that we arestill occupied with the same philosophical problems as were thegreeks.but the people who say this don't  understand why ishas to be so. it is becauseour language has remained the same and keeps seducing us into asking the same questions. as longas there continues to be a verb ' to be'  that looks as if it functions in the same way as ' to eat ' and ' to drink ' , as long as we stillhavethe adjectives ' identical ' , ' true ' , ' false ' ,  ' possible ' , as long as we continueto talk of a river of time , of an expanseof space , etc. , etc. , people will keepstumbling over the samepuzzling difficulties and find themselves staring atsomethingwhich no explanation seems capable of clearing up.and what's more , this satisfies a longing for the transcendent , because , insofar as peoplethinkthey can see ` the limits of human understanding ' ,  theybelieve of course thatthey can see beyond these . ` ` ' ' philosophy is a battle against the bewitchment of ourintelligence by means of language ` ` ` ` ambition is the death of thought'''  these three quotes are from ludwig wittgenstein who redefined philosophysome70 years ago ( but most people have yet to find this out ) .dennett , though he has been a philosopher for some40 years , is one them. it is also curious that both he and his prime antagonist , john searle , studied under famous wittgensteinians ( searle with john austin , dennett with gilbert ryle ) but searle got the point and dennett did not . dennett is a hard determinist ( though he trys to sneak reality in the back door ) , and perhaps this is due to ryle , whose famous book ' the concept of mind ' ( 1949 ) continues to be reprinted . that book did a great job of exorcising the ghost but it left the machine . dennett enjoys making the mistakes wittgenstein , ryle ( andmany others since ) have exposed in detail . byaccident , just before this book , i had read ' 'the minds i' ' , which dennett coauthored withdouglas hofstadter in 1981. they made some bad mistakes ( see my review ) , and saddest of all , they reprinted twofamous articles that pointed the wayout of the mess- --nagel's  ` what is like to be a bat ? ` and an early version of john searle's  chinese room argument explaining why computers do n't think. nagel pointed out that we do noteven know how to recognize whata concept of a bat 's mind would be like. searle similarly explained how we lack a way to conceptualize thinking and how itdiffersfrom what a computer does ( eg , it can translate chinese without understanding it ) . likewise , we lack a clear test for recognizing what countsas good vs bad- -or just intelligible- - for many philosophical and scientific concepts. our use of the words consciousness , choice , freedom , intention , particle ,  thinking ,  determines , wave , cause , happened , event ( and so on endlessly )  are rarely a source of confusion but as soon as we leave normal life and enter philosophy ( and anydiscussion detached from the environment in which language evolved )  chaos reigns. wittgenstein was the first to understand why and to point out how to avoid this . unfortunately , he died inhis prime , his works are composed almost entirely of a series of examples of how the mind ( language ) worksand he never wroteany popular books , so understanding of his work is restricted to a very few . searle is one of the world 's leadingphilosophers and has written manyextremely clear and highly regarded articles and books , some of which have pointed out the glaring defects in dennett's work.his review ` ` consciousness explained away' ' of dennetts 1991 book ` ' consciousness explained''  and his book ''the mystery of consciousness' ' are very well known , and show , in a way that isamazingly clear for philosophical writing , why neither dennett ( nor any of the hundreds of philosophersandscientists who have written on this topic ) havecome closetoexplaining the hard problem- -ie , how do you conceptualizeconsciousness.many suspect we will never be able to conceptualizeany of the reallyimportant things , but it isclear that we are nowhere near it now. dennett has mostly ignored his critics but has favored searle with vituperative personal attacks.searle has been accused by dennett and others of being out to destroy cognitive psychology which is quite funny as modern philosophy is ( mostly ) a branch of cognitive psychology and searle has made it very clear for 30 years that we are a good example of a biological machine that is conscious , thinks , etc , . he just points out that we do n't have any idea how this happens . searle characterizes as ' 'intellectualpathology' ' , the views ofdennett andall those who denythe existence of thevery phenomena they setout to explain. dennett repeats his mistakes here andleaves his reply to his critics to the penultimate page of the book , where we are told that they areall mistaken and it is a waste of spaceto show how !  unsurprisingly , there isnot one reference towittgenstein or searle in theentire book.there arehowever , many references to other old schoolphilosophers who are as confusedas he is. like most people , it does not cross his mindthatthe very inference engineshe thinks with are forcinghim to cometo certainconclusions and that these will oftenbe quite unconnectedwith or wrong about the way things are in the world . they are a jumble of evolutionary curiositieswhich do various tasks in organizing behavior that were useful for survivalhundreds of thousands of years ago.wittgenstein was a pioneerin doingthought experiments in cognitive psychologyand beganto elucidate the nature of these engines and the subtletiesof language in the 30 's , and thus he made the sorts of commentsthat this review begins with. dennett says ( p98 ) that his view is compatibilism , ie , that free will ( whichi hopewe can equate with choice ) is compatible with determinism ( ie , that ''there is at any instant exactly one physically possible future'' --p25 ) . he wants to show that determinism is not the same as inevitablity. however , the whole book is smoke and mirrors by means of which choice , in the sense we normally understand it , disappears and we are left with ` ` choice ` ` , which is something we cannot choose. naturally , this echoes the fate of consiousness in his earlier book ` ` consciousness explained ` ` . it is remarkable that , at a time when we are just beginning to reach the point where we might be able to understand the basics of how a single neuron works ( or how an atom works for that matter ) , that anyone should think they can make the leap to understanding the whole brain and to explain its most complex phenomena. please recall the last sentence of wittgenstein from the opening quote : ' ' and what's more , this satisfies a longing for thetranscendent , because , insofar aspeoplethinkthey can see ` the limits of human understanding ' , theybelieve of course thatthey can see beyond these . ` ` the relation between language ,  thought and reality is extraordinarily complex and everyone gets lost. if one is very , very careful , some understanding is possible , but dennett throws caution to the winds and we are dragged into the quicksand. there are at least 3 different topics here ( evolution of our brain , choice and morality ) and dennett tries vainly to weld them together into a coherent account of how freedom evolves from the deterministic crashing of atoms. there is , however , no compelling reason to accept that bouncing atoms ( or his favorite example , the game of life running on a computer ) are isomorphic with reality. he knows that quantum indeterminacy ( or the uncertainty principle ) is a major obstacle to determinism however defined ( and has been taken by many as an escape to freedom ) but dismisses it due to the fact that such events are too rare to bother with. by extension ,  its unlikely that any such event will happen now or even in our whole lifetime in our brain , so we appear to be stuck with a determined brain ( whatever that may be ) . however , the universe is a big place and its been around a long time ( perhaps forever ) and if even one such quantum effect occurs it would seem to throw the whole universe into an indeterminate state. the notion ' 'there is at any instant exactly one physically possible future' ' cannot be true if at any instant a quantum indeterminacy can occur- -in this case there would seem to be infinitely many possible futures. this recalls one of the escapes from the contradictions of physics- -each instant our universe is branching into infinitely many universes . he correctly rejects the idea that quantum indeterminacy gives us the answer to how we can have choice . this obvious idea has been suggested by many but the problem is that nobody has any idea how to specify an exact sequence of steps which starts with the equations of physics and ends up with the phenomena of consciousness ( or any other emergent phenomenon ) . if so , they will definitely win at least one nobel prize , for not only will they have explained consciousness , they will have explained the universal phenomenon of emergence ( how higher order properties emerge from lower ones ) . so , they would have to solve the ' easy ' problem ( to determine the exact state of the brain corresponding to some mental state and preferably specify the exact position of all the atoms in the brain over time-ignoring uncertainty ) and the ' hard ' one ( what exactly correlates with or produces consciousness or choice etc ? ) . and while they are at it how about also doing the impossible- -an exact and full solution to the quantum field equations for a brain . it is very well known that these equations are uncomputable , even for one atom or a vacuum , as it would require an infinite amount of computer time . but infinite will do for one atom so maybe a brain will take no longer . he starts off on the first page appealing to the laws of physics for protection against fantastic notions such as immaterial souls , but physics is made of notions just as fantastic ( uncertainty ,  entanglement , wave / particle duality , schrodinger 's dead / alivecat etc ) and as feynmann said many times ` ` nobody understandsphysics ! ' ' many think nobody ever will . on pg 2 he says our values have little to do with the goals of our cells and on pg 2 to3 that our personality differences are due to how our ' 'robotic teams are put togther , over a lifetime of growth and experience . ` `  this is a bald dismissal of human nature , of the abundant evidence that our differences are to a large extent programmed into our genes and fixed in early childhood , and is typical of his constant confused wandering back and forth between determinism and environmentalism . on page 9 he notes that free will is a problem and our attitudes to it make a difference , but for whom ?  nobody but philosophers. we make choices. what 's the problem ?  one has to step outside life to experience a problem and then everything becomes a problem. what are consciousness ,  pain ,  yellow , intention , matter , quarks , gravity etc. ?  i doubt that anyone has ever experienced a fundamental change in their interactions with people or their decision making processes due to their thinking about choice. this shows that there is something strange about such questions. wittgenstein would probably say that the language games are different. there are games for language connected with the cognitive templates for decisions or seeing colors etc , and thinking philosophically is operating them in decoupled mode. decoupled modes permit thinking about the past , planning for the future ,  guessing the mental states of others , etc , but if one takes the results in the wrong way and starts to think ` ' john will try to steal my wallet' ' , rather than just imagining that john might do it , confusion enters and those who cannot turn off the decoupled mode or distinguish it from coupled mode , enter the realm of pathology. some aspects of schizophrenia and other mental illness might be seen this way- -they lose control of which mode they are in , eg , notbeing able to see the difference between the motives people have and the motives they might have . one can then see much of the philosophizing people do as operating in these decoupled modes but failing to be able to keep in front of them the differences from the normal mode. normal mode- -eg , what is that lion doing- - was undoubtedly the first one evolved and decoupled modes- -what did that lion do last time or what does he intend to do next- -evolved later. this was probably never a problem for animals- -any animal that spent too much time worrying about what might happen would not be very successful contributing to the gene pool. it is interesting to speculate that only when humans developed culture and began degeneratinggenetically , could large numbers of people survive with genes that led them to spend alot of time in decoupled modes. hence , we have philosophy and this book , which is mostly about running the decision templates in decoupled mode where there are no real consequencesexcept earning royalties for putting the results in a book for other people to use to run their engines in decoupled mode . ' let us alter wittgenstein 's quote to read : ' 'as longas there continues to be a verb ' to decide'  that looks as if it functions in the same way as ' to eat ' and ' to drink ' , as long as we continueto talk of freedom of action , of saying i wish i had done otherwise , etc. , etc. , people will keepstumbling over the samepuzzling difficulties andfind themselves staring atsomethingwhich no explanation seems capable of clearing up. ' ' as withmost philosophy books , nearly every page ,  often every paragraph , changes from one type of language game to another without noticing that now one would have to be joking or dreaming or acting in a play or reciting a story , etc , and not actually intending anything nor describing an actual situation in the world. on page 10 he says we count on free will for the whole way of thinking about our lives , like we count on food and water , but who ever , outside philosophy , standing in front of lunch counter full of food , ever thinks how fine it is that they have free will so they can pick coke instead of mineral water ?  even if i want to be a serious compatibilist and try thinking this in decoupled mode , i have to exit and enter nondecoupled mode to make the actual choice. only then can i go back to decoupled mode to wonder what might have happened if i had not had the ability to make a real choice. wittgenstein noted how pretend games are parasitic on real ones ( this is not a trivial observation ! ) . the ability to engage in very complex decoupled scenarios is already evident in 4 year old children. so i would say that normally , nobody counts on having choice ,  but rather we just choose. on the same page he shows again that he does not grasp cognitive basics. he says we learn to conduct our lives in the conceptual atmosphere of choice ,  and that ` ' it appears to be a stable and ahistorical construct , as eternal and unchanging as arithmetic , but it is not . ' ' and on page 13- - ''it is an evolved creation of human activity and beliefs'' . the whole thrust of cognitive psychology is that we do not learn the basics of planning , deciding , promising ,  resenting ,  etc , but that these are built-in functions of the inference engines that work automatically and unconsciously and start running in very early childhood. there is no evidence that they change as we grow , or are in any way subject to our beliefs , only that they mature just as our body does. on pg 14 he suggests its probable that our having free will depends on our believing we have it ! do we believe we see an apple , feel a pain , are happy ?  the language game of belief is very different from that of knowing. we can believe we have a dollar in our pocket but if we take it out and look at it we ca n't meaningfully then say that we still believe it ( except as a joke etc. ) . the inference engine can run in decoupled ( belief )  mode so we can imagine havingchoices or making them , but in life we just make them and it is only in very odd situations we can say that we believe we made a choice. but dennett is saying thisis the universal case. if making a choice had any dependence on belief than so would everything everything else- -consciousness ,  seeing , thinking , etc. if we take this seriously ( and he says ' the serious problems of free will ' ) then we are getting into trouble and if we actually try to apply it to life , then madness is minutes away . . on page 65 et seq . , he discusses causation , intention and the ` informal predicates ' that we use to describe atoms etc , but cognitive resarch has shown that we describe all objects with a limited number of ontological categories which we analyse with our intuitive physics modules and that when agents ( ie animals or people or things like them- -ie , ghosts or gods ) are involved we use our concepts ( engines ) for agency , intuitive psychology , social minds , etc to decide how to behave. there is almost certainly no causation module but rather it will involve all of these and other inference engines , depending on the precise situation . discussing possibility and necessity is much easier if one talks in terms of the output of our modules for intuitive physics ,  agency , ontological categories etc. of course there is no mention here of wittgenstein 's many incisive comments on causation , intention , deciding , nor of searle 's now classic works on intention and social reality . he spends much time on ainslie 's book ' breakdown of will ' , in which is discussed the hyperbolic discounting faculties ( ie , inference engines ) by which we evaluate probable outcomes . hemakes much of the excellent work of robert frank on altruism , emotion and economics , but the book he cites was 15 years old when this book was published . it was bingham 's idea , amplified by frank and by boyd and richardson ( 1992 ) that cooperation was greatly stimulated by the evolution of means for punishing cheaters. he suggests these as examples of darwinian approaches that areobligatory and promising. indeed they are , and in fact they are standard parts of economic , evolutionary and cognitive theory , but unfortunately ,  he makes little reference to the other work in these fields . all that work tends to show that people do not choose but their brains choose for them . he does not establish any convincing connection between this work and the general problem of choice. onpg 216 he says that making oneself so that one could not have done otherwise is a key innovation in the evolutionary ascent to free will , and that we can only be free if we learn how to render ourselves insensitive to opportunities . but where this ability resides is not revealed for several chapters !  dennett has a penchant for hiding his ideas in a massive amount of rather irrelevant text. again , he gets things backwards , as there is a vast body of very good evidence from biology and psychology that we are get the feelings that we should behave in some way from our inference engines and these are not provided by some part of our conscious self , but by the automatic and unconscious operation of the engines. as he notes , hundreds of experiments with the prisoner 's dilemma and related protocols have shown how easy it is to manipulate people 's choices and that their calculations are not conscious and deliberate at all. when the situation is manipulated to make them conscious , they are much slower and less reliable . so , there has been constant pressure of natural selection to make the engines fast and automatic and inacessible to deliberate thought . dennett says ` we make ourselves ' so that we could not do otherwise and that this is the basis of morality and choice. the evidence would seem to be exactly the opposite. our inference engines give us basic moral intuitions and we generally act in accord with the results. if we or others do not we feel guilt , outrage , resentment etc ,  then cheater genes will invade the population and this is one of the main theories as to how a good part of morality evolved.our genes make us so we ca n't ( mostly ) do otherwise , not our will or whatever dennett thinks can do it . we can often choose to do otherwise but our own intuitions and the knowledge of social disapproval usually serve to limit our choices. these intuitions evolved in small groups between 50 , 000 and some millions of years ago. in the modern world the intuitions are often not to our advantage and the social controls weak. this is a prime reasonfor the chaos in the world . on pg 225 he finally sneaks in a definition of free will as ' 'a complicated snarl of mechanistic causes that look likedecision making ( from certain angles ) ' ' . he claims that thisplays all the valuable roles of free will but lacks some ( unspecified )  properties possessed by traditional free will. the smoke is thick but i am pretty sure one of those unspecified properties is what we understand aschoice. he insists ( top pg 226 ) that his naturalistic account of decision making leaves plenty of room for moral responsibility , but making ourselves so we could n't do otherwise does not seem to describe the way we actually function ,  nor does it seem to leave any room for morality , as that would seem to consist precisely in being able to do otherwise . he does not propose any test for deciding if a choice is voluntary or forced and i doubt he could do so. normally if someone asks us to move our hand , we know what counts as having a choice ,  but , typical of philosophers ,  i expect that regardless of whether it moves or not he will count both as evidence for his position . at this point he also starts his discussion of libet 's well known work on conscious attention which is the only part of the book that i felt was worth my time . on page 253 et seq . , he sneaks in his definition of conscious will- -the ' 'brains user illusion of itself'' ' which has as one of its main roles providing ' 'me with the means of interfacing with myself at other times ` ` . and ` ` illusory or not , conscious will is the persons guide to his or her own moral responsibility for action . ` `  he says the trick we need is to see that ` ` i ` '  control what is happening inside the ' 'simplification barrier'' ... ' 'where decision making happens'' . ` ` mental events' ' become conscious by ' 'entering into memory'' . ' 'the process of self description... is what we are'' . the crucial thing is that choice is possible because the self is distributed over space ( the brain ) and time ( memories ) . he realizes this is going to leave many incredulous ( everyone who can follow this and really understands ! ) . ' 'i know that many people find it hard to graspthis idea or take it seriously. it seems to them to be a trickwith mirrors ,  some kind of verbal slight of hand that whisksconsciousness , and the real self , out of the picture just when it was about to be introduced . ''  many will say he took the words out of their mouth , but i would say it 's incoherent and thateverythingwe know about consciousness and the whole universe ( making the obvious extensions of such claims ) was gone long beforewegot this far. on pg 259 he says that culture has made us rational animals ! this is a stunning denial of human nature ( ie , genetics and evolution ) coming from the person who wrote ' darwin 's dangerous idea' ' ! presumably he is talking about his idea that it is memories spread over space ( the brain and other people ) and time that give us choices and morals and consciousness ( line 6 from bottom ) . he says consciousness is a user-interface but it is never made clear who or where the user is and how it interfaces with the brain ( you will have to suffer through ' consciousness explained to find that there is no answer there either ) . though he makes many references to evolutionary and cognitive psychology , he seldom uses any of the terminology that has been current for decades ( social mind , intuitive psychology , coalitional intuitions etc ) and clearly is not familiar with most of the concepts . if he means that we got the fine details of morality from culture , thats ok , but this is the icing on the cake and the cake was baked by the genes . we are also told here that r&d ( by which he means evolution here , but other things elsewhere ) has given us the self and that language creates new kind of consciousness and morality . i am sure that he will get little agreement on this . it seems quite clear that consciousness and the basics of morality evolved in primates ( and earlier ) long before spoken language ( though it is a very deep topic as to how language evolved from extant capacities in the brain ) . he continues ` ` morality memes arose by accident some tens of thousands of years ago ` ` which would be ok if he meant the icing on the cake but he clearly means the cake ! and then he says the point of morality is not the survival of our genes , which is an amazing ( and totally incorrect ) thing to say , even if he was only referring to memes . on pg 260 he claims that because we do not comprehend our ' 'bland dispositions to cooperate' ' ,  they mean nothing to us , but it is the operation of our templates that is everything to us. there is ample evidence that if one of them is damaged a person cannot function properly as a social being ( eg , autism ) . i would say it is the operation of the templates for intuitive psychology etc which lead dennett to the counterintuitive views that we do not have consciousness and choice in the way we think . he also says here that it was one of the major evolutionary transitions when we were able to change our views and reflect on reasons for them . this again reflects his lack of understanding of evolutionary psychology . i know of no evidence that the basic moral intuitions , like all the templates , are accessible to consciousness . we may decide our cheating was justifiable , or forgive someone else 's cheating , but we still know it was cheating ( ie , we cannot change the engine ) . i suspect my ancestors a million years ago had the same feelings in the same situation but what has happened is that there are lots of other things that may be taken as relevant and that sometimes these will lead me to act contrary to my feelings . another issue is that as culture developed , one had to make many important or ' moral type ` decisions for which the engines were not evolved to give a clear answer . on pg 267 he says that we now replace our ` free floating rationales ' ( probably corresponding to what cognitive psychologists call our templates or inference engines ) with reflection and mutual persuasion . and on pg 286 he says that it is a child 's upbringing - -demanding and giving reasons- - that affects moral reasoning . again , he just has no grasp of what has happened in the last 30 years of research- -the templates do not change with reflection or upbringing . we are then told again that consciousness makes moral issues available over time to the self , which takes responsibility . it is not any more coherent or credible with repetition . on pg 289 he has a chapter summary which repeats the mistaken notions that it is culture that makes it possible to reflect and that choice depends on education ( memory ) and sharing . it 's clear that it is not culture but the inherited cognitive structures that make it possible to reflect and to choose and that culture determines the acceptable actions and their rewards or punishments . on pg 303 he discusses the classic philosophical barrier between ' ought'and ' is ' , unaware that our templates solved that problem long ago- -ie , they tell us how to feel about situations regarding other people . he also seems to be unaware that there are hundreds of cultural universals implanted in our genes ( eg see ' the blank slate ' ) . he often starts into what looks like its going to be a good discussion of some issue in evolutionary psychology , but invariably wanders off into philosophical arcana and winds up with more confusion . this happens on pg 261 where he states that concepts like ' praiseworthy ' were shaped over millennia by culture , while most would say the basis for such concepts is in the genes and each culture only detetermines the details of acceptable reactions to the intuitions its members get from their innate mechanisms . on pg 262 he tries to explain how an ess ( evolutionarily stable strategy ) can produce morality . his idea here is that genetic ` r&d ` produces dim understandings of morals and then culture ( memetics ) produces variations and clarifications . i would say that we all know , and much research has made clear , that we commonly get very clear results from our inference engines and only dimly understand in special cases . culture merely decides what we can do about our feelings . the last part of the book is mostly concerned with moral culpability. he refers to the legal classic by hart and honore , which i started reading 30 years ago since it 's authors were deeply influenced by wittgenstein. dennett tells us that we have control over our own morality and that thinking about morality will improve us. but , there seems no justification whatever for this view in this book . there is nothing at all here to help anyone escape from the dictates of the monkey mind. it is a defensible point of view that those who manage this do so by traveling a spiritual path that has no connection with philosophy - and there is not a hint of spirituality in this entire book- -another telling point considering that many mystics have fascinating things to say about the functioning of the mind. i find more wisdom about how to be free and moral in any of osho 's 200 books than anywhere in philosophy . one rarely finds spiritually and morally advanced people teaching at universities. there is no sign here , nor in anything he has done , that dennett is morally superior. after 40 years of thinking about morality he launches personal attacks on his critics or arrogantly dismisses them . it seems clear that , like all of us , he is trapped in the limits of his inference engines . so , how much opportunity is there to improve our morality ?  it seems clear ( eg , see pinker 's ` the blank slate ` ) that most of our behaviour is genetic and the rest due to unknown factors in our environment , in spite of the vigorous efforts of parents and religions and political parties . on average , maybe 5% of the variation in moral behavior ( variations are the only thing we can study ) is due to our own efforts. the moral choices that matter most today are those affecting the fate of the world. but our moral templates were not evolved to deal with overpopulation and the greenhouse effect . how remarkable it would be if just one of the hundreds of millions of educated people in the world managed to figure out what consiousness or choice or any mental phenomenon really is . and if one did , we would expect them to be a scientist at the cutting edge of research using some exotic fmri equipment and the latest parallel processing neural networked fuzzy logic computer etc. but a philosopher or physicist just sitting there thinking , coming up with the solution to the greatest puzzle there is ! and then writing a whole book about it without checking with the sceptics first . to return to the quote at the beginning- - 'ambition is the death of thought' . indeed- -though clearly wittgenstein was thinking of interesting thoughts

## neg 2. books 318.txt

margin 36.14, 437 words

> i generally like elmore leonard , this is the twelfth book of his i 've read , ranging from his detroit crime capers , to his l.a.-set chili palmer stuff , to some of his westerns . other than the terrible " be cool " , this is probably my least favorite of his books so far . set in the years between the end of world war i and 1934 , the story follows carlos " carl " webster from boyhood to manhood as the son of a wealthy pecan farmer rises to became a hotshot u.s. marshall . the story takes place in the dusty midwest , mainly around tulsa and oklahoma city , as carl faces off with various wanna-be desperados seeking to make a name for themselves . carl is a somewhat vain , cocky lawman , with a keen sense of what kind of quote will get him in the papers . his main foe is the son of a wealthy oil man , a no account young man who has everything he needs , but whose selfish nature and appetite for stirring things up leads him into carl 's path . mixed into this are kinds of period details , from prohibition to will rogers shows to klansmen vigilantes to " true detective " writers to striking miners to mentions of various real-life bank robbers pretty boy floyd , john dillinger , and bonnie and clyde barrow . despite all this background detail , the story itself failed to engage me . there are none of the clever twists and turns that characterize leonard 's best work . there 's a good guy , a bad guy , and an inextricable outcome whose resolution is surprisingly undramatic . in fact , about halfway through the book i realized that the " real story " was n't going to kick in - - i was in it ! and unlike many leonard books , the supporting cast of characters is n't particularly memorable . even leonard 's trademark strong dialogue is mostly missing , subsumed by his attempt to stick to period speech . ultimately , one gets the feeling that leonard was most interested in capturing the vibe of the period , and perhaps did n't spend nearly the same amount of effort on the actual story . that said , the depression and its effects are surprisingly absent from the story , given the time and place . all in all , unless you 're really really into the whole ' 30s gangster thing , not worth the time .

## neg 3. music 461.txt

margin 32.60, 503 words

> in the classic and disturbing 1972 movie deliverance , lewis ( burt reynolds ) gives this ominous warning to ed ( jon voigt ) : " machines are going to fail . systems are going to fail . then.. . survival . " what , i wonder , will richard d . james ( a.k.a. aphex twin , a.k.a. afx ) do when the machines fail ? it 's been nearly five years since his underappreciated album drukqs , where we got a tantalizing possible answer to this question : the plaintive , lovely , satie-esque acoustic keyboard nocturnes intermingled among the abstract , frantic electronic soundscapes throughout its sprawling duration . [another intriguing solution was proposed on the album acoustica : alarm will sound performs aphex twin...] chosen lords , rdj 's first proper cd release since then , is actually a collection of various tracks from his " analord series " of overpriced , elaborately packaged 12-inch vinyl singles that he 's been cranking out over the last year or so . those who were put off by the excesses and overt eccentricity of drukqs may hail these cryptically titled , drum-machine laden compositions as a " return to greatness . " indeed , afx is certainly reviving a more compact , accessible ( for him ) , and straightforward style here , with comparatively regular ( though not quite danceable ) rhythms and those comforting underlying simple synthesizer melodies . i have to say , though , that there 's a disappointing and somewhat melancholy sense here of a great musical mind spinning its wheels . by returning to such familiar ground he seems to be setting up systems and letting them run their course in an almost cynical way , without any of the maniacal glee that was once part of his singular musical personality on unforgettable releases like come to daddy , windowlicker , the richard d . james album , and , yes - - drukqs . notably lacking are the voices that once regularly appeared in his productions - - true , they were usually rather unsettling , distorted , and manipulated voices , but at least they added some welcome humanity . also missing are those rare but beautiful moments of repose ( ballads ? ) such as " flim , " " nannou " and the striking piano interludes on drukqs . in the end , chosen lords , while an undeniably interesting and expertly produced collection of electronic music , is nonetheless a sterile , static , joyless affair . if it inspires any emotion at all , it will probably be pity and sadness as you listen to a possible musical genius coasting along without exploring any new directions for the first time in his otherwise remarkable career . yes , i 'm afraid the machines have failed richard d . james , and i sincerely hope he can survive in this cold and remote musical wilderness of his own creation. .

## neg 4. camera 458.txt

margin 30.99, 425 words

> this s80 used to be the only wide angle compact point and shoot digital camera on the market . it has now been discontinued i 'm told . but , we 're in luck ! there are three other digital point and shoot cameras with a real 28mm wide angle lens ! these are : 1 ) the panasonic dmc-fx01 for $250 , and the 2 ) canon powershot sd800 is for $400. and , 3 ) the kodak easyshare v570 for about $350. so , you ask , " who needs a 28mm lens ? " you do ! most people concern themselves with how long is their telephoto lens . but , most people who " know " know that it is the wide angle lens that is most important- --most of the " best shots " are made with a wide angle lens . for example , you 're in europe and you are trying to " get a shot " of that cathedral of notre dame over there . you need a wide angle lens . you are in the california poppy fields and you want to get the expanse of the golden-yellow poppy flowers with the huge blue sky filled with white clouds above- --you need a wide angle lens . you are sitting at thanksgiving dinner and you want to take a photo from the foot of the table with everyone sitting on the left and right- --you need a wide angle lens . you are in the garden of the california mission and you want to take a photo of the entire garden surrounded by the mission walls- --you need a wide angle lens . it 's christmas day and you want a photo of the entire group of visitors in front of the christmas tree- --you need a wide angle lens . this is where the 28mm lens on this camera comes in ! so , you need this camera ! otherwise you 'll be cutting off heads and leaving aunt sylvia out of the " christmas group photo " this year- --and she 'll disinherit you and as a result of not having a wide angle lens you 'll live a life of poverty and misery everafter ! :o ) if you agree or disagree or know of any other digital point and shoot camera that has a wide angle lens please write , email:boland7214@aol . here 's one more wide angle candidate : kodak easyshare v705 7.1mp digital camera with 5x ultra-wide-angle dual-lens optical zoom

## neg 5. books 7.txt

margin 29.92, 342 words

> noam chomsky has thrived greatly in this great country of his , yours , and mine - the united states of america . he has made millions of dollars teaching , lecturing , selling his books , and investing . his world-wide fame in psycholinguistics is well-deserved . his infamy is merited for his lack of loyalty to his own jewish ethnicity and the u.s. , in spite of the fruits he has received by being a citizen of the united states . he has repaid this country in bile with his incredibly biased analysis of american foreign policy . he goes way beyond a balanced multiculturism , when he always ranks the u.s. and israel as foremost among the terrorist forces in the world now , and even in history . his distrust of any authority , benign or otherwise , is reflected in his dogmatic and unexamined support of the " underdog , " even if that underdog is a suicide bomber or a major terrorist organization such as al queda or hezbollah . yet since 1955 , hypocrite chomsky has worked for the " overdog " massachusetts institute of technology , which has actively and enthusiastically participated in the development of weapons of war and mass destruction , and continues to this very day . chomsky trumps his own potential for gifted analytic objectivity with his simple hatred of the united states and the jewish state . if he were not so attached to the freedom of making money , earning the adulation of the american left , and freedom to express himself , he might be able to give more direct and personal support for our enemies and his friends by taking up residence in north korea , iran , or syria . let us hope he retires outside of our homeland that he hates so much , the united states of america . god bless america , which will continue to give chomsky the right to speak , teach , and make lots of money . raybo

## neg 6. books 454.txt

margin 29.36, 1807 words

> in 1980 michael weiner saw the publication of weiner 's herbal : the guide to herb medicine , which states the medical benefits of marijuana [7]. however he recently stated that the chemicals in marijuana make it too dangerous to be used as medicine . on his program , he strongly cautions against the recreational use of marijuana , occasionally devoting his show to " marijuana horror stories " and its claimed potential to ruin lives . he has authored a number of other books on various herbal medicine topics under this name . more recently , savage 's books are political in nature and published by wnd books , a partnership between the conservative website worldnetdaily and thomas nelson , a publisher of christian books . in january 2003 he published the savage nation : saving america from the liberal assault on our borders , language and culture , his first book under the pseudonym michael savage . the book quickly reached the top of the new york times bestseller list earning savage , as noted above , a commentary show on msnbc . the controversial book directs attacks at " media bias " , the " dominating culture of ' she-ocracy ' " , gays , and liberals . critics have faulted savage for making a number of assertions in the book that he often fails to substantiate with facts or resources . exacerbating this condition is the fact that the book itself has no index . the book is divided into two - to four-page sections , many of which are near-exact replicas to columns he published on the conservative site newsmax.com . in january 2004 , savage published his second political book , the enemy within : saving america from the liberal assault on our schools , faith , and military . his newest book , liberalism is a mental disorder was released on april 12 , 2005. both of these books contained citations of nearly every assertion made , contrary to " the savage nation . " in january 2006 , savage announced that he would be releasing a new book , the political zoo , in mid-march . [8] the book will contain satirical profiles and cartoons of different people in politics as animals in the " political zoo " including one of savage himself , who will be portrayed as the zookeeper . savage has remarked that the book will be " easier to digest " than his previous political books . books as michael weiner plant a tree , new york : collier books , 1975 bugs in peanut butter , boston : little , brown , 1976. man 's useful plants , new york : macmillan . 1976. earth medicine , earth food , new york : macmillan pub . co. , 1980. the way of the skeptical nutritionist , new york : macmillan , 1981. nutrition against aging , bantam books , 1983. secrets of fijian medicine , quantum books , 1983. " vital signs " , avant books , 1983 getting off cocaine , avon books , 1984. maximum immunity , boston : houghton mifflin , 1986. reducing the risk of alzheimer 's , new york : stein and day , 1987. the complete book of homeopathy , garden city park , n.y. : avery pub . , 1989. the herbal bible , san rafael , ca : quantum books , 1992. healing children naturally , san rafael , ca : quantum books , 1993. herbs that heal : prescription for herbal healing , mill valley , ca : quantum books , 1994. the antioxidant cookbook , mill valley , ca : quantum books , 1995. [edit] books as michael savage the savage nation , wnd books , 2003. the enemy within , nelson current , 2004. liberalism is a mental disorder , nelson current , 2005. the political zoo , nelson current , 2006. michael alan weiner was born to a russian jewish family [1] in the borough of the bronx in new york city . michael savage earned a bachelor 's from queens college in education and sociology . he taught high school for several years in new york city . following that , he earned two master 's degrees in ethnobotany and anthropology from the university of hawaii . he then received a ph.d . in nutritional ethnomedicine in 1978 from the university of california , berkeley . his thesis was titled nutritional ethnomedicine in fiji . savage spent many years researching botany in the south pacific , and has a background in alternative medicine . he has stated he was a liberal at one time and never served in the military . weiner was a friend of openly gay beat poet allen ginsberg , offering to arrange readings for ginsberg and lawrence ferlinghetti in 1972. [2] some of his letters to ginsberg are held in ginsberg 's archives and one of those letters describes an encounter with a young fijian man . [3] savage denies writing the letter and called it part of a " smear campaign " by " gay fascists " . [4] savage also once posed naked for a photograph with ginsberg while swimming in fiji . [5] ferlinghetti views weiner 's reincarnation as michael savage as " total opportunism , " the crowning achievement of someone who was " always looking to make a fast buck " and " always trying to think up new schemes to get famous . " michael savage began his radio career in 1992 on san francisco 's #1 news / talk radio station kgo , first doing fill in work for other hosts , then getting his own show on the weekend . two years later he was given a weekday show on kgo 's sister station ksfo where he shared airtime with a liberal talk show host . he chose his " nom de voix " in " the tonga islands in the 1960s . i stumbled upon the name of a [19th-century] shipwreck who was locally infamous -charles savage . his exploits were legendary , " he said . " so the name was bouncing around in my head . " at the time , his slogan was " to the right of rush , and to the left of god . " on january 1 , 1995 he was given his own show during the drive-time hours . the show quickly became a local hit . in 1999 , he came to the attention of the talk radio network . on january 17 , 2000 he started doing an additional two hours of radio which was broadcast nationally . for the next eight months , savage would spend a total of five hours a day just talking . his national experiment was a success , and on september 21 , 2000 , he stopped doing separate shows , beginning a full three-hour national show . after just one year , he was in 150 markets . by 2003 , he was in over 200 markets and is currently the no . 3 radio host in the united states . in june 2003 , he had a salary dispute with his flagship station ksfo who refused to renegotiate his contract . he was off the air for three weeks . on july 1 , 2003 he began his show on a different station : knew in san francisco . since that dispute , he speaks badly of ksfo and of " vanity or pretty boy " sean hannity , whose show replaced his on the station . savage also speaks pejoratively when referencing his fellow talk radio hosts or individuals with whom he disagrees ( see list of michael savage neologisms ) . as of 2005 , savage has between 8 million and 10 million listeners per week . this makes his show the third most widely listened to broadcast in the united states . in 1996 he applied to be a dean at uc berkeley 's graduate school of journalism . when he was not granted an interview due to lack of qualifications- -less than two years of experience in radio , with a ph.d . in epidemiology and nutrition science- -savage filed a discrimination lawsuit that was eventually dismissed . the position instead went to china scholar orville schell who , according to weiner , was less qualified than himself . savage was hired by msnbc to do a one-hour show starting march 8 , 2003. on july 7 , a mere four months later , he was fired for making anti-gay remarks in response to a caller , later identified as prank caller " east coast bob . " savage was doing an " airline horror stories " piece , when bob called into his show to talk about undercover security guards smoking in the bathroom . his next words were " half hour into the flight , i need to suggest that don and mike should take your show so you can go to the dentist because your teeth are really bad " . the words after " should " were bleeped out by a msnbc exec , which would make one believe that the caller was actually making lewd comments about savage 's sexual orientation . savage asked if he was a " sodomite " , to which the caller answered " yes " . savage then said to the caller : " oh , so you 're one of those sodomites . you should only get aids and die , you pig , how 's that ? why do n't you see if you can sue me , you pig . you got nothing better to do than to put me down , you piece of garbage , you got nothing better to do today , go eat a sausage and choke on it . get trichinosis . now do we have another nice caller here who 's busy because he did n't have a nice night in the bathhouse who 's angry at me today ? put another , put another sodomite on....no more calls ? i do n't care about these bums , they mean nothing to me . they 're all sausages . " [6] before the show was canceled , msnbc was replaying his show during primetime hours saturday night ; many believe the show would have been canceled even without his comments , and that msnbc was simply looking for an excuse to dump the program due to pressure from special interest groups . others point out that msnbc has had poor programming and ratings performance for a long time and that many talk shows of all different political stripes have come and gone quickly on the network .

## neg 7. dvd 585.txt

margin 27.95, 818 words

> fifty-five minutes into this film , after freya ( jane march ) listens to the beast 's explanation of his current condition- -it is the punishment of odin for killing a bear- -she says , " what does it mean ? it makes no sense . " although there is still half an hour yet to come , these eight words pretty much sum up this low-budget variant of " beauty and the beast . " the very title blood of beasts ( plural ) makes no sense . the film shows us only one beast- -a kind of man-bear- -and he is a revived and metamorphosed version of odin 's pet bear , blended or fused with the man who killed it . academic scholars might argue that swaggering-but-cowardly sven ( played by william gregory lee ) is a kind of beast as well ( thus giving us two beasts ) , but we have no way of knowing what the writer and director intended . most likely the title was devised by somebody in the marketing department who had not seen the film . surely the blurb on the back of the dvd 's hard case was written by another marketing person who never watched it either ; e.g. , it is untrue that freya " must undertake a deadly battle when her father and fiance are captured by a tormented monster . . . cast out by his people . " nor is it true that " the beast [singular] . . . battles with freya for his redemption . " further , expect no truth in these grand-sounding words : " prepare for the ultimate tale of love and sacrifice , damnation and salvation . " btw , the front of the hard case has a fake sepia picture of jane march / freya shooting an arrow in an impossible manner : the arrow 's shaft is two or three inches above her hand that 's gripping the bow . with one exception , the acting is a perfect match for the script : laughably poor . the exception is the beast ( played by david dukas ) . one is tempted to quip that only this role has " teeth " ; the fact is that only his role permits audio engineers ( or whoever ) to enhance the actor 's voice electronically , only his role required serious make-up , and only his role required a " special effect " ( his morphing back to agnar , which every semi-conscious viewer , by a third of the way into the film , knew was coming ) . other viewers have commented on the comical tropical setting of this viking saga and the laughable " ships . " most preposterous is the tiny skiff that freya and ingrid ( candice hillebrand ) use to rescue king thorsson ( greg melvill-smith ) . on the island , the beast possesses an iron cage ( which clearly has been welded together using 20th - or 21st-century equipment ) ; when the king is confined in it , it can only be secured from the outside- -and yet , when freya is put inside it for her own protection at night , only she has control of its locking device . how convenient . the costumes are also anacronistically interesting , but only ms. march 's deserve extended comment . when we first see her , she is wearing a little black viking bikini as she swims with friends ; then , besides flimsy chain mail , we see her in an array of gowns that seem to be fashoned from finely woven or knit fabrics- -the final one being most noteworthy for its sequined molded push-up bra-top . lest this review seem too harsh , a few individuals connected with this film deserve special mention for their outstanding contributions : mark thomas , who composed the viking music ; rob bishop , one of the focus pullers ; ryan lotter and steven ndlovu , two clapper loaders ; andrew gribble , a grip ; ben phiri , the generator operator ; guy bonner , transport manager ; johannes sithole , fabrication assistant ; kirsty taylor , prosthetics ; maxmillian van der merwe , standby set dresser ; dirk knoesen , stand-by [sic] carpenter ; sally van der merwe , scenic artists [sic] ; janine wyatt-mair , stunt performer ; grace sibiyo , seamstress ; diane allen , hair supervisor ; bianca , trainee make-up assistant ; ian thysse , medic ; and mark ferda , who did double duty as both dialogue editor and re-recording mixer . oh , one more thing : after coming out of her cage in the morning , jane march seems to have a nude swim in the sea , which the poor beast views from hiding , far-far-far away

## neg 8. music 574.txt

margin 25.74, 355 words

> my copy of " reckless nights.. . " ( and yours , too , probably ) has a sticker on front that reads : " one of the most influential musicians of the 20th century . " well , i 'm so glad that columbia cleared that up . otherwise , i 'd have had to make up my own mind , and apparently music labels do n't allow that nowadays . i hope similar stickers are included on chopin , mozart , and bach cds ( with the century adjusted on a per-composer basis ) . scott 's gimmicky fare makes for pleasant listening , but not in such a large dose- -monotony sets in after two or three titles , let alone 22. halfway through this cd , i felt as if i were listening to the drone of a defrosting icebox . for all the outrageous hyperbole thrown at scott- -no one else like him , no way to categorize his music , and so on , and so on- -the reality is that composers and arrangers like ferde grofe , duke ellington , glenn miller , alec templeton , and bill challis covered the same ground far more skillfully- -and , in most instances , earlier- -than scott . concert jazz , symphonic jazz , or whatever you wish to call it , was not the invention of any one man , and certainly not scott . check out grofe 's scores for whiteman- -in particular , his writing for woodwinds and his constant , scott-esque use of muted trumpet . listen to duke ellington 's " extended " compositions circa 1929. for that matter , listen to ellington 's 1933 " daybreak express " - -virtually the template for scott 's galloping miniatures . experience bill challis and glenn miller 's pioneering big band charts . or.. . believe as you 're told to believe , i.e. that scott , and scott alone , performed this kind of music . i mean , who needs history when we 've got hype ? it 's up to you , dear listener

## neg 9. camera 856.txt

margin 25.42, 752 words

> if you 're looking to capture " the decisive moment " with the nikon coolpix 8400 , stop- --do not buy this camera ! ! ! for that matter , carefully check any digicam or other camera with which you want to capture " action , " because what you think you see , may not be what the camera has the ability to capture as an image . let me briefly explain where i 'm coming from : i made my living as a field photojournalist for 40 years . by the time i retired out of the business i had probably created something like a million color and b&w film images . i owned and used mostly nikon equipment all those years ( although i sure liked working with leica rangefinder cameras and short focal length lenses ) , starting with the original nikon f slr ( which i still have ) and finishing up with the n90s and probably ten different lenses of varying focal lengths . i like nikon equipment a lot . i decided to begin working with digital images last year . i was attracted to the coolpix 8400 because the " spread " on the zoom lens was the 35mm camera equivalent of 24mm- -85mm . when i worked with film i probably used my 24mm and 105mm nikkors more than any others in my bag , so this little coolpix beauty had just about what i was looking for in one package . let me say that while the problems with the viewfinder and shutter lag make this camera absolutely useless for editorial photojournalism , it is , nevertheless , a marvel of human ingenuity . for many other uses- --such as taking pictures of fire hydrants or cows standing in a pasture ( put another way , things that do n't move ) , it works wonderfully well . seriously , i shot an assignment here in tucson that was essentially architectual in nature . the images can only be described as superb ( if i do say so myself ) . i worked only with the camera and a tripod on the shoot . working inside i simply changed the light balance within the menu on the 8400 ( which you can pretty much do on any digital camera these days ) , did not have to check the scene with a separate exposure meter , etc. point being that with film i often carried a bunch of light balancing filters and sometimes a separate gossen exposure meter and all sorts of lights to shoot an assignment . even then , i 'd sweat blood until i could get the processed film on a light table . of course with digital , i ( you ) do n't have to worry about any of that stuff . one can check the image immediately and know instantly if you 're good to go . alas , the shutter lag on this , and many other digital cameras made these days , is the " downcheck " which makes me unable to recommend the 8400. there is also the delay in the electronic viewfinder to deal with . the combination of shutter and viewfinder lag make it absolutely impossible to capture an image , the precise composition of which lasts only a split-second . i have taken many good pictures of people working , " action " shots and the like , but it was only by taking large numbers of images of any given activity and then retaining the one or two that said what i intended that i achieved my purpose . essentially , my shooting eye ( which is pretty damned good ) had nothing to with it . it 's like a soldier trying to kill an enemy with a machine-gun- --if he fires enough rounds , one of them is going to hit the other guy . marksmanship has nothing to do with it . same-same shooting with electronic viewfinders and shutter lag . if you shoot enough images , statistically you 're probably going to get a good one . but it 's not a very good way to do things . so if you 're looking to capture what henri cartier-bresson ( i 'm not sure i 've spelled his name correctly ) so artfully described as " the decisive moment , " look at a digital single-lens reflexes , or wait for improvements in digicams .

## neg 10. books 690.txt

margin 24.69, 323 words

> this is a decent book on photographing artwork - - but not the the most comprehensive . the strengths of this book are that mr. saddington ( 1 ) discusses the use digital media , and ( 2 ) makes the process of photographing artwork very user-friendly by providing great visual references throughout . the user-friendly aspect is the book 's strongest selling point , especially for artists who are new or novices at photography , or visually oriented ( i.e. , no patience for reading instructions that come with few or no pictures ) . mr. saddington 's book provides pictures of what makes a bad negative exposure / photograph , and provides a concise explanation for these results , and does the same for an example of a good negative exposure / photograph . he also provides illustrations of setting up equipment and artwork for photographing . the weakness of this book lies in the general details provided ... unfortunately , mr. saddington provides a limited amount of helpful hints and leaves out specific details for for problem shooting ... i base this opinion on my comparison of this book with a book called & quot ; photographing your artwork&quot ; by russell hart . if you buy mr. saddington 's book , i 'd recommend supplementing it with the purchase of mr. hart 's book . the two books complement each other . where mr. saddington 's book lacks in details , mr. hart 's book fills in the information gaps . on the other hand , mr. hart 's book is very text heavy and has very few illustrations ... so if you 're a visually-oriented person , mr. saddington 's book would easily compensate in the area of illustrating this very important process . again , mr. saddington 's book is decent , but it should be used as a supplemental reference , especially for the visually-oriented person

## neg 11. books 923.txt

margin 22.26, 459 words

> by chance before picking this up i had just finished the heart is a lonely hunter by carson mccullers , and was struck by the similarities and differences . it 's a great " compare and contrast " pair , as an exercise for high-schoolers . both are written as first-person accounts by teen-aged girls and are roughly contemporary . heart published in 1940 , and castle in 1948 , both about life in the 30s . both families are poor . in castle though , there is never any question that the girls might go off and get jobs . this is supposedly because they " do n't know how to do anything " . so instead they sell off their belongings and get by on scraps of bread and the odd bit of butter . how charming ! they are " eccentric " , which seems enough in the author 's eyes to exempt them from the expectation of supporting themselves . only stephen the handsome young son of the late housekeeper , enamored of cassandra , does work and gives the family his entire salary . but he is of the class that is expected to toil after all . even he is rewarded in the end- -able to avoid labor with an easy job similar to that of step-mum topaz- -striking poses . unlike the looming and grinding poverty of heart then , the poverty in the castle never amounts to more than a lark- -educated folks playing at being poor until they 're rescued by romantic circumstance . not so in america where mick kelly , who did n't know how to do anything either , went off to work at woolworth 's , and to a life of little hope . in castle the solution comes in the form of that classic deus ex machina , the inheritance . two dashing young wealthy americans one of whom has inherited the castle , show up just in time , with their chatty modern mum . they throw money around and talk too much , in the cliched extravagant american style . most of the remainder of the novel consists of cassandra and her sister rose swooning over one brother or the other , with an eventual romantic result that assures all the characters of economic well being . it 's all so very charming , bourgeois , and harmless . if your life is hard do n't worry- -a man will show up to rescue you ! the reviews for this novel in amazon are overwhelmingly positive . smith was obviously talented . her writing is elegant and a pleasure to read . i wish she had given cassandra a little more ambition .

## neg 12. books 867.txt

margin 17.94, 177 words

> homesick : my own story by jean fritz is a story about an american girl who grows up in china . she spends a good part of her life wishing she could be in america , where she belongs . when she 's not doing that , she 's corresponding with her grandmother , trying to make friends with some young chinese children , and learning british culture in school . as you can see , jean fritz would be an excellent storywriter had she made it up . however , this story is an autobiography , and is in almost no way fictional . jean fritz is an excellent storywriter anyway , though . jean fritz describes the setting as if her pen were a plane ticket . her story line makes it difficult to locate the plot , or even understand the full story . the autobiography is punctuated by emotions . all in all , this is a fine educational history text , but is not , in my opinion , a fitting storybook

## neg 13. dvd 325.txt

margin 16.66, 283 words

> after viewing the avengers with emma peel , which i do every evening after the dreadful news , enjoying repeats and repeats as well , with reluctance i played the hospital dvd . i thought it was terrible . the diagogue idiotic . i could not help but laugh when scott attacked diana . emma peel would have thrown him across the room . i had to play a few episodes of emma peel in the avengers series to cleanse me of this disappointing and terrible hospital dvd . the lovely diana rigg is a great actress and an extremely intelligent woman , and i was saddened that diana after all those wonderful and exciting avengers collection , with her unrivaled beauty and possessing the most beautiful voice and able to do her own stunts took on this dismal role in the hospital dvd . i see that this dvd was dated 1971 , this was only 4 years after her last avenger episodes dated 1967. in hospital , i believe she was 33 years old . oh well , i will cleanse myself of this hospital dvd and devote an eveningr to a few episodes of the avengers with the lovely diana rigg as emma peel . finall , john steed would have been shocked to see how emma reacted to george scott the doctor . can you imagdine if john steed appeared in the hospital dvd to collect diana rigg and ride off into the sunset as they do after an avenger episode . perhaps they will issue hospital 11 , and bringr in john steed and a few other great actors of that series . robert lyons reno , nevad

## neg 14. music 564.txt

margin 16.10, 284 words

> the 4 cd mini gibson amp ' box-set'leaves off genuine off vinyl 78 , and lp ' harder-to-get ' charlie christian / benny goodman recordings . legacy states " master takes " , but absolutely fails to research deep into charlie christian 's recording history . columbia vinyl 2lp 30779 , ( 1972 ) , and columbia 78rpm c -102 along with the columbia " sextet " cds leave legacy far behind . the wang wang blues -78rpm is n't in the 4cd set , and there are far too many ' false-starts ' , which benny goodman discarded for a good reason . star dust is only about 3 minutes , it 's 8 minutes on vinyl . there is even in-studio handclapping after some tunes . i have the 78s , many col . lps , and there is no " studio-live " takes . this 4 cd box could have , and should have been much better in information , content and genuine charlie christian guitar stylings . the 2 readily available bg sextet cds are a better purchase idea , but there are still those super hard-to-get vinyl lp tracks , which are " the master takes " , left off the legacy / sony box set . musicologist 's suggestion , try to get the vinyl lps. skip this misleading 4 cd set of various tracks , + handclapping = not " good enough to keep " , ( airmail special ) . try the 2 benny goodman / charlie christian columbia cds , amazon has both , and most of the benny goodman sextet ' takes ' are master takes , and " good enough to keep !

## neg 15. books 277.txt

margin 16.04, 772 words

> the literature of september 11 is never attacked . when a book speaks of september 11 ( or of terrorism in general ) , it is more or less guaranteed immunity from criticism ; it will almost inescapably be greeted with sympathy . jonathan safran foer 's extremely loud and incredibly close banks on such sympathy , on such reverence . the narrative , which concerns a nine-year-old boy named oskar schell in search of a key that would unlock / unshell the enigma of his dead father ( a narrative stolen , in its basic outline , from guenther grass 's die blechtrommel ) , could have been written entirely without its scattered references to the terrorist interventions . nor is this trauma the only one presented in the novel : the others include hiroshima / nagasaki , the staten island ferry crash , and the dresden bombings . each disaster is generalized to the point at which what is addressed is not a traumatizing event in its specificity , but historical " trauma " itself and the overcoming of trauma through bereavement-inspired creation . oskar , the insufferable brat , attempts to complete the work of mourning for his father , thomas schell , jr. , a victim of september 11 , by compiling an almanac of self-inflicted wounds , the collage of images and letters which is the book we are " reading " - --an almanac which , most likely , is written sometime in the indefinite future ( thomas shell , sr. 's manuscript of 4 / 12 / 78 is heavily edited ( pp . 208-216 ) . who has done the editing ? almost certainly an older version of his grandson oskar ) . if the term , " reading " even applies . whenever a " pregnant " image is described , foer literally re-presents it in the form of a pictorial image . when a flock of birds rises into the sky , it is not enough that we read of these birds- --we must see them as well . words may not be left in their invisibility ; we are presented with supplementary photographs , illustrations , since mere verbality is not enough . ( indeed , the entire novel oozes with misologos - - - the mistrust or hatred of language - - - in terms of both its content and its form . ) photographs , yes , and also a superabundance of blank pages and nearly blank pages . space is not used in the manner it is in the works of edmond jabes , for instance . typography does not substitute for a well-wrought sentence . foer abrogates himself of all responsibilities - - - most specifically , the responsibility to write well . why bother when the pyrotechnics of typography are at his disposal ? as far as the writing is concerned , it is composed of nothing other than mind-numbingly , soul-deadeningly repetitive phrases ( " heavy boots , " " raison d'etre , " etc. ) and sunday school platitudes : " sometimes one simply wants to disappear " ( 184 ) ; " there 's nothing wrong with not understanding yourself " ( 184 ) ; " everything that 's born has to die , which means our lives are like skyscrapers " ( 245 ) ; " how can you say i love you to someone you love ? ... it 's always necessary " ( 314 ) . whenever the author writes something that he finds " beautiful " and " true " ( 165 ) , he congratulates himself on his brilliance and tells us that that thing is " beautiful " and " true . " the entire book reeks of such unearned profundity . we also learn that most dust is made up of human detritus- --a very deep truth indeed , one that foer also communicates in his essay , " emptiness " ( originally published in playboy ) with all of the sanctimoniousness and self-righteousness of the faux naif who serves as the center of the novel , a sunday school lecture in which we learn that famous musicians ( ringo star ) and scientists ( stephen hawking ) are unthreateningly approachable : everything is familiarized . perhaps it is wrong to criticize foer for including so many blank pages in extremely loud and incredibly close , since the entire book is a vacuum : null space into which readers may project their own meanings . joseph suglia , ph.d . , the author of watch out

## neg 16. software 361.txt

margin 15.77, 676 words

> i ca n't for the life of me understand why rosetta stone has garnered such good reviews ( although i see a few negative ones here , so i feel validated ) and seems to have such an outstanding reputation . i find it practically worthless , and it 's expensive to boot . i 'm sure that my experience with the german program would apply to rosetta stone 's other languages as well , as they all taught via the same method . i 've been learning german for about 6 months and besides rosetta stone i have used pimsleur , rocket languages , and have taken private instruction . obviously , private instruction is best . but this review is about software , and pimsleur is best . but rosetta stone has more bells & whistles , which is perhaps why people think it is so good . but it isn't . for example , nowhere in rosetta stone do you actually learn how to say useful things . nowhere do you learn how to say " hello , " " how are you , " what 's your name , " or even " where 's the bathroom . " instead , you will learn how to recognize such useful phrases as " the woman and the boy have a ball on their heads " or " the man is under the donkey " or " these two fish are from the same species " or " the blue triangle is bigger than the red square . " ridiculous ! ! and note i said " learn how to recognize a phrase . " this is the biggest weakness and disappointment with rosetta stone . it really does n't get you to talk at all . you are not required to utter a word . you see four pictures , and the speaker will say ( in german ) " the boy is drinking milk . " now , if you have already heard the word for " boy " ( junge ) and three of the pictures have no boys , you simply click on the picture with the boy and presto , you 're correct ! this multiple choice way of learning is not effective for learning a language ! ( there is a " practice speaking " mode , equally useless , which i mention below ) with pimsleur , which is an audio only program , you hear conversations that will impart essential words and phrases . and they are repeated ( and asks you to repeat ) in such a fashion that it sticks . for example , it was weeks ago that it introduced " how much do i owe you ? " yet i still remember it . ( wie viel shulde ich ihnen ? - -no , i did n't cheat and look it up ! ) pimsleur is brilliant in the way it gradually builds your knowledge and abilities . of course , it is n't perfect as it does n't explain the grammar . but neither does rosetta stone , and rosetta stone is worse because with pimsleur there is also an english speaker who explains some things , while with rosetta stone you are left to twist in the wind . that 's why software language learning programs should be seen as supplements- -supplements to classroom or private instruction . what are the bells & whistles on rosetta stone ? you get to do a lesson in a variety of ways- -seeing pictures with audio ( the speaker ) , or pictures with audio and text , or audio only , for example . there is also a feature where the speaker on the program says a phrase , and you repeat it into a microphone and can compare your voice signature to the speaker's . but i found that this did n't work well at all and was n't worth the trouble . and again , the phrases were n't useful

## neg 17. camera 788.txt

margin 15.74, 227 words

> i had high expectations when purchasing a laser range finder for use on the golf course . after a lot of research , i settled on the pro tour laser . as previous reviewers have stated , this unit is very hard to stabilize . i have a feeling this is true of all lasers . even with supporting both elbows on the hood of a car i found this unit very hard to find yardages for objects beyond 150 yards paricularly when bright sunlight is present . on the golf course , finding the flag and obtaining a yardage at longer yardages is almost impossible if there are objects behind the flag such as trees or landscaping . this unit has been returned and i have gone to a standard handheld gps instead . once the center of the green is initially saved as a waypoint , this is a very reliable and quick method to get a yardage , you just have to convert feet or 1 / 100 's of a mile into yards . i do this with a chart taped on the back of the gps . accuracy is about 2-4 yards which is good enough for anyone but a vey low handicapper . i am staying away from a laser finder until golf courses uniformly put reflectors on their poles .

## neg 18. dvd 229.txt

margin 15.65, 201 words

> pushing the envelope for explicit , over the counter home videos , 9 songs ( tartan ) is about one year of sex and rock'n roll in the life of two lovers . matt is a young glaciologist . he meets lisa at a london rock concert . that night they start an affair . in between attending more concerts , they make passionate love . it 's for real and explicit . nine live-concert song footage is intercut with their coke-snorting , sexual encounters creating a sometimes ironic reflection of their intense physical but otherwise rather bland relationship . and finally , all this takes place in the memory of matt as he flies across the vast frozen wastelands of the south pole . this unscripted film is part musical , part drama , part documentary and part performance . it raises questions about the difference between pornography and art . controversial and much buzzed about , this not fully satisfying experiment is of interest mainly as a novelty item by a usually innovative and creative director for what it could have been . and of course the sex . a special feature eliminates everything but the concert performances .

## neg 19. camera 881.txt

margin 13.87, 160 words

> the e550 is a good camera and this lens does do a good job of zooming in on the subject but due to the way the camera and lens are designed , you must have the camera 's zoom fully extended in order to use this tele lens . so this means if the subject is moving around a lot , such as my daughter playing soccer , you will miss the shots where the action has moved to close to you because you ca n't zoom out . as long as the action remains at some distance to you than this zoom lens is useful . i unfortunately have too many ruined shots because the action moved too close and their heads get cut off , etc. another negative is that the viewfinder does n't show the zoomed in image , you must use the lcd screen to frame a shot , which can be difficult in bright sunlight

## neg 20. camera 991.txt

margin 13.44, 150 words

> if you are going to lay out $500 for a camera , you should expect a fair amount of camera . however , i have a few gripes here . first , there is no remote control for it which makes setting up a shot tough . all the nikons in the d series can use a wireless remote . you can buy an underwater case for those magnificent nikons so you can shoot underwater . you can get over 10 megapixels in a d80 , or d200 and you get that great nikkor lens . you do n't get much of a lens on the dc500 , and 5 megapixels do n't get you very far when it comes to printing and publication quality images . lets face it : this is an expensive point-n-shoot camera for a tourist , not a serious camera . nuff said . -

## neg 21. books 142.txt

margin 13.24, 120 words

> mcmurry 's text is a very friendly , gentle intro to organic . it 's a thoroughly enjoyable read , but it does n't teach you what you need to know . explanations for important mechanisms are usually very brief , and the problems included are usually very basic and general ( the spectroscopy and synthesis problems , in particular ) . if you 're looking to become a chemist , this is not the book to learn from . i 'd recommend vollhardt and schore 's textbook , or any number of sophomore-level texts that will give you the skills you need to approach complicated problems more successfully ( i.e. , on exams or out in the industry )

## neg 22. music 457.txt

margin 13.18, 206 words

> of the dozen tracks featured here , chances are the typical listener will only recognize four : & quot ; signs , & quot ; & quot ; sweet city woman , & quot ; & quot ; one fine morning&quot ; and & quot ; gimme dat ding&quot ; - and the last-named is out of sequence , having come out more than a year before the others . the star of this show is lighthouse 's & quot ; one fine morning , & quot ; and rhino must be praised for offering up the full ( lp ) version rather than the 45-rpm edit , which was about two minutes shorter . it 's a shame , in a way , that this song had lyrics ; had it been an instrumental , it would have found a perfect and permanent home - on & quot ; music from nfl films&quot ; - it had that quality about it . as for the other eight offerings : if they wanted to pick some obscure stuff , why did n't they go all the way and throw in dusk 's & quot ; treat me like a good piece of candy ? & quot

## neg 23. camera 685.txt

margin 12.81, 435 words

> the me-1 provides a modest 1.2x magnification for viewfinders on olympus 's e-300 and e-500 cameras . ideally , this would allow sharper manual focusing and more precise framing . unfortunately , this did not happen when i used the me-1 to make a number of trial images with my e-500 , so i will be returning the me-1 for a refund . ( for the record , i wear prescription eyeglasses while shooting , with my " shooting eye " corrected to 20 / 20 vision . ) like other folks , i find the e-500 viewfinder a trifle small so that it 's not always easy to frame a shot and see exposure data at the same time . the camera must also be pressed against your face when framing , which is not always comfortable . in some ways , the me-1 created more problems than it solved . the me-1 kept the camera further from my face ( though it seemed to bump harder against my glasses ) , but at the cost of *narrowing* my angle of vision in the viewfinder . divide the viewfinder into four equal columns and rows so you have eight squares . the four squares in the middle of the viewfinder were easily visible , but those along the sides , top , and bottom were *less* visible than before , the corners considerably less . to frame a shot , i had to move my eye around the viewfinder much more with the me-1 than without it . to see exposure data , i had to shift my eye almost completely away from the image . more hassle than i need when shooting in the field . fortunately , there is another option that works for me . the e-300 and e-500 come with an ep-5 eyecup , which is definitely too small for my taste . but a larger eyecup is also available , the ep-6. the ep-6 keeps the camera a little further from my face . and with the viewfinder diopter properly adjusted ( a critical step no one seems to mention ) , the ep-6 allows me to see both the entire image and exposure data without shifting my eye very much at all . all of this will vary from person to person , of course , and there may be circumstances when the me-1 is exactly what 's needed - - so two rather than one star . but not in standard shooting conditions , especially if you need to compose , set exposure , and shoot quickly

## neg 24. camera 954.txt

margin 12.57, 77 words

> bought this case along with a digital rebel xti , my first slr . instead of the 18-55mm kit lens i opted for the sigma 17-70mm lens . sad to say , but the case fits only with the kit lens. . the rebel xti with the 17-70mm lens barely fits . so a word of cuation to everyone , if you 're planning on anything other than the kit lens , then do n't get this

## neg 25. dvd 165.txt

margin 12.56, 518 words

> theres only one word to describe this ppv and thats s**t , why did they have to ruin 2 matches ( main events ) what could have saved this event ! this features 4 titles on the line and if you buy the dvd you also get some extras . match 1 world tag team titles - fatal fourway chris jericho and christian ( c , i call them y2c ) vs lance storm and william regal vs dudley boyz vs booker t and goldust ! this match made every body think the ppv was gonna be great ( even though it was'nt ) but a great opener and the winners of this match deserved the titles ! 7.5 / 10 match 2 edge vs a-train short match but had some good highspots , but the end turned the whole damn match around when it ended in dq ! 6 / 10 match 3 eddie gurrero ( tag team champion ) vs chris benoit easily the match of the night and there were'nt any titles on the line and if you liked this you should watch there match at vengeance 2003 ! 8.8 / 10 match 4 kane vs batista ( w / ric flair ) this is where everything changes this match was a squash but had some good moves good win for batista ! 5.5 / 10 match 5 triple threat match - womens championship trish stratus vs jacqueline vs victoria ( c ) we 've got jezabell ( victoria ) whos absessed with trish and jackie was added in since she beat jezabell . jezabell wins via hitting trish with the title and covering jackie ! 5.5 / 10 match 6 single match - wwe championship the big show ( c ) vs kurt angle not bad but just needed either more time or better action , it was cool seeing brock f5ing big show and kurt angle being new champion ! 7.5 / 10 main event match 7 2 out of 3 falls match - world heavyweight championship 1st fall - street fight - 8 / 10 2nd fall - cage match - 6 / 10 3rd fall - ladder match 2 / 10 triple h ( w / ric flair ) vs shawn michaels ( c ) this was something like the second 2 out of 3 falls stipulation match and was a main event outcome : pathetic ! first fall was a bit too long but was really good like there match at summerslam ! second fall had crashing tables and that was it , that was cool but it was much of a match hbk kicked hhh ass easily ! third fall was'nt much and this match could have saved this event ! 7.9 / 10 overall armageddon 2002 had some good matches escpecially benoit vs eddie the 2 main event could have been much better though ! overall : 6.7 / 10 dvd extras : - 5 exclusive interviews - extra match : fatal four-way elimination match to determine the number 1 contender ( from smackdown - 5th december 2002

## neg 26. dvd 674.txt

margin 12.37, 137 words

> the film seems to focus on 70 's punk exclusively . anything post-1980 is glossed over , clumped together and generally viewed with dissapointment by this " documentary " . i think the film does well documenting the roots of punk , seeing as how letts was steeped in the scene at that time ( although the misfits were n't mentioned , which i found odd ) . the interviews with henry rollins and jello biafra were great as well . however , in order to claim to be a documentary , the evolution of punk rock is just as integral ( perhaps more so ) as its origins . i think , basically , letts based the film on his own opinions , likes and dislikes instead of actually documenting punk . i was disapointed .

## neg 27. dvd 539.txt

margin 11.50, 141 words

> this film , like most of his early work , is for hitchcock aficionados only . i am an admirer of hitchcock and also enjoy old british films , but i still found this movie tough going , not least because of the 110 mins running time . the picture quality of this laserlight dvd is not perfect , but it is perfectly watchable and probably a lot better than you 'd expect for the price . the musical score is also okay , but nothing to write home about . laserlight do however pose a mystery that hitch himself would have been proud of . this dvd has no commentary , no documentary and no trailer , not even one of those awful tony curtis intros . so why do laserlight describe this dvd as a ' special edition '

## neg 28. books 580.txt

margin 10.81, 221 words

> this is the latest in a never-ending series of books trying to generalize non-business world ( eg. sports , armed forces , girl scouts , religion , nasa , etc. ) management techniques to the business world . most , possibly all , are of little value because of major differences . 1 ) members constituting the varying organizations are motivated differently , and face greatly significantly different situations . what does eg. a fighter pilot or football coach have in common with a pharmicist , nurse , professor , financial analyst , etc. ? i have no idea . 2 ) key success factors vary from one business to another . for merck , it may be speed of developing new drugs , getting through fda approval , and motivating physicians to use them . for nucor steel , it undoubtedly rests much more on low-cost production . again , what does either have to do with fighter pilots - little , if anything . one is better off reading books from similar situations - eg. about wal-mart ( if you are in retailing ) , about allied-signal or g.e. ( if you are managing a conglomerate ) , and about new york community school district #4 , as managed by sy fliegel , if you are in public school

## neg 29. music 572.txt

margin 10.74, 298 words

> after two albums of wholly instrumental music , joe satriani apparently decided it was time to start singing . " flying in a blue dream " is the only satriani record with several ( six ) vocal cuts . so how are they ? well , satch 's voice is n't superb , but he does an ok job . the problem really is with the material- - it 's clear he 'd gotten used to writing pieces as guitar features . the only real exception to this in my assessment is frantic electric blues " big bad moon " - - the piece is blazing and explosive , the vocal is passable , and satriani is on fire . but pieces like " ride " , " the phone call " and " strange " are all pretty much forgettable ( well , " ride " is actually a bit too irritating to be forgettable.. . ) . the remainder of the material is a mix between exploratory ( and primarily acoustic ) pieces ( " the feeling " ) which are nice but largley filler and " surfing with the alien " styled instrumentals ( " one big rush " , " back to shalla-bal " ) . the exception is the chugging opener and title track , " flying in a blue dream " , which features satriani at his most lyrical as a guitarist . invariably , the album is a bit too weak for its own good- - it 's probably also a bit too long ( about 65 minutes ) and probably would have benefited from being trimmed down a bit . start with " surfing with the alien " , come back to this if you want more of the same

## neg 30. music 27.txt

margin 10.62, 234 words

> now on their sixth studio album ( and second on a major label ) carbon leaf plays it safe with the inoffensive rock / pop of " love , loss , hope , repeat . " lead vocalist barry privett has a warm , pleasant way of delivering his lyrics , and renowned producer peter collins fulfills his duties . nevertheless , the 11-song collection is most notable for its power of subtlety . in fact , it is so subtle that not one song is memorable . some lyrics are heartfelt ( " the war was in color " recounts a conversation between a grandfather and grandson , lead single " learn to fly " regretfully summons up inner strength ) but with such flat , by-the-numbers melodies these songs have little to stand on . everything sounds just fine , but nothing is endearing . every guitar strum and drum beat can be predicted ten seconds prior to its appearance , and privett , despite his appealing voice , could easily be singing one extremely long song . this project is obviously well-intentioned , but many other bands have done this before and better . these guys without a doubt have talent , but this album will soon be forgotten for good reason . next time they will hopefully carve out a more unique sound than the one on this record .

## neg 31. music 473.txt

margin 10.07, 208 words

> unfortunately i was extremely unhappy after listening to the album . unlike many other altan fans , i view maireads singing as the weakest part of the groups appeal despite their having chosen some excellent songs over the course of their recording career . the problem is that on this album they emphasize her singing to the almost total exclusion of their instrumentals which was what attracted me to the group in the first place . and the few instrumentals they do play are played with no spirit almost like & quot ; well i guess we have to put a few instrumentals on&quot ; kind of effort . i 'm sorry , but she has a thin voice and is frequently shrill and off-key on many of their songs . she is however an excellent fiddler and that with the superb abilities of the other members and inspired arrangements made them for me the top irish folk group . alas they have decided to stress her poor-to-mediocre vocals instead of their great abilities in playing reels , jigs , etc. i miss frankie kennedy 's flute too . goodbye altan , your best day 's are over unless you revert to the format of the old days

## neg 32. dvd 537.txt

margin 10.03, 325 words

> i find it almost incomprehensible in this more enlightened technological age that there are a very limited amount of your subscribers who are concerned about the appaling presentation of all but two of these movies and i also wonder as more and more older movies are being re-released enhanced for widescreen tvs that no one seems concerned that arguably the most classic of classical movie musicals remain in a truncated format that cannot be properly watched if one has a widescreen tv . these movies scream out for the widescreen , they were made with the ultimate technology of the time to be seen as wide and as broard as possible . yet they remain stuck in a non anamorphic style that limits their enjoyment to anyone with a widescreen tv and , with one exception , all the people who have written about them dont seem to care . " oklahoma " , " carousel " , " south pacific " and " king and i " need to be updated to 16.9 anamorphic widescreen ( also preferably with some genuine extras and commentaries as well ) . fox are years behind the rest of the movie studios in this regard and have only recently started to adapt their films for the format of the future ( ie observe the two versions of " an affair to remember " ) of course , this is a major rip off , so anyone with a widescreen tv who has not bought these films - -hold off , coz sooner or later they will get a proper release...how long ? that is anybody 's guess , but these postage stamp versions are an insult to anyone who knows anything of widscreen dvd technology ( " sound of music " is fine and " state fair " was made in non widescreen full screen format , an should be viewed with lines either side of the screen

## neg 33. health 242.txt

margin 9.56, 107 words

> the razor i bought came with packets of this gel , as well as the lotion . possibly due to the consistency , the gel gets used up more quickly . it is also not as comfortable to use as the lotion is . the key ingredient that makes the difference is menthol . the gel has menthol , so that 's why it can be irritating . i read a review of shaving basics online , and it says always avoid shaving with products containing menthol . the lotion , on the other hand , always helps get a better shave , and is quite soothing

## neg 34. books 810.txt

margin 9.42, 52 words

> this booklet has a lot of warner brothers drawings , but it does n't delve into the specifics of creating animation very well . i 'd recommend getting the animator 's survival kit instead as it has tons of good and well explained info on the art of creating your own animation

## neg 35. dvd 677.txt

margin 9.34, 463 words

> melanie griffith , rachel leigh cook , and hugh dancy star in this straight-to-video film about one female transporter , who gets into trouble because of someone plotting against her . well , that 's all about it , apparently , but the film tries to give something unique to the otherwise unoriginal plot . i mean , the slightly original character of sarah by melanie griffth , who plays that smuggler in trouble . given a special job by malcom mcdowell with his customary ' i-could-be-very-baaaad ' smile , sarah agrees to carry a pack hidden in her bag . but as you know , someone also wants that package , and ... well , that 's nothing new , but she is attacked on the way . do n't expect any thriller , however . the film 's focus is not about that ; it is the relations about sarah and jack ( dancy ) who live together in a fancy paris apartment . but while sarah is away from paris on business , jack is attracted to a younger lady jenny ( cook ) who also falls for him . thus the film makes an effort to include both love and crime . nice try , considering this interesting point about the character of elder lady sarah , but if the factor is taken away from the film , the end result is nothing but a flat , tired suspence - - suspence as to its relations and its crimes alike . either way , the film is emotilnally very void . ok . two fatally bad things : one , too incredible characters . see , sarah is a professional courier who must know the rules of the job , which could be dangerous . but instead of renting a car ( and it 's europe , where that could be pretty easy ) , she takes a train ( and a night train ! ) in which she becomes an easy target . in this way , the film misses every chance to make it more suspenceful . when some character ( s ) must die , they die like characters in old video games - - they fall , that 's all . the other one ; acting . let me be honest . it was painful to watch the one-dimentional performance of melanie griffith , who was very good in ' another day in paradise . ' maybe she is not the greatest actor , but certainly she can act . but as far as ' tempo ' is concerned , no , i do n't think so . only the location of paris saves this film from utter forgettableness . forget about this one .

## neg 36. camera 760.txt

margin 8.84, 280 words

> this is the 7th olympus camera i 've owned over the years , from film to digital . i have always been very pleased with olympus cameras and their usual superior optics . this camera , though , is a major disappointment , mainly because even though it can shoot in raw , there is no compatible conversion available yet , leaving you unable to process raw images . this renders the camera worthless at this time for serious pictures as you have no choice but to shoot in jpeg . olympus should have ensured that vendors such as adobe had the necessary information to make the compatible raw conversion plug-ins available before this camera hit the market . there 's no excuse for olympus to not have made sure this was the case , indeed it 's downright irresponsible . having said the above , the camera lens is quite nice , the camera itself operates well . you can take quite good pictures . however , the camera is not suitable for flash pictures in medium to low-light situations as there is significant lag time from the time you press the shutter to the picture actually being taken- -- -if you 're taking pictures of people , they will have moved by the time the picture is taken . the battery life is very good . the camera fits nicely in your palm . and , having a 28 - 500 mm lens is great . if you do n't shoot in raw and you do n't depend on flash photography , the camera is worth a look . otherwise , look at other products at this time

## neg 37. music 269.txt

margin 8.78, 157 words

> as a fan of pete seeger 's music , i bought this cd in the hope that the family connection would ensure similar quality of the music . disappointingly , i 've found this album really grates on me after a couple of songs . peggy 's vocal style in particular becomes mighty annoying to listen to over the length of the album , as her delivery can best be described as a neo-hillbilly twang . i may end up combining the best half-dozen songs from this album with some other folk albums to generate a listenable & quot ; best-of&quot ; set , but i 'd find it unthinkable to listen to this entire set in one sitting . only devoted fans of the genre or the duo should invest in this set ; more casual fans of folk should direct their dollars to any of pete 's fine albums such as the carnegie hall classic

## neg 38. books 557.txt

margin 8.75, 119 words

> cooper 's book is yet another warm and fuzzy management guru text - - - from yet another management guru who never served a day as a real manager , of a real company . it contains all sorts of motherhood and apple pie stories - - - along with trite sayings such as & quot ; when you find a back door that 's open , close it&quot ; or my personal favorite & quot ; use the lanterns of your life to help light the way . &quot ; if you 're looking for an inspirational book , one with a solid basis , forget this one . you 'd be better off reading the daily horoscope

## neg 39. books 857.txt

margin 8.56, 435 words

> i have progressively become more and more disappointed with rita mae brown 's books in the past decade . her early books were utterly magnificent ; now , she rarely if ever deviates from her favorite ( and by now , utterly boring ) themes - - southern manners , horse bloodlines , and foxhunting . blessedly , " whisker of evil " was foxhunting-free , but suffered from a heavy-handed overload of the previous two . rita mae brown would be wise to remember that there is a big world outside of her corner of virginia , and many of us have grace , manners , and respect for others - - and we do n't take kindly to being told that only virginians understand these things . that 's just simply not true . that said , there were some delightful aspects of " whisker of evil " - - the mystery itself was great , the animal characters were adorable as ever , and i loved learning more about harry as a person and what makes her tick . her quitting the post office was a great ( and very unexpected ) twist . i liked reading more about her home and her relationships . however , the stultifying minutiae of horse bloodlines was beyond me ; was this directed at a heretofore-unknown segment of rita mae brown 's fan base ? it was so out of context in this book ; certain details contributed to the horses ' relationships to one another , but she took it way too far and i found myself skipping pages . as well , i almost threw the book across the room when i came across a line that stated in so many words that only virginians have manners . this is a common theme of ms. brown 's and it is quite frankly offensive . there is a big , big world outside of virginia - - rita mae brown should know this , she has lived in it - - but her books and characters have become so parochial , insular and snobbish that it is an insult to those of us who do live elsewhere in that big world . i would have thought these kinds of statements were tongue-in-cheek if it was n't such a recurring theme in so many of her books over the past decade . enough already about southern manners ( a biased perception at best ) , ancestor worship , bloodlines ( human and horse ) , and foxhunting . whatever happened to characters like celeste chalfonte

## neg 40. books 143.txt

margin 8.55, 330 words

> main pro : an additional unbiased source of information in an area where there is not nearly enough main con : too few products reviewed as a first time mom ( and a compulsive researcher ) i found this book most helpful as a cross reference with other sources ( baby bargains , girlfriend 's guide to baby gear , and reviews in babycenter and at amazon ) . i will say though that i found myself trusting the advice of alan and denise fields and of vicki lovine more than that of the authors of this book . when reading through bb bargains and girlfriends guide i felt more keenly that the products were being judged by real parents who thought about parents ' needs ; consumer reports seemed a little less thoughtful and definately less comprehensive . getting ready for a baby is a behemoth task . the sheer amount of stuff you need- - clothing , bedding , furniture , strollers , car seats , feeding devices , toys- - and the myriad of choices that exist for each item can be very overwhelming . and because there are so many crib manufacturers , stroller makers , etc , no single superstore like bbrus or target can carry all of the " major " brands . it would be impossible to register at any one of these stores using only the recommendations of consumer reports ' book . now perhaps not everyone enters parenthood quite as clueless as i was about baby gear . and if you have friends and family who can share enough information with you ( and better yet stuff ! ) about these products , then you probably do n't need any of these books . but if you are the kind of person who wants to know all of your options and who works to get the most for her or his money , you 'll need more than this book .

## neg 41. music 709.txt

margin 8.11, 160 words

> i am a huge fan of elvis costello and ran to the shop as soon as i read the great reviews of this album , what a mistake ! ! ! very few of the arrangements offer an improvement over the original version . the cardboard cut salsa montuno of ' clubland ' sounds as classy and natural as a plastic flamingo and the wonderful ska sound of ' watching the detectives ' is lost in a jazz arrangement that does n't offer much to the melody . elvis ' voice is not suited the long sustained notes of ' almost blue ' and most of the songs . it worked well on his ' juliet letters ' album because the brodsky quartet played for his style but with the clean and crisp sound of the metropole orkest it is just painful . for me , ' hora decubitus ' is the only song worth listening from this musical jumble

## neg 42. music 692.txt

margin 7.93, 222 words

> i respect everyone 's opinion in here , and i 've tried so hard to love this album because i love pink floyd and i see how everyone calls it a classic . but i just do not get it . i highly overrated album imo . very childlike and underdeveloped , but maybe that is its charm ? i see 2 very different pink floyds and i have to say i never got into syd 's style . matilda this , lucifer that . the gnome ? come on . astromony domine was a classic but the rest of the album is a tough listen i 'm sorry to say . i 'm sure you 'll say a true floyd fan would love this album , well maybe that 's true . but for me , when waters and gilmour were together , that is the true floyd imo . and their reign started with meddle and ended with the wall . a brilliant 6 album run ( meddle , obc , dsotm , wywh , animals , the wall ) . for serious collectors , this is a must have and i 'll give it 2 stars , but stay away if you expect another ' wish you were here ' purchase , pre-gilmour can be a tough listen .

## neg 43. music 507.txt

margin 7.90, 78 words

> i was , overall , disappointed by this cd . there are many good reviews here , but they generally overpraise . tracks 4 through 8 have too much synthesizer for my ears . a major highlight is track 9 , the crab and the egret , but interestingly , the flute is accompaniment to the wondrous chinese percussion . disappointingly , the cd is only 40 minutes long and left me wanting more tunes without synthesizer accompaniment

## neg 44. books 579.txt

margin 7.59, 62 words

> i was the commander of my highschools afjrotc rocket club so my godfather bought em this book it is very informative but if you are just building basic este kits then this is way to advanced for you as it was for me and the other cadets in the club but if you are really into rockets this book is for yo

## neg 45. music 809.txt

margin 7.55, 248 words

> eight years ago today was the day blondie 's reunion album was released , and though it was great to see blondie back together , no exit just fell short on many levels . 2004 's the curse of blondie ( see my review also on amazon ) is a much better album and should have been their comeback . no exit wo n't exactly take you back to the hooks that made blondie famous . harry 's lyrics are wonderful in " double take , " but the deadpan melody literally kills the song . fans were also not terribly waiting for jazz standards ( " boom boom in the zoom zoom room " ) or revamped demo tracks ( " out in the streets " ) , but the worst cut is the title song that includes a rap verse by coolio . both the band and coolio could have thought of something more productive to sing about . the music is n't catchy either . all is not lost with songs like " night wind sent , " and harry 's own transformation in " forgive and forget , plus who would dare argue blondie 's potential to shake the pop world again when you hear " maria . " as the album 's best track , " maria " is a wonderful reminder of how blondie , and debbie , can still create an infectious pop song that leaves a template on the mind

## neg 46. dvd 275.txt

margin 7.47, 191 words

> this dvd was the first one released by michael buble , and i bought it in hopes of seeing some of his live performances . there are segments of performances , but the editing and fast , wild cuts from one angle to the next to the next to the next really detract from the overall effect . the performances get largely lost . what remains is a lot of footage of michael and his original bandmembers drinking , clubbing , gambling , womanizing , and generally acting like rowdy frat boys . if you really want to be wowed and experience what a live buble concert is like , i highly recommend " caught in the act " . this dvd lives up to it 's name as part of the pbs great performances series produced by david foster . " caught in the act " is slick , glossy , flashy , enormously fun and absolutely true to the real experience . i 've seen buble perform live twice , and i can attest that " caught in the act " is just about as good as being there

## neg 47. music 288.txt

margin 7.36, 215 words

> he was at his best when he sang about the loneliness , perseverance and dreams of ordinary people . in " sandra " for instance it felt like he was singing about a neighbour . the combination of his warm voice with his piano could be very moving and was definitely unique . in the late eighties he started focusing on merely performing and doing cover versions . he released a few inspired tracks now and then , his first christmas album had a lot of charisma and warmth , and " here at the mayflower " was a sincere effort . he is an intelligent person who cares for music and does n't let his superstardom go to his head . so , what has changed ? and why this late in his career ? barry has reinvented himself as a las vegas entertainer , liberace style . and he 's released an album with unchallenging versions of evergreens . i have no doubt that he genuinely wants to make people happy , like liberace did . and i have deep respect for that . but i personally regret that clive davis and manilow have now decided to manufacture products for a larger audience - one that does n't really have any demands .

## neg 48. health 143.txt

margin 7.34, 52 words

> i love this turban . it enables me to dry my hair without wearing a huge towel on my head . it 's lightweight and extremely absorbant . i have been using one for more than 5 years . i 'll never go back to usung a regular towel for my hair

## neg 49. camera 951.txt

margin 7.31, 181 words

> i got this lens in a kit with a nikon d80 camera . this lens failed to deliver the goods 99% of the time . why buy an expensive camera and then use a cheap lens like this ? its silly to spend big money on the camera and have only blurry pictures to show from it . it was only tolerable in very bright situations and using less than 100mm focal length . a cloudly day or all of the 200 mm zoom would result in a picture that had significant distortion noticeable even on little 4x6 prints . very few pictures came out when it was used in the fullest zoom ( 200mm ) . i disliked this lens enough to return the entire camera kit and purchase a different camera ( d200 ) that came with the highly ranked 18-200 vr lens from nikon . if your interested in nice sharp pics , then pass on this lens . if you want to save a few bucks and like blurry photos , this lens is for you. .

## neg 50. music 605.txt

margin 7.07, 163 words

> this cd and the one entitled " night ranger 's greatest hits are almost identical , but are different in this way : " best " contains " i did it for love " . " greatest " contains , instead , " rumours in the air " and " restless kind " . the other 10 tracks on each cd are the same . so , which one to buy ? my choice is the one with the extra track . also , in my opinion , both tracks on " greatest " are better than the one on " best " . in addition , here 's hoping that the band or record label decides to release a true " greatest hits " or " best of " album that will contain about 15 or 16 songs . or maybe a multi-disc compilation that will include some rare tracks . night ranger fans would surely delight to see something like that

## neg 51. music 609.txt

margin 6.51, 241 words

> i love this show ! that said , i do not care for this version of it . the inclusion of the word " concept " in the title means it is just that . this was , thankfully , not the final version of the show that would later spawn the hit song , " one night in bangkok " . with most broadway musicals , the musical numbers tell the basic story of the show . if you listen to the recordings of phantom , mama mia , beauty and the beast , you can discern the basic storyline of the show . listening to this particular recording of chess , though , will leave you wondering " what was that ? " the broadway arrival of chess saw a much needed reworking of the storyline and arrangement of the musical numbers . this recording seems too much like a mish-mash of songs that do n't really relate to each other . for musical fanatics ( like myself ) , i say " yes , you should have this recording in your collection " , if only to understand how much work went into the show before it opened on broadway . if you are only buying the album because of " one night in bangkok " , purchase the broadway recording instead ; you 'll be much happier with the performance by phillip casnoff rather than murray head

## neg 52. health 211.txt

margin 6.44, 546 words

> i use three razors . last year 's model of this braun , a triple blade rotary from the leading manufacturer of rotary razors and standard double edged disposables from the major manufacturer of razors . ok , now , let 's do some math . i get 10 great shaves from a disposable razor . i pay , on average , 40c or so for a disposable razor . that is about a nickel a shave including the shave cream . at a nickel a shave , it would take 3000 shaves before i would spend $150. would take me over 8 years . now , anyone that says any electric razor shaves better than a double edged high quality blade razor ( not even the expensive triple edged ones , just cheap disposables ) is dreaming . the blace does a much better job and much faster . but , sometimes , they can irritate the skin , but electrics can too . i can get irritated by both , sooooo , i rotate between them , and find that reduces my skin irritation problem quite well . i bought this braun ( last year 's model ) after reading the positive reviews here , and later bought a rotary razor . the basic difference is that the cheap model rotary from that major manufacturer is much quieter , shaves just as well , and cost me about 1 / 3 the price . the only thing that is better in the braun is the battery lasts longer . it is possible also , that in some cases , it gives a slightly closer shave than the rotary , but it also tends to miss spots no matter how many times i go over them . the braun also has a problem with my beard when it is longer , like when i have two to three days growth . the rotary and disposable razor breeze through that three day bush . the cleaning machine / charger that comes with the braun is a joke . yes , it cleans the razor great , but it is way oversized and you need a large space for it in your bathroom . even then , say you have that larger space , you can pay between $5.00 and $8.00 each for the cleaning cartridges . i have found they last about a month before drying out . add $60 to your annual cost to just clean your razor . the rotary cleans fine with a brush and the disposable razors with water . finally , the switch that turns on the razor is right where you hold the razor and it also locks the blade . so i am constantly locking the blade position by accident . inexcusable design flaw in a razor this price . do n't get me wrong . this razor shaves fine . it works best on short beards and works better than cheap razors . but for $50 you can get a better rotary razor and for $150 you can shave for over 8 years with a disposable twin blade . does the price difference sound rational to you ? if it does , click " proceed to order "

## neg 53. books 320.txt

margin 6.01, 124 words

> while it 's certainly true that there will always be a gulf between reality and words , communication between reader and writer is nonetheless very real and potentially profound , thanks in no small part to empathy and the imagination . deconstructionism , by denying presence and instead proposing unlimited differences between signs , dismisses any connection between readers and writers and turns language into a hermetic system separated from the outside world which is , of course , inhabited by people who read and people who write . this is exactly what makes deconstructionism so empty and hypocritical : it rejects traditional metaphysics while adopting a pseudo-mystical position which regards language as some unstable and solipsistic alien creature independent of everything and everyone

## neg 54. health 745.txt

margin 5.93, 136 words

> tried this product for 2 weeks ; it did improve the clarity and softness , but i found the product to be too scratchy and it did not rinse off well , seemed to have a sticky feel . since then , i found a wonderful microdermabrasion product called microdermx by nikkel holistic skincare . this product performs like magic ; it is not too scratchy and i can do a whole microderm treatment and not end up feeling like i 've been slapped with a wire brush . i can do the treatment 2-3x 's a week , ( like your supposed to ) but i also use it each morning as a cleanser and everyday is better than the day before . it is a magical product . bette hampton , chicago , i

## neg 55. dvd 472.txt

margin 5.91, 578 words

> this film starts with an event based on a true crime . a talk radio show host in denver was killed by an american nazi . ( this event inspired the " talk radio " play and film . ) this film continues with scenes from a small town in a farming region . no mention of their economic status ; are they losing dollars and population , small businesses , etc. instead we see a small group of white racists who abduct a black man to hunt and kill him ! this seems too exaggerated to believe . federal agents are aware of this but do n't want to act yet . their agent is sent back to get more information . there are groups like that in some sparsely settled areas . the film does n't explain what created them . it shows how some politicians try to use them for votes and contributions . no real names , of course . the federal agent meets to report to her higher ups . then we see terrorists prepare to hold up a bank to raise money for their activities ( based on real events ) . most bank robberies are done by ordinary criminals who are not part of any group . ( the fbi put an end to organized gangs that robbed banks in the 1940s . ) this federal agency does n't interfere because they want more information on their aims ( and their leaders ) . more terrorism is planned : dynamiting a courthouse , attacking a power station , etc. the terrorist plots here would keep this small group busy 24 hours a day ! kathy finds a secret list of " friends " . this is quickly copied with a camera . the federal agents need to know who this group will target so they can arrest them . gary meets with the leader ( who arrives in a helicopter ! ) and shows documents that say kathy is a special investigator . is kathy being served up as a sacrifice ? gary and kathy travel to chicago , where an assassination is planned that will make gary the fall guy . ( another lee harvey oswald ? ) a second " lone gunman " shoots the politician in front of a building . gary fails to shoot , and wo n't ever try this again . costa-gavras gained world fame with his 1969 film " z " . a few years later his film about rebels in south america was popular . his later films have seemed mediocre . a better story might not have tried to cover so many details and plots as this film does ; better pacing could help . the threat from domestic terrorism still needs a good film ( e.g. , timothy mcveigh ) . those who gave this film a high rating must love the images more than the facts . a better film today would show the bad results from " nafta " and " free trade " in harming most americans economically . but hollywood would never allow a film about this " war on the middle class " . the word ` nafta ' in greek and arabic refers to ` petroleum' . nafta is a symbol for the policies designed for big oil . it is like george w . bush calling his policy " operation iraqi liberation " .

## neg 56. music 40.txt

margin 5.85, 55 words

> having listened to steven 's previous albums , greetings from michigan and seven swans countless times , i cannot help but to notice the amount of regurgitation on this album . stevens blatantly rips off his own music . i consider michigan to be sufjan 's masterpiece . do yourself a favor and start there

## neg 57. camera 825.txt

margin 5.73, 104 words

> grainy iso 100 pictures at any light conditions . usage of 5mp and low sharpness options partially solves the problem , but if you take pictures with panasonic dmc-fz7 and compare ... it will be clear that a garbage trash is the right place for this camera . i had panasonic dmc-fz7 and the only cons . is really noisy high iso sensitivity mode . in fz8 camera panasonic implemented the venus iii processor ( fz7 has venus ii processor ) . as a result picture quality really improved at high iso sensitivity modes but dramatically changed for the worse in iso 100 mode

## neg 58. camera 298.txt

margin 5.61, 78 words

> i will keep this review simple . for the price this is an ok deal . however : the bag is a bit bulky and has no belt loop . the battery charger is finicky and has below average build quality batteries are generic rechargeables . you are better off finding a bag that fits your needs perfectly and picking up a separate charger / batteries . it will wind up costing you less in the long run

## neg 59. books 852.txt

margin 5.59, 104 words

> a useful book that provides a good summary comparing differing accounting standards and approaches between countries . however , it is not worth the price . it is supposedly written for later year undergraduate and masters accounting students . it is more suitable for general second year accounting students . plus , as i am working with a multinational european bank in japan , the book is , rapidly becoming , out of date . there is none of the simply but incisive commentary which can be found in other books about the differences and outcomes of general accounting principals drawn from different countries

## neg 60. dvd 121.txt

margin 5.38, 80 words

> appleseed suffers from the problem most big budget , cgi enhanced anime theatrical releases have : gorgeous visuals , but a incomprehensible story filled with dull cliche dialog . trust me , i was sucked in by the amazing trailer like most of you . i wanted this to be a great movie ( as i am a fan of the oav animated series ) . appleseed is worth seeing for the visuals alone.. . but that is about all

## neg 61. dvd 223.txt

margin 5.25, 151 words

> those of you who remember ryan starr from american idol know why she quickly became " has been " material for vh1 's the surreal life . ryan starr also happens to be the worst actress i have ever watched on film , television and or commercials . the director must have agreed with me becaue there are very few shots of ryan that last more than 10 seconds at a time . her dialogue is kept short and simple , and when she does have more than 3 lines at once , the complete lack of feeling , expression & emotion in her voice makes you consider turning off the movie and doing something worthwhile , like cleaning out the fridge or picking at your hang-nails . that is all i can say , i would really like to put this movie behind me and never speak of it again

## neg 62. books 697.txt

margin 5.22, 97 words

> this book contains reproducible mini-books , bingo cards , flash cards , some word search puzzles and fill-in activities . in my opinion , the fill-ins are a bit too challenging . i even had trouble with them . the only thing in this book really " worth it " that i could n't make as well myself , are the mini-books . the mini-books each contain several different sight words , so they seem to me to be more effective for review of words the student has already learned than in the initial learning of them

## neg 63. camera 164.txt

margin 5.22, 271 words

> i love canon products and i have had a complete canon system for about 10 years . i love everything canon does . however i do not understand canon 's reasoning behind producing this lens . the reason for the ef-s lenses is offering wider angle by getting the rear elements of a lens closer to the " film " plane . they cannot do this on film and full frame sensor cameras because the mirror is larger and would hit the rear elements of an ef-s lens . they have indicated , however , that by 35 mm that advantage is gone . why then do they produce a 60 mm macro lens when they already have their macro requirements covered with they current three lenses ? i would guess that the short back focus makes the lens cheaper ; but this lens is only $60 short of the excellent 100 f2.8 usm macro . as i said , if for $60 i can get a lens that has 40 mm more reach ( 66 in 1.6crop cameras ; useful in macro photography ) and that works on all canon cameras , i 'm not going to be thinking about this lens at all . granted , you might not be thinking of buying a ff camera anytime soon , but canon has indicated that eventually they will have ff on all their dslr 's , so why bother with this lens ? the 17-85 or 10-22 are very reasonable offerings for the ef-s lineup , but the 60mm macro does n't make any sense to me . my $0.0

## neg 64. music 658.txt

margin 5.16, 109 words

> like so many new-age artists , ryan farish has a great ear for melodies . unlike most new-age artists , ryan farish has rhythmic problems . he likes to use the delay effect on his piano , but either it is not sycronized with the tempo of the song or he is simply being too sloppy with his playing ( sometimes it 's one problem and sometimes it 's both ) . i do n't know how he let those takes make it on to the final album . also , the massively loud reverse cymbal sounds are way overused and make the entire album very abrasive very quickly

## neg 65. health 9.txt

margin 5.11, 38 words

> the monitor works really well . the functions are a bit limited from the perspective of calorie counting and fitness tracking . if you are looking for a good basic monitor , this is a great unit .

## neg 66. health 701.txt

margin 5.04, 264 words

> to get hot lather , which is nice , you first have to get the device installed on top the can . i would not recommend this if you are easily frustrated . the directions provided are sparse in several languages . first you have to pry the top off the can of shaving cream . they provide a pry tool for that purpose which works well on some brands of shaving cream better than others . then you have to fit the device on top the can . it worked well with one brand in a large size can . when i tried it with a smaller size can of shaving cream it emptied half the can during the installation process . using a different brand in a large can , i had trouble prying the top off the can . if you have time and patience , and are willing to spend some money on various brands of shaving cream to find one that works well , give it a try . otherwise , be forewarned it may lead to frustration and bad language . it would be nice if companies intending to sell products in the us ( apparently manufactured somewhere in asia ) would provide a clear set of instuctions in english , in reasonable large readable type , with illustrations . in this case , they need to clearly specify the type shaving cream can the unit is designed for . i do not need instructions in foreign languages , and get tired of limited instructions in six languages

## neg 67. books 647.txt

margin 4.98, 169 words

> as far as style goes , i found this pretty boring from what i saw in the bookstore . glad i never bought it , races of eberron is much better , as it has three great races ( fourth is n't so hot ) including one living construct type . in fact , from races of eberron i made one changeling druid who has near complete cold adaptation and heat adaptation ( from environment series ) , and a warforged monk which was effective against lycanthropes . what can races of the dragon possibly give you ? flying creatures ? firebreathing creatures ? you could be better off with weaked-down angel or better yet just a birdfolk race ( like raptorans in races of the wild , which by the way also has more variety with its catfolk ) . as for firebreathing , a feat could probably give you the whole fire-eating / fire-blowing act and save you the whole freakish thing of having weird blood .

## neg 68. health 454.txt

margin 4.93, 99 words

> i really wanted to love this fragrance...after all , it is quite expensive and i 'd read rave reviews on many websites...but after one spritz i sold it to a friend of mine ! my favorite perfumes are beyond paradise , ralph lauren romance , ralph lauren style , and dkny be delicious . light blue , to me , smells overwhelmingly of musk . i wore it all day and i ended up feeling nauseous , with a bad headache . this must be one of those perfumes that works well on most everyone else except for me

## neg 69. music 253.txt

margin 4.77, 650 words

> i first became a fan of the gorillaz with their excellent 2nd cd , demon days . the interesting thing about this band is that their music is so strange and so " out there " that when you first hear one of their cd's ...it sounds like complete garbage . but once you listen again and again , you start to like it more and more . eventually you end up really liking the cd . that was the case with demon days . after enjoying that cd fully , i thought i should check out the first gorillaz cd , and i did n't like it all that much . there just seems to be very little actual songs on the cd . way too much of it sounds like complete filler . there were a couple throwaway songs on demon days , but most of the stuff on that cd was great . here , we 've got songs that are just...boring . nothing happens . i was waiting for the melody or a cool tune to occur in some of these songs , but it never happens . you just listen to 2-d whining into the microphone with dull beats in the background . ( such as on songs like new genious , man research , and starshine . ) some songs are nothing but beats with no lyrics at all , sometimes sounding just like static noise . songs like this , such as double bass , are cool for a minute or two , but the song drags on for practically 5 minutes . it gets boring . other songs , like 5 / 4 , m1 a1 , and rock the house are catchy at first , but just do n't have staying power . they get old . 5 / 4 got annoying quickly , m1 a1 and punk lost their appeal quickly , and rock the house is another song that would have been better if they cut about 2 minutes out of it . and songs like latin simone are just annoying . the remixes of 19-2000 and clint eastwood that end the cd are also fairly forgettable , although 19-2000 's kind of catchy on the first couple listens . there are some good songs here , though . tomorrow comes today , clint eastwood , gravity , 19-2000 , and left hand suzuki method are cool songs . slow country 's kind of cool , too . and dracula 's got an awesome , almost haunting sound to it , and it 's really absorbing . although it too , unfortuantely , loses its tune and turns to repetitive and aimless techno noise about half way through it . this small collection of good songs , though , is surrounded by a huge collection of filler tracks . much of this cd just is n't really that good . i do n't know...this cd just seemed empty . very few meaningful tracks , lots of filler , and some really annoying and repetitive songs . some good songs were stretched to almost 5-minutes long , mostly given filler techno beats that ruin the songs . clocking in at 72 minutes , ( which makes it 22 minutes ( ! ) longer than demon days ) this cd was loaded with filler and just not enough good stuff . people interested in the gorillaz should pick up their superior follow-up , demon days , instead of this one . if i listened to this debut cd first , i probably would n't have ended up liking this band very much . the good news about this is that the gorillaz have not hit a sophmore slump ; their cds are getting better , not worse . that is a great sign for the future of this awesome band .

## neg 70. music 44.txt

margin 4.77, 650 words

> i first became a fan of the gorillaz with their excellent 2nd cd , demon days . the interesting thing about this band is that their music is so strange and so " out there " that when you first hear one of their cd's ...it sounds like complete garbage . but once you listen again and again , you start to like it more and more . eventually you end up really liking the cd . that was the case with demon days . after enjoying that cd fully , i thought i should check out the first gorillaz cd , and i did n't like it all that much . there just seems to be very little actual songs on the cd . way too much of it sounds like complete filler . there were a couple throwaway songs on demon days , but most of the stuff on that cd was great . here , we 've got songs that are just...boring . nothing happens . i was waiting for the melody or a cool tune to occur in some of these songs , but it never happens . you just listen to 2-d whining into the microphone with dull beats in the background . ( such as on songs like new genious , man research , and starshine . ) some songs are nothing but beats with no lyrics at all , sometimes sounding just like static noise . songs like this , such as double bass , are cool for a minute or two , but the song drags on for practically 5 minutes . it gets boring . other songs , like 5 / 4 , m1 a1 , and rock the house are catchy at first , but just do n't have staying power . they get old . 5 / 4 got annoying quickly , m1 a1 and punk lost their appeal quickly , and rock the house is another song that would have been better if they cut about 2 minutes out of it . and songs like latin simone are just annoying . the remixes of 19-2000 and clint eastwood that end the cd are also fairly forgettable , although 19-2000 's kind of catchy on the first couple listens . there are some good songs here , though . tomorrow comes today , clint eastwood , gravity , 19-2000 , and left hand suzuki method are cool songs . slow country 's kind of cool , too . and dracula 's got an awesome , almost haunting sound to it , and it 's really absorbing . although it too , unfortuantely , loses its tune and turns to repetitive and aimless techno noise about half way through it . this small collection of good songs , though , is surrounded by a huge collection of filler tracks . much of this cd just is n't really that good . i do n't know...this cd just seemed empty . very few meaningful tracks , lots of filler , and some really annoying and repetitive songs . some good songs were stretched to almost 5-minutes long , mostly given filler techno beats that ruin the songs . clocking in at 72 minutes , ( which makes it 22 minutes ( ! ) longer than demon days ) this cd was loaded with filler and just not enough good stuff . people interested in the gorillaz should pick up their superior follow-up , demon days , instead of this one . if i listened to this debut cd first , i probably would n't have ended up liking this band very much . the good news about this is that the gorillaz have not hit a sophmore slump ; their cds are getting better , not worse . that is a great sign for the future of this awesome band .

## neg 71. dvd 53.txt

margin 4.70, 106 words

> the story here dose n't matter . the main characters fuse into a missle of meth and insanity towards an explosive ending . scwartzman escapes his fate temporarily and murphy is blessed with a reprieve but rourke pays the full price for his evil concoction , meth . quirky directing and film editing can be somewhat distracting but not meaningless . roberts is so gay you want to smack his face . he an rourke have history on film and play out their familiarity . rourke is phenomonal again as an immoral genius , a role he plays better than anyone today in film . br

## neg 72. music 382.txt

margin 4.58, 201 words

> i gave 2 star for this cd not because of the musical quality...but because the last song " goodnight my love " is cut short on this cd . after watching the live performance on cable , i rushed out to buy this cd , labeled by hybrid . only to find out my favorite song " goodnight my love " was cut short . on the cd , it ends with the sax doing a solo then fades away....which leaves the song dangling and unfinished ! ! ! on the video , this song ends with art singing " bring you closer to me " and the music slowly ends beautifully , correctly . there 's a version out which was released by sony in 2003. i do n't know if this version contains the full song . the hybrid label version is simply ridiculous ! ! ! how can you possibly end such a beautiful song short ! ! leaving it unfinished....and well....short and listeners wanting more ! ! ! if someone can verify if the sony conatins the full " goodnight my love " ...or tell me where i can get this verson , would really appreciate it

## neg 73. music 199.txt

margin 4.56, 71 words

> i really liked this when it came ut on vinyl , but in retrospect , it was the cause , not the music . b . raitt is grand , g nash with an excellant cathedral , j c young , and the highlight to me we almost lost detroit by the great gil scott-heron . but the second disc is second rate . edit the filler and it rates higher

## neg 74. books 508.txt

margin 4.49, 373 words

> i 'm a wiccan who formally practices within a traditional gardnerian coven , but practices eclectically within my private practice . i read this book because i had heard that it was recommended to my local library by a christian ; purportedly , wicca 's charm was written by an impartial writer . immediately , you realize that this is n't true . catherine sanders has a clearly stated agenda : that wiccans are simply misguided and misunderstand that what they long for is offered by christianity . i could write a long review debating the merits of sanders ' arguments . instead , i suggest that you consider this if deciding whether to read this book which sanders claims to have thoroughly researched . she relies on the writings of margot adler , carol christ , starhawk and phyllis curott ( with barely a nod to scott cunningham and ronald hutton ) to draw many of her conclusions . yet , missing from her notes are such writers as the farrars , merlin stone , raymond buckland , isaac bonewits , patricia crowley , and the matthews , to name just a few outstanding contributors to neopaganism 's base of knowledge . too often , sanders relies on the statements of young wiccans she interviewed who come across as silly and naive . in another case , she bases her thesis that women 's spirituality ( e.g. , goddess worship ) is misguided and that christianity fits the same spiritual needs that women are seeking via one speech that she heard margot adler give shortly after 9 / 11. sanders requests both christians and neopagans to read her book with an open mind . a fair request . but as you 're reading , closely check out her endnotes and analyze for yourself if this book was truly researched with objectivity in mind , or whether sanders limited herself to sources that would support her belief that christianity has everything that a wiccan desires . one needs to go no further than to consider that as sanders attempts to persuade the reader that christianity has always embraced the value of women that not once does she analyze the epistles of paul .

## neg 75. music 745.txt

margin 4.40, 146 words

> certainly this album offers very little to a fan of the ocean blue 's eariler work . the vocals and guitars sound quite different ( gone is that beautiful dreamy sound ) . and what about those awesome saxaphone and keyboard sounds that made their earlier tracks so fun ? just because steve lau is gay is no reason for the band to abandon keyboards altogether . so , anyway , what does this album offer instead ? harder sounding guitar , angrier sounding vocals , and songs that are somewhat intersting , but are lacking in any magic that would make you want to listen to them after you 've had the cd for a couple weeks . exceptions : & quot ; whenever you 're around&quot ; , and & quot ; slide&quot ; are good enough songs to standout inspite of boring production

## neg 76. health 161.txt

margin 4.39, 307 words

> razor blades are expensive enough as it is , and the trend of " more is better " has reached almost ludicrous points in the industry . what 's that ? five blades , you say ? why , it must be better than four ! meh . i have fine stubble which grows in at varying angles across my neck . the good news is that , while other razors have always been unable to remove all of my stubble on the first try , this blade does , in fact , take care of the problem . in addition to this , it aggravated the skin quite a bit ( this might have as much to do with the vibrating action as with the five blades ) . the precious soothing-aloe strip had little to no effect on my skin ( particularly in the neck area ) . if you have sensitive skin at all , this might not be the razor for you . contrary to the experience of others , however , the extra " trimming " blade worked well for me when getting the spots along the edge of my mouth , under my nose , and when shaping my vast hedge-like sideburns . however , the five blades on the other side dulled remarkably fast . considering my rather fine hairs , i 'm used to exchanging blades once every week or so . now i 'm exchanging them twice a week . seeing as how this product is already so much more expensive than competitors ' products , and seeing as how it is designed to work exclusively with the fusion razor ( and vice versa ) , and seeing as how its lavish wealth of cutting action has clawed at my skin , i find it hard to recommend

## neg 77. health 805.txt

margin 4.37, 74 words

> unfortunately total block did not work well with my rosacea sensitive skin . it caused my skin to become very red and irritated by the end of the day . i do n't doubt this is an excellent sunblock , just not for my rosacea sensitive skin . i use it now on my arms with no problems . i do feel it is very expensive for so little product so will not repurchase

## neg 78. books 738.txt

margin 4.20, 109 words

> if this man took a the time to know the history of u.s. involvment in panama he would know that it was the u.s. that put noriega in power in the first place.it was also the u.s. that killed the previouse leader of panama , omar torrijos.who apposed u.s. control of his county . the united states has used panama for its own gains without regard for the freedom or rights of the panamanian people since the take over of the country by president roosevelt in 1903. one of many good books about the truth of panamanian history is by john perkins " confessions of an economic hitman "

## neg 79. books 99.txt

margin 4.05, 58 words

> less a view from afar or broad exposure of solitude from the human condition , this book more aptly excerpts the author 's personal conflicts with human relationships.....a one-on-one wrestling match with the self with no spectators and no judges . the book is a good read for academic analysis , but not so fun for venturist philosophy

## neg 80. dvd 356.txt

margin 3.96, 62 words

> the original csi series is fantastic because you figure out the crimes by finding the evidence . this series uses the csi name without the investigating that makes the original so good . it is mainly a mellow-drama surrounding the lives of the characters . some people will like the drama the writers have put togethor , but there 's no mystery

## neg 81. software 503.txt

margin 3.82, 52 words

> aquazone is good , but i 've found that serene scene is a better product . aquazone is not as realistic as serene scene and that is what i was looking for . the realism of fish in an aquarium . if i could go back i would buy serene scene instead

## neg 82. music 31.txt

margin 3.80, 167 words

> i think india is one of the most talented artists today . her voice is sensational . sadly , as with many great artists today , this album feels more producer / market-driven rather than artist-driven . i understand that regaetton is popular right now . i would even understand including a few reggaeton-flavored songs to " keep up with the times " ( shakira 's " la tortura " comes to mind ) . but who mixes two genres within a single song ? ! ? " soy differente " flows perfectly as a salsa , until regaetton beats come in . the style feels very out-of-place in this song , as in most other songs in this album . maybe this kind of thing will work at a club , but not for extended listening . in my opinion , the producers are making this album more marketable while stiffling india 's own style . i hope she will regain contol by the next album

## neg 83. books 96.txt

margin 3.74, 493 words

> the amount of violence in this book is excessive over relatively insignificant motives . i had a hard time believing all this was happening in 1948. i am not questioning mosley 's portrayal of racism . however , i did a little research into just how violent place los angeles was in 1948 , and the answer is not very . there may have been poverty , racism , alcholism , but l.a. county seemed pretty safe ; the late 1940s had some of the lowest homicide rates since as far back as one researcher was able to find , 1827 ! mosley may have been more familiar with l.a. of the 1970s and 1980s and just assumed that it had always been that way . throw in speakeasies , gangsters hijacking liquor trucks , and one gets the impression that mosley is confusing the 1948 with 1928. i am not so pedantic as to insist that fiction be historically accurate . but many , many people hail mosley for depicting a dark side of life / era / place that had not been shown before . from what i can tell , he has simply combined stereotypes from the 1920s and 1970s ( i guess those years average to be about 1948 ) . mosley is depicting a fantasy world of his own creation . however , i doubt he ever tried to pass it off as authentic , and i hope readers realize that it is not . easy rawlins in this novel falls into the rather weak , but unfortunately large , group of fictional detectives that actually accomplish little detecting . a detective actually solves a mystery using his own intellect ; that is interesting to read . detectives in less skilled hands solve mysteries via confession . easy does solve one of the murders on his own , but just about everything he " solves " is simply confessed to him . i find that extremely dissatisfying . mosley has packed the book with violence , but seems to know very little about violence himself . none of the fights are well described . easy , for being a self-professed " killing machine " ca n't actually fight worth a damn and is surrounded by guns but does not apparently know anything about them . they are either big or they are small . he does not come of as being hard-boiled , but rather a pathetic braggart mosley does show signs of being a very good writer . but i think he is too far over his head in this genre to come up with something exceptional . i imagine that his work must have improved , but this effort is nothing to get exceited over . and again , i do n't obsess over accuracy , but a little bit of research would have gone a long way in firming the foundation of this novel .

## neg 84. books 342.txt

margin 3.65, 688 words

> i 'd never read berry before , but as far as i can tell , this brief collection of six essays and lectures sticks to familiar territory . however , it 's probably not the best entry point for people who are newcomers to his realm . there are two related problems with the book : one of presentation , and one of tone . the problem with presentation is that the pieces are so short that there 's no room for specifics . so , while one might be more or less in accord with the broad strokes of berry 's vision , there 's no detail to back it all up . the problem with tone is that from the very first page the reader feels like they are being lectured at . of course , some of the pieces are lectures , but there 's a certain condescension that runs throughout the book . it comes out when berry uses certain words such as the three as of " appropriate " , " authentic " and " adequate " . when these are used ( as they often are ) , there he 's obviously made some kind of value judgment , but the reader is never let in on it . the end result of the two flaws is that the reader feels like a hectoring argument is being made without any supporting logic - - which ultimately smacks of preaching to the choir . which is unfortunate , since i tend to agree with berry on a lot of things ( though not his anti-abortion stance ) . small farms are good , agribusiness is bad , stewardship of the land is good , extraction industries are bad , treating the body as an organic whole is good , and things of that nature . alas , he has a tendency of making sweeping assertions and accusations that are far too simplistic and shrill to be useful . two examples from the first 15 pages will suffice to illustrate : " this is a world in which the cultures that preserve nature and rural life will simply be disallowed . " and " communists and capitalists are alike in their contempt for country people , country life , and country places . " berry also succumbs to the trick of creating straw men to counter his theses . for example , in one essay , he claims that conservationists are people who want to simply preserve land in a pristine , untouched state , and that 's all . while there are certainly some conservationists who feel that way , they are a small minority of a a much larger community who actually is in almost total accord with berry 's views on stewardship and land use . it certainly does n't help matters that his view of small-scale farming appears to be heavily tinted with rose-colored glasses . his claims that modern agribusinesses has rendered the small farm economically unviable sounds like a reasonable proposition . however , it ignores the fact that , historically , small scale farming ran on the thinnest of margins , was subject to all kind of external instability ( weather , vermin , etc. ) , and operated on only slightly better than a subsistence level . in farming , cash is scarce , that 's why people abandoned it in droves whenever the opportunity presented itself , such as in wwii , when all those defense-industry factories were opened in california . ( of course , in berry 's vision , you do n't really need cash , because you barter for everything you need from your neighbors . ) berry 's exhortations to create small-scale communities is worthy stuff , and even in cities people are creating this . the growth of csas , farmers markets , and the like in the past decade is a tangible indicator of this . however , to achieve the large scale results berry seeks requires a more rigorous roadmap than what is provided in this slim collection

## neg 85. health 947.txt

margin 3.58, 111 words

> i 've used the cardiochek 6 times , and had my cholesterol checked at a doctor 's office during the same period . my cholesterol levels according to the doctor 's tests are always around 200. with the cardiochek they vary by as much as 90 points . it is a lot of trouble ( and expensive ) to purchase 3 sets of test strips and stab myself 3 times to test total cholesterol , hdl cholesterol , and triglycerides . no test strips are included in the package when i purchased the cardiochek . the box says " includes check strips " but those are something other than test strips

## neg 86. camera 613.txt

margin 3.58, 259 words

> i am far from an expert however even for an amatuer this lens was horrible . i took about 400 shots with my digital rebel xt and got so frustrated witht the poor quality of the auto focus that i immediately returned it / got a refund . in all but the brightest lighting conditions this lens was extremely slow with the autofocus . in many cases the lens could not focus and continually hunted through it 's entire range . since most of my photography is of animals i simply could not wait for the autofocus to work and missed many shots . i tested the autofocus against my canon 18-55 ef-s ( packaged with the rebel xt ) and a canon 75-300 ef . in every instance where the tamron could not focus the canon lenses had no problem ! when the tamron would focus i found the pictures were not as sharp as my canon lenses . again i 'm far from an expert however i was only printing 4x6 photos . i replaced the tamron with a quantaray ( sigma ) 55-200 dc which has proven to have a very good autofocus and great optical quality ( for amatuers. . ) bottom line. . it was hard to part with the tamron because i was really enthused about the zoom range however i would much prefer to use 2 lenses can focus than 1 that doesn't . i have read many reviews with the same problem noted . tamron needs to get thier act together

## neg 87. music 588.txt

margin 3.51, 561 words

> released by atlantic five years after it appeared in australia , presumably to meet high demand for ac / dc 's music , this international version of " dirty deeds done dirt cheap " is a farce . once again , somebody had the rather strange ideas of altering the song sequence , and replacing both " r.i.p. ( rock in peace ) " and " jailbreak " , two of the strongest numbers in the album 's aussie version , with t.n.t. 's " rocker " and " love at first feel " , an ok , if not spectacular song . ah , and " problem child " , already featured in atlantic 's version of " let there be rock " , is also included in here . the same song in two different " official albums " . marvelous ! . oh yeah , and somebody hired hipgnosis in order to re-design the front and back covers . that was a cute detail , but the aussie version 's covers ( classic mid 70 's cartoonish artwork ) are far more appealing . who 's to blame for this rip off ? . somebody at atlantic records ? . some members of ac / dc ? . maybe both ? . who cares anyway ? . once again , now that i 've got used to the aussie album , listening back to this " product " feels worse than a hangover from consuming adulterated , low quality spirits . every enthusiastic record collector knows that both warner music and sony music are serious labels that took , and still take risks , by signing up cutting edge artists and by respecting their will . so , it seems that , with their approval of this re-issue , the surviving members of ac / dc are the ones to blame for this farce to go on , and on , and on ... if this is so ... well ... guys , we , the fans made you filthy rich . we deserve the " real deal " , available worldwide , at a " reasonable price " . i only give this " product " a 2 star rating , just because " love at first feel " remains unreleased in australia . how unusual ! . a final word about this re-issue : i do n't own it . in the words of pete townshend , i " wo n't get fooled again " . in order to get bonus material , you must go through an irritatingly cumbersome internet gimmick . if bon scott ( undisputedly the band 's most uncompromising member ever ) , was still alive , i believe things would be different . by the way , if you are interested in the real stuff , please be so kind as to read my review of " dirty deeds done dirt cheap " ( import ) . other items to be avoided : the skimpy " retrospective " ep " ' 74 jaibreak " , and " bonfire " , a rather steep box set in which at least 6 songs are repeated twice , in different versions . none of these titles include all the songs left out by the adulteration of ac / dc 's first four aussie albums

## neg 88. camera 994.txt

margin 3.35, 176 words

> sure my canon sd-30 is super cute and i get lots of compliments on how small and sexy it is , but heaven forbid you want to take pictures with it ! ! this camera cannot take pictures in low light at all ! every picture i 've taken at parties has been out of focus , which adds up to a lot of hazy photos of great memories . i took it back to the camera shop and the guy said i had the setting right but " yeah , they do n't work well in low light . " well if i needed a bright sunny day for every shot i could make a pinhole camera out of a cardboard box ! the pictures it takes in daylight are nice . but anyone who wants a tiny little camera like this is planning on putting it in their pocket and taking it to parties ! i got the sony cybershot 10.1 and it takes great pictures in low light . later , canon .

## neg 89. camera 15.txt

margin 3.23, 168 words

> as a professional photographer , i find myself going through 5-6 of these cords each year . my equipment is my livelyhood and although it is used often , i am exceptionally careful with all of my gear and do not bang it around or abuse it . i use a stroboframe which makes it necessary to use this cord to raise the flash well above the focal plane of the camera . these cords are very expensive to get just a few months out of them . eventually , the hot shoe connector will either become loose and the connection will no longer function or the plastic connector will break and your flash unit will fall to the ground . ( this has happened twice to me and fortunately i was able to catch the flash unit ! ) the cord is indespensible if you need it , but contact canon usa and ask them to reengineer this cord or expect to replace them every few months

## neg 90. camera 174.txt

margin 3.23, 168 words

> as a professional photographer , i find myself going through 5-6 of these cords each year . my equipment is my livelyhood and although it is used often , i am exceptionally careful with all of my gear and do not bang it around or abuse it . i use a stroboframe which makes it necessary to use this cord to raise the flash well above the focal plane of the camera . these cords are very expensive to get just a few months out of them . eventually , the hot shoe connector will either become loose and the connection will no longer function or the plastic connector will break and your flash unit will fall to the ground . ( this has happened twice to me and fortunately i was able to catch the flash unit ! ) the cord is indespensible if you need it , but contact canon usa and ask them to reengineer this cord or expect to replace them every few months

## neg 91. health 366.txt

margin 3.17, 211 words

> i have found another product that i want to recommend . it 's called alert and is sold by consultants like avon , but you can also go the starlight website and order it . it 's a nutritional supplement and for me does provide energy without the jitters , and as a bonus i do n't feel hungry when i 'm using it . they also have a product specifically for weight loss . i have tried that as well . i did feel a bit jittery at first.. . but it settled after a week or so of taking it . i would recommend it also . i used it a few years ago and lost 35 lbs . i did consistent diet and exercise which obviously is what did the weight loss , but i credit the supplement with giving me the energy to get moving and helping me curb cravings . i 'm now looking for energy and help maintaining that weightless so for me the alert does both of what i need ... energy and hunger control and it 's less expensive than the weight loss supplement so i now use it . i 've used this for years and have not had any problems .

## neg 92. camera 438.txt

margin 3.17, 51 words

> very easy to set up , but no matter what i did , i got several horizontal interference bars . one very nice feature is a built in video modulator that allows you to connect to older tvs using a coax cable instead of rca . i am returning this product

## neg 93. books 47.txt

margin 3.17, 67 words

> if you are interested in a very traditional approach from a professional photographer , this book will provide lots of information . it also provides valuable tips about controlling the dog . but for my taste , i found the photographic results to be uninspiring - too much posing , too much portraiture lighting , not enough of just plain capturing that wonderful dog as it is

## neg 94. music 718.txt

margin 3.12, 92 words

> i 'm a big fan of great big sea and i purchase everything they release . apparently they were trying to give this cd the " feel " of a live , medium-size venue performance . unlike their other live dc offerings , this one sounds like it was recorded with a micro-cassette tape in some fan 's front pocket . it does n't give justice to their usual great vocals and unique sound . overall , i was pretty disappointed and i 'd recommend their earlier offerings over this one .

## neg 95. music 540.txt

margin 3.12, 100 words

> as a contemporary of joan baez ( age-wise ) , i loved her early music and the power of her incredible voice . i even empathize with much of her politics , but unfortunately it 's time she rested on her laurels . her voice on this cd is quite far removed from what she was once capable of , and in fact i would have to say that there is no comparison between her vocal ability on bowery songs , and her earlier quality . like some professional athletes , she seems to not know when to quit.. .

## neg 96. software 561.txt

margin 2.99, 21 words

> while there are many benefits to learning vocabulary with this tool , i found it did not help with conversation .

## neg 97. dvd 911.txt

margin 2.94, 69 words

> i also found this " best of " collection to fall very short of the " best " ! there are clearly many other episodes they could have , and should have used and included to make this truly a " best of " feature . the few cases they did showcase were by far not the scariest ! a definite disappointment , ...though still a fan ! !

## neg 98. books 839.txt

margin 2.92, 140 words

> as a young woman i was appauled by gurian 's lack of respect for women as human beings.what makes me the most furious is his shadowy writing which can lead a young woman to think she is only worth something if she squishes herself to allow the boys and men to take the lead in life.the resounding message is girls and women are potentially inferior and cannot because of our hormones make important contributions to society beyond traditional roles.i do n't remember ever being taken over by hormones and rendered down to a emotional bundle of primative chemical reactions he believes all females to be . i agree with posters about this bridge brain foolishness.gurian is a master at twisting words around and you have to read his books being mindfull of his tricks.his book is full of agenda .

## neg 99. camera 7.txt

margin 2.82, 57 words

> the bag is suppose to hold two cameras , i have a rebel and two lens and cant fit them in with lens filters and extra batteries . i recomend you buy a bigger bag it does not meet the billing here . might be good for a couple of point and shoot cameras but not sl

## neg 100. music 769.txt

margin 2.74, 57 words

> these songs are hacked up versons of rick 's music . i played it a couple of times until i got the library of original lps . the lps are better . at least they carry full versions of songs . i pass on rick and this package . rca cheats people out of good music. .

## neg 101. software 499.txt

margin 2.66, 76 words

> i found this software very difficult to use . it does not have any " stop " or " go back " button . the only way to exit an activity is to hit " esc " button to exit the program and then start all over . when starting over , there is a very lengthy annimated introduction you have to go over each time and i could not find a way to skip it

## neg 102. dvd 985.txt

margin 2.61, 62 words

> i 'm not a fan of stephen king film adaptations . the only one i like is carrie bec it was directed by brian depalma and featured terrific performances by sissy spacek and piper laurie . cujo is boring and not all that suspenseful . i could n't wait for it to end . not worth purchasing . okay as a rental

## neg 103. books 655.txt

margin 2.59, 144 words

> this book is a standard one for graduate-level algebra courses . i practically wore mine out over a year-long course , and came to know it intimately . dummit and foote is a book that teaches via wordy explanations and lots of examples . of course , examples are very important . however , the explanations are often muddled and not clear ( e.g. see tensor products ) . they frequently relegate important theorems or definitions to the exercises , and the organization is poor . consequently , it can be very hard to find things later when you might need them . also , the bindings on this book frequently fail . my book fell apart very quickly , and i know other students who had the same problem . i recommend rotman 's advanced modern algebra instead of dummit and foote .

## neg 104. dvd 230.txt

margin 2.56, 37 words

> robin trower has really lost a lot of his playing ability , same sound but no blazing licks and just a lot of trickery . two stars for the music and his new vocalist is quite good

## neg 105. dvd 154.txt

margin 2.54, 78 words

> " modigliani " ( 2004 ) is a self-indulgent , pretentious and largely fictional portrait of a tragic artist . writer-director mick davis goes overboard on the symbolism while revealing precious little about the man and his work . ironically , the viewer has a better understanding of pablo picasso than amedeo modigliani . despite his boundless enthusiasm , andy garcia is simply too old for the title role . an irritating fiasco that deserved its straight-to-video fate

## neg 106. camera 694.txt

margin 2.53, 73 words

> this case looks good and protects the camera adequately , but is too bulky . it has n't got a lot of room inside - i was unable to fit an extra sd card in its little case and a spare battery . the belt clip is difficult to use , and i end up carrying the case in my hand most of the time . there are better cases for this camera

## neg 107. health 614.txt

margin 2.48, 18 words

> the mirror 's light is quite dim and the magnification ( 5x ) is inadequate for most purposes

## neg 108. music 315.txt

margin 2.48, 61 words

> " what 's up " , the catchy song with the acousitc guitar out of tune ( which , i always thought , would have been the perfect song for heart ) , is the only thing good here . the rest of this album is a mess . linda perry has , of course , gone on to better things

## neg 109. dvd 480.txt

margin 2.47, 154 words

> as the us european command a-2 ( director of air intelligence ) during this phase of the disintegration of yugoslavia , i was surprised to see the ending - - what happened to the admiral and pilot . historical ? no way ! the only plane shot down was a single-seat us air force f-16 pioted by capt mcbrien ( sp ? ) while on combat air patrol ( cap ) , no cameras . some naval f-14s carried film-loaded cameras in pods , but most of the imagery pin-pointing mass graves came from u-2s and satellites ( and good coordination with french peacekeepers on the ground ) . so , this movie was fiction . it could have conveyed a better message , a better review of the decay of the former yugoslavia and the dominant role of serbian forces . but the producers decided action via fiction was better than learning fact

## neg 110. books 877.txt

margin 2.44, 96 words

> i found it to lean very heavily towards a hierarchal view of the relationship between men and women . men are to rule , and women are to submit to that rule . the authors appear to see women as perpetual children who need to be under the continual domination of men , rather than as adults who deal with men on an adult level . i suggest anyone who reads this books should also read " discovering biblical equality . " it gives another view of how the christians world see the role of women

## neg 111. camera 214.txt

margin 2.41, 30 words

> boy , this is way too much to pay for a hood on this lens . it 's a great a lens , but this is hardly worth the price

## neg 112. camera 101.txt

margin 2.41, 30 words

> boy , this is way too much to pay for a hood on this lens . it 's a great a lens , but this is hardly worth the price

## neg 113. camera 949.txt

margin 2.35, 141 words

> i received this as a christmas present . this digital camera works fine for still shots , pictures of my family , etc , but for action shots , kids playing outside , basketball games , etc. it is a big disappointment . i took 47 pictures of my son playing basketball in our school gym and only 5 of them were worth keeping . i 've taken to several games / activities to try it out . i 've tried using the different functions , adjusting the manual setting , and playing with the zoom but nothing has worked . many of the shots are blurred , have shadows ( because of movement ) , or are so dark the people ca n't be seen . i wish i would have known this before i asked for this camera .

## neg 114. camera 841.txt

margin 2.34, 69 words

> this camera has a very poor lens . at 1x zoom , the barrel / spherical distortion is enormous ; try taking a picture of a tiled wall . image quality is also so-so when a picture is viewed at 100% ; scaled down on a computer monitor , the quality is ok . color fidelity is next to nothing when using flash and auto white balance . [...]

## neg 115. dvd 972.txt

margin 2.27, 191 words

> first of all , who was the spastic genius who decided that concert films had to change camera angles every five seconds ? this is terribly anoying , especially when every third shot is of the same audience members . this may be fun for a home video , but not for a mass marketed commercial release . the dance hall crashers are an awesome band . much of the fun of seeing the dhc in concert is their highly kinetic stage presence . it would have been great if this dvd had concentrated on the band as a whole and not just different extreme closeups switched at a dizzying rate . and since the dhc are supposed to be the focus , why does the director insist on featuring so many shots of the audience ? it gets on your nerves . i love the dhc . their live cd has a permanent place on my playlist . but this horribly made dvd only made it through three songs . perhaps if i had been at the front of the stage that night , i would appreciate it more .

## neg 116. dvd 518.txt

margin 2.25, 94 words

> i take this title form the video store thinking in wynton marsalis . when i was watching the dvd i can appreciate that the image is very good ( not great , and i have a 720p tube tv ) and the sound is very good also ( not great , i have a reference equipment ) . but the show is so boring¡ look , you just desire this man stop to blow . the drum 's solo is just awesome , but the rest of the show is to forgive about it

## neg 117. dvd 757.txt

margin 2.19, 71 words

> ¿por qué se le ocurrió a tim burton hacer un remake de este clásico ? el resultado no puede ser peor.. . sólo fui a verla porque sale tim . que vestido de primate resultes igual de atractivo y apasionado que siempre es lo único que vale la pena de toda la historia . tus ojos siguen emitiendo fuego . ¡qué no se apague nunca ! you are the best !

## neg 118. dvd 285.txt

margin 2.17, 50 words

> i had the complete opposite experience with this workout than did the previous reviewer . the combination of doing upper and lower body exercises simultaneously caused my heartrate to soar which caused symptoms of overtraining . many people love this video but i just had a bad experience with it

## neg 119. books 875.txt

margin 2.17, 36 words

> this is for beginners , it 's filled with useless forms , and it provides very little information beyond a common-sense and reasoned approach to real estate . surely there must be better resources than this

## neg 120. music 964.txt

margin 2.11, 245 words

> i remember when this recording came out and wynton marsalis was being hailed as the second coming of jazz . i picked it up right away . i was mystified by the souless mimicry of art blakey 's jazz messengers and miles ' 2nd great quintet- -this punk was supposed to be the savior of jazz ? listen as wynton negotiates technically difficult arrangements , stopping on a dime ! marvel at his ability to explore the full range of dynamics within two bars ! ! gape in wonder at the fussy arrangement of think of one that strips the tune of any semblence of swing ! ! ! i get it , wynton- -you 've mastered the trumpet , technically speaking , which is no mean feat . and you can read music . bully for you . the only trouble is that you have nothing meaningful to say . ordinarily , i 'd feel sorry for you , having wasted all those hours of practice , except that you trashtalk musicians whose dirty drawers you are n't worthy of washing . people like john coltrane , joe zawinul , miles davis , wayne shorter , herbie hancock...i could go on and on , but i think you get the point . this music is jazz by and for people who think that the best way to honor the past is to preserve it like a roach in amber , thus killing it .

## neg 121. health 670.txt

margin 2.09, 60 words

> this shampoo made my dandruff even worse . after using it , it did make my scalp feel cool and cleansed , but an hour later i combed my hair and there were huge flakes in it . if you have to pay a little more for a dandruff shampoo buy paul mitchell 's tea tree shampoo or something .

## neg 122. camera 609.txt

margin 2.05, 148 words

> i got this camera when it was rather new . i am not extremely pleased with it . it is not acting this way because it is 2 years old...it was like this when i bought it . -first of all...it has no lens cover so you have to keep it in a camera bag . incase you touch the lens without relizing...all your pictures will be ruined . -it takes for ever to take a picture . you have to wait for like 2 seconds for the picture to be taken . -it eats up batteries like crazy -it takes forever to turn on -if you have the flash setting on autoflash , the camera will still flash in bright sunlight -the pictures are extremly blurry when you print at home -it has no optical zoom ( but the zoom is really the customer 's choice .

## neg 123. music 57.txt

margin 2.03, 26 words

> this cd is awesome from beginning to end . i really enjoy listening to this type of music . this cd is a must have .

## neg 124. books 793.txt

margin 2.01, 52 words

> if you want the why and the wherefore ... stay away . informative to general audiences , it provides little scientific support for its contention . with the wealth of information out there , this was not the critical review needed , nor was it terribly informative about any particular statin-caused effect

## neg 125. books 713.txt

margin 1.97, 165 words

> if you can learn to dance by reading a book whose recommendation was to hold your partner and & quot ; move to the music&quot ; , then you may find & quot ; kaizen event implementation manual&quot ; useful . this book talks about the history and terminology of lean manufacturing and does go into detail about team member selection . after that , this book shows blank forms of some of the data analysis forms often used during a kaizen event , but tells you nothing of how to complete the forms and analyze the results . nor is there any & quot ; road map&quot ; or guidelines for conducting a kaizen event itself . there is information about how to contact the author in the event that you decide to hire him to & quot ; fill in all blanks&quot ; in person . the book is simply another info-mercial where in this case , you are paying for the advertisement

## neg 126. music 737.txt

margin 1.97, 121 words

> this is not , i repeat not five stars ! in all honesty it 's more like 1.5 or 2 stars and i 'm a big fan of slug & atmosphere.albums like overcast , godlovesugly , the felt project , and the dynospectrum album is much better than this.though the lyrics are thought provoking , but slug has been better , the production does n't hold up.it 's some of the weakest i 've heard from rhymesayers.there 's only a couple tracks that stand out , but i 'd have to say " do n't ever f**king question that " is the best.if you wanna hear slug at his best check out the dynospectrum album.slug spits classic verse after classic verse

## neg 127. music 935.txt

margin 1.95, 74 words

> i am very dissapointed with this dualdisc , because there is no comment ( worning ) about dvd region protection . what can i do with this disc - region 1 , in europe ( region 2 ) ? my message for sony corporation is : " this format will not exist for long with dvd region protection ! sorry . " . my first , and last dualdisc . back to the sacd

## neg 128. books 362.txt

margin 1.94, 26 words

> this book is outdated for the 21st century . the basics are there and in great detail but most of the information is useless for today

## neg 129. health 46.txt

margin 1.93, 61 words

> the bars look like mudpies , are very dry , and all three " flavors " taste the same , meaning that they do n't have much flavor at all . i much prefer certain flavors of balance bars . the only good thing about these clif bars is that i do n't get hungry for several hours after eating one

## neg 130. books 488.txt

margin 1.90, 78 words

> this book refers to philosophical basis of buddhist practices as well as technical clasification of the states to be reached into meditative absortion . it is not a manual nor a guide . no meditation techniques nor yoga excersises can be found on the book . the style is simbolic and poetical . it is an interesting book but the name does not reflect the content . it will be interesting for people more inclined to scholarly work

## neg 131. dvd 161.txt

margin 1.81, 523 words

> we expose our babies / toddlers to a wide variety of cultural sources , in several languages . therefore , having seen similar products it seemed logical to purchase this one , given it is touted as a multilingual introduction to their environment ( our little ones are trilingual : english , spanish and asl , and they ignore us in all them ! ) . big mistake . the video not only reinforces but solidifies the sexist portrayal of love so prevalent in other baby einstein ( be ) items . in earlier be products one could see only female hands manipulating objects as they presented them on screen . male hands were never present . this video goes many steps furhter by featuring male figures only in the background , or at best , an elderly man briefly interacting with a child . everywhere else you see multiple females lovingly playing , caring or otherwise being nurturing to children . males are only seen ( with the exception of a black couple in bed while kids jump to play with them ) in a distant background in entirely detached attitudes , or at least distant , dry and quiet poses , such as talking with a much older ( male ) child . it is as if they are shown there as part of the domestic landscape , however as movable and inane as potted plants , whom you can move and place at will . i felt insulted by this condescending and disqualifying view of male love and nurturing abilities . asides , when you go into the spanish version , it is ( for a professionally produced video ) riddled with mistakes . three objects are mislabeled . in the first , when a cup - the plastic or paper tall type , not the coffee and saucer version , it is called " la taza " , when in reality it should be " el vaso " , as unlike english , where it is interchangeable " vaso " is the specific word for that item . the second - much worse instance , still in the kitchen was to introduce a bowl . there , the clueless scripter translated it as " el bol " , a clear and poor corruption of the english word into a one commonly used in spanglish , instead of calling it " tazo'n " , as its correct name is . the last one i saw was in the yard ( i 'm suprised they did n't call it la yarda ! : " looka mami ! get la troca and go a la marketa a buy a boncha de carrotas ! " ) . this time they called an obvious swing ( two ropes and a seat in between ) " la hamaca " , when in reality hamaca means hammock . fortunately , we are native speakers amnd are abel to catch these pitfalls , but many people relies upon these products to teach their kids other languages . in sum i was discusted with the whole thing .

## neg 132. health 830.txt

margin 1.80, 123 words

> if you 're interested in the chrome model to match your stainless steel appliances be prepared to constantly polish it due to the water spots . my friend owns one and at first i was envious , but now i rather be less fashionable than freak out over the visible water spots . this model has the same shape as the riviera and as i stated in my other review althought it is ergonomic , the riviera collects algae on the bottom of the pitcher so i would be skeptical in buying this one . the only reason i gave it two stars because it ultimately looks cool but you ca n't avoid the water spots and it may be algae friendly .

## neg 133. camera 156.txt

margin 1.79, 45 words

> i bought it for my 18-55 ef-s , and it looks like it is not very efficient - but i guess it is normal for a 18mm ( x 1.6 ) . i would have prefered a " tulip " design like those of sigma

## neg 134. camera 58.txt

margin 1.79, 45 words

> i bought it for my 18-55 ef-s , and it looks like it is not very efficient - but i guess it is normal for a 18mm ( x 1.6 ) . i would have prefered a " tulip " design like those of sigma

## neg 135. dvd 178.txt

margin 1.72, 100 words

> vci 's budget dvd starts out well enough for the obscure thriller lady ice , with nice letterboxed credits foreshadowing interesting widescreen photography to come . unfortunately , as soon as the credits end , the aspect ratio changes to full screen and the rest of the film is presented in one of the worst pan and scan jobs i 've ever seen on dvd . pass on this one from vci , and hopefully down the line there will be a new widescreen transfer so we can see how the film is supposed to look after the credits .

## neg 136. music 918.txt

margin 1.71, 239 words

> despite all reviews posted here in this page are given 5-stars to this release , i need to be honest and explain why i am giving just one poor star . no , i am not crazy . let me explain my point-of-view , and after that you can decide if this jh album really deserves more stars . just to start , this album does not have a spinal-column that could guide the band ( ? ) or the musicians thru a solid path . there are tracks played by a duo , trio , 4tt , and sometimes a very loose quintet , and each of these tracks have a different mood , without any presence of a jazz soul , or even a real smell of jazz . maybe the intention of recording these tunes was to make a homage / tribute to mr strayhorn , or maybe a recognition for mr henderson value in the 20th century jazz history as one of the most important hard-boppers ever . but the result was very poor . if you really love joe henderson ( as i appreciate ) , try any of his albums from the 60 's ( as a band-leader or as a sideman ) , mainly those from the blue note era . in time : i gave one star , in memory of his brilliant carreer . this particular album deserve zero-star .

## neg 137. dvd 754.txt

margin 1.69, 126 words

> just a warning to everyone that buys this version of the dvd , it 's fullscreen and does n't have any special features . now if you 've seen the scenes that were n't included in the extended vhs , but were for some reason on the cable version , you 'd see that they were among some of the funniest in the movie . i 'd really like to see this one get maybe a double dvd release with when nature calls , souped up and some of those great missing scenes including ace singing onstage with cannibal corpse ( funniest scene in the whole movie i thought ) , ace conversing with a few drunks in ray finkle 's hometown and some others .

## neg 138. dvd 892.txt

margin 1.69, 170 words

> what an incredible waste of acting talent " there was a crooked man " turned out to be . director joseph mankiewicz celebrated for classics such as " all about eve " and " the barefoot contessa " should be embarrassed by this bomb . kirk douglas plays paris pittman jr. a charming , persuasive prisoner incarcerated in territorial prison for ten years for an armed robbery that netted him $500 , 000. he hid the loot prior to his capture . it 's presence is common knowledge among the inmates giving him celebrity status . newly appointed warden woodrow lopeman played by henry fonda is trying to use douglas ' influence to coax the inmates help him initiate prison reform . under the guise of playing along with fonda , douglas secretly plots his escape to be reunited with his ill gotten cash . with an excellent cast including hume cronyn , burgess meredith and lee grant , i expected a whole lot more than this disappointing flick delivered

## neg 139. camera 277.txt

margin 1.67, 38 words

> if you got here looking for a bag for an xacti camera , keep looking . this bag is too small . it can be used for holding memoery cards and batteries , but not much more .

## neg 140. camera 257.txt

margin 1.61, 66 words

> this canon camera has poor quality interlacing artifacts all though out , on a 1080p monitor . i have used other hdv format cameras , and they were much better . the low light level recording was filled with fairly large digital grain . if you use a 1080i tube then it will probably look ok in high light , but still plauged in low light

## neg 141. music 149.txt

margin 1.56, 168 words

> why are they butchering pac 's songs like this . i advise anyone to get the bootlegs over this album . the original ghetto gospel and loyal to the game are 2 of my favorite pac songs but the one 's on here are painful to listen to . afeni should have let dj quik , daz , and whoever else that worked with pac do this album . they should have just digitally remastered the bootlegs . this started with still i rise to until the end of time to better dayz and the quality has been going down and down and they hit rock bottom with this one . the 2 stars is 1 because it is pac and another for the song uppercut . the most obvious butcher job is black cotton where em chose a fast beat and you could tell he is trying to speed up pac 's rhyme . i hope they do better with this last album due out this year

## neg 142. music 328.txt

margin 1.54, 265 words

> what they said was that katy ca n't rock just yet because she 's a raw talent and not yet coherent in theme . i saw her live on the chicks with attitude tour with liz phair and the cardigans and charlotte martin and rose was the worst performer of the night . the first problem is that her voice just is n't that strong , secondly , her lyrics never come out as if they 're honest and as if they are always a pretension that people feel a cool girl growing up should say . throughout her set , there was only one song that stuck out as an interesting and unique thing ( passingly honest as well ) and that was " snowflake . " it 's fitting that the song was preceded by an ironic intro about how she 's lived in california for a long time , but she hates warm weather , sounds impossible , but she must be truthful because it 's the only song that breaks out of the leaden grunge guitar mix and hits the audience over the head with songcraft . i 'm sure she has potential for the future , but i think on her next album she should take a hint from beth orton who 's known previous to her most recent album for being a popular artist in the realm of trip hop . stripping down your sound brings the utmost fundamentals of your idea and sound out , and i think that could be helpful for her to put on record

## neg 143. books 682.txt

margin 1.51, 107 words

> i really want to like thich nhat hanh 's books . i want to because people i respect like them , because i believe in the value of mindful living.. . but the truth is that i did n't find this book very helpful . i have real and continuing struggles with anger and this book while interesting in a round about way is , as others have mentioned , not directed toward the problem of anger . it is a mindful living remix . i 'm going to keep searching for a great tnh book and when i do i 'll recommend it . good hunting

## neg 144. camera 502.txt

margin 1.51, 161 words

> for quite sometime lured by media publicity i thought sony a good brand . but this was not at all true for digital cameras . i bought this p73 for myself and an hp 4 mp camera for my cousin much cheaper than sony . both 3x optical zoom . the hp one was far better in image quality . main problem is that photo quality is not so good . it lacks sharpness and in most of the natural occassions becomes a bit hazy . this fact becomes annoying because your friend who has a cannon or an hp camera will take sharper pictures better than you in any light conditions . also , in the same price you might look for something higher than 3x optical zoom , say 5x or so in other brands . also during video , every option of adjusting to light conditions etc will be shut off , another irritating fact . not recommended

## neg 145. camera 607.txt

margin 1.48, 50 words

> i bougt this camera and a olymus camera , both in the same price range , the kodak camera was by far deficeint in quality of image and workmanship . avoid this at all cost the olympus was well made , durable , higher quality picture and ease of use

## neg 146. books 577.txt

margin 1.46, 80 words

> i got really disapointed when i received and read this book . it provides advanced techniques that a regular woodworker would never use . the parts that woodworkers use the most are vague . i 'm not intereset in making violins or boats . i need techniques to bend wood , to use joints for curved surfaces , to build equipment and fixtures to bend wood and so on . this book lacks of the practical guidelines to do so

## neg 147. music 573.txt

margin 1.39, 22 words

> http : / / www.strangeland.com / asp / show.asp ? id=13635 http : / / www3.strangeland.com / asp / show.asp ? id=99

## neg 148. music 120.txt

margin 1.37, 92 words

> while some would call orange and acme " studio " albums , suggesting that they lack originality , but they have rythm . i would call myself a big jsbx fan , i play orange and acme constantly , however i feel that this album is a little too much free form , and free noise for the everyday listener . i would recommend that anyone interested in jsbx start with acme and then move on to orange to develop an appreciation for jsbx , because it is a rather acquired taste

## neg 149. music 603.txt

margin 1.32, 730 words

> with the greatest respect to the incredible bob beldon , joe zawinul , and wayne shorter , this box set should contain a warning . the warning is simple : if you already own most of the stuff in this collection , do n't bother . if you 're completely new to weather report , buy it . coming from someone that 's seen the band perform every year since 1972 and own all their official and quite a few " other " releases , i was really disappointed with this project ( except for the booklet ) . here are a few things that are puzzling : 1 ) a weather report box set includes three songs ( two composed by zawinul and one by shorter ) that were never released by weather report : a . in a silent way . released by miles davis b. super nova , released by wayne shorter c . experience in e ( excerpt ) , released by cannonball adderly ( i agree with the liner notes that point to these songs as pre-cursors , but mentioning them would have been enough - they are all in print ) 2 ) an incredible typo stating that alphonse mouzon was the drummer on " unknown soldier " 3 ) including a barely improved version of nubian sundance that has been in circulation for many years from " other " sources . 4 ) including another " better than , but not by much " version of the " other " sources for the 1978 rockpalast concert on dvd . 5 ) not remastering any of the original recordings . the tape hiss from the live in tokyo ( i sing the body electric ) songs is still clearly heard and not upgrading those old recordings is just plain unacceptable in this day and age . 6 ) finally , the cover itself - i have no words , except to admit " i do n't get it " . having said all that negative stuff - weather report remains the dominant " creative machine " of the jazz rock fusion era and those that missed it should buy this without hesitating . if you 're a long time weather report fan - there 's absolutely nothing to get excited about here . the dvd was especially disappointing to me . i have had that concert on vhs tape for many years and now on dvd ( all from " other " sources ) and was shocked to see such incredible video noise on the official version . zawinul 's black and white keys look like polka-dots in many places . ( i played the dvd in 5 different players ; two tv 's and my computer monitor to make sure it was n't my equipment ) . i should have paid attention to the pr person at sony that told me the concert was taken from a re-broadcast of the show and not from the master tapes . it 's my own fault for having unrealistic expectations . i should probably clarify that while the dvd is in fact clearly better than the " un-offical " version , it still looks like a bootleg ! sad.. . it is of some significance that this " review " is the first time i 've chosen to speak out about something in fusion that was less than flattering . it should also be noted that my disappointment is aimed directly at cbs / sony / bmg and not the musicians / producers . i 'm still amazed that this record company can see fit to release this and hold back the already remastered mahavishnu orchestra live in cleveland cd that was supposed to be released in 2004. lastly , let me make it perfectly clear that zawinul , shorter , and beldon are musicians and people i personally hold in the highest esteem with zawinul and shorter being musical divinities as far as i 'm concerned . while my review is an obvious personal venting , and i realize that zawinul and shorter gave this project their stamp of approval , i think that should n't be mistaken for a personal attack . my remarks are simply observations with some attitude directed at cbs / sony / bmg . by rick calic jazz rock world

## neg 150. health 788.txt

margin 1.21, 58 words

> i used relacore for one week.....it did n't work the only thing it helped with was sleeping . the bottle says take one with each meal and i did by 3pm daily i was fighting to keep my eyes open . if you need help sleeping this is one too take . also i put on 3 pounds

## neg 151. music 506.txt

margin 1.20, 41 words

> good music but a bad title ! elvis has left the planet but a new king has been born with the self proclaimed new king of rock and roll ken rondell at http : / / www.cdbaby.com / cd / bigra

## neg 152. health 593.txt

margin 1.18, 25 words

> the individual packaging is nice but the floss breaks frequently nexcessitating more than one to floss your teath . the glide products are much nicer

## neg 153. health 431.txt

margin 1.17, 39 words

> this product might do for a backpacking weekend with the boy scouts , but compared to a blade razor , or even an electric , it leaves a lot to be desired . i recommend giving it a pass

## neg 154. dvd 627.txt

margin 1.17, 40 words

> many have seen this movie on tv many times . for a b-movie it is great fun and interesting to watch . no extras on the dvd . i wish they did add something from behind the scenes , etc

## neg 155. books 324.txt

margin 1.12, 62 words

> if you have kids or grandkids , who think about politics & like " sf " ; give them this book ! it was one of the many heinlein works that helped me grow up . it is the best & most important of his " for kids novels " . i ment to give it 5 stars ! ! ! !

## neg 156. music 808.txt

margin 1.11, 92 words

> if the name pink floyd was n't on this cd , who would really rate it higher that one or two stars ? i am a pink floyd fan , but i have to say that i do n't like any of their early works . to me , the band begins to make great stuff with " meddle " and their first cd were boring , even with the pink floyd name on it . the only good track is " childhood 's end " , the other tracks are poor

## neg 157. books 436.txt

margin 1.08, 55 words

> we absolutely loved " cloudy with a chance of meatballs " ( i highly recommend it ) but this is nowhere near as good . most of the story is just rehashing the original book , with a little politically-correct " let 's ship the extra food to the hungry " thrown in . lame

## neg 158. dvd 515.txt

margin 1.00, 132 words

> this a dreadful example of what jayne was reduced to play in to feed her children and compensate for the lack of earnings of her deadbeat-husbands / lovers . the only reason to watch it would be because mamie van doren was also in it.but be aware ( and i read that in a biography about jayne ) that in their contracts was specified that they would not appear together in any scene whatsoever.so you see them separately in different scenes.also be aware that if you blink , you will not see either of the 2 blonde beauties . conclusion:get this film for a member of your family who is nostalgic for the ways of the ' 'ol ' south ' , or someone with a white hood showing his eyes onl

## neg 159. dvd 109.txt

margin 1.00, 82 words

> i bought three dvds ( the wood was one of them ) and the dvds were in european codes which means they wo n't play in the united states unless you own a " special " dvd player . i 'm very unhappy with my purchase . my recommendation to you is that you read every single piece of information before you purchase movies that were formatted for another country . this is the catch when you buy movies at cheaper prices

## neg 160. camera 853.txt

margin 0.98, 54 words

> the camera ( canon s-80 ) barely fits in the case and there is no room for even an extra storage card , much less a second battery pack or the charger . i ended up using my old tamrac case that has an extra zippered pouch for accessories . total waste of $$$

## neg 161. health 820.txt

margin 0.97, 57 words

> babyliss pro instant heat 5 jumbo roller hairsetter comes in a compact , useful size . however , the rollers take a long time to heat up . even if left plugged in for a half-hour , they do not reach a high enough temperature to effectively curl thick hair . i would not recommend this product

## neg 162. camera 190.txt

margin 0.97, 78 words

> i wear glasses and press against the viewfinder as hard as i can to help keep the shot stable ( i shoot birds at 700mm ) . the first thing my friend and i did was to compare two identical lenses / cameras etc. - one with , one without , the extender . result : - the image appeared the same size , and the extender slightly blurred the image . in other words - completely useless

## neg 163. music 976.txt

margin 0.90, 15 words

> this cd isnt real good if you like compilations than get the ruff ryders c

## neg 164. dvd 715.txt

margin 0.88, 68 words

> even though tsui hark is one of my favorite hong kong directors , this movie did not at all show his skill . the story was poor along with the actors performances . i may be a little biased since i love john woo , and tsui hark killed their friendship by making this movie . worth checking out but i would'nt buy it if i were you

## neg 165. music 391.txt

margin 0.87, 148 words

> i have to disagree with the majority of folks here who consider this cd the jazz end all . i find it grating , and darn near unlistenable . i have built a small but quality jazz library the last few months . miles davis , dave brubeck , kenny burrell , grant green , cannonball adderley , stan getz , chet baker , wes montgomery , bill evans and thelonius monk to name a few . this guy is by far my least favorite . his playing on miles davis cd 's i have and with monk is largely enjoyable and i know he 's a giant . but this stuff ? . the live recording on disc two was so grating i could n't make it through . it sounded to me like a bunch of geese being slaughtered . give me the other guys anytime

## neg 166. camera 466.txt

margin 0.82, 21 words

> far better models for similair price range - dissapointed with the quality of the finish etc etc. works fine though .

## neg 167. music 887.txt

margin 0.81, 8 words

> it 's not great music to dance to

## neg 168. software 700.txt

margin 0.70, 215 words

> conceptually this is a great game , especially for a child with visions of being a vet . you ( can theoretically ) learn about animals , their care and health issues . those 2 stars for overall are basically for the concept and little else . unfortunately the general usability of this game , vis- à-vis lousy controls , is quite low . it 's nearly impossible to move the character at times , which results in stressful failure in the game . it crashes . it ca n't remember simple settings like , leave the terribly loud and obnoxious music off . playing this multiple times with my 6 year old always goes from excitement to frustration ( bordering on tears more than once as a bunny gets woefully ill while your character is comically stuck bouncing between the sofa and ottoman ) . once going you can engage your child by " studying " the books you 've bought . also , as you analyze the patients you learn about ailments as well as the treatments . that is all good stuff , but on whole the game is too frustrating to enjoy . one final note , this is the first time i 've ever bothered to review any product .

## neg 169. books 988.txt

margin 0.65, 163 words

> margaux with an x is about a young lady who seems to have it all . beauty , popularity and can do about anything without getting into trouble at home . yet she is not happy she holds a dark secret that happened to her when she was young.she is tired of every boy drooling over her and wanting to date her and most having no content to them . she has a gambler as a father and a mother who just watches television all day . her life takes a different turn when she meets danny . he is the total opposite of all the guys she has dated . he is a year behind her in high school he is thin and is not shapely , yet they both start a bond with each other . the book was interesting but after awhile i got tired and could not keep up with the constant bantering and sarcasm of the main characters

## neg 170. camera 571.txt

margin 0.60, 37 words

> the product features are ok , but the screen is very small . also , the resolution needs to be better . the photos were very grainy . an impressive looking product with not so impressive output

## neg 171. books 602.txt

margin 0.59, 159 words

> i read this book on a suggestion from a friend , before i read " reviving ophelia " , because she wanted to see if i would be as dissapointed with it as she was . i was more so . while there are some outstanding essays in this collection , the bias of the editor clearly stands out . there is no one for the outcasts to relate to . there was no musician , nor was there anyone that dealt with an alternative religion . there were no essays from people who had a different relationship with their parents than she had . the sections are poorly named and divided . all in all , it is an unworthy book to be associated with the original . some girls it may " make feel less alone " , but for me it only accentuated the differences . definately take out from the library before you buy it

## neg 172. dvd 441.txt

margin 0.58, 32 words

> for the time period when this was made , this was an excellent movie . made you stop and think , " watch who you 're going to bed with " !

## neg 173. music 7.txt

margin 0.56, 107 words

> ok , so the song playing when brian goes and we see mia for the first time is a song called " deep enough ( urban remix ) " by live . i have the other songs written down , including the one played between the two buildings , so i will find them and tell you . if you all want only the songs that were actually in the movie , rent the dvd , and take about ten minutes to watch the credits and write down the song names and artists . that 's how i have only the songs that are in the movie

## neg 174. dvd 391.txt

margin 0.54, 205 words

> this was a very annoying and boring flick thats barely watchable and throughout the film i kept looking at my watch , the film is not a historical drama nor is it an autobiographical film about william shakespreare infact it is a romantic comedy disguised as a historical drama . my girlfriend insisted that we watch this film together but i was n't in the mood she forced me to watch this , the film was about a struggling young writer shakespeare played by joseph fiennes who falls in love with lady viola played by gwyneth paltro who also happens to inspire his famous play romeo and juliet , this film also won a couple of oscars including gwyny for best actress but i felt like the film was just not that funny because all the characters seemed to talk in an old english style thats hard to understand . overall the film was just o.k. i think that some of the sets and costumes were fantastic and judi dench was great as queen elizabeth but i never want to watch this film again , if your a shakspeare fan and like romantic comedies then you might like this film more than i did .

## neg 175. software 389.txt

margin 0.53, 39 words

> picassa , part of the google suite of programs , is both better than this program and free ! what more do i need to add ? the user interface of picassa is easier to use and more responsive

## neg 176. music 80.txt

margin 0.44, 183 words

> i had never heard leonard cohen 's music but saw references to it frequently when looking at other singers / songwriters . given his status / reputation i thought i should get this cd and learn what all the fuss was about . having had no preconceptions , i have to say i was quite disappointed . i think the music has not aged well and is pretty unremarkable . perhaps the style liberated others to pursue new directions but the work in and of itself is ho hum at best . specific example that speaks volumes : listen to cohen 's singing of his " hallelujah " and then listen to jeff buckley 's cover of that song on " grace " which was recorded in 1994. sorry , leonard , you cannot hold even a birthday-sized candle to jeff buckley 's rendition of your own song . it is a very unflattering comparison that pretty much put the first and last nail in the coffin for my appreciation of cohen 's legacy . " tant pis , vers le bonheur .

## neg 177. dvd 551.txt

margin 0.44, 83 words

> i bought basically , because i love denisee richards and daryl hanna , plus i like also valerie tasso , besides i am a fan of pierre woodman , they all appear on the film , among some well know adult stars like dora venter , rita faltoyano . but really the film is not good at all , it is slow , the elements do n't match . it is sometimes hard to follow . it is really not worth buying it

## neg 178. books 28.txt

margin 0.42, 5 words

> you all like misogynist comics

## neg 179. books 443.txt

margin 0.39, 48 words

> the stationery is cute and colorful , but the pages are very cluttered . while the envelopes have spaces to write addresses and put return labels , the pages are too colorful and bold . a ballpoint or ink pen does n't look good on the paper .

## neg 180. music 141.txt

margin 0.38, 33 words

> this album is okay not their best . a few songs are good other than that this album is fair.purcahse it with your money intelligently ! ! ! ! ! ! ! !

## neg 181. music 460.txt

margin 0.36, 114 words

> this is no saw 85-92 as some people compare it to . oh , no . this is a largely unfulfilling listen . the tracks all sound too similar . i realize richard 's concept was to just utilize anlaog gear , but the drum programming and harmonic " development " is lackluster . only track worth burping over is the last one.. . xmd something . has he been taking piano lessons since druqks ? for those that want some new electronic music that packs a punch , check out nick forte 's new release " young man 's disease " which is better than anything else i 've heard this year .

## neg 182. music 215.txt

margin 0.36, 118 words

> not exactly the " vaults " blowing open , as stated in the promo . these are mostly leftovers and one-offs from the late 1990s , when the group was on hiatus from serious recording . that 's why the set is overloaded with forgettable jingles from television shows , literary journals and graphic design firms . whats good is the material that was recorded for albums and subsequently rejected , such as " reprehensible " , " rest awhile " and " certain people i could name " . but there are too few of these real songs , and they 'd have fit a lot better on that long-awaited b-sides collection from their major label career

## neg 183. books 204.txt

margin 0.36, 69 words

> this book is undoubtedly very good value for a birding handbook ( certainly by european standards ) . but the physical packaging is a total disaster . it has a ridiculously rigid spine and tiny page margins . it is difficult to read text near the spine , and virtually impossible to keep the book open on a particular page . the most unuseable book i 've ever experienced

## neg 184. dvd 461.txt

margin 0.33, 198 words

> well not to bad a deal.most of the movies here are n't too bad ( the inspector general , a farewell to arms , a star is born etc ; ) and have basically clear picture and sound quality.it 's true several of these are silent but even a few of those are good.there is a problem with this set however , after you 've watched these movies once they will begin to wear out my mother and i discovered this when we wanted to watch " the flying deuces " for the second time the film was a lot more blurry and it was difficut to hear some of the dialogue.my advice is not buy this collection unless you find it for sale very cheap , and to just rent some of the better ones.we did get a few things out of this my mother said that she discovered buster keaton , w.c.fields and charlie chaplin because of this for instance , ( and after we liked father 's litle dividend we decided to watch father of the bride which was even better ) so i have decided to give it an extra star just for that

## neg 185. software 582.txt

margin 0.33, 327 words

> the game disk does not run on my laptop . but it will play it on my desktop computer . very annoying , but at least i can play ( other reviewers have not been so lucky ) . the game has some good questions and i enjoy testing my friends knowledge . the game itself is rather simple and not totally fun . the " game board " is the outside of the friends ' apartment building . when you get a question right a window lights up . when you get one wrong a window dims . if you do n't answer the question nothing happens . you win when all the windows on that floor are lit up . i would prefer that they make you answer all questions - none of this passing on a question - it would up the ante and perhaps add some excitement . if you play a multi-player game you cannot select which letter is your buzzer and the letters assigned by the game designers are adjacent keys on the keyboard ! it 's silly for the two players to be huddled together , hovering over the same part of the keyboard when the designers could have selected other letter keys set further apart . there are some video clips and still images accompanying the questions , but it 's mostly a trivia game without visual aids or embellishments . think trivial pursuit with a computer screen as the cards . this game was a gift . if i had to do it over again i 'd probably spend my money instead on scene it ! friends edition . as of right now , scene it ! friends edition is on sale at circuit city for the same price as this game is on amazon . ( and though i have n't played it , the reviews of that game are much better than this one ) .

## neg 186. books 757.txt

margin 0.32, 62 words

> i bought this book , the paperback version . the text is good , it describes all his letters and tries to do a lot of explanations too . however the prints of his paintings are not that impressive . they are very dark prints . go for some other book if you want to see the corect colors of his paintings

## neg 187. health 375.txt

margin 0.27, 67 words

> the best kind of electric toothbrush ( according to my hygienist ) is one with a rotating top to the head , that way it gets the gums better . i ordered this one and i do n't like it.. . besides the lack of rotating head , it is very loud and i feel like i 'm going to wake up my roommates . : )

## neg 188. books 982.txt

margin 0.23, 66 words

> for all of you looking for that favorite book " the silly book " , join my club ( not literally ) . the book that has the ode to boodleheimer was written by stoo hample not babette cole . i have been searching for this book for years . good luck everyone , and let me know if you find an extra copy for sale

## neg 189. dvd 815.txt

margin 0.20, 263 words

> this video 's only redeeming quality is its excellent pilates instruction . like all stott videos this one takes extra care to explain proper form and technique . unfortunately , the aerobics portion is extremely boring and simple . you just walk in place the whole time with no interesting variations . if you are looking for a video for a beginner , this one might work for you if you are truly new to exercise and are really out of shape . although i consider myself a beginner when it comes to exercise , this video was too easy for me . i have n't exercised consistently in several years . however , i do have a moderately active lifestyle . i walk and hike on occassion and i play with my kids at the park- -that sort of thing . if you have trouble with everyday activities because you are out of shape , this would be a great place to start . if you are somewhat fit , this video might be too easy for you as well . you might also like this video if you feel like you have no coordination . there are no fancy moves at all . if you can walk , you can do this video . i like simple steps , but this was too simple . in general , though , i think you 'd be better off saving your money and taking a walk . spend your money on one of the other excellent stott videos that focuses exclusively on pilates

## neg 190. music 919.txt

margin 0.18, 242 words

> almost 10 years later.. . and i am still waiting for the punchline . i think this is the most properly named album of all time.. . as the easiest summation is : it lacks any punch and keeps you waiting for something that never comes ! its terrible , especially when contrasted with pornograffitti . gone are the great guitar tone , riffing , rhythm , power , and groove that marked most of the prior three albums . it 's what the forth side to " iii sides to every story " could have been.. . " yours , mine , the truth , and the suck " . the songs are lackluster , but its really the guitar sound that kills this album album . " no respect " , surprisingly , by name , is the only song worth any respect and the only song near upbeat on the album . " waiting for the punchline " still remains in my top 5 worst albums of all time.. . i dont write negative reviews unless a cd is really bad in general or really bad compared to the bands other work . in this case , it fits both.. . its bad for extreme.. . and stands up as exceptionally bad among all other bands ' albums as well . conversely , in my opinion , iii sides and pornograffitti are 4 and 5 star albums , respectively

## neg 191. books 232.txt

margin 0.14, 68 words

> it was amazing when i read this , how self centered and morally wrong this man was . it makes me sick to my stumach to read it . this was nothing more then glorifing his looting and murdering in cold blood . if you have a chance skip this one and read somthing like " company commander " or " band of brothers " somthing worth while

## neg 192. books 33.txt

margin 0.12, 28 words

> if you are looking for a book that does a cover to cover job of bashing western civilization with complete and obvious bias , this is it .

## neg 193. camera 931.txt

margin 0.12, 23 words

> excelent product.i get about 15 times the life of ordinary batteries . i would reccomend to anybody who uses their camera a lo

## neg 194. health 209.txt

margin 0.11, 21 words

> i have always thought that a man 's shaver would work on woman 's beard . this one does not .

## neg 195. dvd 885.txt

margin 0.09, 199 words

> well , at least the movie is faithful to its source in its spirit . based on a book written on 1902 , it 's nostalgia of the british empire belongs to that era . the plot deals with a soldier who is expelled from his regiment for refusing to go to fight a colonial war in sudan because of his impending marriage . not only his colleagues regard him now as a coward , but also his future wife . he had no choice then but to go to war to prove he is a real man and not a coward . the filmmakers try nothing in terms to bring the material up to date , to our more contemporary ( and one hopes , more enlightened ) attitudes . there 's no post colonial guilt here whatsoever . in some ways , this speaks well of the filmmakers in terms of not trying to tamper with the original material ; in another way , it is a bit shocking seeing such jingoism in a contemporary movie . all of this would n't matter much if the movie was entertaining ; unfortunately , it is only intermittently so

## neg 196. dvd 468.txt

margin 0.07, 26 words

> avoid this cheapo release of these great film ! subpar prints..certainly not from original 35mm elements..wait for the good one to come out down the road

## neg 197. camera 431.txt

margin 0.04, 18 words

> if you lose this cord just get a flash card reader . it 's cheaper and more practical

## neg 198. music 514.txt

margin 0.01, 175 words

> i bought this based on reviews of " bass queen in the mix . " to me it sounds like the west coast edition of northern exposure without the 4 / 4 house beat . in other words , its very electronic sounding , almost completely non-vocal and not very funky at all . i listened to " eargasm " by plump dj 's and icey 's " funky breaks " after this and it 's definitely missing variety , skill in mixing and that " neck snapping " funky quality that make the plumps and icey so indispensible . not too bad but not that interesting either . i prefer her " mixtress " and still have not heard " bass queen.. . " btw , my speakers are flat down to below 30 hz and i did n't find the recording quality or the bass that impressive . listen to crystal method 's " phd " or " block rockin ' beats " by chemical brothers after this to see what i mean
