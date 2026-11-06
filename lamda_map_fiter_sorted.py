#learn lamda
future_age = lambda age: age + 5

print(future_age(26))

#boolean
is_adult = lambda age: age>=18

print(is_adult(26))
print(is_adult(15))

# learn processing data
# map proses all of item
temperatures = [36.5, 38.5, 37.2, 39.5]

result = list(map(lambda temp: temp + 1, temperatures))

print(result)

# filter chose item base on condition
fever = list(filter(lambda temp: temp >= 37.5, temperatures))

print(fever)


# sorted used for shorte the data
ages = [26, 17, 32, 19]

# lower to higher
result_ages = sorted(ages)
# higher to lower
result_ages_hl = sorted(ages, reverse=True)

print(result_ages)
print(result_ages_hl)