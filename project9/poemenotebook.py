import kivy
from kivy.app import App
from kivy.uix.pagelayout import PageLayout
from kivy.uix.button import Button
from kivy.utils import get_color_from_hex


class PageLayout(PageLayout):

    def __init__(self):

        super(PageLayout, self).__init__()
        btn1 = Button(text='Welcome to ENGL233 Critical Reading')
        btn1.background_color = [111/255, 69/255, 148/255, 1]
        btn2 = Button(text='This is Just to Say\n\n\n\nI have eaten\nthe plums\nthat were in\nthe icebox\n\nand which\nyou were probably\nsaving\nfor breakfast\n\nForgive me\nthey were delicious\nso sweet\nand so cold\n\n-William Carlos Williams')
        btn2.background_color = [1, 105/255, 180/255, 1]
        btn3 = Button(text='My Papa`s Waltz\n\n\n\nThe whiskey on your breath   \nCould make a small boy dizzy\nBut I hung on like death:   \nSuch waltzing was not easy.\n\nWe romped until the pans   \nSlid from the kitchen shelf\nMy mother’s countenance   \nCould not unfrown itself.\n\nThe hand that held my wrist   \nWas battered on one knuckle\nAt every step you missed\nMy right ear scraped a buckle.\n\nYou beat time on my head   \nWith a palm caked hard by dirt,   \nThen waltzed me off to bed   \nStill clinging to your shirt.\n\n-Theodore Roethke')
        btn3.background_color = [168/255, 245/255, 200/255, 1]
        btn4 = Button(text='The Road Not Taken\n\n\n\nTwo roads diverged in a yellow wood, \nAnd sorry I could not travel both\nAnd be one traveler, long I stood\nAnd looked down one as far as I could\nTo where it bent in the undergrowth\n\nThen took the other, as just as fair, \nAnd having perhaps the better claim, \nBecause it was grassy and wanted wear\nThough as for that the passing there\nHad worn them really about the same,\n\nAnd both that morning equally lay\nIn leaves no step had trodden black.\nOh, I kept the first for another day!\nYet knowing how way leads on to way, \nI doubted if I should ever come back.\n\nI shall be telling this with a sigh\nSomewhere ages and ages hence: \nTwo roads diverged in a wood, and I—\nI took the one less traveled by, \nAnd that has made all the difference.\n\n-Robert Frost')
        btn4.background_color = [111/255, 69/255, 148/255, 1]
        btnfreud = Button(text='The “Uncanny”\n\n(1919)\n\n\n\nSIGMUND FREUD')
        btnfreud.background_color = [1, 105/255, 180/255, 1]
        btn5 = Button(text='\nIt is only rarely that a psychoanalyst feels impelled to in\nvestigate the subject of aesthetics even when aesthetics is\nunderstood to mean not merely the theory of beauty, but\nthe theory of the qualities of feeling. He works in other\nplanes of mental life and has little to do with those sub\ndued emotional activities which, inhibited in their aims\nand dependent upon a multitude of concurrent factors,\nusually furnish the material for the study of aesthetics. But\nit does occasionally happen that he has to interest himself\nin some particular province of that subject; and then it usu\nally proves to be a rather remote region of it and one that\nhas been neglected in standard works.\nThe subject of the “uncanny” is a province of this kind.\nIt undoubtedly belongs to all that is terrible—to all that\narouses dread and creeping horror; it is equally certain,\ntoo, that the word is not always used in a clearly definable\nsense, so that it tends to coincide with whatever excites\ndread. Yet we may expect that it implies some intrinsic\nquality which justifies the use of a special name. One is\ncurious to know what this peculiar quality is which allows\nus to distinguish as “uncanny” certain things within the\nboundaries of what is “fearful.”\nAs good as nothing is to be found upon this subject in\nelaborate treatises on aesthetics, which in general prefer to\nconcern themselves with what is beautiful, attractive and\nsublime, that is with feelings of a positive nature, with the')
        btn5.background_color = [1, 105/255, 180/255, 1]
        btn6 = Button(text='\ncircumstances and the objects that call them forth, rather\nthan with the opposite feelings of unpleasantness and re\npulsion. I know of only one attempt in medico\npsychological literature, a fertile but not exhaustive paper\nby E. Jentsch. But I must confess that I have not made a\nvery thorough examination of the bibliography, especially\nthe foreign literature, relating to this present modest con\ntribution of mine, for reasons which must be obvious at\nthis time;3 so that my paper is presented to the reader without any claim of priority.\nIn his study of the “uncanny,” Jentsch quite rightly lays\nstress on the obstacle presented by the fact that people vary\nso very greatly in their sensitivity to this quality of feeling.\nThe writer of the present contribution, indeed, must himself plead guilty to a special \nobtuseness in the matter,\nwhere extreme delicacy of perception would be more in\nplace. It is long since he has experienced or heard of anything which has given \nhim an uncanny impression, and he\nwill be obliged to translate himself into that state of feeling, and to awaken in \nhimself the possibility of it before he\nbegins. Still, difficulties of this kind make themselves felt\npowerfully in many other branches of aesthetics; we need\nnot on this account despair of finding instances in which\nthe quality in question will be recognized without hesitation by most people.\nTwo courses are open to us at the start. Either we can\nfind out what meaning has come to be attached to the word\n“uncanny” in the course of its history; or we can collect all\nthose properties of persons, things, sensations, experiences\nand situations which arouse in us the feeling of uncanniness, \nand then infer the unknown nature of the uncanny')
        btn6.background_color = [1, 105/255, 180/255, 1]
        btn7 = Button(text='\nfrom what they all have in common. I will say at once that\nboth courses lead to the same result: the “uncanny” is that\nclass of the terrifying which leads back to something long\nknown to us, once very familiar. How this is possible, in\nwhat circumstances the familiar can become uncanny and\nfrightening, I shall show in what follows. Let me also add\nthat my investigation was actually begun by collecting a\nnumber of individual cases, and only later received confirmation\nafter I had examined what language could tell us.\nIn this discussion, however, I shall follow the opposite\ncourse.\nThe German word unheimlich4 is obviously the opposite\nof heimlich, heimisch, meaning “familiar,” “native,” “belonging to the home”;\nand we are tempted to conclude that\nwhat is “uncanny” is frightening precisely because it is not\nknown and familiar. Naturally not everything which is new\nand unfamiliar is frightening, however; the relation cannot\nbe inverted. We can only say that what is novel can easily\nbecome frightening and uncanny; some new things are\nfrightening but not by any means all. Something has to be\nadded to what is novel and unfamiliar to make it uncanny.\nOn the whole, Jentsch did not get beyond this relation of\nthe uncanny to the novel and unfamiliar. He ascribes the\nessential factor in the production of the feeling of uncanniness to \nintellectual uncertainty; so that the uncanny would\nalways be that in which one does not know where one is,\nas it were. The better orientated in his environment a person is, \nthe less readily will he get the impression of something uncanny in \nregard to the objects and events in it.\nIt is not difficult to see that this definition is incomplete,\nand we will therefore try to proceed beyond the equation')
        btn7.background_color = [1, 105/255, 180/255, 1]
        btn8 = Button(
            text='\nof unheimlich with unfamiliar. We will first turn to other\nlanguages. But foreign dictionaries tell us nothing new,\nperhaps only because we speak a different language. Indeed, \nwe get the impression that many languages are without a word for this \nparticular variety of what is fearful.nI wish to express my indebtedness to Dr. Th. Reik for\nthe following excerpts:LATIN: (K. E. Gorges, Deutschlateinisches Wörterbuch,\n1898). Ein unheimlicher Ort [an uncanny place]—locus\nsuspectus; in unheimlicher Nachtzeit [in the dismal night\nhours]—intempesta nocte.\nGREEK: (Rost’s and Schenki’s Lexikons). Xenos, strange, foreign.\nENGLISH: (from dictionaries by Lucas, Bellow, Flügel,\nMuret-Sanders). Uncomfortable, uneasy, gloomy, dismal,\nuncanny, ghastly; (of a house) haunted; (of a man) a repulsive fellow.\nFRENCH: (Sachs-Villatte). Inquiétant, sinistre, lugubre,mal à son aise.\nSPANISH: (Tollhausen, 1889). Sospechoso, de mal aguëro, lugubre, siniestro.\nThe Italian and the Portuguese seem to content themselves with words which \nwe should describe as circumlocutions. In Arabic and Hebrew “uncanny” means the same\nas “daemonic,” “gruesome.”\nLet us therefore return to the German language. In Daniel Sanders’ Wörterbuch \nder deutschen Sprache (1860),\nthe following remarks\ni [abstracted in translation] are found\nupon the word heimlich; I have laid stress on certain passages by italicizing them.\nHeimlich, adj.: I. Also heimelich, heinielig, belonging to\nthe house, not strange, familiar, tame, intimate, comfortable, homely, etc.\n(a) (Obsolete) belonging to the house or the family, or\nregarded as so belonging (cf. Latin familiaris): Die Heimlichen, the members \nof the household; Der heimliche Rat\n[him to whom secrets are revealed] Gen. xli. 45; 2 Sam.\nxxiii. 23; now more usually Geheimer Rat [Privy Councillor], cf. Heimlicher')
        btn8.background_color = [1, 105/255, 180/255, 1]
        btn9 = Button(
            text='\nheimlich and accustomed to men.” “If these young creatures are \nbrought up from early days among men they become quite heimlich, friendly,” etc.\n(c) Friendly, intimate, homelike; the enjoyment of quiet\ncontent, etc., arousing a sense of peaceful pleasure and security as \nin one within the four walls of his house. “Is it\nstill heimlich to you in your country where strangers are\nfelling your woods?” “She did not feel all too heimlich\nwith him.” “To destroy the Heimlichkeit of the home.” “I\ncould not readily find another spot so intimate and heimlich as \nthis.” “In quiet Heinzlichkeit, surrounded by close\nwalls.” “A careful housewife, who knows how to make a\npleasing Heimlichkeit (Häuslichkeit)\n5 out of the smallest\nmeans.” “The protestant rulers do not feel . . . heimlich\namong their catholic subjects.” “When it grows heimlich\nand still, and the evening quiet alone watches over your\ncell.” “Quiet, lovely and heimlich, no place more fitted for\nher rest.” “The in and out flowing waves of the currents\ndreamy and heimlich as a cradle-song.” Cf. in especial\nUnheimlich. Among Swabian and Swiss authors in especial, often as \ntrisyllable: “How heimelich it seemed again\nof an evening, back at home.” “The warm room and the\nheimelig afternoon.” “Little by little they grew at ease and\nheimelig among themselves.” “That which comes from\nafar . . . assuredly does not live quite heimelig (heimatlich\n[at home], freundnachbarlich [in a neighborly way])\namong the people.” “The sentinel’s horn sounds so heimelig \nfrom the tower, and his voice invites so hospitably.”\nThis form of the word ought to become general in order to\nprotect the word from becoming obsolete in its good sense\nthrough an easy confusion with II. [see below]. ‘“The')
        btn9.background_color = [1, 105/255, 180/255, 1]
        btn10 = Button(text='\nZecks [a family name] are all “heimlich.”’ ‘“Heimlich”?\nWhat do you understand by “heimlich”?’ ‘Well, . . . they\nare like a buried spring or a dried-up pond. One cannot\nwalk over it without always having the feeling that water\nmight come up there again.’ ‘Oh, we call it “unheimlich”;\nyou call it “heimlich.” Well, what makes you think that\nthere is something secret and untrustworthy about this family?”’ Gutzkow.\nII. Concealed, kept from sight, so that others do not get\nto know about it, withheld from others, cf. Geheim [secret]; \nso also Heimlichkeit for Geheimnis [secret]. To do\nsomething heimlich, i.e. behind someone’s back; to steal\naway heimlich; heimlich meetings and appointments; to\nlook on with heimlich pleasure at someone’s discomfiture;\nto sigh or weep heimlich; to behave heimlich, as though\nthere was something to conceal; heimlich love, love-affair,\nsin; heimlich places (which good manners oblige us to\nconceal). 1 Sam, v. 6; “The heimlich chamber” [privy]. 2\nKings x. 27 etc.; “To throw into pits or Heimlichkeit.” Led\nthe steeds heimlich before Laomedon.” “As secretive,\nheimlich, deceitful and malicious towards cruel masters . .\n. as frank, open, sympathetic and helpful towards a friend\nin misfortune.” “The heimlich art” (magic). “Where public\nventilation has to stop, there heimlich machinations begin.” \n“Freedom is the whispered watchword of heimlich\nconspirators and the loud battle-cry of professed revolutionaries.” \n“A holy, heimlich effect.” “I have roots that are\nmost heimlich, I am grown in the deep earth.” “My heimlich pranks.” \n(Cf. Heimtücke [mischief]). To discover, disclose, betray someone’s Heimlichkeiten; “to concoct\nHeimlichkeiten behind my back.” Cf. Geheimnis.\nCompounds and especially also the opposite follow')
        btn10.background_color = [1, 105/255, 180/255, 1]
        btn11 = Button(text='\nmeaning I. (above): Unheimlich, uneasy, eerie, bloodcurdling; \n“Seeming almost unheimlich and ‘ghostly’ to him.”\n“I had already long since felt an unheimlich, even gruesome feeling.” \n“Feels an unheimlich horror.” “Unheimlich\nand motionless like a stone-image.” “The unheimlich mist\ncalled hill-fog.” “These pale youths are unheimlich and are\nbrewing heaven knows what mischief.” “‘Unheimlich’ is')
        btn11.background_color = [1, 105/255, 180/255, 1]
        btn12 = Button(text='')
        btn12.background_color = [168/255, 245/255, 200/255, 1]

        self.add_widget(btn1)
        self.add_widget(btn2)
        self.add_widget(btn3)
        self.add_widget(btn4)
        self.add_widget(btnfreud)
        self.add_widget(btn5)
        self.add_widget(btn6)
        self.add_widget(btn7)
        self.add_widget(btn8)
        self.add_widget(btn9)
        self.add_widget(btn10)
        self.add_widget(btn11)


class Critical_Reading(App):

    def build(self):

        return PageLayout()


if __name__ == '__main__':
    Critical_Reading().run()
