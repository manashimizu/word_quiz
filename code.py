import random
wordList = {
  "講堂": "auditorium",
  "空の": "empty",
  "家具": "furniture",
  "マンション": "apartment",
  "家賃": "rent",
  "に腹を立てる": "resent",
  "強引な": "aggressive",
  "販売員": "salesman",
  "署名する": "sign",
  "契約": "contract",
  "要因": "factor",
  "投資する": "invest",
  "株": "stock",
  "輸入する": "import",
  "様々な": "various",
  "加工していない": "raw",
  "を輸出する": "export",
  "を製造する": "manufacture",
  "商品": "goods",
  "経済の": "economic",
  "発展": "development",
  "を見捨てる": "abandon",
  "伝統的な": "traditional",
  "価値観": "value",
  "いまだかつてない": "unprecedented",
  "危機": "crisis",
  "目的": "purpose",
  "規制": "regulation",
  "を保護する": "protect",
  "国内の": "domestic",
  "産業": "industry",
  "に着手する": "undertake",
  "大幅な": "sweeping",
  "規制緩和": "deregulation"
}

qCount = int(input('How many questions do you want to study? : '))
now = 0
score = 0

while now < qCount:
  now += 1
  randomWord = random.choice(list(wordList))
  print(randomWord)
  inputWord = input('Enter the meaning of this word. : ')

  if inputWord == wordList[randomWord]:
    print('Correct!')
    score += 1
  else:
    print(f'Wrong. The answer is "{wordList[randomWord]}".')

print(f'Your score is {score}/{qCount}.')