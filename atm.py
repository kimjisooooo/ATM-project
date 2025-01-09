#입력 검증 및 에러 처리 추가
#잘못된 입력 값(숫자가 아닌 값, 음수 값 등)
#유효하지 않은 메뉴 선택 시 경고 메세지 또는 사용방법 재안내

receipts = []
balance = 3000 #현재 잔액을 보여주세요

while True:
    print()
    num = input("사용하실 기능을 선택해주세요 (1:입금, 2:출금, 3:영수증보기, 4:종료)")
    if num == '4':
        break
    if num == '1':
        deposit_amount = input("입금할 금액을 입력해주세요 : ")
        if deposit_amount.isdigit() and int(deposit_amount) > 0:
            balance = balance + int(deposit_amount)
            receipts.append(("입금", deposit_amount, balance))
            print(f"입금하신 금액은 {deposit_amount}원 이고 현재 잔액은 {balance}원 입니다.")
        else:
            print("입금한 금액을 숫자 형태와 음수가 아닌 값을 입력해주세요.")

    if num == '2':
        withdraw_amonut = int(input("출금할 금액을 입력해주세요 : "))
        withdraw_amonut = min(balance, withdraw_amonut)
        balance -= withdraw_amonut 
        receipts.append(("출금", withdraw_amonut, balance))
        print(f"출금하신 금액은 {withdraw_amonut}원 이고 현재 잔액은 {balance}원 입니다.")

    if num == '3':
        if receipts:
            print("\n=======영수증 목록=======")
            # idx = 1
            # for action, amount, current_balance in receipts:
            #     print(f"{idx}. {action}: {amount}원\n   잔액: {current_balance}원\n")
            #     idx += 1
            for i in receipts:
                print(f"{i[0]}: {i[1]} | 잔액 : {i[2]}원")
        else:
            print("\n내역이 없습니다.")


print(f"서비스를 종료합니다. 현재 잔액은 {balance}원 입니다.")