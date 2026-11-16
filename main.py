# 분자 구조 후보 생성기 (고등학교 교육용)

# 1. 원소별 기본 원자가 설정
valence = {
    "B": 3,
    "C": 4,
    "N": 3,
    "O": 2,
    "F": 1,
    "Si": 4,
    "Cl": 1,
    "Br": 1,
    "I": 1
}

# 2. 분자식 입력 및 분석
def parse_formula(formula):
    counts = {}
    i = 0

    while i < len(formula):
        if not formula[i].isupper():
            return None

        element = formula[i]
        i += 1

        if i < len(formula) and formula[i].islower():
            element += formula[i]
            i += 1

        if element != "H" and element not in valence:
            return None

        number = ""

        while i < len(formula) and formula[i].isdigit():
            number += formula[i]
            i += 1

        if number == "":
            number = 1
        else:
            number = int(number)

        if number <= 0:
            return None

        counts[element] = counts.get(element, 0) + number

    return counts


# 3. 원자에 붙어 있는 수소 표시
def atom_text(element, hydrogen):
    if hydrogen == 0:
        return element

    return element + "H" + str(hydrogen)


# 4. 분자 구조 후보 탐색
def find_structures(counts):

    elements = []

    for element in counts:
        if element != "H":
            for i in range(counts[element]):
                elements.append(element)

    n = len(elements)

    if n == 0:
        print("수소 이외의 원자가 필요합니다.")
        return

    target_h = counts.get("H", 0)

    # 원자 사이의 결합 차수
    bonds = [1] * (n - 1)

    bond_symbols = {
        1: "-",
        2: "=",
        3: "#"
    }

    result_count = 0

    # 가능한 결합 구조 탐색
    while True:

        hydrogen = []
        used = [0] * n

        # 각 원자가 사용한 결합 수 계산
        for i in range(n - 1):
            used[i] += bonds[i]
            used[i + 1] += bonds[i]

        valid = True

        # 원자별 남은 원자가 계산
        for i in range(n):

            element = elements[i]
            remaining = valence[element] - used[i]

            if remaining < 0:
                valid = False
                break

            hydrogen.append(remaining)

        # 분자식의 수소 개수와 비교
        if valid and sum(hydrogen) == target_h:

            result_count += 1

            structure = atom_text(elements[0], hydrogen[0])

            for i in range(n - 1):
                structure += bond_symbols[bonds[i]]
                structure += atom_text(elements[i + 1], hydrogen[i + 1])

            print("후보", result_count, ":", structure)

        # 결합 차수를 다음 경우로 변경
        position = n - 2

        while position >= 0 and bonds[position] == 3:
            bonds[position] = 1
            position -= 1

        if position < 0:
            break

        bonds[position] += 1

    print("\n총 구조 후보 수:", result_count)


# 5. 프로그램 실행
print("=" * 40)
print("분자 구조 후보 생성기")
print("=" * 40)

print("예시: CH4, H2O, C2H6O, C3H6")

formula = input("분자식을 입력하세요: ")

counts = parse_formula(formula)

if counts is None:
    print("잘못된 분자식입니다.")
else:
    print("\n입력한 분자식:", formula)
    print("\n[구조 후보]")

    find_structures(counts)

print("\n탐색이 완료되었습니다.")















