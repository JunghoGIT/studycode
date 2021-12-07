# /c/ProgramData/Anaconda3/python
# -*- coding: utf-8 -*-

# Open "alice.txt" and assign the file to "file"

def main():
  with open('data/news_article.txt', encoding="utf-8") as file:
    text = file.read()

  n = 0
  for word in text.split():
    if word in ['오미크론', '코로나']:
      n += 1

  print('오미크론 및 코로나 단어가 나오는 개수는 {} 이다.'.format(n))


if __name__ == "__main__":
  main()