# Exercicio 1
def duplicatas(arr):
    n = len(arr)
    duplicatas = []
    for i in range(n):
        for j in range(i+1, n):
            if arr[i] == arr[j]:
                duplicatas.append(arr[j])
    print(f'The duplicates: {duplicatas}')

if __name__ == '__main__':
    duplicatas([1,2,3,4,5,5,6,6,7])


# Exercício 2
def frequente(arr):
    n = len(arr)
    max_count = 0
    frequent_element = None
    for i in range(n):
        count = 1
        for j in range(i+1, n):
            if arr[i] == arr[j]:
                count += 1
        if count > max_count:
            max_count = count
            frequent_element = arr[i]

    print("Count:", max_count)
    print("Most Frequent Element:", frequent_element)

if __name__ == '__main__':
    frequente([1,2,3,4,5,5,5,6,6,6,6,7])
