import random
import textwrap

# Define a list of passages with their respective author, title, and analysis
passages = [
    # Lanval
    {
        "passage": "This knight--by now you know the one-- Who'd served the King with many a deed, One day got on his noble steed And went riding, just for fun.",
        "author": "Marie de France",
        "title": "Lanval",
        "analysis": "This passage introduces Lanval, a knight who served King Arthur but feels abandoned. It sets up themes of isolation and longing for connection."
    },
    {
        "passage": "The knight took a step toward The maiden; she called him forward; Near the bed he sat down, near. '[Character],' she said, 'my friend, my dear.'",
        "author": "Marie de France",
        "title": "Lanval",
        "analysis": "This passage describes Lanval\u2019s encounter with a mysterious maiden, marking the beginning of their otherworldly romance, central to the lai's themes of love and loyalty."
    },
    {
        "passage": "Her body was well-shaped, and sweet. A rich mantle of white ermine, Lined with silk, alexandrine, Was her quilt, but she'd pushed it away.",
        "author": "Marie de France",
        "title": "Lanval",
        "analysis": "This passage emphasizes the maiden's physical beauty, reflecting the medieval ideal of courtly love and the power dynamics in romantic relationships."
    },
    {
        "passage": "Now [Character] knows not what to do; He's very thoughtful, very sad. A man alone, with no counsel--or bad-- A stranger in a strange land.",
        "author": "Marie de France",
        "title": "Lanval",
        "analysis": "Lanval\u2019s isolation is highlighted here, as his exile and loneliness underscore the emotional and social pressures of his situation."
    },
    {
        "passage": "[Character] has found a noble hostel: The more he spends, in buying bold, The more he'll have of silver and gold.",
        "author": "Marie de France",
        "title": "Lanval",
        "analysis": "Lanval\u2019s sudden wealth, granted by the maiden, reflects the fantastical elements of the story, with the idea of unlimited riches symbolizing desire and escape from societal constraints."
    },
    {
        "passage": "But if he can't prove his defense Then we must pronounce this sentence: He loses his right to serve the King, And the King will send him packing.",
        "author": "Marie de France",
        "title": "Lanval",
        "analysis": "This passage foreshadows the stakes of Lanval\u2019s trial, where his honor and place in Arthur\u2019s court are at risk, raising themes of loyalty and reputation."
    },
    {
        "passage": "If ever you want my conversation, You won't be able to think of a place Where a man may have his girl, and no eye chase Them with reproach or accusation.",
        "author": "Marie de France",
        "title": "Lanval",
        "analysis": "The maiden\u2019s promise to always be with Lanval emphasizes the supernatural and secret nature of their relationship, exploring themes of hidden love and societal judgment."
    },
    {
        "passage": "He'd offered her an ugly insult. He boasted of a friend so fair, So full of pride, breeding, honor, That the chambermaid who waited on her...",
        "author": "Marie de France",
        "title": "Lanval",
        "analysis": "This passage highlights the conflict between Lanval and Queen Guinevere, illustrating the tension between courtly loyalty and personal honor."
    },
    {
        "passage": "[Character] begins his own defense: Against his lord's honor he's made no offense; He refutes, word for word, The demand for love the Queen says she heard.",
        "author": "Marie de France",
        "title": "Lanval",
        "analysis": "Lanval\u2019s trial serves as a moment of moral confrontation, where truth and false accusation are central to the outcome, reflecting on the nature of justice in Arthurian legend."
    },
    {
        "passage": "The lady rides in at the palace door, Lovelier than any, since or before, To come there. Up to the King she rides, And dismounts, so she can be seen from all sides.",
        "author": "Marie de France",
        "title": "Lanval",
        "analysis": "This passage marks the climax of the lai, where the maiden arrives to save Lanval, embodying themes of divine intervention and the power of love."
    },

    # Beowulf
   {
        "passage": "The Spear-Danes in days gone by, and the kings who ruled them had courage and greatness. We have heard of those princes\u2019 heroic campaigns.",
        "author": "Unknown",
        "title": "Beowulf",
        "analysis": "This passage opens the poem by setting the tone of heroism and valor that characterized the early rulers of the Spear-Danes, establishing a legacy of greatness."
    },
    {
        "passage": "A ring-whorled prow rode in the harbor, ice-clad, outbound, a craft for a prince. They stretched their beloved lord in his boat, laid out by the mast, amidships, the great ring-giver.",
        "author": "Unknown",
        "title": "Beowulf",
        "analysis": "This passage describes a traditional Viking funeral, emphasizing the cultural significance of honor and ritual in sending off a revered leader."
    },
    {
        "passage": "The fortunes of war favored them. Friends and kinsmen flocked to their ranks, young followers, a force that grew to be a mighty army.",
        "author": "Unknown",
        "title": "Beowulf",
        "analysis": "This passage highlights the communal strength and unity in times of war, showing how loyalty and kinship were essential to building powerful armies."
    },
    {
        "passage": "Orders for work to adorn that wall stead were sent to many peoples. And soon it stood there, finished and ready, in full view, the hall of halls.",
        "author": "Unknown",
        "title": "Beowulf",
        "analysis": "The passage illustrates the construction of a grand hall, symbolizing the central role of craftsmanship and community in maintaining a ruler\u2019s legacy."
    },
    {
        "passage": "Far and wide through the world, I have heard, men adorned that hall with wonder, but the hall awaited a barbarous burning. That doom abided, but in time it would come.",
        "author": "Unknown",
        "title": "Beowulf",
        "analysis": "This passage foreshadows destruction, introducing the theme of impermanence and the inevitable fall of even the most impressive structures."
    },
    {
        "passage": "The harp being struck, and the clear song of a skilled poet telling with mastery of man\u2019s beginnings, how the Almighty had made the earth, a gleaming plain girdled with waters.",
        "author": "Unknown",
        "title": "Beowulf",
        "analysis": "This passage highlights the role of oral tradition and poetry in celebrating creation and praising divine power, emphasizing the cultural importance of storytelling."
    },
    {
        "passage": "And filled the broad lap of the world with branches and leaves; and quickened life in every other thing that moved.",
        "author": "Unknown",
        "title": "Beowulf",
        "analysis": "The passage reflects a sense of reverence for nature and creation, portraying the world as a flourishing, living entity, filled with divine energy."
    },
    {
        "passage": "The Almighty had made the earth, a gleaming plain girdled with waters; in His splendor, He set the sun and moon to be earth\u2019s lamplight.",
        "author": "Unknown",
        "title": "Beowulf",
        "analysis": "This passage conveys a religious worldview, attributing the beauty and order of the natural world to divine creation, highlighting the sacredness of the cosmos."
    },
    {
        "passage": "The ancient blade broke, bit into the monster\u2019s skin, drew blood again. Despair descended on the wretched hall-guest as the wound paralyzed his mortal spirit.",
        "author": "Unknown",
        "title": "Beowulf",
        "analysis": "The passage describes the struggle between supernatural forces and the power of ancient weapons, symbolizing the collision between human effort and fate."
    },
    {
        "passage": "Then the weathered veteran laid the precious sword in the lap of his lord, raised his voice and recounted the exploits of their fathers.",
        "author": "Unknown",
        "title": "Beowulf",
        "analysis": "This passage emphasizes the importance of ancestry and the passing of wisdom through generations, as veterans recount the deeds of past heroes."
    },

    # Sir Gawain and the Green Knight
    {
        "passage": "After the siege and the assault had ceased at Troy, the city been destroyed and burned to brands and ashes, the warrior who wrought there the trains of treason was tried for his treachery, the truest on earth.",
        "author": "Unknown",
        "title": "Sir Gawain and the Green Knight",
        "analysis": "This opening passage connects the events of the poem to classical legends like Troy, establishing a heroic and historical context for the story."
    },
    {
        "passage": "And when this Britain was founded by this great hero, bold men loving strife bred therein, and many a time they wrought destruction.",
        "author": "Unknown",
        "title": "Sir Gawain and the Green Knight",
        "analysis": "The passage highlights the legacy of conflict in Britain, setting up a world where chivalry and violence coexist."
    },
    {
        "passage": "For there the feast was held full fifteen days alike with all the meat and the mirth that men could devise.",
        "author": "Unknown",
        "title": "Sir Gawain and the Green Knight",
        "analysis": "This passage describes the grand feast at King Arthur\u2019s court, portraying the atmosphere of abundance and celebration in Camelot."
    },
    {
        "passage": "He was entirely green, all green was this man and his clothing; a straight coat sat tight to his sides; a fair mantle above, adorned within.",
        "author": "Unknown",
        "title": "Sir Gawain and the Green Knight",
        "analysis": "This passage introduces the Green Knight, whose unnatural appearance emphasizes the supernatural and mysterious nature of his character."
    },
    {
        "passage": "The axe, that is heavy enough, to handle as he likes; and I shall abide the first blow as bare as I sit.",
        "author": "Unknown",
        "title": "Sir Gawain and the Green Knight",
        "analysis": "Here, the Green Knight proposes his challenge, setting the stage for the central test of courage and honor in the story."
    },
    {
        "passage": "That was Gawain\u2019s first course come in with blare of trumpets, which were hung with many a bright banner.",
        "author": "Unknown",
        "title": "Sir Gawain and the Green Knight",
        "analysis": "This passage describes the formal atmosphere of courtly life and grandeur, adding to the theme of ceremony and tradition."
    },
    {
        "passage": "The lord, shouting for joy, shot and alighted full oft, and passed the day thus with joy till the dark night.",
        "author": "Unknown",
        "title": "Sir Gawain and the Green Knight",
        "analysis": "This passage captures the lord\u2019s joy in hunting, reflecting the medieval culture of hunting as both sport and symbol of nobility."
    },
    {
        "passage": "The knight took his leave and went his way; many a tiresome path he rode, as I heard the book tell.",
        "author": "Unknown",
        "title": "Sir Gawain and the Green Knight",
        "analysis": "This passage shows Gawain\u2019s journey, which is both physical and symbolic, representing his quest for honor and the trials he must face."
    },
    {
        "passage": "Gawain caught his breath, and stealthily he reached for the axe.",
        "author": "Unknown",
        "title": "Sir Gawain and the Green Knight",
        "analysis": "The passage describes a key moment in the challenge, illustrating Gawain\u2019s resolve and courage in facing the Green Knight\u2019s test."
    },
    {
        "passage": "But Gawain said, 'Though I be not now he that ye speak of, to reach such reverence as ye rehearse here, I am a man unworthy.'",
        "author": "Unknown",
        "title": "Sir Gawain and the Green Knight",
        "analysis": "This passage highlights Gawain\u2019s humility and his struggle with the expectations placed upon him as a knight."
    },

    # The General Prologue (The Canterbury Tales)
    {
        "passage": "Whan that Aprille with his shoures soote, The droghte of March hath perced to the roote, And bathed every veyne in swich lic\u00f3ur Of which vert\u00fa engendred is the flour;",
        "author": "Geoffrey Chaucer",
        "title": "The Canterbury Tales: The General Prologue",
        "analysis": "This opening passage sets the scene of springtime renewal and the beginning of pilgrimages, establishing a backdrop of nature\u2019s rejuvenation as a metaphor for spiritual journeys."
    },
    {
        "passage": "Bifil that in that seson on a day, In Southwerk at the Tabard as I lay, Redy to wenden on my pilgrymage To Caunterbury with ful devout corage,",
        "author": "Geoffrey Chaucer",
        "title": "The Canterbury Tales: The General Prologue",
        "analysis": "This passage introduces the narrator\u2019s intent to go on pilgrimage, establishing the context for the assembly of the pilgrims and the framing device of the tales."
    },
    {
        "passage": "A Knyght ther was, and that a worthy man, That fro the tyme that he first bigan To riden out, he loved chivalrie, Trouthe and hon\u00f3ur, fredom and curteisie.",
        "author": "Geoffrey Chaucer",
        "title": "The Canterbury Tales: The General Prologue",
        "analysis": "This passage introduces the Knight, an exemplar of chivalry and honor, whose reputation as a noble warrior serves as the ideal of medieval knighthood."
    },
    {
        "passage": "With hym ther was his sone, a yong Squi\u00e9r, A lovyere and a lusty bacheler, With lokkes crulle as they were leyd in presse. Of twenty yeer of age he was, I gesse.",
        "author": "Geoffrey Chaucer",
        "title": "The Canterbury Tales: The General Prologue",
        "analysis": "The Squire, the Knight\u2019s son, is depicted as youthful and energetic, embodying ideals of courtly love and reflecting the generational difference between father and son."
    },
    {
        "passage": "Ther was also a Nonne, a Prioresse, That of hir smylyng was ful symple and coy; Hire gretteste ooth was but by seinte Loy, And she was cleped madame Eglentyne.",
        "author": "Geoffrey Chaucer",
        "title": "The Canterbury Tales: The General Prologue",
        "analysis": "The Prioress is introduced as an overly refined religious figure, highlighting themes of religious hypocrisy and social appearances in Chaucer\u2019s critique of medieval institutions."
    },
    {
        "passage": "A Monk ther was, a fair for the maistrie, An outridere, that lovede venerie; A manly man, to been an abbot able. Ful many a deyntee hors hadde he in stable;",
        "author": "Geoffrey Chaucer",
        "title": "The Canterbury Tales: The General Prologue",
        "analysis": "This passage describes the Monk, whose love of hunting and worldly pleasures contradicts the expected behavior of monastic life, furthering Chaucer\u2019s critique of the Church."
    },
    {
        "passage": "A Marchant was ther with a forked berd, In motteleye, and hye on horse he sat; Upon his heed a Flaundryssh bevere hat; His bootes clasped faire and fetisly.",
        "author": "Geoffrey Chaucer",
        "title": "The Canterbury Tales: The General Prologue",
        "analysis": "The Merchant is depicted as a successful businessman, characterized by his fine dress and shrewd dealings, embodying the rising middle class of Chaucer\u2019s time."
    },
    {
        "passage": "A Sergeant of the Lawe, war and wys, That often hadde been at the Parvys, Ther was also, ful riche of excellence. Discreet he was, and of greet reverence\u2014",
        "author": "Geoffrey Chaucer",
        "title": "The Canterbury Tales: The General Prologue",
        "analysis": "This passage introduces the Lawyer, noted for his wisdom and reverence, embodying the ideal of a learned and respected professional in medieval society."
    },
    {
        "passage": "A good man was ther of religioun, And was a povre Person of a Toun; But riche he was of hooly thoght and werk. He was also a lerned man, a clerk,",
        "author": "Geoffrey Chaucer",
        "title": "The Canterbury Tales: The General Prologue",
        "analysis": "The Parson is depicted as a humble and virtuous priest, representing the ideal Christian figure in contrast to the other religious characters in the prologue."
    },
    {
        "passage": "A Miller was ther, a stout carl for the nones; Ful byg he was of brawn and eek of bones. That proved wel, for over-al, ther he cam, At wrastlynge he wolde have alwey the ram.",
        "author": "Geoffrey Chaucer",
        "title": "The Canterbury Tales: The General Prologue",
        "analysis": "This passage introduces the Miller, a strong and bawdy character known for his physical prowess and crude behavior, adding to the variety of personalities on the pilgrimage."
    },

    # The Wife of Bath’s Prologue and Tale
    {
        "passage": "Experience, though noon auctoritee were in this world, is right ynough for me to speke of wo that is in mariage:",
        "author": "Geoffrey Chaucer",
        "title": "The Wife of Bath's Prologue",
        "analysis": "The Wife of Bath establishes herself as an authority on marriage based on personal experience, dismissing scholarly or religious authority."
    },
    {
        "passage": "For lordinges, sith I twelf yeer was of age, housbondes at chirche dore I have had five",
        "author": "Geoffrey Chaucer",
        "title": "The Wife of Bath's Prologue",
        "analysis": "The Wife of Bath proudly boasts of having had five husbands, challenging societal norms about women's roles and remarriage."
    },
    {
        "passage": "Lo, here the wise king daun Salomon: I trowe he hadde wives many oon, As wolde God it leveful were to me To be refresshed half so ofte as he.",
        "author": "Geoffrey Chaucer",
        "title": "The Wife of Bath's Prologue",
        "analysis": "The Wife of Bath justifies her multiple marriages by referencing the biblical King Solomon, humorously expressing her wish for the same liberty."
    },
    {
        "passage": "I wol bistowe the flour of al myn age In th\u2019actes and in fruit of mariage.",
        "author": "Geoffrey Chaucer",
        "title": "The Wife of Bath's Prologue",
        "analysis": "The Wife of Bath asserts her intention to spend her life enjoying the benefits of marriage, emphasizing her unapologetic embrace of her desires."
    },
    {
        "passage": "Now sire, thanne wol I telle you forth my tale. As evere mote I drinke win or ale, I shal saye sooth: tho housbondes that I hadde, As three of hem were goode, and two were badde.",
        "author": "Geoffrey Chaucer",
        "title": "The Wife of Bath's Prologue",
        "analysis": "The Wife of Bath reveals her experience with different kinds of husbands, highlighting her power in managing relationships, especially over the bad ones."
    },
    {
        "passage": "For half so boldely can ther no man Sweren and lyen as a woman can.",
        "author": "Geoffrey Chaucer",
        "title": "The Wife of Bath's Prologue",
        "analysis": "The Wife of Bath ironically reflects on women\u2019s ability to lie, continuing her subversive and humorous critique of gender roles."
    },
    {
        "passage": "Whan that I hadde dronke a draughte of sweete win, Metellius, the foule cherl, the swin, That with a staf birafte his wif hir lif For she drank win, though I hadde been his wif.",
        "author": "Geoffrey Chaucer",
        "title": "The Wife of Bath's Prologue",
        "analysis": "The Wife of Bath compares herself to a historical figure, stressing her independence and refusal to be controlled, particularly by male figures."
    },
    {
        "passage": "Blessed be God that I have wedded five, Of whiche I have piked out the beste, Bothe of hir nether purs and of hir cheste.",
        "author": "Geoffrey Chaucer",
        "title": "The Wife of Bath's Prologue",
        "analysis": "She celebrates her five marriages and notes how she strategically benefited from each, showcasing her pragmatism and wit."
    },
    {
        "passage": "Forbede us thing, and that desiren we;",
        "author": "Geoffrey Chaucer",
        "title": "The Wife of Bath's Prologue",
        "analysis": "The Wife of Bath points out a human tendency to desire what is forbidden, especially in the context of relationships."
    },
    {
        "passage": "Wommen desiren to have sovereinetee As wel over hir housbonde as hir love, And for to been in maistrye him above.",
        "author": "Geoffrey Chaucer",
        "title": "The Wife of Bath's Tale",
        "analysis": "In her tale, the Wife of Bath reveals that women desire sovereignty and control over their husbands, reflecting her own views on marriage and gender dynamics."
    },

    # The York Play of the Crucifixion
    {
        "passage": "Sir knights, take heed hither in haste, This death without trouble we cannot draw, Ye know yourselves as well as I How lords and leaders of our law Have given doom that this dolt shall die.",
        "author": "Unknown",
        "title": "The York Play of the Crucifixion",
        "analysis": "The soldiers prepare to carry out the crucifixion, emphasizing their duty-bound role in fulfilling the orders of their leaders, while dehumanizing Jesus as a 'dolt.'"
    },
    {
        "passage": "The foulest death of all shall he die for his deeds. That means cross him we shall. Behold so right he redis.",
        "author": "Unknown",
        "title": "The York Play of the Crucifixion",
        "analysis": "The soldiers discuss the brutality of the crucifixion, portraying it as a deserved punishment for Jesus, and foreshadowing the suffering that he will endure."
    },
    {
        "passage": "Come forth thou cursed knave, Thy comfort soon shall cool. Thy reward here shalt thou have.",
        "author": "Unknown",
        "title": "The York Play of the Crucifixion",
        "analysis": "The soldiers mock Jesus, continuing the theme of ridicule and cruelty as they prepare him for the crucifixion, demonstrating their callousness."
    },
    {
        "passage": "Almighty God my Father free, Let this matter be kept in mind, Thou bid\u2019st that I should obedient be, For Adam\u2019s guilt I should be pyned.",
        "author": "Unknown",
        "title": "The York Play of the Crucifixion",
        "analysis": "Jesus speaks, accepting his fate as a sacrifice for humanity's sins, highlighting the Christian themes of redemption and obedience to divine will."
    },
    {
        "passage": "Look that the lad on length be laid, And made full fast unto this tree. For all his acts he shall be flayed.",
        "author": "Unknown",
        "title": "The York Play of the Crucifixion",
        "analysis": "The soldiers coldly discuss the physical process of crucifying Jesus, treating it as a routine task while foreshadowing the violence to come."
    },
    {
        "passage": "His falling was more cruel Than all the hurts he had. Now may a man well count The last joint of this lad.",
        "author": "Unknown",
        "title": "The York Play of the Crucifixion",
        "analysis": "The soldiers comment on the physical suffering inflicted on Jesus, emphasizing the cruelty and relentless nature of the punishment."
    },
    {
        "passage": "Forgive these men that do me pain. What they do know they not, Therefore, my Father I crave Let never their sins be sought.",
        "author": "Unknown",
        "title": "The York Play of the Crucifixion",
        "analysis": "Jesus' plea for forgiveness highlights his compassion and the Christian theme of mercy, even in the face of extreme suffering."
    },
    {
        "passage": "We! hark, sir knights, for Mahomet\u2019s blood! Of Adam-kind is all his thought. The wizard waxeth worse than mad, This doleful deed he dreadeth not.",
        "author": "Unknown",
        "title": "The York Play of the Crucifixion",
        "analysis": "The soldiers mock Jesus\u2019 focus on humanity\u2019s salvation, dismissing his teachings and characterizing him as a madman."
    },
    {
        "passage": "Let\u2019s see who bears him best. His limbs on length then shall I lead, And even unto the bore them bring.",
        "author": "Unknown",
        "title": "The York Play of the Crucifixion",
        "analysis": "The soldiers prepare to nail Jesus to the cross, treating the act with an air of competition, dehumanizing Jesus further."
    },
    {
        "passage": "If any mourning may be mete Or mischief measured unto mine. My Father that all grief may mend, Forgive these men that do me pain.",
        "author": "Unknown",
        "title": "The York Play of the Crucifixion",
        "analysis": "Jesus reflects on his suffering and the sorrow it causes, once again expressing his plea for forgiveness for his persecutors."
    },

    # The Second Shepherds' Play

    {
        "passage": "Lord, but this weather is cold! And I am ill wrapped. A am nearly a dolt, so long have I napped.",
        "author": "Unknown",
        "title": "The Second Shepherds' Play",
        "analysis": "The opening lines emphasize the harsh weather conditions and the shepherds\u2019 physical discomfort, reflecting the hardships faced by common folk during the time."
    },
    {
        "passage": "These men that are wed have not their own will, They are full hard put to, but they sigh full still.",
        "author": "Unknown",
        "title": "The Second Shepherds' Play",
        "analysis": "This passage humorously reflects on the struggles of married life, with the shepherds lamenting their lack of autonomy under the rule of their wives."
    },
    {
        "passage": "Was never since Noah's flood such floodings seen; Winds and rains so rude and storms so keen;",
        "author": "Unknown",
        "title": "The Second Shepherds' Play",
        "analysis": "The shepherds compare their current struggles with the biblical flood, using hyperbole to emphasize the extreme weather conditions and their misfortune."
    },
    {
        "passage": "Now Lord, in thy names seven that made both moon and stars, More than I can count in heaven, thy will from bliss me bars;",
        "author": "Unknown",
        "title": "The Second Shepherds' Play",
        "analysis": "Mak invokes the Lord\u2019s name, but his lament about being barred from happiness contrasts with his later actions of deception, showcasing his duplicitous character."
    },
    {
        "passage": "Peace, I say, lad, no more of jangling, Hold your tongue!",
        "author": "Unknown",
        "title": "The Second Shepherds' Play",
        "analysis": "The shepherds chide one another, displaying the camaraderie and banter typical of their social interactions, which adds humor to the play\u2019s depiction of rural life."
    },
    {
        "passage": "A fat sheep, I dare say, A good fleece, I dare lay, Pay back when I may, But this will I 'borrow'.",
        "author": "Unknown",
        "title": "The Second Shepherds' Play",
        "analysis": "Mak steals a sheep under the guise of \u2018borrowing,\u2019 reflecting his cunning nature and the central conflict of the play as he tries to deceive the shepherds."
    },
    {
        "passage": "Ah, my middle! I pray to God so mild, If ever I you beguiled, That I should eat this child That lies in this cradle.",
        "author": "Unknown",
        "title": "The Second Shepherds' Play",
        "analysis": "Mak\u2019s wife attempts to hide the stolen sheep by pretending it is their newborn child, adding a layer of farcical comedy to the deception plot."
    },
    {
        "passage": "He is like to our sheep. How, Gib, may I peep?",
        "author": "Unknown",
        "title": "The Second Shepherds' Play",
        "analysis": "The shepherds begin to suspect that the \u2018child\u2019 is actually the stolen sheep, revealing the comic resolution of the deception as the truth starts to emerge."
    },
    {
        "passage": "Rise, gentle shepherds, for now is he born Who shall fetch from the fiend what from Adam was torn.",
        "author": "Unknown",
        "title": "The Second Shepherds' Play",
        "analysis": "An angel announces the birth of Christ, shifting the tone of the play from comedy to religious reverence, tying the nativity story to the lives of the common shepherds."
    },
    {
        "passage": "Hail, comely and clean! Hail, young child! Hail, maker, as I mean, of a maiden so mild!",
        "author": "Unknown",
        "title": "The Second Shepherds' Play",
        "analysis": "The shepherds greet the Christ child with reverence and gifts, marking the culmination of their spiritual journey and the play\u2019s transition from earthly struggles to divine salvation."
    },

]

random.shuffle(passages)

def display_wrapped_text(text, width=70):
    """Helper function to display wrapped text to avoid breaking words."""
    wrapped_text = textwrap.fill(text, width)
    print(wrapped_text)

def show_instructions():
    """Display game instructions at the beginning."""
    instructions = [
        "Welcome to the English 1 Midterm Study Guide!",
        "Instructions:",
        "- You will be shown a passage from a text.",
        "- Guess the title of the text.",
        "- Type 'skip' to skip the current passage.",
        "- Type 'q' at any time to quit the quiz.",
    ]
    print("\n".join(instructions))

def quiz():
    # Show instructions at the start
    show_instructions()

    for passage_data in passages:
        # Display the passage text
        print("\nIdentify the following passage:\n")
        display_wrapped_text(f"\"{passage_data['passage']}\"")

        # Get user input for the title guess
        title_guess = input("\nWhat is the title of the text? (Type 'skip' to skip or 'q' to quit): ").strip().lower()

        # Check for exit or skip commands
        if title_guess == 'q':
            print("Exiting the quiz.")
            break
        elif title_guess == 'skip':
            print("Skipping this passage.")
            continue

        # Check if the title guess is correct
        correct_title_words = set(passage_data['title'].lower().split())
        title_guess_words = set(title_guess.lower().split())
        
        if title_guess_words.issubset(correct_title_words):
            print("\nCorrect! Your guess matches the title.")
        else:
            print("\nIncorrect. Your guess does not match the title.")

        # Display the correct answer
        print("\nCorrect answer:")
        print(f"Author: {passage_data['author']}")
        print(f"Title: {passage_data['title']}")
        display_wrapped_text(f"Analysis: {passage_data['analysis']}")

        # Ask if the player is ready for the next passage
        ready_for_next = input("\nAre you ready for the next passage? (y/n or 'q' to quit): ").strip().lower()
        if ready_for_next == 'q':
            print("Exiting the quiz.")
            break
        elif ready_for_next == 'n':
            print("Stopping the quiz.")
            break

    print("Thanks for playing!")

# Run the quiz
quiz()