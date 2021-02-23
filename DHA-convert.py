# Decimal > Hex > ASCII converter.
# by MikeTheScriptKid.
# I made this for a CTF challenge on THM to decode a flag.

decimal = int(input("Enter your decimal: "))
hex = hex(decimal)[2:]
ascii = bytearray.fromhex(hex).decode()

print("HEX:", hex , "\n" "ASCII:", ascii)
