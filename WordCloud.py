from wordcloud import WordCloud
import matplotlib.pyplot as plt

text = "Python is an amazing programming language for data science and artificial intelligence."

wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)

plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title('Word Cloud')
plt.show()
