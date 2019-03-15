class GLIBC:
    def __init__(self, seed=1):
        self.seed = seed
        self.states = [seed]

        for i in range(1, 31):
            self.states.append((16807 * self.states[i - 1]) % (2 ** 31 - 1))
        for i in range(31, 34):
            self.states.append(self.states[i - 31])
        for i in range(34, 345):
            self.states.append((self.states[i - 31] + self.states[i - 3]) % 2 ** 32)

    def random(self):
        o = int(str(bin(self.states[-1])[:-1]), 2)
        self.states.append((self.states[-31] + self.states[- 3]) % 2 ** 32)
        return o


##CRACKER
def predict_new_value(numbers):
    if len(numbers) < 31:
        print('ERROR: za mało liczb!')
        exit(-1)
    return ((numbers[-31] + numbers[-3]) % 2 ** 32, (numbers[-31] + numbers[-3] + 1) % 2 ** 32)


seed = 1

glibc = GLIBC(seed)
numbers = []
for i in range(10000):
    numbers.append(glibc.random())
if_predicted = []
for k in range(10000):
    predicted_numbers = predict_new_value(numbers)
    new_number = glibc.random()
    numbers.append(new_number)
    if_predicted.append(new_number in predicted_numbers)
prob_of_win = sum(if_predicted)/len(if_predicted)
print('Prawdopodobieństwo poprawnego zgadnięcia kolejnej liczby wynosi: ', prob_of_win)
print('Czy prawdopodobieństwo jest znacząco większe od 0.5: ', prob_of_win > (1/2 + 1/2**10))
# for j in range(10):
#     predicted_numbers = predict_new_value(numbers)
#     print('Podejrzewamy, że zostanie wylosowana jedna z tych dwóch liczb ', predicted_numbers)
#     new_number = glibc.random()
#     numbers.append(new_number)
#     print('GLIBC wylosował: ', new_number)
#     print('Czy cracker zgadł liczbę? ', new_number in predicted_numbers)