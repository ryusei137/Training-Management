training = {
    "ベンチプレス": 80,
    "スクワット": 100,
    "デッドリフト": 120
}

name = input("種目名を入力してください")

if name in training:
    print(f"{name}の重量は{training[name]}kgです")
else:
    print("登録されていません")
    weight = int(input("重量を入力してください"))
    training[name]= weight
    print(f"{name}を追加しました")

for exercise in training:
    print(f"{exercise}:{training[exercise]}kg")

print(f"合計重量は{sum(training.values())}kg")
print(f"最大重量は{max(training.values())}kg")
print(f"最小重量は{min(training.values())}kg")
print(f"種目数は{len(training)}個")

max_weight=max(training.values())

for exercise in training :
    if training[exercise]== max_weight :
        print(f"最大重量の種目は{exercise}です")


print(f"平均重量は{sum(training.values())/len(training)}kgです")

delete= input("削除する種目を入力してください")

if delete in training :
    del training[delete]
    print(f"種目{delete}は削除されました")
    print("現在の種目一覧")
    for exercise in training:
     print(f"{exercise}:{training[exercise]}")

else:
    print("その種目は登録されていません")

update=input("重量を変更する種目を入力してください")

if update in training:
    new_weight=int(input("新しい重量を入力してください"))
    training[update]= new_weight
    print(f"{update}の重量を{new_weight}kgに変更しました")

else:
    print ("その種目は登録されていません")