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
# Maths learning cards: short notes, simple steps and worked examples
# ----------------------------------------------------------------------
MATHS_LEARNING_CARDS = {
    "Counting and number recognition": {
        "idea": "Numbers tell us how many things there are. Count one object at a time.",
        "remember": ["Say the number names in order.", "Tens are groups of 10. Ones are single units.", "When comparing numbers, look at the tens first, then the ones."],
        "steps": ["Point to the first object.", "Say 1, then move to the next object.", "Stop when every object has been counted."],
        "example": "For 34, there are 3 tens and 4 ones. 30 + 4 = 34."
    },
    "Addition and subtraction": {
        "idea": "Addition joins groups. Subtraction takes away or finds the difference.",
        "remember": ["Addition sign: +", "Subtraction sign: −", "You can check subtraction by adding the answer back."],
        "steps": ["For addition, start with the larger number and count on.", "For subtraction, count back or find the gap.", "For larger numbers, add or subtract tens and ones separately."],
        "example": "36 + 12: first 36 + 10 = 46. Then 46 + 2 = 48."
    },
    "Multiplication and division": {
        "idea": "Multiplication is equal groups. Division shares into equal groups.",
        "remember": ["3 × 4 means 3 groups of 4.", "Division is the opposite of multiplication.", "Skip-counting can help with times tables."],
        "steps": ["Draw equal groups or use objects.", "For multiplication, add the equal groups.", "For division, share the objects equally."],
        "example": "4 × 3 = 3 + 3 + 3 + 3 = 12. So 12 ÷ 4 = 3."
    },
    "Fractions": {
        "idea": "A fraction shows equal parts of a whole.",
        "remember": ["The top number is the numerator: parts we have.", "The bottom number is the denominator: equal parts in total.", "The parts must be equal in size."],
        "steps": ["Count the total equal parts.", "Count how many parts are selected.", "Write selected parts on top and total parts below."],
        "example": "If a shape has 4 equal parts and 1 is shaded, the fraction is 1/4."
    },
    "Shapes and patterns": {
        "idea": "Shapes have features. Patterns repeat or follow a rule.",
        "remember": ["A triangle has 3 sides.", "A square has 4 equal sides.", "Look for what changes and what stays the same in a pattern."],
        "steps": ["Look at the shapes or numbers.", "Compare one item with the next.", "Say the rule, then use it to find what comes next."],
        "example": "2, 4, 6, 8: add 2 each time, so the next number is 10."
    },
    "Simple word problems": {
        "idea": "A word problem tells a small story using numbers. Work out what the question is asking.",
        "remember": ["Altogether or in total may mean addition.", "Left or remaining may mean subtraction.", "Equal groups may mean multiplication or division. Read the whole question."],
        "steps": ["Read the problem slowly.", "Underline the numbers and the question.", "Choose an operation, solve it and check whether the answer makes sense."],
        "example": "There are 3 bags with 5 marbles each. Equal groups: 3 × 5 = 15 marbles."
    },
}


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
