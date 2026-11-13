"""
content.py - all the learning content for NeuroBridge, stored as plain Python
dictionaries and lists. You can edit any text here without touching app.py.
"""

# ----------------------------------------------------------------------
# Inspirational messages (original, shown randomly on the dashboard)
# ----------------------------------------------------------------------
QUOTES = [
    "Every page you read makes your brain stronger. 🌟",
    "Mistakes are proof that you are trying. Keep going! 💪",
    "Small steps every day lead to big adventures. 🚶‍♀️",
    "You learn at your own pace, and that is perfectly okay. 🐢",
    "Reading is a superpower, and you are building yours. 🦸",
    "Be proud of how far you have come. 🌈",
    "A curious mind can learn anything. 🔍",
    "Practice makes progress, not perfection. ✨",
]

# ----------------------------------------------------------------------
# Stories: 6 original stories, grouped by reading level
# Each story has: title, level, time, emoji, description, paragraphs,
# vocabulary (word -> meaning/example/emoji) and exactly 5 questions
# (3 facts, 1 vocabulary, 1 inference).
# ----------------------------------------------------------------------
STORIES = [
    {
        "id": "bird",
        "title": "The Little Bird Who Kept Trying",
        "level": "Beginner",
        "time": "3 minutes",
        "emoji": "🐦🌳🌤️",
        "description": "A small bird learns that practice helps you do hard things.",
        "paragraphs": [
            "Pip was a little bird with soft yellow feathers. He lived in a nest high in a tall oak tree.",
            "Every morning, Pip watched the other birds fly. They flew over the hills and the river. Pip wanted to fly too.",
            "One day, Pip stood at the edge of the nest. He flapped his wings and jumped. Plop! He landed on a pile of leaves.",
            "Pip felt sad. His mum said, “Do not give up, Pip. Every bird learns a little at a time.”",
            "So Pip tried again the next day. And the day after that. Each time, he flew a little bit further.",
            "At last, Pip flapped his wings and flew all the way to the river. He was so proud. Pip learned that if you keep trying, you can do hard things.",
        ],
        "vocabulary": {
            "edge": {"meaning": "The side or end of something.", "example": "Pip stood at the edge of the nest.", "emoji": "📏"},
            "flapped": {"meaning": "Moved up and down quickly.", "example": "The bird flapped its wings.", "emoji": "🪽"},
            "proud": {"meaning": "Feeling happy about something you did.", "example": "She was proud of her drawing.", "emoji": "😊"},
            "further": {"meaning": "A longer way away.", "example": "He threw the ball further than before.", "emoji": "➡️"},
        },
        "questions": [
            {"q": "Where did Pip live?", "options": ["In a nest in a tall oak tree", "In a cave", "In a barn", "On a river bank"],
             "answer": "In a nest in a tall oak tree", "explain": "The story says Pip lived in a nest high in a tall oak tree."},
            {"q": "What happened the first time Pip jumped?", "options": ["He landed on a pile of leaves", "He flew to the river", "He met a cat", "He fell in the water"],
             "answer": "He landed on a pile of leaves", "explain": "Pip said “Plop!” and landed on a pile of leaves."},
            {"q": "Where did Pip fly to at last?", "options": ["The hills", "The river", "The school", "The sea"],
             "answer": "The river", "explain": "At last, Pip flew all the way to the river."},
            {"q": "What does the word “proud” mean?", "options": ["Feeling happy about something you did", "Feeling very sleepy", "Feeling cold", "Feeling lost"],
             "answer": "Feeling happy about something you did", "explain": "Proud means you feel happy about something you did well."},
            {"q": "Why did Pip fly a little further each day?", "options": ["Because he kept practising", "Because the wind was strong", "Because he was hungry", "Because he was bigger"],
             "answer": "Because he kept practising", "explain": "Pip tried again and again, so he got better each time."},
        ],
    },
    {
        "id": "library",
        "title": "Mia and the Magical Library",
        "level": "Beginner",
        "time": "3 minutes",
        "emoji": "📚🚪✨",
        "description": "Mia finds a little blue door at the back of her library.",
        "paragraphs": [
            "Mia loved books. On Saturday, she went to the old library on her street.",
            "At the back of the library, Mia saw a small blue door. She had never seen it before. She pushed it open.",
            "Inside, the shelves sparkled like stars. A book floated down and landed in her hands. It was called “The Book of Colours”.",
            "When Mia opened it, a red butterfly flew out. Then a green frog hopped out. Then a yellow sun floated up to the ceiling.",
            "“Books can take you anywhere,” whispered a soft voice. Mia smiled.",
            "She read until the library closed. Then she borrowed the book and took it home. The next Saturday, she went back to find the little blue door again.",
        ],
        "vocabulary": {
            "library": {"meaning": "A place where you can read and borrow books.", "example": "We borrow books from the library.", "emoji": "📚"},
            "sparkled": {"meaning": "Shone with little bright lights.", "example": "The water sparkled in the sun.", "emoji": "✨"},
            "floated": {"meaning": "Moved slowly through the air or on water.", "example": "The balloon floated up.", "emoji": "🎈"},
            "whispered": {"meaning": "Spoke in a very quiet voice.", "example": "She whispered a secret.", "emoji": "🤫"},
        },
        "questions": [
            {"q": "What colour was the little door?", "options": ["Blue", "Red", "Green", "Yellow"],
             "answer": "Blue", "explain": "Mia saw a small blue door at the back of the library."},
            {"q": "What was the magic book called?", "options": ["The Book of Colours", "The Book of Stars", "The Big Book of Frogs", "The Blue Book"],
             "answer": "The Book of Colours", "explain": "The book was called “The Book of Colours”."},
            {"q": "What flew out of the book first?", "options": ["A red butterfly", "A green frog", "A yellow sun", "A blue bird"],
             "answer": "A red butterfly", "explain": "First a red butterfly flew out. Then came the frog and the sun."},
            {"q": "What does “sparkled” mean?", "options": ["Shone with little bright lights", "Fell down", "Made a loud noise", "Became very old"],
             "answer": "Shone with little bright lights", "explain": "Sparkled means shone with tiny bright lights, like stars."},
            {"q": "Why did Mia go back the next Saturday?", "options": ["She wanted to find the magic door again", "She had to return a toy", "She was lost", "She wanted to buy a book"],
             "answer": "She wanted to find the magic door again", "explain": "Mia loved the magic, so she went back to look for the little blue door."},
        ],
    },
    {
        "id": "map",
        "title": "The Mystery of the Missing Map",
        "level": "Intermediate",
        "time": "5 minutes",
        "emoji": "🗺️🔍🐶",
        "description": "Two children follow clues to find a missing treasure map.",
        "paragraphs": [
            "Kiran and his sister Asha were exploring their grandfather's attic on a rainy afternoon. They were looking for the old treasure map that Grandpa had promised to show them, but the wooden chest where it was kept was empty.",
            "“Someone has taken it,” gasped Asha. Kiran bent down and studied the dusty floor. There were small, muddy paw prints leading towards the window.",
            "They followed the prints down the stairs, across the hall and into the kitchen. Under the table sat Biscuit, the family puppy, chewing something made of paper.",
            "“Biscuit, no!” cried Kiran. He gently pulled the paper from the puppy's mouth. It was the map, a little wet and crumpled, but still in one piece.",
            "Grandpa laughed when he saw it. “Biscuit must have thought it was a treat,” he said. He placed the map under a heavy book to flatten it.",
            "That evening, the three of them studied the map together. A red cross marked a spot beneath the old mango tree in the garden. The real adventure was about to begin.",
        ],
        "vocabulary": {
            "attic": {"meaning": "A room at the top of a house under the roof.", "example": "Old boxes were stored in the attic.", "emoji": "🏠"},
            "crumpled": {"meaning": "Squashed with folds and creases.", "example": "He found a crumpled note in his bag.", "emoji": "📄"},
            "studied": {"meaning": "Looked at something very carefully.", "example": "She studied the picture closely.", "emoji": "🧐"},
            "marked": {"meaning": "Showed a place with a sign or symbol.", "example": "An X marked the spot.", "emoji": "❌"},
        },
        "questions": [
            {"q": "Where were Kiran and Asha searching for the map?", "options": ["In the attic", "In the garden", "In the kitchen", "At school"],
             "answer": "In the attic", "explain": "They were exploring their grandfather's attic."},
            {"q": "What did Kiran notice on the dusty floor?", "options": ["Muddy paw prints", "A torn page", "A silver key", "Wet footprints from Grandpa"],
             "answer": "Muddy paw prints", "explain": "Kiran saw small, muddy paw prints leading towards the window."},
            {"q": "Who was chewing the map?", "options": ["Biscuit the puppy", "Asha", "Grandpa", "A mouse"],
             "answer": "Biscuit the puppy", "explain": "Biscuit, the family puppy, was chewing the paper under the table."},
            {"q": "What does “crumpled” mean?", "options": ["Squashed with folds and creases", "Clean and flat", "Very colourful", "Cut in half"],
             "answer": "Squashed with folds and creases", "explain": "A crumpled paper has been squashed, so it has folds and creases."},
            {"q": "Why did Grandpa put the map under a heavy book?", "options": ["To make it flat again", "To hide it from Biscuit forever", "To make it heavier", "To dry the book"],
             "answer": "To make it flat again", "explain": "The map was crumpled, so the heavy book would press it flat."},
        ],
    },
    {
        "id": "rainforest",
        "title": "A Journey Through the Rainforest",
        "level": "Intermediate",
        "time": "5 minutes",
        "emoji": "🌴🦜🐒",
        "description": "A young explorer discovers the sights and sounds of the rainforest.",
        "paragraphs": [
            "Deep in the rainforest, the morning mist hung between the tall trees like a soft white blanket. Leo, a young explorer, adjusted his backpack and began his walk along the narrow path.",
            "Above him, the canopy was thick with green leaves. Monkeys chattered and swung from branch to branch, while bright parrots flashed red and blue between the trees.",
            "Leo stopped beside a wide river. Tiny frogs sat on the lily pads, and dragonflies skimmed over the water.",
            "Suddenly, rain began to fall. Rainforests get heavy rain almost every day. Leo pulled a giant leaf over his head and used it like an umbrella.",
            "When the rain stopped, the forest smelled fresh and sweet. Drops sparkled on every leaf. Leo wrote in his notebook: “Rainforests are home to more kinds of plants and animals than almost anywhere else on Earth.”",
            "As the sun set, Leo walked back to camp. He was tired but happy. He promised to protect the rainforest and tell others about its wonders.",
        ],
        "vocabulary": {
            "canopy": {"meaning": "The top layer of leaves and branches in a forest.", "example": "Birds nest in the canopy.", "emoji": "🌳"},
            "explorer": {"meaning": "A person who travels to learn about new places.", "example": "The explorer drew a map.", "emoji": "🧭"},
            "mist": {"meaning": "A thin cloud of tiny water drops near the ground.", "example": "Mist covered the hills.", "emoji": "🌫️"},
            "protect": {"meaning": "To keep something safe from harm.", "example": "We protect nature by not dropping litter.", "emoji": "🛡️"},
        },
        "questions": [
            {"q": "What hung between the trees in the morning?", "options": ["Mist", "Smoke", "Snow", "Rain"],
             "answer": "Mist", "explain": "The morning mist hung between the tall trees like a soft white blanket."},
            {"q": "What did Leo use as an umbrella?", "options": ["A giant leaf", "His backpack", "A notebook", "A coat"],
             "answer": "A giant leaf", "explain": "Leo pulled a giant leaf over his head."},
            {"q": "What did Leo write in his notebook?", "options": ["Rainforests have many kinds of plants and animals", "How to build a camp", "A list of his favourite foods", "The names of the monkeys"],
             "answer": "Rainforests have many kinds of plants and animals", "explain": "He wrote that rainforests are home to more kinds of plants and animals than almost anywhere else."},
            {"q": "What does “canopy” mean?", "options": ["The top layer of leaves and branches", "A muddy path", "A kind of river", "A type of bird"],
             "answer": "The top layer of leaves and branches", "explain": "The canopy is the high roof of leaves and branches in a forest."},
            {"q": "Why did Leo promise to protect the rainforest?", "options": ["He saw how special and full of life it is", "He was told to by a monkey", "He was afraid of the rain", "He wanted to live there"],
             "answer": "He saw how special and full of life it is", "explain": "Leo enjoyed the wonders of the forest, so he wanted to keep it safe."},
        ],
    },
    {
        "id": "inventor",
        "title": "The Clever Little Inventor",
        "level": "Advanced",
        "time": "7 minutes",
        "emoji": "💡🔧🌊",
        "description": "A ten-year-old invents a flood alarm to help her town.",
        "paragraphs": [
            "Nina lived in a small town where the river often flooded the lower streets after heavy storms. While the grown-ups worried, Nina, who was only ten years old, wondered whether there might be a way to help.",
            "She spent a week sketching ideas in her notebook, but most of her first designs were far too complicated. Then, one afternoon, she noticed that a cork floats on water. If a floating cork could press a button when the water rose, it might set off an alarm.",
            "Nina collected a plastic bottle, a small battery, a buzzer and some wire from her father's toolbox. After many failed attempts, her first device finally buzzed loudly when she placed it in a bucket of water.",
            "She tied the device to a post beside the river. That night, a heavy storm arrived. As the water crept higher, the cork rose and the buzzer began to sound. Neighbours woke up and moved their belongings to safety before the flood reached their doors.",
            "The next morning, the whole town gathered to thank her. The mayor asked Nina to make more alarms for every street near the river. Nina smiled and said she would need some help.",
            "Soon, her classmates joined her in a workshop, and together they built twenty alarms. Nina discovered that clever ideas become even more powerful when people work together.",
        ],
        "vocabulary": {
            "device": {"meaning": "A small tool or machine made for a special job.", "example": "A torch is a useful device.", "emoji": "🔌"},
            "complicated": {"meaning": "Hard to understand because it has many parts.", "example": "The puzzle was too complicated.", "emoji": "🧩"},
            "belongings": {"meaning": "The things that belong to you.", "example": "Pack your belongings before you leave.", "emoji": "🎒"},
            "workshop": {"meaning": "A room where people make or fix things.", "example": "They built a kite in the workshop.", "emoji": "🛠️"},
        },
        "questions": [
            {"q": "What often happened to the lower streets after heavy storms?", "options": ["They flooded", "They froze", "They filled with sand", "They closed for repairs"],
             "answer": "They flooded", "explain": "The river often flooded the lower streets after heavy storms."},
            {"q": "What made the alarm's buzzer start to sound?", "options": ["The rising water lifted the cork", "A neighbour pressed a button", "The wind blew the bottle", "Nina shouted"],
             "answer": "The rising water lifted the cork", "explain": "As the water crept higher, the cork rose and the buzzer sounded."},
            {"q": "What did the neighbours do when the buzzer woke them?", "options": ["They moved their belongings to safety", "They went back to sleep", "They built a wall", "They ran to the river"],
             "answer": "They moved their belongings to safety", "explain": "They woke up and moved their belongings to safety before the flood arrived."},
            {"q": "What does “complicated” mean?", "options": ["Hard to understand because it has many parts", "Very small", "Cheap and simple", "Bright and shiny"],
             "answer": "Hard to understand because it has many parts", "explain": "Complicated things have many parts, so they are not easy to understand."},
            {"q": "Why did Nina say she would need some help?", "options": ["There were many alarms to build", "She was afraid of the storm", "She had lost her notebook", "She did not like the mayor"],
             "answer": "There were many alarms to build", "explain": "The mayor wanted alarms for every street, which is too much work for one person."},
        ],
    },
    {
        "id": "stars",
        "title": "The Secret of the Starry Night",
        "level": "Advanced",
        "time": "7 minutes",
        "emoji": "🌟🔭🌙",
        "description": "Zara climbs a hill to discover what the stars have to say.",
        "paragraphs": [
            "In the village of Moonfield, people said that on the clearest night of the year, the stars would whisper a secret. Most children laughed at the old tale, but twelve-year-old Zara was curious.",
            "One cold evening, she climbed to the top of Windy Hill with a blanket, a flask of warm milk and her grandfather's old telescope. The sky above her was an enormous bowl of glittering lights.",
            "Hours passed. Zara noticed that the stars were not all the same. Some were white, some were blue, and some were a faint orange. She wrote each colour in her notebook and drew careful maps of the patterns.",
            "Just before dawn, a bright streak of light crossed the sky: a shooting star. Zara held her breath. In that silent moment, she felt wonderfully small and wonderfully connected to the universe at the same time.",
            "When she returned home, her grandfather asked if the stars had told her their secret. Zara thought carefully. “They did,” she said. “The secret is that the more patiently you look, the more you find.”",
            "From that night on, Zara kept a star diary. Years later, she became an astronomer, a scientist who studies space, and she often told children the secret of the starry night.",
        ],
        "vocabulary": {
            "telescope": {"meaning": "A tool that makes faraway things look closer.", "example": "He looked at the moon through a telescope.", "emoji": "🔭"},
            "glittering": {"meaning": "Shining with many tiny flashes of light.", "example": "The glittering lights filled the sky.", "emoji": "💫"},
            "patiently": {"meaning": "Calmly, without hurrying or giving up.", "example": "She waited patiently for her turn.", "emoji": "⏳"},
            "astronomer": {"meaning": "A scientist who studies stars and space.", "example": "The astronomer studied a new planet.", "emoji": "👩‍🔬"},
        },
        "questions": [
            {"q": "Where did Zara climb to watch the stars?", "options": ["Windy Hill", "Moonfield Tower", "The village school", "A mountain by the sea"],
             "answer": "Windy Hill", "explain": "Zara climbed to the top of Windy Hill."},
            {"q": "Which object belonged to Zara's grandfather?", "options": ["The telescope", "The blanket", "The notebook", "The flask"],
             "answer": "The telescope", "explain": "She took her grandfather's old telescope."},
            {"q": "What crossed the sky just before dawn?", "options": ["A shooting star", "A plane", "A cloud", "A bird"],
             "answer": "A shooting star", "explain": "A bright streak of light, a shooting star, crossed the sky."},
            {"q": "What does “patiently” mean?", "options": ["Calmly, without hurrying or giving up", "Very quickly", "Angrily", "Loudly"],
             "answer": "Calmly, without hurrying or giving up", "explain": "Patiently means staying calm and waiting or trying without rushing."},
            {"q": "What is the “secret” that Zara found?", "options": ["Looking carefully and patiently shows you more", "Stars can talk like people", "You must never climb hills", "Only grown-ups can see stars"],
             "answer": "Looking carefully and patiently shows you more", "explain": "Zara said the more patiently you look, the more you find."},
        ],
    },
]

LEVELS = ["Beginner", "Intermediate", "Advanced"]

# ----------------------------------------------------------------------
# Maths question bank
# Each entry: (question, correct answer, [three wrong answers], explanation)
# Organised as MATHS_BANK[topic][difficulty] = list of entries.
# ----------------------------------------------------------------------
CLASS_LEVELS = {
    "Class 1-2": "Easy",
    "Class 3-4": "Medium",
    "Class 5-6": "Challenging",
}
DIFFICULTIES = ["Easy", "Medium", "Challenging"]

MATHS_BANK = {
    "Counting and number recognition": {
        "Easy": [
            ("🍎🍎🍎🍎  How many apples are there?", "4", ["3", "5", "6"], "Touch each apple and count: 1, 2, 3, 4. There are 4 apples."),
            ("What number comes after 6?", "7", ["5", "8", "9"], "Count on from 6: 6, then 7. The number after 6 is 7."),
            ("Which number is the biggest: 3, 9 or 5?", "9", ["3", "5", "1"], "Count up: 3, 5, 9. The number that comes last is the biggest, so 9."),
            ("⭐⭐⭐⭐⭐⭐  How many stars are there?", "6", ["5", "7", "8"], "Count each star: 1, 2, 3, 4, 5, 6. There are 6 stars."),
            ("What number comes before 10?", "9", ["8", "11", "1"], "Count back one from 10. The number before 10 is 9."),
        ],
        "Medium": [
            ("Count by 2s: 2, 4, 6, __", "8", ["7", "9", "10"], "Add 2 each time: 6 + 2 = 8."),
            ("Which number is between 14 and 16?", "15", ["13", "17", "20"], "Count: 14, 15, 16. The middle number is 15."),
            ("Which number is the smallest: 27, 18 or 31?", "18", ["27", "31", "81"], "Compare the tens first. 18 has 1 ten, the others have 2 or 3 tens. So 18 is the smallest."),
            ("Count by 5s: 5, 10, 15, __", "20", ["16", "25", "30"], "Add 5 each time: 15 + 5 = 20."),
            ("How many tens are in 40?", "4", ["2", "10", "40"], "Count in tens: 10, 20, 30, 40. That is 4 tens."),
        ],
        "Challenging": [
            ("Count by 10s: 30, 40, 50, __", "60", ["55", "70", "51"], "Add 10 each time: 50 + 10 = 60."),
            ("Which number is made of 6 tens and 3 ones?", "63", ["36", "603", "9"], "6 tens is 60. Add 3 ones to get 63."),
            ("What number comes after 199?", "200", ["190", "201", "2000"], "199 + 1 = 200. The hundreds digit goes up and the other digits become 0."),
            ("Count back by 3s: 15, 12, 9, __", "6", ["7", "5", "3"], "Take away 3 each time: 9 - 3 = 6."),
            ("Which list goes from smallest to largest?", "25, 45, 52", ["52, 45, 25", "25, 52, 45", "45, 25, 52"], "Compare the tens: 25 has 2 tens, 45 has 4 tens, 52 has 5 tens. So 25, 45, 52."),
        ],
    },
    "Addition and subtraction": {
        "Easy": [
            ("You have 5 apples 🍎 and receive 2 more. How many apples do you have?", "7", ["6", "8", "3"], "Start with 5 and count 2 more: 6, 7. The answer is 7."),
            ("3 + 4 = ?", "7", ["6", "8", "5"], "Start at 3 and count on 4: 4, 5, 6, 7. The answer is 7."),
            ("8 - 3 = ?", "5", ["4", "6", "11"], "Start at 8 and count back 3: 7, 6, 5. The answer is 5."),
            ("🐟🐟🐟🐟🐟🐟  There are 6 fish. 2 swim away. How many are left?", "4", ["3", "5", "8"], "Take away 2 from 6: 5, 4. There are 4 fish left."),
            ("10 - 5 = ?", "5", ["4", "6", "15"], "Half of 10 is 5, so 10 - 5 = 5."),
        ],
        "Medium": [
            ("24 + 13 = ?", "37", ["36", "47", "27"], "Add the tens: 20 + 10 = 30. Add the ones: 4 + 3 = 7. Then 30 + 7 = 37."),
            ("45 - 20 = ?", "25", ["35", "65", "15"], "Take away 2 tens from 45. You are left with 25."),
            ("36 + 28 = ?", "64", ["54", "62", "74"], "36 + 20 = 56. Then 56 + 8 = 64."),
            ("70 - 34 = ?", "36", ["46", "34", "44"], "70 - 30 = 40. Then 40 - 4 = 36."),
            ("58 + 19 = ?", "77", ["67", "78", "87"], "Add 20 instead: 58 + 20 = 78. Then take away 1 to get 77."),
        ],
        "Challenging": [
            ("256 + 138 = ?", "394", ["384", "404", "494"], "Add hundreds: 200 + 100 = 300. Tens: 50 + 30 = 80. Ones: 6 + 8 = 14. Total: 300 + 80 + 14 = 394."),
            ("500 - 247 = ?", "253", ["263", "353", "257"], "Count up from 247 to 250 (3), then to 500 (250). 3 + 250 = 253."),
            ("1000 - 650 = ?", "350", ["450", "400", "250"], "Think: 650 + 350 = 1000. So the answer is 350."),
            ("468 + 275 = ?", "743", ["633", "733", "753"], "468 + 200 = 668. Then 668 + 75 = 743."),
            ("Which sum is equal to 90?", "45 + 45", ["50 + 50", "60 + 20", "70 + 10"], "45 + 45 = 90. The others make 100, 80 and 80."),
        ],
    },
    "Multiplication and division": {
        "Easy": [
            ("2 × 3 = ?", "6", ["5", "8", "23"], "2 × 3 means 3 groups of 2, or 2 + 2 + 2 = 6."),
            ("5 × 2 = ?", "10", ["7", "12", "25"], "5 groups of 2 is 2 + 2 + 2 + 2 + 2 = 10."),
            ("🍪 There are 3 plates with 2 cookies on each plate. How many cookies are there?", "6", ["5", "8", "32"], "3 plates with 2 cookies each: 2 + 2 + 2 = 6."),
            ("10 ÷ 2 = ?", "5", ["8", "12", "2"], "Share 10 into 2 equal groups. Each group has 5."),
            ("Share 8 sweets 🍬 equally between 2 children. How many sweets does each child get?", "4", ["2", "6", "16"], "8 shared into 2 equal groups is 4 each, because 4 + 4 = 8."),
        ],
        "Medium": [
            ("6 × 7 = ?", "42", ["36", "48", "13"], "6 × 7 = 42. Tip: 6 × 7 is 6 × 5 (30) plus 6 × 2 (12), which is 42."),
            ("9 × 4 = ?", "36", ["32", "40", "13"], "9 × 4 means 4 groups of 9: 9 + 9 + 9 + 9 = 36."),
            ("56 ÷ 8 = ?", "7", ["6", "8", "48"], "8 × 7 = 56, so 56 ÷ 8 = 7."),
            ("72 ÷ 9 = ?", "8", ["7", "9", "63"], "9 × 8 = 72, so 72 ÷ 9 = 8."),
            ("A box holds 6 eggs 🥚. How many eggs are in 5 boxes?", "30", ["11", "36", "25"], "5 boxes of 6 eggs: 6 × 5 = 30."),
        ],
        "Challenging": [
            ("12 × 11 = ?", "132", ["122", "123", "142"], "12 × 10 = 120. Add one more 12: 120 + 12 = 132."),
            ("15 × 6 = ?", "90", ["80", "96", "21"], "10 × 6 = 60 and 5 × 6 = 30. Then 60 + 30 = 90."),
            ("144 ÷ 12 = ?", "12", ["11", "13", "132"], "12 × 12 = 144, so 144 ÷ 12 = 12."),
            ("4 buses each carry 36 children. How many children are there in total?", "144", ["140", "124", "40"], "36 × 4: 30 × 4 = 120 and 6 × 4 = 24. Then 120 + 24 = 144."),
            ("252 ÷ 6 = ?", "42", ["52", "32", "46"], "6 × 42 = 252 (6 × 40 = 240 and 6 × 2 = 12). So 252 ÷ 6 = 42."),
        ],
    },
    "Fractions": {
        "Easy": [
            ("🍕 A pizza is cut into 2 equal parts. You eat 1 part. What fraction did you eat?", "1/2", ["1/3", "2/1", "1/4"], "1 part out of 2 equal parts is written 1/2, or one half."),
            ("Which fraction means “one out of three equal parts”?", "1/3", ["1/2", "3/1", "2/3"], "The top number counts the parts you take (1). The bottom number is all the equal parts (3). So 1/3."),
            ("What is half of 10?", "5", ["2", "8", "20"], "Half means sharing into 2 equal parts. 10 shared by 2 is 5."),
            ("🟦🟦⬜⬜  What fraction of the squares are blue?", "2/4", ["1/4", "3/4", "4/2"], "2 squares out of 4 are blue, so the fraction is 2/4 (which is the same as one half)."),
            ("Which is bigger: 1/2 or 1/4?", "1/2", ["1/4", "They are the same", "Cannot tell"], "Cutting something into 2 pieces makes bigger pieces than cutting it into 4. So 1/2 is bigger."),
        ],
        "Medium": [
            ("What is 1/4 of 12?", "3", ["4", "6", "8"], "Share 12 into 4 equal groups. Each group has 3."),
            ("Which fraction is equal to 1/2?", "2/4", ["1/4", "3/4", "2/3"], "2/4 means 2 parts out of 4, which is the same amount as 1 part out of 2."),
            ("1/5 + 2/5 = ?", "3/5", ["3/10", "2/10", "1/5"], "The bottom numbers are the same, so add the top numbers: 1 + 2 = 3. The answer is 3/5."),
            ("What is 1/3 of 18?", "6", ["3", "9", "15"], "Share 18 into 3 equal groups. Each group has 6."),
            ("Which fraction is the largest?", "3/4", ["1/4", "2/4", "1/2"], "All have bottom number 4 (or equal 1/2). The bigger the top number, the bigger the fraction. So 3/4 is the largest."),
        ],
        "Challenging": [
            ("3/8 + 2/8 = ?", "5/8", ["5/16", "6/8", "1/8"], "The bottom numbers are the same. Add the top numbers: 3 + 2 = 5. The answer is 5/8."),
            ("What is 3/4 of 20?", "15", ["5", "10", "16"], "1/4 of 20 is 5. So 3/4 is 3 × 5 = 15."),
            ("Which fraction is equal to 2/3?", "4/6", ["2/6", "3/6", "4/9"], "Double the top and the bottom of 2/3: 4/6. It is the same amount."),
            ("7/10 - 3/10 = ?", "4/10", ["4/20", "10/10", "3/7"], "The bottom numbers are the same. Subtract the top numbers: 7 - 3 = 4. The answer is 4/10."),
            ("Which list goes from smallest to largest?", "1/4, 1/2, 3/4", ["3/4, 1/2, 1/4", "1/2, 1/4, 3/4", "1/4, 3/4, 1/2"], "Think of 1/2 as 2/4. So the order is 1/4, 2/4, 3/4, or 1/4, 1/2, 3/4."),
        ],
    },
    "Shapes and patterns": {
        "Easy": [
            ("How many sides does a triangle 🔺 have?", "3", ["2", "4", "5"], "Count the sides of a triangle: 1, 2, 3."),
            ("Which shape has 4 equal sides?", "Square", ["Triangle", "Circle", "Oval"], "A square has 4 sides that are all the same length."),
            ("🔴🔵🔴🔵🔴  What comes next?", "🔵", ["🔴", "🟢", "🟡"], "The pattern is red, blue, red, blue, red... so blue comes next."),
            ("How many corners does a square have?", "4", ["3", "5", "0"], "A square has 4 corners, one at the end of each side."),
            ("🟦🟦🟨🟦🟦🟨  What comes next?", "🟦", ["🟨", "🔴", "🟩"], "The pattern is blue, blue, yellow, and it repeats. After yellow comes blue."),
        ],
        "Medium": [
            ("How many sides does a hexagon have?", "6", ["5", "7", "8"], "A hexagon has 6 sides. “Hex” means six."),
            ("2, 4, 6, 8, __  What comes next?", "10", ["9", "12", "11"], "The pattern adds 2 each time: 8 + 2 = 10."),
            ("Which shape has 5 sides?", "Pentagon", ["Hexagon", "Square", "Triangle"], "A pentagon has 5 sides. “Penta” means five."),
            ("🔺🟦🟦🔺🟦🟦🔺  What comes next?", "🟦", ["🔺", "🟨", "🔴"], "The pattern is triangle, blue, blue. After the triangle comes blue."),
            ("Which solid shape looks like a dice 🎲?", "Cube", ["Sphere", "Cone", "Cylinder"], "A dice has 6 square faces. That shape is a cube."),
        ],
        "Challenging": [
            ("3, 6, 12, 24, __  What comes next?", "48", ["36", "30", "27"], "Each number is double the one before: 24 × 2 = 48."),
            ("How many edges does a cube have?", "12", ["6", "8", "10"], "A cube has 4 edges on top, 4 on the bottom and 4 going up the sides. 4 + 4 + 4 = 12."),
            ("1, 4, 9, 16, __  What comes next?", "25", ["20", "24", "36"], "These are square numbers: 1×1, 2×2, 3×3, 4×4. The next is 5×5 = 25."),
            ("How many faces does a cube have?", "6", ["4", "8", "12"], "A cube has a top, a bottom and 4 sides. That makes 6 faces."),
            ("What is the rule for 5, 8, 11, 14?", "Add 3 each time", ["Add 2 each time", "Add 5 each time", "Multiply by 2"], "8 - 5 = 3, 11 - 8 = 3, 14 - 11 = 3. The rule is to add 3 each time."),
        ],
    },
    "Simple word problems": {
        "Easy": [
            ("Sam has 4 pencils ✏️. Mum gives him 3 more. How many pencils does Sam have now?", "7", ["6", "8", "1"], "4 and 3 more: 4 + 3 = 7."),
            ("There are 9 birds 🐦 on a tree. 4 fly away. How many birds are left?", "5", ["4", "6", "13"], "9 take away 4: 9 - 4 = 5."),
            ("Each child gets 2 balloons 🎈. There are 3 children. How many balloons are needed?", "6", ["5", "8", "9"], "3 children with 2 balloons each: 2 + 2 + 2 = 6."),
            ("Anu has 10 stickers. She gives 5 to her friend. How many does she have left?", "5", ["4", "6", "15"], "10 take away 5: 10 - 5 = 5."),
            ("There are 6 red cars 🚗 and 3 blue cars. How many cars are there in all?", "9", ["8", "3", "10"], "Put the groups together: 6 + 3 = 9."),
        ],
        "Medium": [
            ("A shop has 24 apples. It sells 9. How many apples are left?", "15", ["14", "16", "33"], "24 - 9 = 15. You can do 24 - 10 = 14 and then add 1 back."),
            ("A box has 8 pens. How many pens are in 6 boxes?", "48", ["14", "42", "56"], "6 boxes of 8 pens: 8 × 6 = 48."),
            ("Riya read 15 pages on Monday and 18 pages on Tuesday. How many pages did she read altogether?", "33", ["23", "32", "34"], "15 + 18 = 33. (15 + 10 = 25, then + 8 = 33.)"),
            ("36 children sit in 4 equal rows. How many children are in each row?", "9", ["8", "10", "32"], "Share 36 into 4 equal rows: 36 ÷ 4 = 9."),
            ("A book costs ₹45 and a pen costs ₹12. How much do they cost together?", "₹57", ["₹33", "₹47", "₹67"], "45 + 12 = 57. So they cost ₹57 together."),
        ],
        "Challenging": [
            ("A school has 6 classes with 35 children in each class. How many children are there?", "210", ["200", "41", "180"], "35 × 6: 30 × 6 = 180 and 5 × 6 = 30. Then 180 + 30 = 210."),
            ("Tom had ₹500. He bought a bag for ₹275. How much money does he have left?", "₹225", ["₹325", "₹235", "₹775"], "500 - 275 = 225. (275 + 225 = 500.)"),
            ("72 sweets are shared equally among 9 children. Each child eats 3 sweets. How many sweets does each child have left?", "5", ["8", "6", "3"], "First, 72 ÷ 9 = 8 sweets each. Then 8 - 3 = 5 sweets left."),
            ("A shopkeeper sells 125 mangoes on Monday and 238 on Tuesday. How many mangoes are sold in two days?", "363", ["353", "373", "113"], "125 + 238: 100 + 200 = 300, 20 + 30 = 50, 5 + 8 = 13. Then 300 + 50 + 13 = 363."),
            ("A rope 90 cm long is cut into pieces that are each 15 cm long. How many pieces are there?", "6", ["5", "7", "75"], "90 ÷ 15 = 6, because 15 × 6 = 90."),
        ],
    },
}
MATHS_TOPICS = list(MATHS_BANK.keys())

# ----------------------------------------------------------------------
# Game content
# ----------------------------------------------------------------------
# Letter-Sound Match: (letter, correct word, [other words]). First = practice.
LETTER_SOUND_ROUNDS = [
    ("b", "🏀 ball", ["☀️ sun", "🎩 hat"]),
    ("s", "☀️ sun", ["🐟 fish", "🐱 cat"]),
    ("m", "🌙 moon", ["🐶 dog", "🍎 apple"]),
    ("t", "🐯 tiger", ["🦆 duck", "🐷 pig"]),
    ("f", "🐟 fish", ["🌳 tree", "🐱 cat"]),
    ("p", "🐷 pig", ["🌙 moon", "🐶 dog"]),
    ("d", "🐶 dog", ["🐯 tiger", "☀️ sun"]),
    ("c", "🐱 cat", ["🐷 pig", "🏀 ball"]),
]

# Build the Word: first = practice
BUILD_WORDS = ["cat", "dog", "sun", "fish", "bird", "star", "tree"]

# Word-Picture Match: (word, correct emoji, [other emojis]). First = practice.
WORD_PICTURE_ROUNDS = [
    ("apple", "🍎", ["🍌", "🍇", "🍓"]),
    ("cat", "🐱", ["🐶", "🐭", "🐰"]),
    ("sun", "☀️", ["🌙", "⭐", "☁️"]),
    ("book", "📖", ["✏️", "🎒", "📏"]),
    ("fish", "🐟", ["🐦", "🐢", "🐸"]),
    ("house", "🏠", ["🏫", "⛺", "🏰"]),
    ("tree", "🌳", ["🌸", "🌵", "🍄"]),
    ("car", "🚗", ["🚲", "✈️", "🚂"]),
]

# Put the Story in Order: (title, events in the CORRECT order). First = practice.
STORY_ORDER_ROUNDS = [
    ("Growing a plant 🌱", ["Plant the seed in soil", "Water the seed", "A small green plant grows", "The plant makes a flower"]),
    ("Getting ready for school 🎒", ["Wake up", "Brush your teeth", "Eat breakfast", "Walk to school"]),
    ("Pip learns to fly 🐦", ["Pip jumps from the nest", "Pip lands on the leaves", "Pip tries again each day", "Pip flies to the river"]),
    ("Mia in the library 📚", ["Mia sees a blue door", "A magic book floats down", "A butterfly flies out", "Mia borrows the book"]),
    ("A rainy day 🌧️", ["Dark clouds come", "Rain starts to fall", "Puddles form on the ground", "A rainbow appears"]),
]
