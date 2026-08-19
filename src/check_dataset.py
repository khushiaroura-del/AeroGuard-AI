import numpy as np

file_path = "data/raw/DASHlink_full_fourclass_raw_comp.npz"

data = np.load(file_path, allow_pickle=True)

print("Dataset successfully loaded!")
print("\nFiles inside dataset:")

for name in data.files:
    print(name)

    value = data[name]

    print("Shape:", value.shape)
    print("Data type:", value.dtype)
    print()