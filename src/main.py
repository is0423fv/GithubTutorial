# main.py

while True:
    print("数値を入力してください")
    input_num = int(input()) # 入力コマンド

    if input_num == 0:
        print('プログラムを終了します')
        break

    elif input_num == 1:
        print("Eroor")

    elif input_num == 2:
        print("Hello World")

    # -- ここに処理を追加してみよう --
    else:
        print('該当するコマンドがありません')
