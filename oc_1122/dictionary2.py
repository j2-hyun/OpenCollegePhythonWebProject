menu={'라면':4000,'만두':3500,'보쌈':28000}
# print(menu)
#
# a=input("메뉴를 입력하세요:")
# print(a)

candidate=input("메뉴를 입력하세요 :")
is_candidate_exist=candidate in menu
if candidate in menu == True:
    gagyuk = menu[candidate]
    print(candidate+"는 "+str(gagyuk)+"원입니다")
else:
    print(candidate+'란 메뉴는 없습니다')

