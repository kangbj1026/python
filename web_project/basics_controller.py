from flask import Blueprint, jsonify, request
from response_utils import api_response # api_response 함수 임포트

basics_bp = Blueprint('basics', __name__, url_prefix='/api/basics')

@basics_bp.route('/variables', methods=['GET'])
def get_variables_and_types():
    name = "Alice"
    age = 30
    height = 175.5
    is_student = True
    
    data = {
        "name": name,
        "age": age,
        "height": height,
        "is_student": is_student,
        "types": {
            "name_type": str(type(name)),
            "age_type": str(type(age))
        }
    }
    return api_response(data=data, message="Variables and types retrieved successfully", status_code=200)

@basics_bp.route('/operators', methods=['GET'])
def get_operators_result():
    a = 10
    b = 3
    
    data = {
        "a": a,
        "b": b,
        "addition": a + b,
        "subtraction": a - b,
        "multiplication": a * b,
        "division": a / b,
        "floor_division": a // b,
        "modulo": a % b,
        "exponentiation": a ** b
    }
    return api_response(data=data, message="Operators result retrieved successfully", status_code=200)

@basics_bp.route('/conditional', methods=['GET'])
def get_conditional_result():
    score = request.args.get('score', type=int, default=85)
    
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    else:
        grade = "C 이하"
        
    data = {"score": score, "grade": grade}
    return api_response(data=data, message="Conditional result retrieved successfully", status_code=200)

@basics_bp.route('/loops', methods=['GET'])
def get_loops_result():
    fruits = ["apple", "banana", "cherry"]
    
    loop_results = {
        "for_loop_fruits": fruits,
        "while_loop_count": []
    }
    
    count = 0
    while count < 5:
        loop_results["while_loop_count"].append(f"카운트: {count}")
        count += 1
        
    return api_response(data=loop_results, message="Loops result retrieved successfully", status_code=200)

@basics_bp.route('/functions', methods=['GET'])
def get_functions_result():
    name = request.args.get('name', type=str, default="Bobs")
    x = request.args.get('x', type=int, default=5)
    y = request.args.get('y', type=int, default=3)

    message = f"안녕하세요, {name}님!"
    
    result_add = x + y
        
    data = {
        "greeting_message": message,
        "addition_result": result_add
    }
    return api_response(data=data, message="Functions result retrieved successfully", status_code=200)

@basics_bp.route('/lists', methods=['GET'])
def get_lists_result():
    my_list = [1, 2, 3, "hello", True]
    
    # 리스트 조작은 API 호출 시마다 초기화되므로, 결과를 반환하는 방식으로 변경
    initial_list = list(my_list) # 원본 복사
    my_list.append(4)
    list_after_append = list(my_list)
    my_list.remove("hello")
    list_after_remove = list(my_list)
    
    data = {
        "initial_list": initial_list,
        "first_element": initial_list[0],
        "list_after_append": list_after_append,
        "list_after_remove": list_after_remove
    }
    return api_response(data=data, message="Lists result retrieved successfully", status_code=200)

@basics_bp.route('/tuples', methods=['GET'])
def get_tuples_result():
    my_tuple = (1, 2, "three")
    
    data = {
        "tuple": my_tuple,
        "first_element": my_tuple[0]
    }
    return api_response(data=data, message="Tuples result retrieved successfully", status_code=200)

@basics_bp.route('/dictionaries', methods=['GET'])
def get_dictionaries_result():
    person = {"name": "Charlie", "age": 25, "city": "Seoul"}
    
    initial_person = dict(person)
    person["age"] = 26
    person_after_age_change = dict(person)
    person["job"] = "Engineer"
    person_after_job_add = dict(person)
    
    data = {
        "initial_dictionary": initial_person,
        "name": initial_person['name'],
        "dictionary_after_age_change": person_after_age_change,
        "dictionary_after_job_add": person_after_job_add
    }
    return api_response(data=data, message="Dictionaries result retrieved successfully", status_code=200)

@basics_bp.route('/sets', methods=['GET'])
def get_sets_result():
    my_set = {1, 2, 3, 2, 1} # 중복 제거
    
    initial_set = list(my_set) # JSON 직렬화를 위해 리스트로 변환
    my_set.add(4)
    set_after_add = list(my_set)
    my_set.remove(1)
    set_after_remove = list(my_set)
    
    data = {
        "initial_set": initial_set,
        "set_after_add": set_after_add,
        "set_after_remove": set_after_remove
    }
    return api_response(data=data, message="Sets result retrieved successfully", status_code=200)