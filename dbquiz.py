from pymongo import MongoClient #pymongo를 쓰겠습니다.
client = MongoClient('localhost', 27017) #내 컴퓨터에서 돌아가고있는 MongoDB에 접속할것입니다.
db = client.dbsparta #dbsparta라는 이름의 데이터베이스에 접속할겁니다. 없으면 해당 db를 만듭니다.

movie = db.movies.find_one({'title':'매트릭스'})
met = movie['star']
print(met)

# 여러개 찾기 - 예시 ( _id 값은 제외하고 출력)
same_movie = list(db.movies.find({'star':met},{'_id':False}))
for each_movie in same_movie:
    print(each_movie['title'])

# 바꾸기 - 예시
db.movies.update_one({'title':'매트릭스'},{'$set':{'star':'0'}})