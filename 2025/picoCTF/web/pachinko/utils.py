def serializeData(data):
    data = data[:]
    if len(data) % 3 != 0:
        data.extend([1] * (3 - len(data) % 3))
    return [
        {
            "input1": data[i],
            "input2": data[i + 1],
            "output": data[i + 2]
        } for i in range(0, len(data), 3)
    ]


class Encoder:
    def __init__(self):
        self.addrs = []
        self.data = []

    def add(self, addr, data):
        assert addr in range(0, 0x10000) and data in range(0, 0x10000)
        self.addrs.append(addr)
        self.data.append(data)
    def encode(self):
        assert len(self.addrs) == len(self.data)
        word_size = 3 * 3 * 2
        serialized_data = serializeData([x if x != 0 else 1 for x in self.data])
        data_address = 0x1000 + len(self.addrs) * word_size
        d = []
        for i in range(len(self.addrs)):
            if self.data[i] != 0:
                d.append({
                    "input1": (data_address + 2 * i) // 2,
                    "input2": (data_address + 2 * i) // 2,
                    "output": 1
                })
                d.append({
                    "input1": (0x1000 + word_size * (i + 1) - 2) // 2,
                    "input2": (0x1000 + word_size * (i + 1) - 2) // 2,
                    "output": (0x1000 + word_size * (i + 1) - 2) //2
                })
                d.append({
                    "input1": 1,
                    "input2": 1,
                    "output": ~((self.addrs[i] - 0x2000) // 2)
                })
            else:
                d.append({
                    "input1": 100,
                    "input2": 100,
                    "output": 1
                })
                d.append({
                    "input1": (0x1000 + word_size * (i + 1) - 2) // 2,
                    "input2": (0x1000 + word_size * (i + 1) - 2) // 2,
                    "output": (0x1000 + word_size * (i + 1) - 2) // 2
                })
                d.append({
                    "input1": 1,
                    "input2": 1,
                    "output": ~((self.addrs[i] - 0x2000) //2)
                })
        d.extend(serialized_data)
        return {"circuit": d}
