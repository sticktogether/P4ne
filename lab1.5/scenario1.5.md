Работа с файлами 
===

###### tags: `Python` `CSR` `Courses`

## Открытие файла
```
f = open('file.txt')
dir(f)
```

## 
* __f.seek(0)__

    пройтись по файлу заново

* __f.readlines()__
    
     считать файл по строкам

* __f.close()__
    
     закрыть файл
* __f.strip()__
    
    форматирование (без пробелов)

## Открытие и автоматическое закрытие файла
```
with open('log.txt') as f:
  for i in f:
    ...
```
## Выбор уникальных значений
```
L = ["test1", "test2", "test1"]
set(L) - множество
L2 = list(set(L)) - список
```

## Выбор строк со значением
```
for current_file in files:
  with open(current_file) as f:
    for line in f:
      if "ip address" in line:
        print(line)
```






___

![Jetnf](https://www.linuxcenter.ru/assets/img/parnters/partner3.png)