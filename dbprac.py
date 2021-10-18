from pymongo import MongoClient #pymongo를 쓰겠습니다.
client = MongoClient('localhost', 27017) #내 컴퓨터에서 돌아가고있는 MongoDB에 접속할것입니다.
db = client.dbsparta #dbsparta라는 이름의 데이터베이스에 접속할겁니다. 없으면 해당 db를 만듭니다.

# 코딩 시작
#insert / find / update / delete

# 저장 - 예시
doc = {'name':'bobby','age':21}
db.users.insert_one(doc)

# 한 개 찾기 - 예시
user = db.users.find_one({'name':'bobby'})

# 여러개 찾기 - 예시 ( _id 값은 제외하고 출력)
same_ages = list(db.users.find({'age':21},{'_id':False}))

# 바꾸기 - 예시
db.users.update_one({'name':'bobby'},{'$set':{'age':19}})

# 지우기 - 예시
db.users.delete_one({'name':'bobby'})