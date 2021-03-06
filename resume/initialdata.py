import django
from django.conf import settings
settings.configure()
django.setup()
django.configure()

from models import *
from datetime import date

Quotations = [
    ["""C.V. Wedgwood""", """English historian, author of "The Thirty Years War,"
     one of the best-written histories I have ever read""", """An educated man
     should know everything about something and something about everything."""],
    ["""Benjamin Franklin""", """A Founding Father of the United States""",
     """An investment in knowledge pays the best interest"""],
    ["""Albert Einstein""", """Father of Modern Physics""", """It is not so
     very important for a person to learn facts. For that he does not really
     need a college. He can learn them from books. The value of an education in
     a liberal arts college is not the learning of many facts but the training
     of the mind to think something that cannot be learned from textbooks."""],
    ["""Seneca the Younger""", """Roman Stoic Philosopher""", """[People who
     take time for philosophy] alone really live; for they are not content to
     be good guardians of their own lifetime only. They annex every age to
     their own; all the years that have gone before them are an addition to their
     store. Unless we are most ungrateful, all those men, glorious fashioners
     of holy thoughts, were born for us; for us they have prepared a way of
     life. By other men's labours we are led to the sight of things most
     beautiful that have been wrested from darkness and brought into light;
     from no age are we shut out, we have access to all ages, and if it is
     our wish, by greatness of mind, to pass beyond the narrow limits of
     human weakness, there is a great stretch of time through which we
     may roam."""],
    ["""Henry David Thoreau""", """Trancsendentalist thinker and author""",
     """Men sometimes speak as if the study of the classics would at length
     make way for more modern and practical studies; but the adventurous
     student will always study classics, in whatever language they may be
     written and however ancient they may be. For what are the classics
     but the noblest recorded thoughts of man? They are the only oracles
     which are not decayed, and there are such answers to the most modern
     inquiry in them as Delphi and Dodona never gave. We might as well omit
     to study Nature because she is old."""],
    ["""Leonardo da Vinci""", """Italian Renaissance polymath""",
     """Iron rusts from disuse; stagnant water loses its purity
      and in cold weather becomes frozen; even so does inaction sap
      the vigor of the mind."""],
    ["""Francis Bacon""", """English philsopher, scientist, and author""",
     """There is no comparison between that which is lost by not succeeding and
     that which is lost by not trying."""],
    ["""Allen Ginsberg""", """American poet""", """My interest in reading is
     the profit by other men's experiences. I sometimes find (only lately)
     authors talking directly to me, from the bottom of their minds."""],
    ["""Niels Bohr""", """A father of quantum mechanics""",
     """We must be clear that when it comes to atoms, language can be used
     only as in poetry. The poet, too, is not nearly so concerned with describing
     facts as with creating images and establishing mental connections."""],
    ["""John Dewey""", """American educational reformer""", """A possibility of
     continuing progress is opened up by the fact that in learning one act,
     methods are developed good for use in other situations. Still more
     important is the fact that the human being acquires a habit of learning.
     He learns to learn."""],
    ["""Ruth Bader Ginsburg""", """U.S. Supreme Court Justice""", """I’m a very
     strong believer in listening and learning from others"""],
    ["""Maria Montessori""", """Italian educator and philosopher of education""",
     """Education is a work of self-organization by which man adapts himself to
     the conditions of life."""],
    ["""Neil deGrasse Tyson""", """American Astrophysicist""", """It's the
     inspired student that continues to learn on their own. That's what
     separates the real achievers in the world from those who pedal along,
     finishing assignments."""],
    ["""Ada Lovelace""", """English mathematician and writer, the first
     programmer""", """I am more determined than ever in my future plans; and I
     have quite made up my mind that nothing must be suffered to interfere with
     them. I intend to make such arrangements in town as will secure me a couple
     hours daily (with very few exceptions) for my studies."""],
]

for quotation in Quotations:
    temp = Quotation(quotation[0], quotation[1], quotation[2])
    temp.save()


Semesters = [
    ["Spring 2012", 3.95, True],
    ["Fall 2011", 4.0, True],
    ["Spring 2011", 4.0, True],
    ["Fall 2010", 4.0, True],
    ["Spring 2010", 3.93, True],
    ["Fall 2009", 3.92, True],
    ["Spring 2009", 3.67, True],
    ["Fall 2008", 3.12, False]
]

Courses = [
    ["Spring 2012", "ARTH3014W - Art of India", "A", """This class covered the
     history of art in India from its distant past to the present. Like the other
     art history class I took, it was quite challenging. The test format was almost
     the same: we were randomly shown a number of slides from a very large pool,
     and we had to try to identify the date, the location, the artist (if known),
     and how the piece fit into the larger context of the history of art in that
     location. I particularly enjoyed looking at Indian temple architecture, and
     the course hammered home the relationship between art history and
     political/religious history in India."""],
    ["Spring 2012", "CNES 3107 - Age of Constantine the Great", "A-", """This
     was one of my favorite classes at the University of Minnesota. The
     professor who taught it was an elderly British gentleman who studied at
     Oxford in his youth. He had bushy eyebrows, an encyclopedic knowledge of
     Late Antiquity and the Middle Ages, and a sense of humor reminiscent of
     Monty Python. And of course, having spent most of my college career at
     this point studying the Classical Greece and Rome, I really enjoyed
     looking at the transition into the Middle Ages."""],
    ["Spring 2012", "CNES 3951W - Senior Thesis", "A", """I wrote my senior
     thesis under the tutelage of the head of the Classical Civilizations
     department. He was a Rhodes Scholar, a University of Chicago alumnus,
     and a stickler for old school grammar and style. I wrote about Lucian of
     Samosata, a second-century Syrian satirist who wrote his satires in the
     Attic Greek spoken some six hundred years before his birth. He was both
     an exemplar of and an outlier from the retrospective Greek cultural
     phenomenon known as the "Second Sophistic." Although Lucian is no longer
     a household name, he had a pronounced effect on the development of
     European satire, influencing authors such as Erasmus, Fielding,
     and Swift. But what really drew me to study him was the modernity of his
     humor. I laugh when I read his work, even though much of its genius is
     lost to the modern reader, as it depends in part on parodies in language
     and style that are lost in translation or mimics works that are no longer
     extant or commonly read."""],
    ["Spring 2012", "GRK 3004 - Intermediate Greek Poetry: The Iliad of Homer",
     "A", """Reading Homer in the original was a great experience. I Learned
     about the meter of Greek poetry and discussed the Iliad in depth in an
     academic context. There is a reason that Homer is perhaps the most revered
     poet of the Western tradition. Aside from my sheer delight in his
     storytelling, I felt as if I was connecting to an even more distant past,
     knowing that the versions of the Iliad and Odyssey which became canonical
     were part of a larger group of epic tales (the "Epic Cycle") that had been
     performed orally for many hundreds of years before they were written
     down."""],
    ["Spring 2012", "HIST 3600", "A", """An interdisciplinary examination of
     the Renaissance taught by a team of three professors from the Art History,
     History, and Italian and French Literature departments, respectively,
     lecturing in tandem. This was a fitting end to my course of study, since
     my senior thesis involved tracing the reemergence of a classical author's
     works in the Renaissance. But more than that, examining how the
     rediscovery of the Classical world changed the course of the development
     of Western Civilization was a validation of the importance of everything I
     had studied. And of course the reintegration of Classical motifs and ideas
     produced a complex cultural landscape that one could spend a whole
     lifetime reading and writing about without even scratching the surface.
     The art--awe-inspiring. The thinkers--demigods. The politics--chaos."""],
    ["Fall 2011", "ANTH 3001 - Introduction to Archeology", "A", """This course
     was an excellent overview of how history of pre-literate societies is
     investigated (and how the techniques involved can also be used to augment
     the written history of literate societies). Archeology draws on a wide
     variety of other fields of knowledge to achieve its ends. We studied soil
     composition and skeletal structure. We learned about dating techniques
     such as radiocarbon dating, Potassium-Argon dating, and thermoluminescence.
     The class also introduced us to the debate among archaeologists about what
     constitutes a valid interpretative framework for looking at the history of
     civilizations that only left material remains to posterity."""],
    ["Fall 2011", "CNES 3535 - Death and the Afterlife in the Ancient World",
     "A", """This course focused on the traditions and beliefs surrounding
     death and the afterlife within a number of ancient religious and cultural
     communities, including Zoroastrians, ancient Egyptians, Mesopotamian
     polytheists, Greek and Roman polytheists, Jews, and Christians. The
     professor was an expert in multiple ancient languages and was incredibly
     knowledgeable about the history of Judaism and Christianity. One of the
     things we looked at was the progressive development of ideas about heaven,
     hell, and Satan, which historians believe have their origins in
     Zoroastrian dualism."""],
    ["Fall 2011", "CSCL 3173W - The Rhetoric of Everyday Life", "A", """The
     title of this course was somewhat misleading, although my attempts to
     produce an alternate title have produced rather unsatisfactory results: I
     might call it "Ideas about the changing perceptions of time and day-to-day
     life in the industrial and post-industrial world." We read some Marx and
     Foucault, which I found rewarding. But much of the material we were
     assigned I found to be worthless, because it was written in an almost
     incomprehensible style and was completely unsupported by evidence."""],
    ["Fall 2011", "GRK 1002 - Intermediate Greek Prose: Xenophon's Anabasis",
     "A", """Having completed the prerequisite two semesters of Greek grammar,
     I began to read (with substantial effort) an unadapted text, Xenophon's
     Anabasis, which is the story of a group of Greek mercenaries who march
     into Persia to aid an upstart brother of the Persian king in a coup.
     Although it is a historical account written by a participant in the
     expedition, it is not a book often read for its historical content. That
     being said, it is an entertaining story written in a somewhat approachable
     Greek. It made a good first foray into Greek literature, although in
     retrospect I might have preferred to read something by the satirist Lucian
     of Samosata (who is another common choice for a first unadapted text)."""],
    ["Fall 2011", "LING 3001 - Introduction to Linguistics", "A", """In this
     class I was introduced to all the major aspects of the systematic study of
     language. Having never studied linguistics, I found it a useful complement
     to my study of foreign languages and English. Knowing more about syntactical
     structure and phonetics has aided me in my language study and tutoring."""],
    ["Spring 2011", "CNES 3106 - Rome in the Age of Nero", "A", """This was one
     of the least satisfying classes I had in the Classical Civilizations
     program. The professor seemed little interested in the topic at hand. His
     lack of enthusiasm was mirrored by the majority of the students, but he
     nonetheless insisted on class discussions. Session after session, we would
     sit there in dead silence, or else the professor and a few faithful
     (myself included) would have a small discussion surrounded by a large but
     silent crowd. In principle, I am all for class discussion, but I think
     that, given the general reticence, everyone would have benefited more if
     the professor had chosen to lecture us on demography or city planning or
     something else that wasn't covered in the readings. Nonetheless, the
     readings provided an interesting look into one of the more controversial
     and strange periods of Roman history."""],
    ["Spring 2011", "CNES 5601 - Sexuality and Gender in Ancient Greece and Rome",
     "A", """This was the only graduate level course I took at the University
     of Minnesota. There were three other students in the graduate section,
     and we would meet with the professor for small discussions every week.
     Each week we rotated who would lead the discussion. And of course the
     subject matter was fascinating. Greek and Roman sexual and gender ideology
     differed radically from our modern sensibilities. At the same time, the
     ideas Plato expressed in his Symposium were incorporated into later
     Christian (and hence European) sexual ideology."""],
    ["Spring 2011", "GRK 1002 - Beginning Classical Greek II", "A", """For the
     second semester of Attic Greek, we continued to use Groton's From Alpha to
     Omega, getting into the complexities of participles, the subjunctive and
     optative moods, conditionals, indirect discourse, and other such
     constructions. One nice thing about studying Ancient Greek is that
     because there is no burden of having to learn to fluidly manipulate the
     language in speech, by the end of the second semester you learn almost
     all the basic grammatical constructions. This means that when you start
     your third semester, you are prepared to read an unadapted text in
     Greek."""],
    ["Spring 2011", "RUSS 3102 - Advanced Russian II", "A", """Unfortunately,
     the University of Minnesota's Russian program only offered six semesters.
     But by the end of this last one, I was well equipped to continue my
     studies on my own. I had a knowledge of most of the essential grammar, and
     with the help of a dictionary, I was able to read whatever I might
     encounter."""],
    ["Fall 2010", "CNES 1002 - Wolrd of Greece", "A", """This course focused
     more on the ideologies underpinning Greek society than on the
     chronological succession of political events and wars. One thing that I
     found fascinating was the extent to which Homer's works, although they are
     obviously mythological, do contain accurate historical information about
     the bronze age society they describe. Their partial historicity derives
     from their origins in oral traditions which date back to the bronze age.
     Archaeological evidence corresponds with some of Homer's descriptions
     (for instance, his description of palace architecture). There are also
     many anachronistic interpolations, of course."""],
    ["Fall 2010", "CNES 3008 - History of Ancient Art", "A", """This was
     possibly the hardest class I took at the University of Minnesota.
     It covered the art of the Ancient world in general, including Mesopotamia,
     Egypt, Africa, Greece, Western Europe, and Rome. The exams consisted of
     six or seven slides selected from a pool of about two hundred which we
     were to have studied. The professor put them up on his projector for about
     7 minutes each. In that time we had to identify the place of origin,
     the approximate date, the artist (if one was known), and how the piece
     fit into the larger trend of art history in that place at that time. The
     second of the two tests was cumulative. We also had to write a
     non-research-based five page paper about a piece of art in the Minneapolis
     Institute of Arts, discussing how if fit into the period and place to
     which it belonged without referring to the provided descriptions in the
     museum (which the professor warned us were often inaccurate)."""],
    ["Fall 2010", "GRK 1001 - Beginning Classical Greek I", "A", """For the
     first semester of Ancient Greek we used the textbook From Alpha to Omega,
     which is an excellent and thorough resource. I enjoyed learning the
     language and studied assiduously. Having already studied Russian
     (a language with a lot of irregularity that retains the nearly complete
     Indo-European case system), Greek grammar seemed refreshingly logical
     and manageable. I even acted occasionally as an informal tutor for some
     of my fellow students."""],
    ["Fall 2010", "RUSS 3101 - Advanced Russian I", "A", """During my 5th
     semester of Russian, we used a new textbook, V Puti, which I did not like
     very much. I felt that a fully fledged grammar reference (such as Derek
     Offord's Modern Russian) would have been more appropriate. Fortunately my
     teacher continued to provide us with copious supplementary material,
     such as films and stories."""],
    ["Spring 2010", "ENGL 3221 - The American Novel to 1900", "A", """In this
     course we read some classic American literature including Melville's
     Moby-Dick and Hawthorne's The House of the Seven Gables. We also read a
     number of lesser known books that dated to an earlier epoch of American
     history. Of the latter, the one that most stands out in my memory is
     Charles Brockden Brown's Wieland, a thoroughly spooky and surprisingly
     modern horror/thriller story that was first published in 1798."""],
    ["Spring 2010", "HIST 3736 - The History of Eastern Orthodoxy", "A-",
     """This class offered a glimpse into the complex religious and political
     history of Eastern Europe. The professor was an elderly Greek man with a
     real passion for the subject. He was a tough grader and expected a lot
     from his students. One book I found particularly interesting was The
     Western Front of the Eastern Church by Barbara Skinner. The book dealt
     with the complex struggle for supremacy in Eastern Europe between Eastern
     Orthodox Christianity and Catholicism, and how confessional divides became
     intricately intertwined with politics and national identity. It is a
     bewilderingly complex cultural landscape."""],
    ["Spring 2010", "RUSS 3002 - Intermediate Russian II", "A", """During my
     fourth semester of Russian, I was finally introduced to the last of the
     cases of the Russian noun, which meant I had the complete basic toolkit to
     understand written Russian. We spent a fair amount of the semester reading
     short stories by a number of Russian authors, including Leo Tolstoy."""],
    ["Spring 2010", "RUSS 3404 - Tolstoy in Translation", "A", """This class
     had the heaviest reading load of any I took in college. In the course of
     one semester we read War and Peace, Anna Karenina, and a number of
     Tolstoy's short stories, such as The Death of Ivan Ilych.
     The professor was incredibly knowledgeable about all things Tolstoy.
     He could cite which volume of Tolstoy's collected works any given piece
     was in, and there are more than twenty large tomes of his collected
     writings. Tolstoy was incredibly prolific. He wrote more than 5,000 pages
     by hand before reducing War and Peace to the final product, which
     consisted of about 1400 printed pages in its first edition. War and Peace
     remains one of my favorite novels, and is my favorite work of historical
     fiction. I am currently working my way through it in the original."""],
    ["Fall 2009", "BIOL 1001 - Evolution and Ecology", "A", """Frankly, I took
     this class because it fulfilled one of the few remaining College of
     Liberal Arts graduation requirements that my AP test scores from high
     school had not covered. That is not to say, however, that I find biology
     boring. On the contrary, I find it fascinating, especially in its
     connection to physics (e.g. electrophysiology, which is what my father
     studies). In retrospect, I wish I had signed up for a harder biology
     course to meet the requirement."""],
    ["Fall 2009", "ENGL 3007 - Shakespeare", "A", """I had read some
     Shakespeare in my High School English classes, but it was enjoyable to
     explore his work in greater depth and discuss it in a more serious
     academic context. I still consider Shakespeare to be the greatest
     wordsmith of the English language, and I have consistently found his
     words worthy of commitment to memory. "And by a sleep to say we end the
     heart-ache and the thousand natural shocks that flesh is heir to, 'tis a
     consummation devoutly to be wish'd." No one else can write like that."""],
    ["Fall 2009", "HUM 1001 - Humanities in the West I: Greece and Rome", "A-",
     """This course fully exposed me for the first time to the wonders of the
     so-called "Classical Civilizations," and in a way it was thus responsible
     for my choice of major. It was rather broad in scope, focusing on the
     culture (especially the literary culture) of both Greece and Rome. Here,
     for the first time, I read the Aeneid and began to see the tendrils of
     Homer coming down through the ages to our modern day; here I first read
     the Meditations of the Stoic philosopher-emperor Marcus Aurelius."""],
    ["Fall 2009", "RUSS 3001 - Intermediate Russian I", "A", """For my third
     semester of Russian I had a new teacher who used a slightly different
     approach. While she did use the second book of the Nachalo series, she
     supplemented it with many handouts and other readings (such as short
     stories with vocabulary help). She also incorporated her own anecdotes
     from years as an interpreter for the Hungarian delegation to the Soviet
     Union. She was an excellent teacher."""],
    ["Spring 2009", "ARTS 1101 - Drawing", "B+", """This class met once a week
      for 4 hours. Apart from the occasional critique, we would spend almost
      the entire class drawing with only a small break in the middle. The
      professor assigned several hours of homework each week. Drawing could be
      quite draining sometimes, but it was also very rewarding, and it did
      foster a new appreciation for visual aesthetics and perception."""],
    ["Spring 2009", "AST 1001 - Introduction to Astronomy", "A", """This was
     one of my favorite classes in college. The course covered what we
     understand of the development of the Universe since the big bang. What I
     learned had a profound influence on my personal philosophy of life. The
     thought that we are intimately tied with the physical nature of this
     universe still fills me with awe. Cosmology remains one of my favorite
     subjects, and I still have my notebook from this class, which I
     occasionally review."""],
    ["Spring 2009", "ENGW 1101W - Introduction to Creative Writing", "A-",
     """The lectures for this class were given in a large hall by guest
     lecturers, who were usually visiting authors. But what really made the
     class for me was my TA, who was a bright young poet and singer-songwriter.
     He did a good job motivating us and giving us a little of his passion for
     the art of literary creation."""],
    ["Spring 2009", "RUSS 1102 - Beginning Russian II", "A-", """At this early
     stage in my study of Russian, I still had little concept of what I had
     gotten into, but I was enjoying it. The textbook we were using,
     Nachalo provided little insights into Russian culture: there was a
     section on New Years celebrations (New Years is the Russian Christmas); a
     section on how to decline alcohol; a cast of characters that included a
     local "businessman" with questionable intentions. The book was fine, but
     in retrospect I find it frustrating that we were not introduced to the
     instrumental case until the end of the 4th semester, another year down
     the line. This meant that I was unable to say things like, "I cut the
     bread with the knife" or "I went to the movies with my friend" for quite
     some time."""],
    ["Fall 2008", "AST 1905 - Cosmic Catastrophes", "B+", """This course
     focused on how cosmic phenomena can and do effect life on earth. We
     discussed the possible cosmic origins of life, the impact of the meteor
     which caused the Cretaceous-Paleogene extinction, and the future of life
     on earth. I found one of the books we read, The Life and Death of Planet
     Earth by Ward and Brownlee, particularly interesting. Among other things,
     the authors suggest that, despite the proliferation of greenhouse gases by
     humans, ultimately the earth's atmosphere will lose its carbon dioxide to
     outer space. If this is true, there will theoretically come a time when
     plants will no longer have enough carbon dioxide to produce oxygen, which
     will spell the end of (oxygen-based) life on Earth."""],
    ["Fall 2008", "CSCI 1901 - Computer Programming I", "Withdrawn", """When I
     started college, I intended to study computer science. This was the first
     course in the Computer Science program at the University of Minnesota. The
     class introduced many of the basic concepts of computer programming,
     including recursion, algorithmic problem solving, the structure of
     computer programs, and how computer programs fit into the larger scheme of
     a computer's organizational hierarchy. We were learning Scheme, which is a
     fine starting language, but about half way through the semester, I decided
     that I did not want to study computer science for my undergraduate
     education. I made up my mind that I wanted to study the humanities, and
     so, in a somewhat immature fit of impetuosity, I dropped the course."""],
    ["Fall 2008", "Math 2243 - Linear Algebra and Differential Equations", "C+",
     """This was my third semester of calculus, as I had taken AP Calculus BC in
     high school. It is regrettable that I did not take it more seriously. When
     I dropped computer science, I wanted to withdraw from this class as well.
     Since my new plan was was to study literature, and I felt there was
     therefore no further reason for me to study math. Of course I can laugh at
     my shortsightedness and immaturity in retrospect, but I do I wish that I
     had paid more attention and worked harder in this class. I fully plan on
     reviewing the subject matter in due time."""],
    ["Fall 2008", "RUSS 1101 - Beginning Russian I", "A-", """I took this class
     because I had read some Dostoevsky and Tolstoy in my spare time in high
     school, and I had thoroughly enjoyed both. As I began to study the
     language, I fell in love with its strangeness, its near-perversity. I had
     yet to realize the importance of stress or the complexity of the Russian
     verb-system (don't get me started on verbs of motion). But the passion
     born then still burns inside me now."""]
]

for sem in Semesters:
    temp = Semester(sem[0], sem[1], sem[2])
    temp.save()
    for course in Courses:
        if course[0] == sem[0]:
            temp2 = Course(temp, course[1], course[2], course[3])
            temp2.save()

AcademicAwards = [
    ["AP Scholar with Distinction", """In high school I took six AP classes,
     scoring a four or higher on every exam I took. Below you see my AP
     Transcript. My scores qualified me for the "AP Scholar with Distinction"
     designation, which is awarded to anyone who scores a 3 or higher on five
     exams and averages a 3.5 or higher on all exams taken."""],
    ["Greek Student of the Year 2010 -2011", """In recognition of my devotion
     to the study of Attic Greek, the Classical and Near Eastern Studies
     Department at the University of Minnesota awarded me the designation
     "Greek Student of the Year" for the fall and spring semesters of my junior
     year of college. There was a small ceremony held in the department's
     fireplace room, and I was presented with this certificate as well as a
     recently published scholarly book about the archeology of Athens.""",
     "greeksoy.jpg"],
    ["University of Minnesota Dean's List Seven Consecutive Semesters, Graduation with Disction",
     """During my undergraduate education, I made the Dean's List every
     semester except my first. When I graduated, I did so "with distinction"
     in acknowledgment of the fact that I had a cumulative GPA higher than
     3.75. As a token of this accomplishment, I was allowed to wear a gold
     neck tassel for my graduation ceremony. Here is a picture of my parents
     and I on the day of my graduation.""", "graduationday.jpg"]
]

for award in AcademicAwards:
    if len(award) > 2:
        temp = AcademicAward(award[0], award[1], award[2])
    else:
        temp = AcademicAward(award[0], award[1])
    temp.save()

APCourses = [
    ["English Literature and Composition", "4"],
    ["European History", "4"],
    ["Calculus BC", "5 (AB)/5 (BC)"],
    ["US History", "4"],
    ["English Language and Composition", "4"],
    ["Psychology", "5"]
]

for course in APCourses:
    temp = APCourse(course[0], course[1])
    temp.save()

Languages = [
    ["English", "Native", True],
    ["Russian", "High Intermediate", True],
    ["Spanish", "Intermediate", True],
    ["German", "Intermediate", True],
    ["Attic Greek", False],
    ["Latin", False],
    ["Turkish", False],
    ["Japanese", False]
]

LanguageDetails = [
    ["English", "Extensive vocabulary and firm grasp of English grammar"],
    ["English", "Excellent written and verbal communication abilities"],
    ["Russian", "Six semesters of study in college"],
    ["Russian", "Ability to hold steady and wide-ranging conversations"],
    ["Russian", "Ability to read Russian literature and news"],
    ["Spanish", "Began studying in March of 2013 using Duolingo"],
    ["Spanish", "Ability to read Spanish language literature and news"],
    ["German", "Began studying in spring of 2014 using Duolingo and other resources"],
    ["Attic Greek", "Four semesters of study in college"],
    ["Attic Greek", "Achieved the ability to read unadapted intermediate Greek texts"],
    ["Attic Greek", "Familiarity with the Greek roots of English"],
    ["Latin", "Intensive independent study over the summer of 2011"],
    ["Latin", "Basic familiarity with Latin grammar"],
    ["Latin", "Familiarity with the Latin roots of English"],
    ["Turkish", "Intermittent study over several years using Duoling and the Russian textbook Uchebnik Turetskogo Iazyka (Textbook of the Turkish Language)"],
    ["Japanese", "Four years of study in high school"],
    ["Japanese", "Achieved intermediate profeciency"],
    ["Japanese", "Basic familiarity with Japanese grammar"],
    ["Japanese", "Knowledge of some important phrases"]
]

for lang in Languages:
    if len(lang) > 2:
        temp = Language(lang[0], lang[1], lang[2])
    else:
        temp = Language(langauge=lang[0], current=lang[1])
    temp.save()
    for det in LanguageDetails:
        if det[0] == lang[0]:
            temp2 = LanguageDetail(temp, det[1])
            temp2.save()


ComputerSkills = [
    ["Windows", "Computer"],
    ["Linux", "Computer"],
    ["Web Design", "Computer"],
    ["Computer Science", "Computer"]
]

ComputerSkillDetails = [
    ["Windows", "Knowledge of the MS Office Suite, especially Word and Excel"],
    ["Linux", "Comfort at the command line"],
    ["Linux", """Familiarity with multiple Linux distributions, including
     Debian, Debian derivatives (Linux Mint and Ubuntu), OpenSuse, and Arch
     derivatives (Manjaro, Antergos)"""],
    ["Web Design", "Django"],
    ["Web Design", "Bootstrap"],
    ["Web Design", "Javascript, including familiarity with Vue.JS"],
    ["Computer Science", """Knowledge of the essential abstract tools used in
     all programming languages"""],
    ["Computer Science", "Intermediate Python"]
]

for someskill in ComputerSkills:
    temp = Skill(someskill[0], someskill[1])
    temp.save()
    for detail in ComputerSkillDetails:
        if someskill[0] == detail[0]:
            temp2 = SkillDetail(temp, detail[1])
            temp2.save()

Jobs = [
    ["Assistant Paralegal",
     "Fragomen, Del Rey, Bernsen & Loewy, LLP",
     date(2015, 2, 1)],
    ["Staff Tutor",
     "Project: VISION",
     date(2013, 9, 1),
     date(2015, 2, 1)],
    ["Recess Supervisor",
     "Strech-n-Grow North, Inc.",
     date(2013, 10, 1),
     date(2014, 6, 1)],
    ["Tutor",
     "Somali American Parent Association",
     date(2012, 10, 1),
     date(2013, 4, 1)],
    ["Barista",
     "Publika Cafe",
     date(2012, 10, 1),
     date(2013, 3, 1)],
    ["Lead Worker",
     "O. Meredith Wilson Library, University of Minnesota",
     date(2010, 6, 1),
     date(2012, 8, 1)],
    ["Pathology Research Assistant",
     "University of Chicago Hospitals",
     date(2009, 6, 1),
     date(2009, 8, 1)]
]

PriorTitles = [
    ["Assistant Paralegal",
     "Administrative Assistant",
     date(2016, 1, 1)],
    ["Recess Supervisor",
     "Recess Coach",
     date(2014, 3, 1)],
    ["Lead Worker",
     "Student Library Assistant",
     date(2011, 6, 1)]
]

Duties = [
    ["Assistant Paralegal",
     """Drafting complex responses to government requests for
     additional evidence on immigration petitions""",
     False,
     ["Writing"]],
    ["Assistant Paralegal",
     "Managing numerous competing deadlines for various immigration matters",
     False,
     ["Time and Project Management"]],
    ["Assistant Paralegal",
     """Leading the preparation of high touch immigration cases
     requiring close coordination with client management""",
     False,
     ["Critical Thinking", "Client Service"]
     ],
    ["Assistant Paralegal",
     """Communicating with clients via email and phone to inform them of
     pressing issues in immigration""",
     False,
     ["Client Service", "Writing"]],
    ["Assistant Paralegal",
     """Developing standardized approaches to complex immigration case types
     and team infrastructure (such as template letters and emails) to
     facilitate the preparation of such cases""",
     False,
     ["Writing", "Critical Thinking"]],
    ["Assistant Paralegal",
     """Training and advising coworkers on various immigration case
     types/clients""",
     False,
     ["Teaching"]],
    ["Assistant Paralegal",
     """Photocopying and scanning visa petitions to prepare them for filing
     with United States Citizenship and Immigration Services""",
     True,
     ["Administrative"]],
    ["Assistant Paralegal",
     """Processing questionnaires from foreign nationals who wish to apply for
     or extend immigrant or nonimmigrant status""",
     True,
     ["Administrative"]],
    ["Assistant Paralegal",
     """Filling out expense reports for attorneys""",
     True,
     ["Administrative"]],
    ["Staff Tutor",
     """I tutored three to five students daily in grades six through twelve in
     all subjects""",
     False,
     ["Teaching"]],
    ["Staff Tutor",
     """I prepared academic enrichment activities for students who finished
     their homework early""",
     False,
     ["Teaching", "Writing"]],
    ["Staff Tutor",
     "I attended tutor trainings and workshops",
     False],
    ["Staff Tutor",
     """I taught the English and Mathematics sections of an ACT preparation
     class""",
     False,
     ["Teaching"]],
    ["Staff Tutor",
     """I ran a "Freshman Camp" for students about to begin their freshman year
     of high school""",
     False,
     ["Teaching"]],
    ["Staff Tutor",
     """I facilitated the "Teen Advisory Panel," which sought to engage
     teenages on community issues in Chicago's Chinatown""",
     False],
    ["Staff Tutor",
     """I entered and analyzed student attendance data""",
     False,
     ["Administrative"]],
    ["Staff Tutor",
     """I wrote and edited letters of inquiry to grantmakers""",
     False,
     ["writing"]]
]

Projects = [
    ["Assistant Paralegal",
     """Prepared an L-1 Blanket Amendment petition and numerous L-1 Blanket
     visas on an expedited basis""",
     """When one of our clients purchased an Italian-owned company without
     realizing the impact to the 12 or so E-2 visa holders then working for
     that company in the U.S., I handled the expedited L-1 blanket amendment
     petition preparation that would allow the client to prepare L-1 blanket
     petitions on behalf of the affected employees. The client in question has
     a reputation for its somewhat opaque internal corporate relationships, but
     I worked with them to obtain the necessary documentation to evidence the
     corporate relationships not only of the new Italian subsidiary, but also
     of multiple previous acquisitions which had not yet been added to the
     company's L-1 Blanket. The L-1 Blanket amendment petition I expeditiously
     prepared was quickly approved. While preparing the L-1 blanket amendment
     petition, I also carried out the eligibility analysis for the employees of
     the Italian subsidiary who had previously held E-2 status, and who were
     understandably somewhat concerned about the sudden invalidation of their
     visas. I understood not only the concern of the employees, but also the
     client's desire to have the situation resolved as soon as possible, and
     I prepared the cases on an expedited basis. All of the cases I prepared
     were approved in a timely manner.""",
     ["Writing", "Client Service", "Critical Thinking"]
     ],
    ["Assistant Paralegal",
     "Prepared multiple O-1 visa petitions for senior executives",
     """When one of our bigger clients decided to hire first one and then
     a second digital marketing executive, I handled the preparation of the
     O-1 petitions. Because these individuals were being offered positions at
     Vice President- and Senior Director-level, respectively, both cases
     attracted the attention of senior leadership at the client company. Under
     this increased scrutiny, I prepared case roadmaps, gathered supporting
     documentation, drafted expert testimonial letters, answered client
     questions, managed expectations, and prepared the O-1 petitions, including
     lengthy (around 30 page) company letters of support. Both petitions were
     approved without issuance of requests for additional evidence."""]
]

for job in Jobs:
    if len(job) <= 3:
        temp = Position(title=job[0], employer=job[1], start_date=job[2])
    else:
        temp = Position(job[0], job[1], job[2], job[3])
    temp.save()
    for oldtitle in PriorTitles:
        if oldtitle[0] == job[0]:
            temp2 = PriorTitle(temp, oldtitle[1], oldtitle[2])
            temp2.save()
    for duty in Duties:
        if duty[0] == job[0]:
            temp3 = Duty(temp, duty[1], duty[2])
            temp3.save()
            if len(duty) > 3:
                for tag in duty[3]:
                    temp4 = DutyTag(temp3, tag)
                    temp4.save()
    for proj in Projects:
        if proj[0] == job[0]:
            temp5 = Project(proj[1], proj[2])
            temp5.save()
            if len(proj) > 3:
                for tag in proj[3]:
                    temp6 = ProjectTag(temp5, tag)
                    temp6.save()

Interests = [
    ["The Written Word", """Writing as a means of communication is unique in that it can
     equally express both the rational/cerebral and the intuitive/emotional
     aspects of human experience. It provides ground for an intersection of art
     and science and it is means of transcending the temporal bounds of
     mortality. Through the written word I have spoken with great thinkers who
     have been dead for centuries, I have given vent to my own feelings and
     struggles, I have sharpened my introspective powers and taken greater
     agency in my own development.""", "writtenword.png"],
    ["Language", """I find several aspects of language particularly interesting:
     syntax, phonology, and semantics. I enjoy studying foreign languages and
     thinking about how people use language in writing and speech. But what
     interests me most about language is difficult to express. It has to do
     with the way fundamental cultural ideas and perceptions are encoded in
     the structure of a language. Because language is dynamic, and the
     language spoken at any given time in any given place has developed over
     centuries, it contains intimations of the cultural history and ideology
     of the people who speak it. By studying language, it is possible to access
     these underlying currents of thought and experience in a sort of indirect
     way.""", "language.png", """hese are the opening lines of the Iliad, a
     text which marked the beginning of European literary culture. I had the
     pleasure of reading selections of the Iliad in the original for my 4th
     semester of Greek in college."""],
    ["Art", """Art for art's sake is a fundamental principle in my life. I have
     found no better therapy for the "thousand natural shocks that flesh is heir
     to" than the creation of something artistic simply for its own sake. Art
     is a meditation and a catharsis. It is a transcendent mode of
     communication that operates on a level beyond our practical concerns, our
     instincts for survival. Good art touches the very foundations of what it
     means to be a human being, to feel these desires and these frustrations,
     to struggle daily against the insurmountable, to revel in the ephemeral
     beauty of our existence. Art is an explanation beyond words even when it
     uses words, an ascription of meaning beyond the constraints of the
     pragmatic mind, for it operates in the unbounded realm of the imagination.
     Art is life.""", "art.png", """A sketch I drew of the great American folk
     singer Woody Guthrie"""],
    ["Science and Technology", """Under this broad heading I would include
     cosmology, astronomy, astrophysics, physics, engineering, chemistry,
     biology, physiology, psychology, mathematics, computer science,
     and web design. Science represents a fundamental part of my world view.
     It is an established and carefully regulated means for evaluating the
     world around us in a standardized and verifiable manner, and it produces
     results that are useful in terms of predicting events, explaining the
     past, and designing products and tools to take advantage of the nature of
     the universe.""", "science.png", """This image is derived from an image in
     the public domain by Geek3. For more information visit
     https://commons.wikimedia.org/wiki/File:VFPt_Solenoid_correct2.svg"""],
    ["Thought", """By "thought" I mean systems of ideas, frameworks for
     interpreting the world. Our minds, having been shaped by the pragmatic
     hand of evolution, are incapable of processing the totality of the world
     around us, and they consequently operate by making groupings, reductions,
     approximations, eliminations. The integral of these simplifications is
     what might be called a world view. World views are the result of the
     complex interfacing of the individual and society. I like to learn about
     these interpretive frameworks both on the individual and the societal
     level, especially through the study of world religion, mythology,
     ethnography, and philosophy.""", "thought.jpg", """This image of a statue
     of the Scottish philosopher David Hume is derived from an image in the
     public domain by Bandan. For more information visit
     https://commons.wikimedia.org/wiki/File:DavidHume.jpg"""],
]

for interest in Interests:
    if len(interest) > 3:
        temp = Interest(interest[0], interest[1], interest[2], interest[3])
    else:
        temp = Interest(interest[0], interest[1], interest[2])
    temp.save()

ideals = [
    ["The Importance of Education", """This idea has its roots in the very
     bedrock of my personal identity. My parents made it the constant
     refrain of my upbringing. I cherish their ideal as my own and with an
     equal fervor. I view my college degree more as having equipped me with
     the tools to pursue self-education than as having prepared me for any
     specific job, and I have made the broadening of my education my daily
     task since I've graduated."""],
    ["The Value of the Liberal Arts", """When I selected Classical
     Civilizations as my major in college, I made a decision to invest in a
     broad education that emphasized thinking. I made the investment knowing
     full well what the Liberal Arts offer a dedicated student: a wide-ranging
     ability to solve problems, excellence in written and verbal communication,
     and, most importantly, the ability to learn. I made that choice because I
     truly believe in the value of the Liberal Arts in making strong, capable
     citizens, thinkers, and workers."""],
    ["Honesty and Accountability", """I view honesty and accountability as the
     foundation of good relationships, both personal and professional. Without
     honest communication, there can be no effective collaboration, which is so
     key in our ever-increasingly interconnected world. Without accountability
     there can be no constructive efforts to deal with mistakes. I try to cultivate
     these characteristics in myself, and I also look for them in others when I am
     forming relationships."""],
    ["Open-Mindedness", """I consider some flexibility in ideas to be another
     fundamental component of cooperation. Keeping an open mind fosters
     creativity in problem solving. Moreover, it helps disarm the personal
     attachment to ideas which is so often at the root of personal conflict. It
     is all too easy to mistake criticism of an idea for a personal attack,
     and open-mindedness helps prevent such misunderstandings."""],
    ["Cooperation and Proactive Engagement", """Cooperation is at the heart of
     any successful effort. We are capable of achieving much more when we work
     together effectively than we can as individuals. By proactive engagement,
     I mean mindful, continual engagement with coworkers to address any issues
     that might reduce the effectiveness of collaboration. I might liken
     proactive engagement to cleaning a house. If the cleaning is done
     regularly, it is a task which requires some attention, but is not
     overwhelming. But if the cleaning is neglected for a long period, it
     becomes a substantial, potentially very stressful task."""]
]

for ideal in ideals:
    temp = Ideal(ideal[0], ideal[1])
    temp.save()
