# Flask의 Blueprint, jsonify, request 모듈을 임포트합니다.
# Blueprint는 관련된 라우트와 뷰 함수를 그룹화하여 애플리케이션을 모듈화하는 데 사용됩니다.
# jsonify는 파이썬 딕셔너리나 리스트를 JSON 형식의 응답으로 변환합니다.
# request는 클라이언트로부터의 HTTP 요청 데이터를 다루는 데 사용됩니다.
from flask import Blueprint, jsonify, request

# 사용자 정의 데코레이터인 handle_response를 임포트합니다.
# 이 데코레이터는 API 응답을 표준화하고 예외 처리를 담당합니다.
from utils.decorators import handle_response

# 'basics'라는 이름의 Blueprint를 생성합니다.
# 이 Blueprint에 정의된 모든 라우트의 URL은 '/api/basics'로 시작합니다.
basics_bp = Blueprint('basics', __name__, url_prefix='/api/basics')

# 변수와 데이터 타입을 반환하는 API 엔드포인트입니다.
# GET 요청을 처리하며, handle_response 데코레이터를 통해 응답이 처리됩니다.
@basics_bp.route('/variables', methods=['GET'])
@handle_response(message="Variables and types retrieved successfully", status_code=200)
def get_variables_and_types():
	# 다양한 타입의 변수를 선언합니다.
	name = "Alice"
	age = 30
	height = 175.5
	is_student = True
	
	# 변수 값과 각 변수의 타입을 포함하는 딕셔너리를 생성하여 반환합니다.
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
	return data

# 연산자 결과를 반환하는 API 엔드포인트입니다.
# GET 요청을 처리하며, handle_response 데코레이터를 통해 응답이 처리됩니다.
@basics_bp.route('/operators', methods=['GET'])
@handle_response(message="Operators result retrieved successfully", status_code=200)
def get_operators_result():
	# 두 개의 숫자를 정의합니다.
	a = 10
	b = 3
	
	# 다양한 산술 연산의 결과를 포함하는 딕셔너리를 생성하여 반환합니다.
	data = {
		"a": a,
		"b": b,
		"addition": a + b,          # 덧셈
		"subtraction": a - b,       # 뺄셈
		"multiplication": a * b,    # 곱셈
		"division": a / b,          # 나눗셈 (부동 소수점)
		"floor_division": a // b,   # 몫 (정수 나눗셈)
		"modulo": a % b,            # 나머지
		"exponentiation": a ** b    # 거듭제곱
	}
	return data

# 조건문(if-elif-else) 결과를 반환하는 API 엔드포인트입니다.
# GET 요청을 처리하며, handle_response 데코레이터를 통해 응답이 처리됩니다.
@basics_bp.route('/conditional', methods=['GET'])
@handle_response(message="Conditional result retrieved successfully", status_code=200)
def get_conditional_result():
	# 요청 파라미터에서 'score' 값을 가져오거나 기본값 85를 사용합니다.
	score = request.args.get('score', type=int, default=85)
	
	# 점수에 따라 학점을 결정하는 조건문입니다.
	if score >= 90:
		grade = "A"
	elif score >= 80:
		grade = "B"
	else:
		grade = "C 이하"
		
	# 점수와 학점을 포함하는 딕셔너리를 반환합니다.
	data = {"score": score, "grade": grade}
	return data

# 반복문(for, while) 결과를 반환하는 API 엔드포인트입니다.
# GET 요청을 처리하며, handle_response 데코레이터를 통해 응답이 처리됩니다.
@basics_bp.route('/loops', methods=['GET'])
@handle_response(message="Loops result retrieved successfully", status_code=200)
def get_loops_result():
	# 과일 리스트를 정의합니다.
	fruits = ["apple", "banana", "cherry"]
	
	# 반복문 결과를 저장할 딕셔너리를 초기화합니다.
	loop_results = {
		"for_loop_fruits": fruits,  # for 루프는 리스트 자체를 반환
		"while_loop_count": []      # while 루프 결과 저장용 리스트
	}
	
	# while 루프를 사용하여 0부터 4까지 카운트합니다.
	count = 0
	while count < 5:
		loop_results["while_loop_count"].append(f"카운트: {count}")
		count += 1
		
	return loop_results

# 함수 사용 결과를 반환하는 API 엔드포인트입니다.
# GET 요청을 처리하며, handle_response 데코레이터를 통해 응답이 처리됩니다.
@basics_bp.route('/functions', methods=['GET'])
@handle_response(message="Functions result retrieved successfully", status_code=200)
def get_functions_result():
	# 요청 파라미터에서 'name', 'x', 'y' 값을 가져오거나 기본값을 사용합니다.
	name = request.args.get('name', type=str, default="Bobs")
	x = request.args.get('x', type=int, default=5)
	y = request.args.get('y', type=int, default=3)

	# 인사 메시지를 생성합니다.
	message = f"안녕하세요, {name}님!"
	
	# 두 숫자의 덧셈 결과를 계산합니다.
	result_add = x + y
		
	# 인사 메시지와 덧셈 결과를 포함하는 딕셔너리를 반환합니다.
	data = {
		"greeting_message": message,
		"addition_result": result_add
	}
	return data

# 리스트(List) 조작 결과를 반환하는 API 엔드포인트입니다.
# GET 요청을 처리하며, handle_response 데코레이터를 통해 응답이 처리됩니다.
@basics_bp.route('/lists', methods=['GET'])
@handle_response(message="Lists result retrieved successfully", status_code=200)
def get_lists_result():
	# 초기 리스트를 정의합니다.
	my_list = [1, 2, 3, "hello", True]
	
	# 리스트의 초기 상태를 복사합니다.
	initial_list = list(my_list) 
	# 리스트에 요소를 추가합니다.
	my_list.append(4)
	# 추가 후 리스트 상태를 복사합니다.
	list_after_append = list(my_list)
	# 리스트에서 요소를 제거합니다.
	my_list.remove("hello")
	# 제거 후 리스트 상태를 복사합니다.
	list_after_remove = list(my_list)
	
	# 리스트 조작 결과를 포함하는 딕셔너리를 반환합니다.
	data = {
		"initial_list": initial_list,
		"first_element": initial_list[0],
		"list_after_append": list_after_append,
		"list_after_remove": list_after_remove
	}
	return data

# 튜플(Tuple) 사용 결과를 반환하는 API 엔드포인트입니다.
# GET 요청을 처리하며, handle_response 데코레이터를 통해 응답이 처리됩니다.
@basics_bp.route('/tuples', methods=['GET'])
@handle_response(message="Tuples result retrieved successfully", status_code=200)
def get_tuples_result():
	# 튜플을 정의합니다. 튜플은 한 번 생성되면 변경할 수 없습니다.
	my_tuple = (1, 2, "three")
	
	# 튜플과 첫 번째 요소를 포함하는 딕셔너리를 반환합니다.
	data = {
		"tuple": my_tuple,
		"first_element": my_tuple[0]
	}
	return data

# 딕셔너리(Dictionary) 조작 결과를 반환하는 API 엔드포인트입니다.
# GET 요청을 처리하며, handle_response 데코레이터를 통해 응답이 처리됩니다.
@basics_bp.route('/dictionaries', methods=['GET'])
@handle_response(message="Dictionaries result retrieved successfully", status_code=200)
def get_dictionaries_result():
	# 초기 딕셔너리를 정의합니다.
	person = {"name": "Charlie", "age": 25, "city": "Seoul"}
	
	# 딕셔너리의 초기 상태를 복사합니다.
	initial_person = dict(person)
	# 딕셔너리의 값을 변경합니다.
	person["age"] = 26
	# 변경 후 딕셔너리 상태를 복사합니다.
	person_after_age_change = dict(person)
	# 딕셔너리에 새 키-값 쌍을 추가합니다.
	person["job"] = "Engineer"
	# 추가 후 딕셔너리 상태를 복사합니다.
	person_after_job_add = dict(person)
	
	# 딕셔너리 조작 결과를 포함하는 딕셔너리를 반환합니다.
	data = {
		"initial_dictionary": initial_person,
		"name": initial_person['name'],
		"dictionary_after_age_change": person_after_age_change,
		"dictionary_after_job_add": person_after_job_add
	}
	return data

# 세트(Set) 조작 결과를 반환하는 API 엔드포인트입니다.
# GET 요청을 처리하며, handle_response 데코레이터를 통해 응답이 처리됩니다.
@basics_bp.route('/sets', methods=['GET'])
@handle_response(message="Sets result retrieved successfully", status_code=200)
def get_sets_result():
	# 초기 세트를 정의합니다. 세트는 중복된 요소를 허용하지 않습니다.
	my_set = {1, 2, 3, 2, 1} 
	
	# 세트의 초기 상태를 리스트로 변환하여 복사합니다 (JSON 직렬화를 위함).
	initial_set = list(my_set) 
	# 세트에 요소를 추가합니다.
	my_set.add(4)
	# 추가 후 세트 상태를 리스트로 변환하여 복사합니다.
	set_after_add = list(my_set)
	# 세트에서 요소를 제거합니다.
	my_set.remove(1)
	# 제거 후 세트 상태를 리스트로 변환하여 복사합니다.
	set_after_remove = list(my_set)
	
	# 세트 조작 결과를 포함하는 딕셔너리를 반환합니다.
	data = {
		"initial_set": initial_set,
		"set_after_add": set_after_add,
		"set_after_remove": set_after_remove
	}
	return data
