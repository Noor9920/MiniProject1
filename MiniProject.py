fo=open("movie.txt","r")
f1=open("rating.txt","r")
s=fo.read()
s1=f1.read()
s1=s1.split("\n")
list_movie=['Movie_id','Movie_name','Genre','year']
list_rating=['Movie_id','Movie_rating']
#print(s1)
list1=[] #An Empty List
list2=[] #A list for storing data of Movies
list3=[] #An Empty List
list4=[] #A list for storing data of Ratings
s=s.split()
#print(s)
for i in range(len(s)):
    list1.append(s[i].split(','))
#print(list1)
for each in range(len(list1)):
    list2.append(dict(zip(list_movie,list1[each])))
#print(list2)

for i in range(len(list1)):
    list2[i]['Genre']=list1[i][2].split('|')
#print(list2)
for i in range(len(s1)):
    list3.append(s1[i].split(','))
#print(list3)
for each in range(len(list3)):
    list4.append({list_rating[i]:float(list3[each][i]) for i in range(len(list_rating))})
#print(list4)
Genre=set()
year=set()
for i in range(len(list2)):
    Genre.update(x for x in list2[i]['Genre'])
#print(Genre)

for i in range(len(list4)):
    year.update(x for x in [list2[i]['year']])
#print(year)

def movie_count_each_genre():
    """This function Counts movie for each Genre"""
    print('Counting the movies for each Genre')
    print()
    count=0
    for each in Genre:
        for i in range(len(list2)):
            if each in list2[i]['Genre']:
                count+=1
        print('The count of movie in',each,'is :',count)
        count=0
    print()
        
def movie_count_for_specific_genre():
    """This Function counts Movies with Rating Greater than 4"""

    print("counting Movies with Rating Greater than 4")
    print()
    count=0
    for each in Genre:
        for i in range(len(list2)):
            if each in list2[i]['Genre']:
                if list4[i]['Movie_rating']>4:
                    count+=1
        print('The count of movie with rating greater than 4 in',each,'is :',count)
        count=0
    print()
    
def movie_count_released_after_2000():
    """This Function counts Movie which were released after year 2000 and had rating
    greater than 3.5"""

    print("counting Movie which were released after year 2000 and had rating greater than 3.5")
    print()
    count=0
    for each in Genre:
        for i in range(len(list2)):
            if int(list2[i]['year'])>2000:
                   if each in list2[i]['Genre']:
                       if list4[i]['Movie_rating']>3.5:
                           count+=1
        print('The count of movie released after 2000 with rating greater than 3.5 in',each,'is :',count)
        count=0
    print()
    
def top_movie_of_each_genre():
    """This Function returns the top movies of each Genre"""

    print('Counting The top Movies of each genre')
    print()
    c=0
    for each in Genre:
        for i in range(len(list2)):
            if each in list2[i]['Genre']:
                if list4[i]['Movie_rating']>c:
                    c=list4[i]['Movie_rating']
                    movie=list2[i]['Movie_name']
        if c>0:
            print("The best",each,"Movie is: ",movie)
            c=0
    print()
def top_movie_in_each_year():
    """This Function returns the Top movies in each year"""

    print('Counting the Top Movies in each year')
    print()
    c=0
    for each in year:
        for i in range(len(list2)):
            if each in list2[i]['year']:
                if list4[i]['Movie_rating']>c:
                    c=list4[i]['Movie_rating']
                    movie=list2[i]['Movie_name']

        if c>0:
            print("Top Movie of Year",each,"was: ",movie)
            c=0
    print()
movie_count_each_genre()
movie_count_for_specific_genre()
movie_count_released_after_2000()
top_movie_of_each_genre()
top_movie_in_each_year()
