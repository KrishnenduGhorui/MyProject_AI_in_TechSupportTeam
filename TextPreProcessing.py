import re
import nltk
nltk.download('all')
from nltk.stem import WordNetLemmatizer
lemmatizer=WordNetLemmatizer()
from nltk.corpus import stopwords 



def textclean(Text):
  text=Text.lower()
  text=re.sub('[\r\n]',' ',text)
  text=re.sub('[^0-9a-zA-Z]',' ',text)
  text=text.split()
  text=[lemmatizer.lemmatize(word) for word in text if word not in set (stopwords.words('english'))]
  text=' '.join(text)
  return text