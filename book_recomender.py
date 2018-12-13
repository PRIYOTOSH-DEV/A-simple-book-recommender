import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import warnings
warnings.simplefilter(action='ignore')

books = pd.read_csv('BX-Books.csv', sep=';', error_bad_lines=False, encoding="latin-1")
books.columns = ['ISBN', 'bookTitle', 'bookAuthor', 'yearOfPublication', 'publisher', 'imageUrlS', 'imageUrlM', 'imageUrlL']
users = pd.read_csv('BX-Users.csv', sep=';', error_bad_lines=False, encoding="latin-1")
users.columns = ['userID', 'Location', 'Age']
ratings = pd.read_csv('BX-Book-Ratings.csv', sep=';', error_bad_lines=False, encoding="latin-1")
ratings.columns = ['userID', 'ISBN', 'bookRating']


print(ratings.shape)
print(list(ratings.columns))

ratings.head(10)

plt.rc("font",size=15)
ratings.bookRating.value_counts(sort=False).plot(kind='bar')
plt.title('Rating Distribution\n')
plt.xlabel('Rating')
plt.ylabel('count')
plt.savefig('ratings.png',bbox_inches='tight')
plt.show()

print(books.shape)
print(list(books.columns))

books.head()

print(users.shape)
print(list(users.columns))

users.head()

users.Age.hist(bins=[0,10,20,30,40,50,100])
plt.title('Age Distribution\n')
plt.xlabel('Age')
plt.ylabel('Count')
plt.savefig('age.png',bbox_inches='tight')
plt.show()


rating_count=pd.DataFrame(ratings.groupby('ISBN')['bookRating'].count())
rating_count.sort_values('bookRating',ascending=False).head()

most_rated_books=pd.DataFrame(['0971880107','0316666343','038550420',
'0060928336','0312195516'],index=np.arange(5),columns=['ISBN'])
most_rated_books_summary=pd.merge(most_rated_books,books,on='ISBN')
most_rated_books_summary

