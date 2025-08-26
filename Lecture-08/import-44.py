import struct

record_fomat = 'i20sif'
record_size = struct.calcsize(record_fomat)

with open("records.bin", "rb") as file:
    file.seek(record_size)

    data = file.read(record_size)

    record = struct.unpack(record_fomat, data)

    record = (record[0], record[1].decode().strip('\x00'), record[2], record[3])

    print(f"ID: {record[0]} Name: {record[1]} Age: {record[2]} GPA: {record[3]}")
