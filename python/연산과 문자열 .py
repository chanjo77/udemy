# 예제
# 성인이 되어서 취직한 친구들과 1년중 두번은 정기적으로 만나기로 했습니다.

# 조건 1 랜덤으로 뽑아야합니다.
# 조건 2 하반기(7 ~ 12)와 상반기(1 ~ 6)에 한번씩 만나야합니다.

# 출력문 : 정기모임은 상반기 X월 하반기 X월에 진행합니다.

# 조건 1
from random import *

# 조건 2
day1 = randrange(1,7)
day2 = randrange(7,13)

# 출력문
print ("정기 모임은 상반기" + str(day1) + "월 하반기 " + str(day2) + "월에 진행합니다." )


#출력값
# 정기 모임은 상반기4월 하반기 12월에 진행합니다.