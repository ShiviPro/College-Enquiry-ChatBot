from nltk.chat.util import Chat, reflections
import string

pairs = [
    [
      "hello|hey", ["Hey there","Hi", "Oh hey",  ]
    ],
    [
        "who (.*) you ?|what (.*) you ?", ["I'm 'Sean', I'm an A.I. - based robot.\nCould you please give your name ?",
                                           "Myself 'Sean', I'm an A.I. - based robot.\nCould you please give your name ?",
                                           "My name is 'Sean', I'm an A.I. - based robot.\nCould you please give your name ?", ]
    ],
    [
        "i'm (.*)", ["Ok %1, now could you tell me, what is it you want to know ?", ]
    ],
    [
        "myself (.*)", ["Ok %1, now could you tell me, what is it you want to know ?", ]
    ],
    [
        "my name is (.*)", ["Ok %1, now could you tell me, what is it you want to know ?", ]
    ],
    [
        "i (.*) know (.*) college ?", ["""'yyyyy' has a 1.8 acre campus which comprises of the diferent buildings:
	* University Gardens
	* yyyyy Student Centre
	* yyyyy Centre for Research
	* Polyhouse Gardens
	* yyyyy Instrumentation Facility
	* University Auditorium
	* yyyyy Innovation Studio
	* Univerity Theatre
	* University Professional Clubs
	* University Hospitals
	* University Indoor Stadium
	* University GYM
	* University Lounge
	* University Mall
	* Food Kiosks
	* Student Residencies(Boys/Girls Hostels and Apartments)
	* yyyyy Central Library
	* Laboratories: COMPUTER(REGULAR as well as MAC LAB), PHY/CHEM/BOTANY/ZOOLOGY labs.
	* Different Blocks: Administrative and Academic blocks

Would you like to know about any building in particular ?""", ]
    ],
    [
        "(.*) i (.*) know (.*) university gardens.|i (.*) know (.*) university gardens.", [
        "The 'University Gardens' comprise of a lushy green landscape filled with various colourful shrubs,\nand I'm pretty sure that you would be quite be impressed by the view of it.", ]
    ],
    [
        "(.*) i (.*) know (.*) student centre ?|i (.*) know (.*) student centre ?", [
        "Well, from what I know, 'Student Centre' is the centre of all the 'Student Clubs' that essentially are the semi-autonomous social organisations managed by students.\nWould you like to know about the 'Student Clubs' ?", ]
    ],
    ["(.*) i (.*) know (.*) student centre ?|i (.*) know (.*) student centre ?", [
        "Well, from what I know, 'Student Centre' is the centre of all the 'Student Clubs' that essentially are the semi-autonomous social organisations managed by students.\nWould you like to know about the 'Student Clubs' ?", ]
     ],
    [
        "(.*) i (.*) know (.*) the student clubs ?|i (.*) know (.*) the student clubs ?", [
        "This, in my opinion is the best place to hangout in your free/liesure time,\nsince here you can have fun playing various indoor games ranging from Fantasy to Action genre\n as well as outdoor games ranging from hand-held games like 'Badminton' to foot-held games like 'Soccer'.\nAll this by just participating and/or coordinating in different Club actvities.", ]
    ],
    [
        "(.*) i (.*) know (.*) the centre for research ?|i (.*) know (.*) the centre for research ?", [
        "Well, as you can tell by the name that 'RESEARCH' is the main concern of this division.\nNow the research that is done here might be from various 'Curriculam Changes' to any changes in the 'Placement Criteria'. ", ]
    ],
    [
        "(.*) i (.*) know (.*) polyhouse gardens ?|i (.*) know (.*) polyhouse gardens ?", [
        "The 'PolyHouse Gardens' portray some of the beautiful, and sensitive 'shrubs' sheltered inside a large 'Green House' wherein you are going to enjoy a certain 'ambience'.", ]
    ],
    [
        "(.*) i (.*) know (.*) yyyyy instrumentation facility ?|i (.*) know (.*) yyyyy instrumentation facility ?", [
        "Well, the 'Instrumentation Facility' deals with supplies and repairs of various musical instruments; physical, chemical, as well as biological apparatus.\nIn some cases, it can also be used as a 'Laboratory facility' for experimenting on various industry-level equipments.", ]
    ],
    [
        "(.*) i (.*) know (.*) university auditorium ?|i (.*) know (.*) university auditorium ?", ["""Well, the 'University Auditorium' is the epi-centre of all the university activities that includes :
	* EDM Nights,
	* Guest Lectures,
	* Celebrity Interviews,
	* Various Plays,
	* Educational Seminars,
	many such things.
      It is a big hall of that can capacitate atleast 500 people easily at a time.\nIt consists of a total of 10 A.C.s part of an efficient Air-Condtioning System, and a big stage surrounded by special seats fixed for 'Dignitaries'.""", ]
    ],
    [
        "(.*) i (.*) know (.*) innovation studio ?|i (.*) know (.*) innovation studio ?", [
        "Ok, now this is some interesting thing to talk about. The 'Innovation Studio' as you might have guessed has something to do with innovation.\nWell, it's here that students bring  their budding project ideas in order to seek further advice, and/or to build their projects.\nSince the ambience of this place is helpful in productive thinking, students love to visit this  place.\nWho knows maybe, one day you also make your dream project come true.", ]
    ],
    [
        "(.*) i (.*) know (.*) the university theatre ?|i (.*) know (.*) the university theatre ?", [
        "If you're into dramatics, then it's a place of which you might want to keep track with.\nSince this contains some of the biggest yyyyy's drama artists, it will always be helpful for you. ", ]
    ],
    [
        "(.*) i (.*) know (.*) the professional clubs ?|i (.*) know (.*) the professional clubs ?", [
        "Ok, so the 'Professional Clubs' will help you with expanding your skill-set, in case you sit for the University's 'Campus Placements'(or, 'on-site placements').\nSince in this process, you will be tested for your professionalism regarding skills like, flawless english-speaking along with many other competitive tasks and ofcourse, the interviews. ", ]
    ],
    [
        "(.*) i (.*) know (.*) the university hospitals ?|i (.*) know (.*) the university hospitals ?", [
        '''Let us consider a situation wherein you catch cetain fever ie seasonal, you're coughing, as well as burning up !\nWhat do you do ?\nWell this is when you visit the 'University Hospitals' ,\nwhrein you will be given proper treatment and medicines for the same.\nIn case of physical problem, you shall always visit the hospital, since "PRECAUTION IS BETTER THAN CURE" ''']
    ],
    [
        "(.*) i (.*) know (.*) the indoor stadium ?|i (.*) know (.*) the indoor stadium ?", [
        "Well, isn't it obvious, it's the place where you can play any outdoor game you wanna play.\nJust name it and the guys would provide you the corresponding place(or, court) to play it.\nMay it be Football, Basketball, Rugby, Hockey, Tennis(both table as well as lawn), and etc ; if you want to play it, here you can.", ]
    ],
    [
        "(.*) i (.*) know (.*) the gym ?|i (.*) know (.*) the gym ?", [
        '''Woof, so many sweaty people, I can't stand the sound of it.\nBut it maybe that you are interested in having a perfect body, or just daily exercise commitment. Well whatever the reason may be you can join the University Gyms(there a total of 4).\nBe ready to sweat as much you can prior to visiting this place.\nWell it's as they say, "No pain, no gain".''', ]
    ],
    [
        "(.*) i (.*) know (.*) the university lounge ?|i (.*) know (.*) the university lounge ?", [
        "Okk, so it's Friday night, and you might be wondering what to do first.\nWell the University Lounge is probably the best place to go and enjoy your time as the weekend begins.", ]
    ],
    [
        "(.*) i (.*) know (.*) the university mall ?|i (.*) know (.*) the university mall ?", [
        "Ohh yeah, the Mall could also be a viable place to hangout on Friday evenings.\nIt mostly is the place you would want to visit in the evenings, because of the lighting, place and the overall aura that the place carries.", ]
    ],
    [
        "(.*) i (.*) know (.*) the food kiosks ?|i (.*) know (.*) the food kiosks ?", ["""Okk, so it's the 'Food Kiosks' which you might be visiting most frequently when inside the University Campus,\nsince here you can get your daily meals(ie, Breakfast, Lunch, and Dinner) apart from the members of the Hostel Mess.\nBy the way, would you like to know about the Hostel Mess ?""", ]
    ],
    [
        "(.*) i (.*) know (.*) the hostel mess ?|i (.*) know (.*) the hostel mess ?", [
        "The 'Hostel Mess' is the place where you can get your daily meals(all 4) at an annual subscription of Rs. XXXXX for a vide variety of the food available to choose from.\nNOTE - Only available for those who opted for Hostel facilities.", ]
    ],
    [
        "(.*) i (.*) know (.*) the student residencies / hostels ?|i (.*) know (.*) the student residencies / hostels ?",[
        "The 'Student Residencies' or as they are commonly known as 'Hostels', are the buildings that reside the students of the University.\nThe students here can opt for many different kinds of rooms (one-seater, two-seater, three-seater, four-seater).\nApart from the additional Laundary and Mess facilities, there is the Mini Departmental Store, Cloak Room, and the Study Room.\nIn case of any misconduct and/or problem regarding any important related matter to any of the provided hostel facilities, the student can also approach the Warden Office,\nwhich is used to maintain the discipline of the Hostels.\nEvery room is equipped with the required amount of Chairs, Beds, and Study Tables(depends on the no. of the students in the room), a tubelight, a CFL bulb,  a Bathroom(with Geyser), a Washroom , and a Cooler/A.C.(whichever is opted by the students of the room.)", ]
    ],
    [
        "(.*) i (.*) know (.*) the library ?|i (.*) know (.*) the library ?", [
        "Well the 'Central Library', is your go-to destination for getting any of the books respective to your courses/fields/departments.\nYou can issue a book for a standard period of 1 week and/or reissue it after a week.\nIt can also be a place for undisturbed reading, coding, designing, and pretty much anything related to productivity.  ", ]
    ],
    [
        "(.*) i (.*) know (.*) the labs ?|i (.*) know (.*) the labs ?", [
        "There is a vast variety of labs present in the Academic blocks; depending on your course and the department your course is concerned with.\nThe labs are specifically designed to provide the best experience while performing experiments of various sorts.\nSome of these are open on Saturdays as well as Sundays for Students to practise for some extra time.", ]
    ],
    [
        "(.*) i (.*) know (.*) the academic blocks ?i (.*) know (.*) the academic blocks ?", ['''There are certain academic blocks in the campus. These concern different departments, and are as follows:
        * Business Block - Building No. 14.
        * Computer Science And Engineering - Building No. 33, 34, and 37.
        * Mechanical Engineering - Building No. 56.
        * Civil engineering - Building No. 57
        * Electronics And Electrical Engineering - Building No. 36
        * Bioengineering And Biosciences - Building No. 26
        * Architecture And Design - Building No. 18
        * Hotel Management And Tourism - Building No. 13
        * Computer Application - Building No. 38
        * Pharmaceutical Sciences - Building No. 26
        * Agriculture - Building No. 25
        * Journalism, Films, And Creative Arts - Building No. 19
        * Chemical Engineering And Physical Sciences - Building No. 27
        * Law - Building No. 21
        * Polytechnic - Building No. 55
        * Social Sciences And Foreign Languages - Building No. 20

    Apart form these blocks there are the residential blocks, and the Administrative Blocks, which are as follows:
        * Boys Hostels:
            **1 - 43
            **2 - 45
            **3 - 46
            **4 - 47
            **5 - 51
            **6 - 52
        * Girls Hostels:
            **1 - 09
            **2 - 10
            **3 - 11
            **4 - 12
            **5 - 21
            **6 - 22
       * Admission Block - Building No. 30, 31, and 32.
       * Administration Block -  Building No. 28, and 29.''', ]
    ],
    [
        "quit", [
        "It was nice talking to you. But like all great things, this also needs to end.\n Best of luck for future.Bye !", ]
    ],
    [
		"hindi", ["आपका बहुत बहुत स्वागत है । कॉलेज के बारे में कोई सवाल है, मुझसे पूछो!", ]
	],
    [
      "नमस्कार|सादर नमस्कार|नमस्ते", ["आपको भी नमस्ते","आपको भी सादर नमस्कार" ]
    ],
    [
		"आप कौन हैं ?|आप क्या हैं ?", ["मैं 'सीन' हूँ, एक ए.आई. - आधारित रोबोट। क्या आप अपना नाम बता सकते हैं?",
                                      "मेरा नाम 'शान' है, मैं ए.आई. - आधारित रोबोट। क्या आप अपना नाम बता सकते हैं?", ]
	],
    [
		"मैं (.*) हूँ|मेरा नाम (.*) है", ["ठीक है %1, अब आप बता सकते हैं कि आप क्या जानना चाहते हैं?", ]
	],
    [
		"मैं कॉलेज के बारे में जानना चाहूंगा?", ["""'yyyy' में 1.8 एकड़ का परिसर है, जिसमें अलग-अलग इमारतें हैं:
* यूनिवर्सिटी गार्डन
* yyyyy छात्र केंद्र
* अनुसंधान के लिए yyyyy केंद्र
* पॉलीहाउस गार्डन
* yyyyy इंस्ट्रूमेंटेशन सुविधा
* विश्वविद्यालय सभागार
* yyyyy नवाचार स्टूडियो
* यूनीवर्सिटी थियेटर
* यूनिवर्सिटी प्रोफेशनल क्लब
* विश्वविद्यालय अस्पताल
* विश्वविद्यालय इंडोर स्टेडियम
* विश्वविद्यालय GYM
* यूनिवर्सिटी लाउंज
* यूनिवर्सिटी मॉल
* खाद्य कियोस्क
* छात्र निवास (लड़के / लड़कियाँ छात्रावास और अपार्टमेंट)
* य्येय केंद्रीय पुस्तकालय
* प्रयोगशालाएँ: कंप्यूटर (REGULAR साथ ही MAC LAB), PHY / CHEM / BOTANY / ZOOLOGY लैब।
* विभिन्न ब्लॉक: प्रशासनिक और शैक्षणिक ब्लॉक

क्या आप विशेष रूप से किसी भी इमारत के बारे में जानना चाहेंगे?""", ]
	],
    [
		"हाँ, मैं विश्वविद्यालय के उद्यानों के बारे में जानना चाहूंगा?", ["'यूनिवर्सिटी गार्डन' में विभिन्न रंग-बिरंगी झाड़ियों से भरे हरे-भरे परिदृश्य का समावेश है, और मुझे पूरा यकीन है कि आप इसे देखकर काफी प्रभावित होंगे।", ]
	],
    [
		"हाँ, मैं छात्र केंद्र के बारे में जानना चाहूंगा?", ["जहाँ तक मैं जानता हूं, 'स्टूडेंट सेंटर' उन सभी 'स्टूडेंट्स क्लब्स' का केंद्र है, जो अनिवार्य रूप से छात्रों द्वारा प्रबंधित अर्ध-स्वायत्त सामाजिक संगठन हैं।\nक्या आप 'स्टूडेंट क्लब' के बारे में जानना चाहेंगे?", ]
	],
    [
		"हाँ, मैं छात्र क्लबों के बारे में जानना चाहूंगा?", ["यह, मेरी राय में आपके खाली समय में यही आपका अड्डा होगा, क्योंकि यहाँ आप 'बैडमिंटन' जैसे हैंड-गेम्स जैसे आउटडोर गेम्स खेलने का मज़ा ले सकते हैं।\nपैर के माध्यम से खेले जाने वाले खेल जैसे 'सॉकर'।\nयह सब विभिन्न क्लब अधिनियमों में सिर्फ भाग लेने और / या समन्वय करके।", ]
	],
    [
		"हाँ, मैं अनुसंधान केंद्र के बारे में जानना चाहूंगा?", ["वैसे, जैसा कि आप बता सकते हैं कि 'अनुसंधान' इस विभाजन की मुख्य काम है।\nअब जो शोध यहाँ किया जाता है वह विभिन्न 'पाठ्यक्रम में बदलाव' से लेकर 'प्लेसमेंट मानदंड' में किसी भी बदलाव तक हो सकता है।", ]
	],
    [
		"हाँ, मैं पॉलीहाउस उद्यानों के बारे में जानना चाहूंगा?", ["'पॉलीहाउस गार्डन' एक बड़े 'ग्रीन हाउस' के अंदर कुछ खूबसूरत, और संवेदनशील 'झाड़ियों' को चित्रित करता है, जिसमें आप एक निश्चित 'माहौल' का आनंद ले सकते हैं।", ]
	],
    [
		"हाँ, मैं yyyyy इंस्ट्रूमेंटेशन सुविधा के बारे में जानना चाहूंगा?", ["खैर, 'वाद्ययंत्र सुविधा' विभिन्न संगीत वाद्ययंत्रों की आपूर्ति और मरम्मत से संबंधित है; भौतिक, रासायनिक, साथ ही साथ जैविक उपकरण। कुछ मामलों में, इसका उपयोग विभिन्न उद्योग-स्तरीय उपकरणों पर प्रयोग करने के लिए एक 'प्रयोगशाला सुविधा' के रूप में भी किया जा सकता है।", ]
	],
    [
		"हाँ, मैं यूनिवर्सिटी ऑडिटोरियम के बारे में जानना चाहूंगा?", ["""खैर, 'विश्वविद्यालय सभागार' विश्वविद्यालय की सभी गतिविधियों का उप-केंद्र है, जिसमें शामिल हैं:
* ईडीएम नाइट्स,
* अतिथि व्याख्यान,
* सेलिब्रिटी साक्षात्कार,
* विभिन्न नाटकों,
* शैक्षिक सेमिनार, ऐसी बहुत सी बातें।
  यह एक बड़ा हॉल है जो एक बार में कम से कम 500 लोगों को आसानी से बैठने की क्षमता रखता है। इसमें एक कुशल एयर-कंडिशनिंग सिस्टम
  का कुल 10 A.C. हिस्सा शामिल है, और 'गणमान्य व्यक्तियों' के लिए तय विशेष सीटों से घिरा एक बड़ा मंच है।""", ]
	],
    [
		"हाँ, मैं यूनिवर्सिटी थिएटर के बारे में जानना चाहूंगा?", ["यदि आप नाटकीयता में रुचि रखते हैं, तो यहाँ आप अधिक बार आएंगे। चूँकि इसमें कुछ सबसे बड़े yyyyy के ड्रामा कलाकार शामिल हैं,\nइसलिए यह हमेशा आपके लिए उपयोगी होगा।", ]
	],
    [
		"हाँ, मैं इनोवेशन स्टूडियो के बारे में जानना चाहूंगा?", ["ठीक है, अब इस बारे में बात करने के लिए कुछ दिलचस्प बात है। 'इनोवेशन स्टूडियो' जैसा कि आपने अनुमान लगाया होगा कि इनोवेशन के साथ कुछ करना है।\nखैर, यह यहाँ है कि छात्रों को आगे की सलाह लेने के लिए और / या अपनी परियोजनाओं के निर्माण के लिए अपने नवोदित परियोजना विचारों को लाना है।\nचूँकि इस जगह का परिवेश उत्पादक सोच में सहायक है, इसलिए छात्रों को इस जगह की यात्रा करना बहुत पसंद है।\nकौन जानता है कि हो सकता है, एक दिन आप भी अपने ड्रीम प्रोजेक्ट को साकार करें।", ]
	],
    [
		"हाँ, मैं पेशेवर क्लबों के बारे में जानना चाहूंगा?", ["ठीक है, इसलिए 'व्यावसायिक क्लब' आपको विश्वविद्यालय के 'कैम्पस प्लेसमेंट' (या, 'ऑन-साइट प्लेसमेंट') के लिए बैठने की स्थिति में, आपके कौशल-सेट के विस्तार में मदद करेंगे।\nइस प्रक्रिया के बाद से, आपको कई अन्य प्रतिस्पर्धी कार्यों और साक्षात्कार के साथ-साथ, धाराप्रवाह अंग्रेजी बोलने जैसे कौशल के बारे में आपके व्यावसायिकता का परीक्षण किया जाएगा।", ]
	],
    [
		"हाँ, मैं विश्वविद्यालय अस्पतालों के बारे में जानना चाहूंगा?", ["आइए हम एक ऐसी स्थिति पर विचार करें जिसमें आपको मौसमी बुखार हो जाता हैं, साथ ही आपको खांसी होती है! आप क्या करेंगे ?\nखैर तब आप 'यूनिवर्सिटी अस्पताल' में जाते हैं, जब आपको उचित उपचार और दवाइयाँ दी जाती हैं। शारीरिक समस्या के मामले में, आप हमेशा अस्पताल का दौरा करेंगे।"]
	],
    [
		"हाँ, मैं इनडोर स्टेडियम के बारे में जानना चाहूंगा?", ["खैर, यह स्पष्ट नहीं है, यह वह जगह है जहाँ आप कोई भी बाहरी खेल खेल सकते हैं जिसे आप खेलना चाहते हैं।\nबस इसे नाम बोलें और लोग आपको उसे खेलने के लिए संबंधित स्थान प्रदान करेंगे।\nयह फुटबॉल, बास्केटबॉल, रग्बी, हॉकी, टेनिस (दोनों टेबल के साथ-साथ लॉन), और आदि हो सकता है;\n यदि आप इसे खेलना चाहते हैं, तो यहाँ आप कर सकते हैं।", ]
	],
    [
		"हाँ, मैं जिम के बारे में जानना चाहूंगा?", ["नहीं, इतने पसीने से तर लोग, मैं यह सहन नहीं कर सकता।\nलेकिन यह हो सकता है कि आप एक संपूर्ण शरीर, या सिर्फ दैनिक व्यायाम की प्रतिबद्धता में रुचि रखते हैं।\nखैर जो भी कारण हो आप विश्वविद्यालय जिम (कुल 4) में शामिल हो सकते हैं।\nइस जगह पर जाने से पहले जितना हो सके उतना पसीना बहाने के लिए तैयार रहें।", ]
	],
    [
		"हाँ, मैं यूनिवर्सिटी लाउंज के बारे में जानना चाहूंगा?", ["ठीक है, हम मानते हैं की यह शुक्रवार की संध्या है, और आप सोच रहे होंगे कि पहले क्या करना है। वीकेंड शुरू होते ही अपने समय का आनंद लेने और घूमने का सबसे अच्छा स्थान शायद यूनिवर्सिटी लाउंज है।", ]
	],
    [
		"हाँ, मैं यूनिवर्सिटी मॉल के बारे में जानना चाहूंगा?", ["ओह हाँ, मॉल शुक्रवार की शाम को घूमने के लिए एक व्यवहार्य स्थान हो सकता है।\nयह वो जगह है जहाँ आप शाम को घूमना चाहेंगे, क्योंकि प्रकाश, और समग्र आभा कि जगह वहन करती है।", ]
	],
    [
		"हाँ, मैं फूड कियोस्क के बारे में जानना चाहूंगा?", ["ठीक है, वह याही है, जो आप यूनिवर्सिटी कैंपस के अंदर सबसे अधिक बार जाएंगे,\nयहाँ से आप हॉस्टल मेस के सदस्यों के अलावा अपना दैनिक भोजन (जैसे, नाश्ता, दोपहर का भोजन और रात का खाना) प्राप्त कर सकते हैं।\nवैसे,क्या आप हॉस्टल मेस के बारे में जानना चाहेंगे?", ]
	],
    [
		"हाँ, मैं हॉस्टल मेस के बारे में जानना चाहूंगा?", ["'हॉस्टल मेस' वह स्थान है जहाँ आप अपना दैनिक भोजन (सभी 4) रुपये की वार्षिक सदस्यता पर प्राप्त कर सकते हैं। यहाँ विभिन्न प्रकार के भोजन उपलब्ध हैं। नोट - केवल उन लोगों के लिए उपलब्ध है जो हॉस्टल सुविधाओं का विकल्प चुनते हैं।", ]
	],
    [
		"हाँ, मैं छात्र निवासों / छात्रावासों के बारे में जानना चाहूंगा?", ["'छात्र निवास' या जैसा कि वे आमतौर पर "
                                                                            "'छात्रावास' के रूप में जाना जाता है, "
                                                                            "वे इमारतें हैं जहान पे विश्वविद्यालय के "
                                                                            "छात्र निवास करते हैं।\nयहाँ के छात्र कई "
                                                                            "अलग-अलग प्रकार के कमरों (एक-सीटर, "
                                                                            "दो-सीटर, तीन-सीटर, चार-सीटर) का विकल्प "
                                                                            "चुन सकते हैं।\nअतिरिक्त लॉन्डरी और मेस "
                                                                            "सुविधाओं के अलावा, मिनी डिपार्टमेंटल "
                                                                            "स्टोर, क्लोक-रूम और स्टडी-रूम भी "
                                                                            "है।\nकिसी भी छात्रावास की किसी भी "
                                                                            "महत्वपूर्ण सुविधा से संबंधित किसी भी "
                                                                            "समस्या के मामले में, छात्र वार्डन "
                                                                            "कार्यालय से भी संपर्क कर सकता है, "
                                                                            "जिसका उपयोग छात्रावासों के अनुशासन को "
                                                                            "बनाए रखने के लिए किया जाता है।\nहर कमरा "
                                                                            "आवश्यक कुर्सियों, बिस्तरों और स्टडी टेबल "
                                                                            "(कमरे में छात्रों की संख्या पर निर्भर "
                                                                            "करता है), एक ट्यूबलाइट, एक सीएफएल बल्ब, "
                                                                            "एक बाथरूम (गीजर के साथ), एक वॉशरूम और एक "
                                                                            "कूलर से सुसज्जित है। / एसी (जो भी कमरे "
                                                                            "के छात्रों द्वारा चुना जाता है।)", ]
	],
    [
		"हाँ, मैं लाइब्रेरी के बारे में जानना चाहूंगा?", ["वैसे 'सेंट्रल लाइब्रेरी', आपके पाठ्यक्रमों / क्षेत्रों / विभागों से संबंधित पुस्तकों में से किसी को प्राप्त करने के लिए आपका एक गंतव्य है।\nआप 1 सप्ताह की मानक अवधि के लिए एक पुस्तक ले सकते हैं और / या एक सप्ताह के बाद इसे फिर से ली जा सकती हैं।\nयह शांन्ति से रीडिंग, कोडिंग, डिजाइनिंग और उत्पादकता से संबंधित बहुत कुछ के लिए भी एक जगह हो सकती है", ]
	],
    [
		"हाँ, मैं प्रयोगशालाओं के बारे में जानना चाहूंगा?", ["शैक्षणिक ब्लॉकों में मौजूद प्रयोगशालाओं की एक विशाल विविधता है; आपके पाठ्यक्रम और विभाग के आधार पर आपके पाठ्यक्रम का संबंध है।\nप्रयोगशालाओं को विशेष रूप से विभिन्न प्रकार के प्रयोगों को करते हुए सबसे अच्छा अनुभव प्रदान करने के लिए डिज़ाइन किया गया है।\nइनमें से कुछ शनिवार के साथ-साथ कुछ अतिरिक्त समय के लिए छात्रों के लिए रविवार को भी खुले हैं।", ]
	],
    [
		"हाँ, मैं अकादमिक ब्लॉक के बारे में जानना चाहूंगा?", ["""परिसर में कुछ शैक्षणिक ब्लॉक हैं। ये चिंता विभिन्न विभागों, और निम्नानुसार हैं:
        * बिजनेस ब्लॉक - बिल्डिंग नंबर 14
        * कंप्यूटर साइंस एंड इंजीनियरिंग - बिल्डिंग नंबर 33, 34, और 37
        * मैकेनिकल इंजीनियरिंग - बिल्डिंग नंबर 56
        * सिविल इंजीनियरिंग - बिल्डिंग नंबर 57
        * इलेक्ट्रॉनिक्स और इलेक्ट्रिकल इंजीनियरिंग - बिल्डिंग नंबर 36
        * बायोइंजीनियरिंग और बायोसाइंसेस - बिल्डिंग नं 26
        * वास्तुकला और डिजाइन - बिल्डिंग नं 18
        * होटल प्रबंधन और पर्यटन - बिल्डिंग नंबर 13
        * कंप्यूटर एप्लीकेशन - बिल्डिंग नंबर 38
        * फार्मास्युटिकल साइंसेज - बिल्डिंग नंबर 26
        * कृषि - भवन संख्या 25
        * पत्रकारिता, फिल्म्स, और क्रिएटिव आर्ट्स - बिल्डिंग नंबर 11
        * केमिकल इंजीनियरिंग और भौतिक विज्ञान - बिल्डिंग नंबर 27
        * कानून - बिल्डिंग नंबर 21
        * पॉलिटेक्निक - बिल्डिंग नंबर 55
        * सामाजिक विज्ञान और विदेशी भाषाएं - बिल्डिंग नंबर 20


इन ब्लॉकों के अलावा आवासीय ब्लॉक और प्रशासनिक ब्लॉक हैं, जो इस प्रकार हैं:
        * लड़कों के छात्रावास:
            **1 - 43
            **2 - 45
            **3 - 46
            **4 - 47
            **5 - 51
            **6 - 52
        * लड़कियों के छात्रावास:
            **1 - 09
            **2 - 10
            **3 - 11
            **4 - 12
            **5 - 21
            **6 - 22


       * एडमिशन ब्लॉक - बिल्डिंग नंबर 30, 31 और 32
       * प्रशासन ब्लॉक - बिल्डिंग नंबर 28 और 29""", ]
	],

    [
		"telugu", ["హే, కాలేజీకి సంబంధించి ఏవైనా ప్రశ్నలు ఉంటే, నన్ను అడగండి!", ]
	],
    [
        "హలో", ["హలో", ]
    ],
    [
		"ఎవరు / మీరు ఏమిటి ?", ["నేను / మైసెల్ఫ్ / నా పేరు 'సీన్', నేను A.I. - ఆధారిత రోబోట్. దయచేసి మీ పేరు ఇవ్వగలరా?", ]
	],
    [
		"నేను / మైసెల్ఫ్ / నా పేరు (.*)", ["సరే %1, ఇప్పుడు మీరు ఏమి తెలుసుకోవాలనుకుంటున్నారో చెప్పగలరా?", ]
	],
    [
		"నేను కళాశాల / మౌలిక సదుపాయాల గురించి తెలుసుకోవాలనుకుంటున్నాను?", ["""'yyyyy' లో 1.8 ఎకరాల ప్రాంగణం ఉంది, దీనిలో విభిన్న భవనాలు ఉన్నాయి:
* యూనివర్శిటీ గార్డెన్స్
* yyyyy విద్యార్థి కేంద్రం
* yyyyy సెంటర్ ఫర్ రీసెర్చ్
* పాలీహౌస్ గార్డెన్స్
* yyyyy ఇన్స్ట్రుమెంటేషన్ సౌకర్యం
* యూనివర్శిటీ ఆడిటోరియం
* yyyyy ఇన్నోవేషన్ స్టూడియో
* యూనివర్సిటీ థియేటర్
* యూనివర్శిటీ ప్రొఫెషనల్ క్లబ్‌లు
* విశ్వవిద్యాలయ ఆసుపత్రులు
* యూనివర్శిటీ ఇండోర్ స్టేడియం
* విశ్వవిద్యాలయం GYM
* యూనివర్శిటీ లాంజ్
* యూనివర్శిటీ మాల్
* ఫుడ్ కియోస్క్‌లు
* స్టూడెంట్ రెసిడెన్సీలు (బాలురు / బాలికల హాస్టళ్లు మరియు అపార్టుమెంట్లు)
* yyyyy సెంట్రల్ లైబ్రరీ
* ప్రయోగశాలలు: కంప్యూటర్ (రెగ్యులర్ అలాగే MAC LAB), PHY / CHEM / BOTANY / ZOOLOGY ల్యాబ్‌లు.
* వివిధ బ్లాక్స్: అడ్మినిస్ట్రేటివ్ మరియు అకాడెమిక్ బ్లాక్స్

మీరు ప్రత్యేకంగా ఏదైనా భవనం గురించి తెలుసుకోవాలనుకుంటున్నారా?""", ]
	],
    [
		"అవును, నేను విశ్వవిద్యాలయ తోటల గురించి తెలుసుకోవాలనుకుంటున్నాను?", ["'యూనివర్శిటీ గార్డెన్స్' వివిధ రంగురంగుల పొదలతో నిండిన పచ్చని ప్రకృతి దృశ్యాన్ని కలిగి ఉంటుంది మరియు మీరు దీనిని చూస్తే మీరు చాలా ఆకట్టుకుంటారని నాకు చాలా ఖచ్చితంగా తెలుసు.", ]
	],
    [
		"అవును, నేను విద్యార్థి కేంద్రం గురించి తెలుసుకోవాలనుకుంటున్నాను?", ["నాకు తెలిసిన దాని నుండి, 'స్టూడెంట్ సెంటర్' అన్ని 'స్టూడెంట్ క్లబ్'లకు కేంద్రంగా ఉంది, అవి తప్పనిసరిగా విద్యార్థులచే నిర్వహించబడే సెమీ అటానమస్ సామాజిక సంస్థలు. మీరు 'స్టూడెంట్ క్లబ్స్' గురించి తెలుసుకోవాలనుకుంటున్నారా?", ]
	],
    [
		"అవును, నేను విద్యార్థి క్లబ్‌ల గురించి తెలుసుకోవాలనుకుంటున్నాను?", ["ఇది మీ ఉచిత / అబద్ధాల సమయంలో హ్యాంగ్అవుట్ చేయడానికి ఉత్తమమైన ప్రదేశం అని నా అభిప్రాయం, ఎందుకంటే ఇక్కడ మీరు ఫాంటసీ నుండి యాక్షన్ కళా ప్రక్రియ వరకు వివిధ ఇండోర్ ఆటలను అలాగే 'బ్యాడ్మింటన్' వంటి చేతితో పట్టుకునే ఆటల నుండి బహిరంగ ఆటలను ఆనందించవచ్చు. 'సాకర్' వంటి పాదాల ఆటలు. విభిన్న క్లబ్ యాక్టివిటీలలో పాల్గొనడం మరియు / లేదా సమన్వయం చేయడం ద్వారా ఇవన్నీ.", ]
	],
    [
		"అవును, నేను పరిశోధన కేంద్రం గురించి తెలుసుకోవాలనుకుంటున్నాను?", ["సరే, ఈ డివిజన్ యొక్క ప్రధాన ఆందోళన 'రీసెర్చ్' అని మీరు పేరుతో చెప్పగలరు. ఇప్పుడు ఇక్కడ జరిపిన పరిశోధన వివిధ 'కరికులం మార్పులు' నుండి 'ప్లేస్ మెంట్ క్రైటీరియా'లో ఏవైనా మార్పులకు ఉండవచ్చు.", ]
	],
    [
		"అవును, నేను పాలీహౌస్ తోటల గురించి తెలుసుకోవాలనుకుంటున్నాను?", ["'పాలీహౌస్ గార్డెన్స్' ఒక పెద్ద 'గ్రీన్ హౌస్' లోపల ఆశ్రయం పొందిన అందమైన మరియు సున్నితమైన 'పొదలను' చిత్రీకరిస్తుంది, దీనిలో మీరు ఒక నిర్దిష్ట 'వాతావరణాన్ని' ఆస్వాదించబోతున్నారు.", ]
	],
    [
		"అవును, నేను yyyyy ఇన్స్ట్రుమెంటేషన్ సౌకర్యం గురించి తెలుసుకోవాలనుకుంటున్నాను?", ["బాగా, 'ఇన్స్ట్రుమెంటేషన్ ఫెసిలిటీ' వివిధ సంగీత వాయిద్యాల సరఫరా మరియు మరమ్మతులతో వ్యవహరిస్తుంది; భౌతిక, రసాయన, అలాగే జీవ ఉపకరణం. కొన్ని సందర్భాల్లో, వివిధ పరిశ్రమ-స్థాయి పరికరాలపై ప్రయోగాలు చేయడానికి దీనిని 'ప్రయోగశాల సౌకర్యం'గా కూడా ఉపయోగించవచ్చు.", ]
	],
    [
		"అవును, నేను విశ్వవిద్యాలయ ఆడిటోరియం గురించి తెలుసుకోవాలనుకుంటున్నాను?", ["""సరే, 'యూనివర్శిటీ ఆడిటోరియం' అన్ని విశ్వవిద్యాలయ కార్యకలాపాలకు ఎపి-సెంటర్:
* EDM నైట్స్,
* అతిథి ఉపన్యాసాలు,
* ప్రముఖ ఇంటర్వ్యూలు,
* వివిధ నాటకాలు,
* విద్యా సెమినార్లు,
ఇలాంటివి చాలా ఉన్నాయి ఇది ఒక పెద్ద హాల్, ఒకేసారి కనీసం 500 మందిని సులభంగా కెపాసిట్ చేయగలదు. ఇది సమర్థవంతమైన ఎయిర్ కండిషనింగ్ సిస్టమ్ యొక్క మొత్తం 10 A.C. ల భాగాన్ని కలిగి ఉంటుంది మరియు 'డిగ్నిటరీస్' కోసం ప్రత్యేక సీట్లతో చుట్టుముట్టబడిన పెద్ద వేదిక.""", ]
	],
    [
		"అవును, నేను విశ్వవిద్యాలయ థియేటర్ గురించి తెలుసుకోవాలనుకుంటున్నాను?", ["మీరు నాటక రంగంలో ఉంటే, అది మీరు ట్రాక్ చేయదలిచిన ప్రదేశం. ఇది చాలా పెద్ద యియీ యొక్క నాటక కళాకారులను కలిగి ఉన్నందున, ఇది మీకు ఎల్లప్పుడూ సహాయపడుతుంది.", ]
	],
    [
		"అవును, నేను ఇన్నోవేషన్ స్టూడియో గురించి తెలుసుకోవాలనుకుంటున్నాను?", ["సరే, ఇప్పుడు ఇది మాట్లాడటానికి కొన్ని ఆసక్తికరమైన విషయం. మీరు In హించినట్లు 'ఇన్నోవేషన్ స్టూడియో'కి ఆవిష్కరణతో సంబంధం ఉంది. సరే, విద్యార్థులు మరింత సలహాలు తీసుకోవటానికి మరియు / లేదా వారి ప్రాజెక్టులను నిర్మించడానికి వారి చిగురించే ప్రాజెక్ట్ ఆలోచనలను తీసుకువచ్చారు. ఈ స్థలం యొక్క వాతావరణం ఉత్పాదక ఆలోచనకు సహాయపడుతుంది కాబట్టి, విద్యార్థులు ఈ స్థలాన్ని సందర్శించడానికి ఇష్టపడతారు.ఎవరికి తెలుసు, ఒక రోజు మీరు మీ కలల ప్రాజెక్టును కూడా నిజం చేసుకుంటారు.", ]
	],
    [
		"అవును, నేను ప్రొఫెషనల్ క్లబ్‌ల గురించి తెలుసుకోవాలనుకుంటున్నాను?", ["సరే, మీరు విశ్వవిద్యాలయం యొక్క 'క్యాంపస్ ప్లేస్‌మెంట్స్' (లేదా, 'ఆన్-సైట్ ప్లేస్‌మెంట్స్') కోసం కూర్చుంటే, మీ నైపుణ్యం-సమితిని విస్తరించడానికి 'ప్రొఫెషనల్ క్లబ్‌లు' మీకు సహాయపడతాయి. ఈ ప్రక్రియలో, మచ్చలేని ఆంగ్ల భాషతో పాటు అనేక ఇతర పోటీ పనులు మరియు ఇంటర్వ్యూలు, ఇంటర్వ్యూలు వంటి నైపుణ్యాలకు సంబంధించి మీ నైపుణ్యం కోసం మీరు పరీక్షించబడతారు.", ]
	],
    [
		" అవును, నేను విశ్వవిద్యాలయ ఆసుపత్రుల గురించి తెలుసుకోవాలనుకుంటున్నాను?", ["మీరు సెటైన్ జ్వరం అంటే కాలానుగుణమైన పరిస్థితిని పరిశీలిద్దాం, మీరు దగ్గుతో పాటు దహనం చేస్తున్నారు! మీరు ఏమి చేస్తారు ? మీరు 'యూనివర్శిటీ హాస్పిటల్స్' ను సందర్శించినప్పుడు ఇది మీకు సరైన చికిత్స మరియు మందులు ఇవ్వబడుతుంది. శారీరక సమస్య విషయంలో, మీరు ఎల్లప్పుడూ ఆసుపత్రిని సందర్శించాలి, ఎందుకంటే నివారణ కంటే మంచిది."]
	],
    [
		"అవును, నేను ఇండోర్ స్టేడియం గురించి తెలుసుకోవాలనుకుంటున్నాను?", ["బాగా, ఇది స్పష్టంగా లేదు, మీరు ఆడాలనుకునే ఏదైనా బహిరంగ ఆట ఆడగల ప్రదేశం ఇది. దీనికి పేరు పెట్టండి మరియు అబ్బాయిలు మీకు ఆడటానికి సంబంధిత స్థలాన్ని (లేదా, కోర్టు) అందిస్తారు. ఇది ఫుట్‌బాల్, బాస్కెట్‌బాల్, రగ్బీ, హాకీ, టెన్నిస్ (టేబుల్ మరియు లాన్ రెండూ), మరియు మొదలైనవి కావచ్చు; మీరు దీన్ని ప్లే చేయాలనుకుంటే, ఇక్కడ మీరు చేయవచ్చు.", ]
	],
    [
		"అవును, నేను జిమ్ గురించి తెలుసుకోవాలనుకుంటున్నాను?", ["వూఫ్, చాలా చెమటతో ఉన్న ప్రజలు, నేను దాని శబ్దాన్ని నిలబడలేను. కానీ మీరు సంపూర్ణ శరీరాన్ని కలిగి ఉండటానికి లేదా రోజువారీ వ్యాయామ నిబద్ధతతో ఆసక్తి కలిగి ఉండవచ్చు. కారణం ఏమైనప్పటికీ మీరు యూనివర్శిటీ జిమ్స్‌లో చేరవచ్చు (అక్కడ మొత్తం 4). ఈ స్థలాన్ని సందర్శించడానికి ముందు మీరు చెమట పట్టడానికి సిద్ధంగా ఉండండి. నొప్పి లేదు, లాభం లేదు అని వారు చెప్పినట్లే.", ]
	],
    [
		"అవును, నేను విశ్వవిద్యాలయ లాంజ్ గురించి తెలుసుకోవాలనుకుంటున్నాను?", ["సరే, కాబట్టి ఇది శుక్రవారం రాత్రి, మొదట ఏమి చేయాలో మీరు ఆలోచిస్తూ ఉండవచ్చు. వారాంతం ప్రారంభమైనప్పుడు మీ సమయాన్ని ఆస్వాదించడానికి విశ్వవిద్యాలయ లాంజ్ బహుశా ఉత్తమమైన ప్రదేశం.", ]
	],
    [
		"అవును, నేను యూనివర్శిటీ మాల్ గురించి తెలుసుకోవాలనుకుంటున్నాను?", ["ఓహ్, మాల్ శుక్రవారం సాయంత్రం హ్యాంగ్అవుట్ చేయడానికి కూడా అనువైన ప్రదేశం. లైటింగ్, స్థలం మరియు మొత్తం ప్రకాశం కారణంగా ఇది సాయంత్రం మీరు సందర్శించాలనుకునే ప్రదేశం.", ]
	],
    [
		"అవును, నేను ఆహార కియోస్క్‌ల గురించి తెలుసుకోవాలనుకుంటున్నాను?", ["సరే, ఇది విశ్వవిద్యాలయ ప్రాంగణంలో ఉన్నప్పుడు మీరు ఎక్కువగా సందర్శించే 'ఫుడ్ కియోస్క్స్', ఇక్కడ నుండి మీరు హాస్టల్ మెస్ సభ్యులతో పాటు మీ రోజువారీ భోజనాన్ని (అనగా, అల్పాహారం, భోజనం మరియు విందు) పొందవచ్చు.మార్గం ద్వారా, మీరు హాస్టల్ గజిబిజి గురించి తెలుసుకోవాలనుకుంటున్నారా?", ]
	],
    [
		"అవును, నేను విద్యార్థి నివాసాలు / హాస్టళ్ల గురించి తెలుసుకోవాలనుకుంటున్నాను?", [" 'స్టూడెంట్ రెసిడెన్సీలు' లేదా వాటిని సాధారణంగా 'హాస్టల్స్' అని పిలుస్తారు, ఇవి విశ్వవిద్యాలయ విద్యార్థులు నివసించే భవనాలు. ఇక్కడి విద్యార్థులు అనేక రకాల గదులను ఎంచుకోవచ్చు (ఒక సీటర్, రెండు సీట్లు, మూడు సీట్లు, నాలుగు సీట్లు). అదనపు లాండరీ మరియు మెస్ సౌకర్యాలతో పాటు, మినీ డిపార్ట్‌మెంటల్ స్టోర్, క్లోక్ రూమ్ మరియు స్టడీ రూమ్ ఉన్నాయి. అందించిన ఏదైనా హాస్టల్ సదుపాయాలకు సంబంధించి ఏదైనా దుష్ప్రవర్తన మరియు / లేదా ఏదైనా ముఖ్యమైన సమస్యకు సంబంధించి, విద్యార్థి వార్డెన్ కార్యాలయాన్ని కూడా సంప్రదించవచ్చు, ఇది హాస్టళ్ల క్రమశిక్షణను నిర్వహించడానికి ఉపయోగించబడుతుంది. ప్రతి గదిలో అవసరమైన మొత్తంలో కుర్చీలు, పడకలు మరియు స్టడీ టేబుల్స్ (గదిలోని విద్యార్థుల సంఖ్యపై ఆధారపడి ఉంటుంది), ట్యూబ్‌లైట్, సిఎఫ్ఎల్ బల్బ్, బాత్రూమ్ (గీజర్‌తో), వాష్‌రూమ్ మరియు కూలర్ ఉన్నాయి. / ఎసి (గది విద్యార్థులు ఏది ఎంచుకుంటారు.)", ]
	],
    [
		"అవును, నేను లైబ్రరీ గురించి తెలుసుకోవాలనుకుంటున్నాను?", [" 'సెంట్రల్ లైబ్రరీ', మీ కోర్సులు / ఫీల్డ్‌లు / విభాగాలకు సంబంధించిన పుస్తకాలలో దేనినైనా పొందే గమ్యం. మీరు 1 వారానికి ప్రామాణిక కాలానికి పుస్తకాన్ని జారీ చేయవచ్చు మరియు / లేదా వారం తరువాత తిరిగి విడుదల చేయవచ్చు. ఇది కలవరపడని పఠనం, కోడింగ్, డిజైనింగ్ మరియు ఉత్పాదకతకు సంబంధించిన ఏదైనా చాలా చక్కని ప్రదేశం.", ]
	],
    [
		"అవును, నేను ప్రయోగశాలల గురించి తెలుసుకోవాలనుకుంటున్నాను?", ["అకాడెమిక్ బ్లాకులలో అనేక రకాల ప్రయోగశాలలు ఉన్నాయి; మీ కోర్సు మరియు మీ కోర్సుకు సంబంధించిన విభాగాన్ని బట్టి. వివిధ రకాల ప్రయోగాలు చేస్తున్నప్పుడు ఉత్తమ అనుభవాన్ని అందించడానికి ప్రయోగశాలలు ప్రత్యేకంగా రూపొందించబడ్డాయి. వీటిలో కొన్ని శనివారాలు మరియు ఆదివారాలు విద్యార్థులు అదనపు సమయం కోసం ప్రాక్టీస్ చేయడానికి తెరిచి ఉంటాయి.", ]
	],
    [
		"అవును, నేను అకాడెమిక్ బ్లాకుల గురించి తెలుసుకోవాలనుకుంటున్నాను?", ["""క్యాంపస్‌లో కొన్ని అకాడెమిక్ బ్లాక్‌లు ఉన్నాయి. ఇవి వేర్వేరు విభాగాలకు సంబంధించినవి మరియు ఈ క్రింది విధంగా ఉన్నాయి:
        * బిజినెస్ బ్లాక్ - బిల్డింగ్ నెంబర్ 14.
        * కంప్యూటర్ సైన్స్ అండ్ ఇంజనీరింగ్ - బిల్డింగ్ నెంబర్ 33, 34, మరియు 37.
        * మెకానికల్ ఇంజనీరింగ్ - భవనం సంఖ్య 55.
        * సివిల్ ఇంజనీరింగ్ - భవనం సంఖ్య 57
        * ఎలక్ట్రానిక్స్ మరియు ఎలక్ట్రికల్ ఇంజనీరింగ్ - భవనం సంఖ్య 36
        * బయో ఇంజనీరింగ్ మరియు బయోసైన్సెస్ - బిల్డింగ్ నం. 26
        * ఆర్కిటెక్చర్ అండ్ డిజైన్ - బిల్డింగ్ నం. 18
        * హోటల్ మేనేజ్‌మెంట్ అండ్ టూరిజం - బిల్డింగ్ నెంబర్ 13
        * కంప్యూటర్ అప్లికేషన్ - బిల్డింగ్ నెంబర్ 38
        * ప్రవేశాలు - NO.30 కొనుగోలు
        * ఫార్మాస్యూటికల్ సైన్సెస్ - బిల్డింగ్ నెంబర్ 26
        * వ్యవసాయం - భవనం సంఖ్య 25
        * జర్నలిజం, ఫిల్మ్స్ మరియు క్రియేటివ్ ఆర్ట్స్ - బిల్డింగ్ నెంబర్ 19
        * కెమికల్ ఇంజనీరింగ్ మరియు ఫిజికల్ సైన్సెస్ - బిల్డింగ్ నెంబర్ 27
        * చట్టం - భవనం సంఖ్య 21
        * ప్లేస్‌మెంట్ సెల్ - బిల్డింగ్ నెం .22
        * పాలిటెక్నిక్ - భవనం సంఖ్య 55
        * సాంఘిక శాస్త్రాలు మరియు విదేశీ భాషలు - భవనం సంఖ్య 20

    ఈ బ్లాకులను ఏర్పరచడమే కాకుండా, రెసిడెన్షియల్ బ్లాక్స్ మరియు అడ్మినిస్ట్రేటివ్ బ్లాక్స్ ఉన్నాయి, అవి ఈ క్రింది విధంగా ఉన్నాయి:
        * బాలుర హాస్టళ్లు:
            ** 1 - 43
            ** 2 - 45
            ** 3 - 46
            ** 4 - 47
            ** 5 - 51
            ** 6 - 52
        * బాలికల హాస్టళ్లు:
            ** 1 - 09
            ** 2 - 10
            ** 3 - 11
            ** 4 - 12
            ** 5 - 21
            ** 6 - 22

       * అడ్మిషన్ బ్లాక్ - బిల్డింగ్ నెంబర్ 30, 31, మరియు 32.
       * అడ్మినిస్ట్రేషన్ బ్లాక్ - బిల్డింగ్ నెంబర్ 28, మరియు 29.""", ]
	],
    [
		"User", ["Prog", ]
	],
    [
		"User", ["Prog", ]
	],
]


def chatbot_functionality():
    print("Hey there, have any queries regarding the college, Ask Me !\nPlease write each sentence in lower-case alphabets.\nType 'quit' to leave.\nAnd type 'hindi' or 'telugu' to converse in the concerned language.")
    interact = Chat(pairs, reflections)
    interact.converse()


chatbot_functionality()
