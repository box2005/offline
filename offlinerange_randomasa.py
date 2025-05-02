import random
import hashlib
import base58
import threading
import bitcoin
import ecdsa
from ecdsa import SigningKey, SECP256k1
import requests
import time
import os
from itertools import islice
import secrets
from Crypto.Random.random import randrange
from Crypto.Random import get_random_bytes
import sys
import binascii
import secret
import subprocess
from datetime import datetime
now = datetime.now()

# Format as string

  # Output: 2023-03-15 14:30:45


#20030027752
#200030027895
#577654
#custome = '223456789ab0c1deff'
custome = '12345abc67890def135790246812345abc67890def1357902468'
awalan = "1"
#custome = '0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef'
awal = 1
#10000000000000001000000000000000000000000000000000000000
#96504221359394147265961430809081309606056705059246204376003859348971987197952 #10000000000000000000000
akhir = 9000000
total = awal+akhir
x = 10
turu = 0
formatted = now.strftime("%Y-%m-%d %H:%M:%S")
print(f"mulai jam : {formatted}")
print(f"awalan 2digit : {awalan}")
print(f"mulai dari : {awal}")
print(f"berakhir di : {total}")
print(f"worker : {x}")
print(f"delay: {turu}")

length_of_string = 2
length_of_string2 = 3
#sample_str = "cdef0123456789abcdef0123456789abcdef0123456789abcdef0123456789ab"
sample_str = "9876054321fedcba"

# k is an argument which will set the length


def convert_and_print(hex_keys):
    """Convert hex keys to WIF and print the results.""" #19vkiEajfhuZ8bs8Zu2jgmC6oqZbWqhxhG
    for private_key in hex_keys:

        #print(generate_random_hex(64))
        #private_key= generate_256bit_hex_max_900()
        #private_key=generate_256bit_hex_in_range()
        #private_key=new_generate_hex_in_specific_range()  #puzzle69
        #private_key=generate_bitcoin_private_key_2010()
        #result = subprocess.run(['openssl', 'rand', '-hex', '32'], capture_output=True, text=True)
        #private_key = result.stdout.strip()
        #private_key = ''.join(secrets.choice(custome) for _ in range(64))
        #private_key1 = ''.join(random.choice(custome) for _ in range(2))
        #private_key2 = ''.join(random.choice(custome) for _ in range(62))
        #private_key = private_key1+private_key2
        gen1 = ''.join(random.choices(sample_str, k = length_of_string))
        gen2 = ''.join(random.choices(sample_str, k = length_of_string))
        gen3 = ''.join(random.choices(sample_str, k = length_of_string))
        gen4 = ''.join(random.choices(sample_str, k = length_of_string))
        gen5 = ''.join(random.choices(sample_str, k = length_of_string))
        gen6 = ''.join(random.choices(sample_str, k = length_of_string))
        gen7 = ''.join(random.choices(sample_str, k = length_of_string))
        gen8 = ''.join(random.choices(sample_str, k = length_of_string2))

        #generated_string = ''.join(random.sample(sample_str, k = length_of_string))
        #private_key =   awalan + generated_string # + 'e'
        #private_key =   awalan + gen1 + gen2 + gen3 + gen4 + gen5 + gen6 + gen7 + gen8 # + 'e'
        private_key =   awalan + gen8 + gen2 + gen3 + gen4 + gen5 + gen6 + gen7 + gen1
        #+ gen3 + gen4 + gen5 + gen6 + gen7 + gen8 # + 'e'

        #private_key=gen_pvkey()
        #private_key=generate_bitcoin_private_key_2010()
        #secure_random = secrets.randbelow(79883506477280744916321471659589023934353523876312879740933983379498773809001) -1234567890  # 1-100 inclusive
        #secure_random = secrets.randbelow(115792089237316195423570985008687907852837564279074904382605163141518161494336) - 1123  # 1-100 inclusive
        #secure_random = secrets.randbelow(590295810358705651711) -1 # 1-100 inclusive
        #private_key = decimal_to_hex_recursive(secure_random)
        #p = len(private_key)
        #if p < 64 :
        #    private_key = "B" + private_key
        #private_key = binascii.hexlify(os.urandom(32)).decode()
        compressed_address, uncompressed_address, wif = generate_bitcoin_address(private_key)
        #uncompressed_address, wif = generate_bitcoin_address(private_key)


        #compressed_address = "1LruNZjwamWJXThX2Y8C2d47QqhAkkc5os"
        #addresses = compressed_address  #1LruNZjwamWJXThX2Y8C2d47QqhAkkc5os
        #balances, hist_balance = get_balances(addresses)
        #compressed_balance = balances #.get(compressed_address, 0)
        #hist_balance_compres = hist_balance

        #uncompressed_address = "1LruNZjwamWJXThX2Y8C2d47QqhAkkc5os"
        #uncompressed_address #1LruNZjwamWJXThX2Y8C2d47QqhAkkc5os
        #balances, hist_balance = get_balances(addresses)
        #uncompressed_balance = balances #.get(uncompressed_address, 0)
        #hist_balance_uncompres = hist_balance

        #print(hist_balance_compres/100000000)
        #print(hist_balance_uncompres/100000000)

        print(f"hitung: {private_key}")
        #print(f"Hex {private_key} | {compressed_address} || {uncompressed_address}")
        #print(f"Hex {private_key} || {uncompressed_address}")


        if compressed_address == "19vkiEajfhuZ8bs8Zu2jgmC6oqZbWqhxhG":
            with open('foundnjajaloffline.txt', 'a') as f:
                f.write(f'{private_key} | Compressed Address: {compressed_address} \n')
        if uncompressed_address == "19vkiEajfhuZ8bs8Zu2jgmC6oqZbWqhxhG":
            with open('foundnjajaloffline.txt', 'a') as f:
                f.write(f'{private_key} | Uncompressed Address: {uncompressed_address} \n')

        #time.sleep(0)
        #wif_key = hex_to_wif(hex_key)
        #public_key = bitcoin.privtopub(wif_key)
        #btc = bitcoin.pubtoaddr(public_key)
        #print(f"Hex {private_key}, saldo:{balances},BTC:{addresses}")
        #if btc in("1KYUv7nSvXx4642TKeuC2SNdTk326uUpFy,1PitScNLyp2HCygzadCh7FveTnfmpPbfp8"):
        #   print(f"KETEMU Hex {hex_key}, WIF:{wif_key},BTC:{btc}")
        #   break
    #print(f"Hex terakhir: {hex_key}, WIF:{wif_key},BTC:{btc}")
    #formatted_end = now.strftime("%Y-%m-%d %H:%M:%S")
    #selisih = formatted - formatted_end
    #print(f"selesai jam : {formatted_end}")

# secp256k1 curve order (n)
CURVE_ORDER = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364140

def gen_pvkey():
    while True:
        bits = secrets.randbits(254)
        if 1 <= bits < CURVE_ORDER:  # Valid range for Bitcoin
            return hex(bits)[2:].zfill(64)


def decimal_to_hex_recursive(decimal):
    conversion_table = "0123456789ABCDEF"
    if decimal == 0:
        return ''
    else:
        return decimal_to_hex_recursive(decimal // 16) + conversion_table[decimal % 16]
#print(secure_random)
#print("Hexadecimal:", decimal_to_hex_recursive(secure_random))
#hex = decimal_to_hex_recursive(secure_random)
#print("Hexadecimal:", hex)
#print(f"Length: {len(hex)}")


def hex_to_wif(hex_private_key):
    """Convert hexadecimal private key to Wallet Import Format (WIF)."""
    # Add version byte (0x80 for mainnet)
    extended_key = '80' + hex_private_key.zfill(64) + '01' # Ensure it's 64 characters long

    # Convert hex to bytes
    extended_key_bytes = bytes.fromhex(extended_key)

    # Perform SHA-256 hashing twice
    first_hash = hashlib.sha256(extended_key_bytes).digest()
    second_hash = hashlib.sha256(first_hash).digest()

    # Get the first 4 bytes of the second hash for checksum
    checksum = second_hash[:4]

    # Append checksum to extended key
    wif_key_bytes = extended_key_bytes + checksum

    # Convert to base58
    wif_key = base58.b58encode(wif_key_bytes)

    return wif_key.decode('utf-8')

    #target1="1EhqbyUMvvs7BfL8goY6qcPbD6YKfPqb7e"
hex_private_key="0000000000000000000000000000000000000000000000000000000000000000"

def generate_bitcoin_address(private_key):
    private_key = private_key.zfill(64)
    #print(private_key)
    sk = ecdsa.SigningKey.from_string(bytes.fromhex(private_key), curve=ecdsa.SECP256k1)
    vk = sk.get_verifying_key()
    public_key = vk.to_string('compressed')
    public_key2 = vk.to_string('uncompressed')

    # Generate compressed address
    h160 = hashlib.new('ripemd160', hashlib.sha256(public_key).digest()).digest()
    address = b'\x00' + h160
    checksum = hashlib.sha256(hashlib.sha256(address).digest()).digest()[:4]
    #compressed_address="1MVDYgVaSN6iKKEsbzRUAYFrYJadLYZvvZ"
    compressed_address = base58.b58encode(address + checksum).decode('utf-8')

    # Generate uncompressed address
    #h160 = hashlib.new('ripemd160', hashlib.sha256(vk.to_string()).digest()).digest()
    h160 = hashlib.new('ripemd160', hashlib.sha256(public_key2).digest()).digest()
    address = b'\x00' + h160
    checksum = hashlib.sha256(hashlib.sha256(address).digest()).digest()[:4]
    #uncompressed_address = "1MVDYgVaSN6iKKEsbzRUAYFrYJadLYZvvZ"
    uncompressed_address = base58.b58encode(address + checksum).decode('utf-8')

    # Generate WIF
    wif = base58.b58encode_check(b'\x80' + bytes.fromhex(private_key)).decode('utf-8')

    return compressed_address, uncompressed_address, wif
    #return uncompressed_address, wif


def get_balances(addresses):
    #url = f'https://blockstream.info/api/address/'
    base_url = "https://blockstream.info/api"
    address_url = f"{base_url}/address/{addresses}"
    #print(address_url)
    try:
        # Batch request to get balances for multiple addresses
        #response = requests.post(url + 'compressed_address', json=addresses)
        response = requests.get(address_url)

    # Raise an exception for bad status codes (4xx or 5xx)
        response.raise_for_status()

    # Parse the JSON response
        data = response.json()
        #print(data['chain_stats']['funded_txo_sum'])
        hist_balance = data['chain_stats']['funded_txo_sum']

        #print(data)
        #if response.status_code == 200:
        #   data = response.json()
        #balances = {}
        #for addr in data:
        #        #balance = funded_txo_sum['value'] #sum([utxo['value'] for utxo in addr['utxos']])
        balances = (data['chain_stats']['funded_txo_sum'] - data['chain_stats']['spent_txo_sum'])/100000000
                #print(balance)
            #balances[addr['address']] = balance
        return balances, hist_balance
    except requests.RequestException as e:
            print(f"Error fetching balances: {e}")
    #return {addr: 0 for addr in addresses}
    return get_balances


# Function to convert private key to WIF
#i = 0
def private_key_to_wif(private_key_bytes):
    # Add prefix 0x80 for mainnet private keys
    extended_key = b"\x80" + private_key_bytes
    # Double SHA-256 hash for checksum
    checksum = hashlib.sha256(hashlib.sha256(extended_key).digest()).digest()[:4]
    # Combine extended key and checksum
    wif_key = base58.b58encode(extended_key + checksum)
    return wif_key.decode("utf-8")


def generate_random_hex(length=8):
    """Generate a cryptographically secure random hex string.

    Args:
        length: Length of hex string (each byte = 2 hex chars)

    Returns:
        Random hex string of specified length
    """
    max_value = 16**length - 1
    random_num = randrange(0, max_value + 1)
    #print(random_num)
    return format(random_num, f'0{length}x')

def generate_random_hex2(length=8):
    """Generate random hex using bytes (more efficient for large lengths)"""
    #num_bytes = (length + 1) // 2  # Round up
    num_bytes = (length + 2) // 2  # Round up
    random_bytes = get_random_bytes(num_bytes)
    return random_bytes.hex()[:length]

def generate_256bit_hex_max_900():
    max_val = 0x6b8f000000000000000000000000000000000000000000000000000000000000
    #0x9000000000000000000000000000000000000000000000000000000000000000
    #0x6b80000000000000000000000000000000000000000000000000000000000000
    # Get 32 random bytes (256 bits)
    random_bytes = get_random_bytes(32)
    random_num = int.from_bytes(random_bytes, 'big')
    # Modulo operation to ensure we stay within range
    random_num %= (max_val + 1)
    return format(random_num, '064x')

def generate_256bit_hex_in_range():
    # Calculate the range size
    min_val = 0x1aaaaaaaaaaaaaaaaa
    #1fffffffffffffffff
    #109A859B68CA1AE49C
    #0x6b80000000000000000000000000000000000000000000000000000000000000

    range_size = 0x1fffffffffffffffff
    #0x6b8f000000000000000000000000000000000000000000000000000000000000 - min_val + 1

    # Generate random offset and add to min_val
    random_offset = randrange(range_size)
    random_num = min_val + random_offset

    return format(random_num, '064x')

def generate_bitcoin_private_key_2010():
    # Secp256k1 curve order (n)
    curve_order = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364140

    # Generate valid private key
    private_key = randrange(1, curve_order)

    # Format as 64-character hex, zero-padded
    return format(private_key, '064x')

def new_generate_hex_in_specific_range():
    # Define range (inclusive bounds as hex literals)
    min_val = 0x1e1111111111111111  # Lower bouneed
    max_val = 0x1fffffffffffffffff  # Upper bound

    # Calculate span (+1 to include max_val)
    span = max_val - min_val + 1

    # Generate cryptographically secure random number in [min_val, max_val]
    random_num = min_val + secrets.randbelow(span)

    # Convert to hex (without '0x' prefix)
    #f"{random_num:x}"
    return f"{random_num:x}"






def threaded_conversion(start, end, thread_count):
    """Run the conversion in multiple threads."""
    threads = []

    # Calculate the range for each thread
    end = end + start
    range_size = (end - start + 0) // thread_count

    for i in range(thread_count):
        thread_start = start + i * range_size
        #st12 = start+end
        thread_end = start + (i + 1) * range_size if i < thread_count - 1 else end + 0



        #global hex_private_key
        #counter = hex(int(hex_private_key, 16) - 1)[2:]
        #hex_private_key = "".zfill(64 - len(counter)) + counter
        # Convert integer to hexadecimal string (without '0x' prefix)
        # hex_private_key = format(i, 'x').zfill(64)  # Ensure it's 64 characters long
         # Create hexadecimal keys from the countdown numbers
        hex_keys = [format(num, 'x') for num in range(thread_start,thread_end)]
        #print(hex_keys)
        # Create and start a new thread for each chunk of keys
        thread = threading.Thread(target=convert_and_print, args=(hex_keys,))
        threads.append(thread)
        thread.start()
    #print("tidak ketemu")
    #print(thread_end)
    # Wait for all threads to complete
    for thread in threads:
        thread.join()

# Example usage 295147905179352825.856
if __name__ == "__main__":
    countdown_start = awal #input("Enter your countdown_start: ")
    countdown_start = int(countdown_start)
    #countdown_start = 295147905179356025856  # Starting number for countdown
    countdown_end = akhir    # Ending number for countdown

    threaded_conversion(countdown_start, countdown_end, thread_count=x)
    print(countdown_start+countdown_end)
    #print(f"Selisih waktu: {selisih}")
    #print(f"Total detik: {selisih.total_seconds()} detik")
