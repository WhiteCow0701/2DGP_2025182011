# 게임월드 리스트 초기화
# world = [] # 객체들의 리스트, 빈 리스트

world = [[],[],[]] # 객체들의 리스트, 빈 리스트


# 객체들을 게임월드에 추가하는 함수
def add_object(o, depth = 0): # depth = 0 이면 기본적으로 첫 번째 레이어에 추가
    world[depth].append(o)


def remove_object(o):
    for layer in world: # 모든 layer를 순회하면서 객체를 제거
        if o in layer:  # 객체가 해당 레이어에 존재하면 제거
            layer.remove(o)
            return # 제거 후 함수 종료
        
    

# 게임 로직
def update():
    for layer in world: # 모든 레이어를 순회하면서 업데이트
        for o in layer[:]:
            o.update()
            if getattr(o, 'is_out_of_bounds', False):
                layer.remove(o)


# 게임 월드 렌더링
def render():
    for layer in world: # 모든 레이어를 순회하면서 렌더링
        for o in layer:
            o.draw()
