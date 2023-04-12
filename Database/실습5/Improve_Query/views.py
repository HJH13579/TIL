from django.shortcuts import render
from django.db import connection
from django.db import reset_queries

from .models import PetSitter, Pet

# Create your views here.
import random
import time

# shell로 create_petsitter 실행
# 그 후 get_pet_data 실행
# 다만, 함수를 바꿔서 실행할때마다 shell을 껐다 다시 실행

def create_petsitter():
    with open('names', encoding='utf-8') as f:
        for line in f.readlines():
            pet_sitter = PetSitter.objects.create(
                first_name=line.split(' ')[0],
                last_name=line.split(' ')[1],
                age=random.randint(1, 80)
            )

            Pet.objects.create(
                name=line,
                pet_sitter=pet_sitter
            )

def get_sql_queries(origin_func):
    def wrapper(*args, **kwargs):
        reset_queries()
        start_time = time.time()

        origin_func(*args, **kwargs)

        query_info = connection.queries
        for query in query_info:
            print(query['sql'])
            pass
        print(f'total time: {time.time() - start_time}')
        print(len(query_info))
    return wrapper



@get_sql_queries
def get_pet_data():

    pets = Pet.objects.all()
    # pets = pets.select_related('pet_sitter')
    # pet_sitters = PetSitter.objects.prefetch_related('pet_set')
    for pet in pets:
        print(f"{pet.name} | 집사 {pet.pet_sitter.first_name}")
