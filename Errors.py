
for x in range (-15,15):
    try:
        print(30/x)
        print("значения х ", x)
        print(type (x))
        print("15" + x)
    except ZeroDivisionError:
        print("Ну ну ну.Не делите на ноль")
        continue
    except TypeError:
        print("15" + str(x))
        #отлавливать:  , , , 