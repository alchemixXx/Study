question2 = '''Зимой и летом одним цветом'''
anser2 = "йолка"
ready = input("Ты готов ? (Да/Нет)")
if ready == "Да":
    print("Хорошо загадка на 1 бал")
    print("---------------")
    print(question2)
    print("---------------")
    print("Вы можите возпользиваться подсказкой")
    print("чтобы активиривать подсказку напишыте 'подсказка")
    anser2= input ()
    if anser2.lower() == "подсказка":
        print("Оно в сосновом лесу")
        anser2 = input ()
        if anser2.lower == anser2:
            print("У вас пол бала")
            counter = counter + 0.5
        else: 
            print("Сори")
    elif enswer == ("йолка"):
        print("У вас бал")
        counter = counter + 1
    else: 
        print("не правильно")
        print("У вас 0 балов")
print("У вас "+str(counter)+"балов")