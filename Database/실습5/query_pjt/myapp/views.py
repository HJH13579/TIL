from django.shortcuts import render
from .models import Pet, PetSitter
from django.db import connection, reset_queries

# decorator 만들기
def get_sql_queries(origin_func):
    def wrapper(*args, **kwargs):
        reset_queries()

        origin_func(*args, **kwargs)

        query_info = connection.queries
        for query in query_info:
            print(query['sql'])

    return wrapper

# def get_pet_data():
#     reset_queries()

#     pets = Pet.objects.all()
#     for pet in pets:
#         print(f'{pet.name} | {pet.pet_sitter.first_name}')

#     query_info = connection.queries
#     for query in query_info:
#         print(query['sql'])

@get_sql_queries
def get_pet_data():
    # 이러면 DB 요청 n번
    # pets = Pet.objects.all()

    # # Lazy Loading
    # pets = Pet.objects.all()
    # pets = pets.select_related('pet_sitter')
    # pets = pets.filter(name='taeho')
    # pets = pets.filter(age__gt=20) # >=20

    # pet의 입장에서 sitter은 한명이기에 .select_related 사용
    # 이러면 DB 요청 1번
    pets = Pet.objects.all().select_related('pet_sitter')
    for pet in pets:
        print(f'{pet.name} | {pet.pet_sitter.first_name}')


# article = Article.objects.get(pk=pk).prefech_related('comment_set')
# comments = article.comment_set.all()

# article = Article.objects.prefech_related('comment_set').get(pk=pk)
# comments = article.comment_set.all()