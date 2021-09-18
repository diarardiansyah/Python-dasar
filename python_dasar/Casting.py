# Casting type data integer
print("====INTEGER====")
data_int = 0
print("Data :", data_int, type(data_int))

data_float = float(data_int)
data_str = str(data_int)
data_bool = bool(data_int)
print("Data :", data_float, type(data_float))
print("Data :", data_str, type(data_str))
print("Data :", data_bool, type(data_bool))

# Casting type data string
print("====STRING====")
data_str = "20"
print("Data :", data_str, type(data_str))

data_int = int(data_str) # Untuk mengubah ke integer harus berupa angka
data_float = float(data_str)
data_bool = bool(data_str) # Akan menjadi false jika string kosong
print("Data :", data_int, type(data_int))
print("Data :", data_float, type(data_float))
print("Data :", data_bool, type(data_bool))

# Casting type data float
print("====FLOAT====")
data_float = 12.4
print("Data :", data_float, type(data_float))

data_int = int(data_float)
data_str = str(data_float)
data_bool = bool(data_float)
print("Data :", data_int, type(data_int))
print("Data :", data_str, type(data_str))
print("Data :", data_bool, type(data_bool))

# Casting type data boolean
print("====BOOLEAN====")
data_bool = True
print("Data :", data_bool, type(data_bool))

data_int = int(data_bool)
data_str = str(data_bool)
data_float = float(data_bool)
print("Data :", data_int, type(data_int))
print("Data :", data_str, type(data_str))
print("Data :", data_float, type(data_float))
