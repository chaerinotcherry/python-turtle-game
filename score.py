import turtle

# Score 클래스 정의
class Score:
    def __init__(self):
        self.score = 0  # 점수 초기화
        self.pen = turtle.Turtle()  # 점수를 표시할 turtle 객체
        self.pen.hideturtle()  # 점수를 표시하는 터틀을 숨깁니다.
        self.pen.penup()  # 펜을 들고
        self.pen.goto(-250, 250)  # 화면 좌측 상단에 점수 표시 위치 설정
        self.update_score_display()  # 처음 점수를 화면에 표시

    # 점수를 업데이트하고 화면에 표시하는 함수
    def update_score_display(self):
        self.pen.clear()  # 이전에 그려진 점수 지우기
        self.pen.write(f"Score: {self.score}", font=("Arial", 10, "normal"))

    # 점수를 증가시키는 함수
    def increase_score(self, points):
        self.score += points  # 점수 증가
        self.update_score_display()  # 점수 업데이트

    # 점수를 감소시키는 함수 (예: 실패시)
    def decrease_score(self, points):
        self.score -= points  # 점수 감소
        self.update_score_display()  # 점수 업데이트
        
    def get_score(self):
        return self.score