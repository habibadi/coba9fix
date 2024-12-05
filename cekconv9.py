from telethon.sync import TelegramClient, events, Button
import asyncio
import winsound  # Untuk memainkan suara alarm di Windows
from telethon.tl.types import PeerChat, PeerChannel, InputPeerChat
import requests
import json
import asyncio
import datetime
import time
import re
from telethon.tl.types import MessageMediaDocument, MessageMediaPhoto
from telethon import TelegramClient, events, sync, tl
import telethon
from telethon.errors import AuthKeyUnregisteredError
from telethon.errors import PersistentTimestampOutdatedError
import os
from telethon.tl.types import InputPeerChannel
import asyncio
import aiohttp
from telethon.tl.types import InputPeerChannel, InputPeerUser
from concurrent.futures import ThreadPoolExecutor
from collections import deque
from datetime import datetime, timedelta, timezone
import traceback
import statistics
from collections import Counter
from collections import Counter, defaultdict
import pymysql
import pytz


# Ganti dengan informasi Anda sendiri
#api_id = '20623228'
#api_hash = '98017a0e6daf0198a836d5cbcd2d9b96'

run_position = False
fifo_queue = deque()
expired_fifo_queue = deque()

api_id = '14167964'
api_hash = '371a87545c9a82871e7daf51437883f8'
out1 = ""
out2 = ""
entity = ""
# Inisiasi penerima
user_id = 4151033946

userId_McapBot = "@ttfbotbot"
userId_TgBot = "@RickBurpBot"
userId_Prio2 = "@paris_trojanbot"
doge_smart = "solana_alerts_dogeebot"
session_name = 'session_name'
user_tesrick = 2228414903
user_check_x = 2198583984
user_news = 2087255766
user_news_p0 = 4266297407
trend_list = 4239753664
Dj_channel= 2015507752
P00_alert = 2470737780
plonk_bot = 2193363840
wallet_arlet = 4516477192
ALERTERR = 4597186327
gambler = 2391890259
entity1 = None
swicth= True
buyer_bot = 0
cek_mcap = 2325472102
cobaaan = 4722263486

# Inisialisasi klien Telegram
client = TelegramClient(session_name, api_id, api_hash)
banned = ["Red Bean", "cats" , "**Simon's Cat" , "BLUE" , "LEAF", "HUNGRY" , "FRIED" , "DAWG", "SWAG", "DARK", "HUNGRY", "SWAG", "DEVIL", "CHlKO", "PANFLlP", "MUSHl", "EVlLDOGE", "SNlFFY", "PlNDA", "ROARKlT", "SNlFFY", "WISH"]
#Tools and Forward messages ================================================================================================================================================
banned_wallet = ["35fzgfD4vS8fWt2yRDrT1aG9Z3otWRE53hyESFFzAijY", "4wd6tHctTEiYuoLLn6mi7T9gXd9RT58w2q5jXZG2FN51", "ewGF1MtkaewDHDQSLnmLyLViJzHisSgTxHv7s1tcvbo" ,"FtLF1iFw6qxnWwBqudV8NdZuURtb79PL8wGZim2CuLzs","GYmzLDuN5MM96tosXhGjcVyX15K78xF19SYnuA3ChYkS", "Fu3cbX91uGFLdm78HZf3SJdkKsPEUwwDmbCCfTEtqote", "4scDibb8LPqDNchtKqoMJRjgZC9x7z7gEiw57KkK81ek" , "ewGF1MtkaewDHDQSLnmLyLViJzHisSgTxHv7s1tcvbo" , "225DbTXRw5JYxyMjNkoddoJpoeQFvdF92fn4Dqas8UNV" , "DeVNNc2cVbx6zx4eqosciA5nuf2wWejtFFrVzWuwNtoU", "GYRMdZrdxgarYpYbA7q5dk24UXGW99Wi8X6NrD3X7Cua", "7ZPFGD1QfghJjCG5AbM9Gkve1HsFdZAqKTCL4ZFV2LMT", "5KHqy5JRp6Bz6SVQJZdxr1yHQDWHsm6Z1xSWs6cJjCcC", "9xq4YuWc21i7pCgPpapfrBp3m1dtSHVgpguctnpus8rd" , "9Gmc5BeP5vsqMeXMWn3VCmxAN8SxNnzEsJaPEuyYNaYW" , "9VpdeDf4krozG4StFX98AezKZqmDEgABiCsjs3JChvVD", "3FnV7DWZCmN9a4caZUyxxkKm5vwRTQgbZEjWa3DLiAqD", "HGUNQ2YC47HDUwv3TQJCNT3sSy5PvAc1HsuvJELueno6", "HGUNQ2YC47HDUwv3TQJCNT3sSy5PvAc1HsuvJELueno6","DVKKYe2dBRUKE2BN3Km8EQVug5mEV3en7LgNxxVqRhv9", "FtLF1iFw6qxnWwBqudV8NdZuURtb79PL8wGZim2CuLzs" ,"7xZYqDB5osFNB1DRgnZtV9ue1bn3AFeDedgWR7hJ7c5u", "87fkEVZXdN1BEhQRwXpdxiBANRJyWR7QX5Q5hprrUeVt"]

check_wallet = [
    "H83234m795YMcfFMVT6FezX6qxwrnycYx3Av9SqmQVLg",
    "8MqRTAQnjhDYH7TWS1b1DjFog4CLZfySWE5cZeotG2VW",
    "9YdVFpBh2HKQR8ChC3H6y8RjUWcbw7sS8ub1LEbg3y5h",
    "HdxkiXqeN6qpK2YbG51W23QSWj3Yygc1eEk2zwmKJExp",
    "CsQsycSotefhUHUm2i7amnX4RTCAWQsShqVCQssNL3st",
    "CATGF",
    "nig6FoG3RV7dqXuouCTpVsHA58YZ14EaFauXPRAoger",
    "GAWPLNxT6DhvCNKLsxD7z4iVq1SPPjqZme4Q9MBrStBM",
    "HgnPTfFtgf9NaXp2sdHaBd5F7avWaV3v2K4B2WaeTNQL",
    "B16dbsa5n3ydJZBS99D2BK3GhCpaytSwkmKiZgo7x8d4",
    "WoTF",
    "5SCN3TzmAeiFGPamNYnohywca71wQD7dvEJN5SNDU6wK"
]

class MySQLConnection:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.conn = None
        self.connect()

    def connect(self):
        try:
            self.conn = pymysql.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database,
                connect_timeout=10
            )
            print("Koneksi berhasil menggunakan pymysql!")
        except pymysql.MySQLError as e:
            print(f"Error koneksi: {e}")
            traceback.print_exc()

    def get_cursor(self):
        if self.conn is None or not self.conn.open:
            print("Koneksi hilang, mencoba untuk reconnect...")
            self.connect()
        return self.conn.cursor()

    def commit(self):
        if self.conn:
            self.conn.commit()

    def close(self):
        if self.conn and self.conn.open:
            self.conn.close()
            print("Koneksi berhasil ditutup.")

# Membuat instance koneksi
mysql_conn = MySQLConnection(
    host="127.0.0.1",
    user="root",
    password="112233",  # Gantilah dengan password root yang benar
    database="inside_gem"
)

def insert_data_ray_list(ca, alpha, bot, smart, kol, dev, insider, sniper, whale1, whale2, ray_wallet, mcmoney):
    try:
        cursor = mysql_conn.get_cursor()
        insert_query = """
        INSERT INTO ray_list 
        (ca, alpha, bot, smart, kol, dev, insider, sniper, whale1, whale2, ray_wallet, mcmoney, created_at) 
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, NOW());
        """
        data = (ca, alpha, bot, smart, kol, dev, insider, sniper, whale1, whale2, ray_wallet, mcmoney)
        cursor.execute(insert_query, data)
        mysql_conn.commit()
        print("Data berhasil diinsert ke tabel ray_list!")
    except pymysql.MySQLError as e:
        print(f"Error saat insert data: {e}")
        traceback.print_exc()
    except Exception as e:
        print(f"Exception lain: {e}")
        traceback.print_exc()
    finally:
        cursor.close()


# Fungsi untuk insert data
def insert_data_twitter(kata_kunci, full_link, msg_id, coin_name):
    try:
        cursor = mysql_conn.get_cursor()
        insert_query = """
        INSERT INTO twitter_info (kata_kunci, full_link, msg_id, coin_name, created_at)
        VALUES (%s, %s, %s, %s, NOW());
        """
        data = (kata_kunci, full_link, msg_id, coin_name)
        cursor.execute(insert_query, data)
        mysql_conn.commit()
        print("Data berhasil diinsert ke tabel twitter_info!")
    except pymysql.MySQLError as e:
        print(f"Error saat insert data: {e}")
        traceback.print_exc()
    except Exception as e:
        print(f"Exception lain: {e}")
        traceback.print_exc()

def insert_data_coin_gem(ca_id, platform, fdv_init, fdv_top, keyword, msg_id, x_from_init):
    try:
        cursor = mysql_conn.get_cursor()
        insert_query = """
        INSERT INTO coin_gem (ca_id, platform, fdv_init, fdv_top, keyword, msg_id, x_from_init, created_at)
        VALUES (%s, %s, %s, %s, %s, %s, %s, NOW());
        """
        data = (ca_id, platform, fdv_init, fdv_top, keyword, msg_id, x_from_init)
        cursor.execute(insert_query, data)
        mysql_conn.commit()
        print("Data berhasil diinsert ke tabel coin_gem!")
    except pymysql.MySQLError as e:
        print(f"Error saat insert data: {e}")
        traceback.print_exc()
    except Exception as e:
        print(f"Exception lain: {e}")
        traceback.print_exc()

def insert_data_signal(ca, holder, smart, created, mcap):
    try:
        cursor = mysql_conn.get_cursor()  # Ganti sesuai metode Anda untuk mendapatkan cursor
        insert_query = """
        INSERT INTO data_signal (ca, holder, smart, created, mcap, created_at)
        VALUES (%s, %s, %s, %s, %s, NOW());
        """
        data = (ca, holder, smart, created, mcap)
        cursor.execute(insert_query, data)
        mysql_conn.commit()
        print("Data berhasil diinsert ke tabel data_signal!")
    except pymysql.MySQLError as e:
        print(f"Error saat insert data: {e}")
        traceback.print_exc()
    except Exception as e:
        print(f"Exception lain: {e}")
        traceback.print_exc()


def get_recent_wallet_signal_tokens():
    try:
        cursor = mysql_conn.get_cursor()
        time_15_minutes_ago = datetime.now() - timedelta(minutes=15)
        select_query = """
        SELECT ca FROM wallet_signal WHERE created_at >= %s AND master > 0;
        """
        cursor.execute(select_query, (time_15_minutes_ago,))
        result = cursor.fetchall()
        return [row[0] for row in result] if result else []
    except pymysql.MySQLError as e:
        print(f"Error saat mencari data: {e}")
        traceback.print_exc()
        return []
    except Exception as e:
        print(f"Exception lain: {e}")
        traceback.print_exc()
        return []


# Fungsi untuk mencari kombinasi ca_id dan platform
def find_coin_gem_by_ca_id_and_platform(ca_id, platform):
    try:
        cursor = mysql_conn.get_cursor()
        select_query = """
        SELECT * FROM coin_gem WHERE ca_id = %s AND platform = %s;
        """
        cursor.execute(select_query, (ca_id, platform))
        result = cursor.fetchone()
        #print("POKWOPKWPOKWPOWKPOKWPOWKPWKWPOKWPOWKPKWPOWKPWOKPWOKWPKWPKWPWOKPWOKWPOKWPOKWPOKWPOWK")
        #print(result)
        return True if result else False
    except pymysql.MySQLError as e:
        print(f"Error saat mencari data: {e}")
        traceback.print_exc()
        return False
    except Exception as e:
        print(f"Exception lain: {e}")
        traceback.print_exc()
        return False

def find_coin_gem_by_ca_id_and_platform_60mnt(ca_id, platform):
    try:
        cursor = mysql_conn.get_cursor()
        time_60_minutes_ago = datetime.now() - timedelta(minutes=60)
        select_query = """
        SELECT * FROM coin_gem WHERE ca_id = %s AND platform = %s AND created_at >= %s LIMIT 1;
        """
        cursor.execute(select_query, (ca_id, platform, time_60_minutes_ago))
        result = cursor.fetchone()
        #print("POKWOPKWPOKWPOWKPOKWPOWKPWKWPOKWPOWKPKWPOWKPWOKPWOKWPKWPKWPWOKPWOKWPOKWPOKWPOKWPOWK")
        #print(result)
        return True if result else False
    except pymysql.MySQLError as e:
        print(f"Error saat mencari data: {e}")
        traceback.print_exc()
        return False
    except Exception as e:
        print(f"Exception lain: {e}")
        traceback.print_exc()
        return False


def find_coin_gem_by_ca_id_and_platform_xmnt(ca_id, platform, mins):
    try:
        cursor = mysql_conn.get_cursor()
        time_60_minutes_ago = datetime.now() - timedelta(minutes=mins)
        select_query = """
        SELECT * FROM coin_gem WHERE ca_id = %s AND platform = %s AND created_at >= %s LIMIT 1;
        """
        cursor.execute(select_query, (ca_id, platform, time_60_minutes_ago))
        result = cursor.fetchone()
        #print("POKWOPKWPOKWPOWKPOKWPOWKPWKWPOKWPOWKPKWPOWKPWOKPWOKWPKWPKWPWOKPWOKWPOKWPOKWPOKWPOWK")
        #print(result)
        return True if result else False
    except pymysql.MySQLError as e:
        print(f"Error saat mencari data: {e}")
        traceback.print_exc()
        return False
    except Exception as e:
        print(f"Exception lain: {e}")
        traceback.print_exc()
        return False

def find_coin_gem_by_ca_id_and_platform_xmnt_fdv(ca_id, platform, mins):
    try:
        cursor = mysql_conn.get_cursor()
        time_60_minutes_ago = datetime.now() - timedelta(minutes=mins)
        select_query = """
        SELECT fdv_init FROM coin_gem WHERE ca_id = %s AND platform = %s AND created_at >= %s LIMIT 1;
        """
        cursor.execute(select_query, (ca_id, platform, time_60_minutes_ago))
        result = cursor.fetchone()
        
        return result[0] if result else False
    except pymysql.MySQLError as e:
        print(f"Error saat mencari data: {e}")
        traceback.print_exc()
        return False
    except Exception as e:
        print(f"Exception lain: {e}")
        traceback.print_exc()
        return False

    
# Fungsi untuk mendapatkan daftar ca dari tabel wallet_signal dengan minimal 3 kolom lebih dari 0 dan created_at tidak lebih dari 30 menit
def get_wallet_signal_with_conditions():
    try:
        cursor = mysql_conn.get_cursor()
        time_30_minutes_ago = datetime.now() - timedelta(minutes=30)
        select_query = """
        SELECT ca, whale1, whale2, ray_wallet, master FROM wallet_signal 
        WHERE created_at >= %s AND is_sent < 2 AND whale2 > 0 AND(
            (whale1 > 0  AND ray_wallet > 0) OR
            (whale1 > 0 AND master > 0) OR
            (ray_wallet > 0 AND master > 0)
        );
        """
        cursor.execute(select_query, (time_30_minutes_ago,))
        result = cursor.fetchall()
        
        formatted_message = "\n".join([
            f"{i + 1}. <code>{row[0]}</code> Whale1: {row[1]}, Whale2: {row[2]}, Ray Wallet: {row[3]}, Master: {row[4]} "
            f"[<a href=https://bullx.io/terminal?chainId=1399811149&address={row[0]}>bullx</a>] "
            for i, row in enumerate(result)
        ])

        for row in result:
            upsert_wallet_signal(row[0], 0, 0, 0, 0, 0, 0, 0, is_sent=2)
        return formatted_message

    except pymysql.MySQLError as e:
        print(f"Error saat mencari data: {e}")
        traceback.print_exc()
        return "Terjadi kesalahan saat mencari data."
    except Exception as e:
        print(f"Exception lain: {e}")
        traceback.print_exc()
        return "Terjadi kesalahan saat mencari data."
    
# Fungsi untuk mendapatkan data dari tabel wallet_signal berdasarkan input ca
def get_wallet_signal_by_ca(ca):
    try:
        cursor = mysql_conn.get_cursor()
        select_query = """
        SELECT * FROM wallet_signal WHERE ca = %s;
        """
        cursor.execute(select_query, (ca,))
        result = cursor.fetchone()
        if result:
            columns = ["whale1", "whale2", "ray_wallet", "momentum"]
            filtered_result = [val for col, val in zip(["ca", "whale1", "whale2", "ray_wallet", "master", "bot", "momentum", "smarter", "is_sent", "created_at"], result) if col in columns]
            formatted_message = " | ".join([f"{col}: {val}" for col, val in zip(columns, filtered_result)])
            return formatted_message

        else:
            return ""
    except pymysql.MySQLError as e:
        print(f"Error saat mencari data: {e}")
        traceback.print_exc()
        return "Terjadi kesalahan saat mencari data."
    except Exception as e:
        print(f"Exception lain: {e}")
        traceback.print_exc()
        return "Terjadi kesalahan saat mencari data."


def get_wallet_signal_by_ca_5params(ca):
    try:
        cursor = mysql_conn.get_cursor()
        select_query = """
        SELECT * FROM wallet_signal WHERE ca = %s;
        """
        cursor.execute(select_query, (ca,))
        result = cursor.fetchone()
        if result:
            columns = ["whale1", "whale2", "ray_wallet", "master", "momentum", "smarter"]
            filtered_result = [val for col, val in zip(["ca", "whale1", "whale2", "ray_wallet", "master", "bot", "momentum", "smarter", "is_sent", "created_at"], result) if col in columns]
            formatted_message = " | ".join([f"{col}: {val}" for col, val in zip(columns, filtered_result)])
            return formatted_message

        else:
            return ""
    except pymysql.MySQLError as e:
        print(f"Error saat mencari data: {e}")
        traceback.print_exc()
        return "Terjadi kesalahan saat mencari data."
    except Exception as e:
        print(f"Exception lain: {e}")
        traceback.print_exc()
        return "Terjadi kesalahan saat mencari data."
    
def get_wallet_signal_smart(ca):
    try:
        cursor = mysql_conn.get_cursor()
        select_query = """
        SELECT smarter FROM wallet_signal WHERE ca = %s;
        """
        cursor.execute(select_query, (ca,))
        result = cursor.fetchone()
        if result:
            return result[0]
        else:
            return None
    except pymysql.MySQLError as e:
        print(f"Error saat mencari data: {e}")
        traceback.print_exc()
        return "Terjadi kesalahan saat mencari data."
    except Exception as e:
        print(f"Exception lain: {e}")
        traceback.print_exc()
        return "Terjadi kesalahan saat mencari data."

# Fungsi untuk mendapatkan data dari tabel wallet_signal berdasarkan input ca
def get_wallet_signal_by_ca_3param(ca):
    try:
        cursor = mysql_conn.get_cursor()
        select_query = """
        SELECT * FROM wallet_signal WHERE ca = %s;
        """
        cursor.execute(select_query, (ca,))
        result = cursor.fetchone()
        if result:
            columns = ["whale1", "whale2", "ray_wallet", "master", "bot"]
            filtered_result = [val for col, val in zip(["ca", "whale1", "whale2", "ray_wallet", "master", "bot", "momentum", "smarter", "is_sent", "created_at"], result) if col in columns]
            formatted_message = " | ".join([f"{col}: {val}" for col, val in zip(columns, filtered_result)])
            return formatted_message

        else:
            return ""
    except pymysql.MySQLError as e:
        print(f"Error saat mencari data: {e}")
        traceback.print_exc()
        return "Terjadi kesalahan saat mencari data."
    except Exception as e:
        print(f"Exception lain: {e}")
        traceback.print_exc()
        return "Terjadi kesalahan saat mencari data."
    

def is_wallet_sent_by_no(no):
    try:
        cursor = mysql_conn.get_cursor()
        select_query = """
        SELECT * FROM wallet_signal WHERE is_sent < %s;
        """
        cursor.execute(select_query, (no,))
        result = cursor.fetchone()
        if result:
            return True
        else:
            return False
    except pymysql.MySQLError as e:
        print(f"Error saat mencari data: {e}")
        traceback.print_exc()
        return "Terjadi kesalahan saat mencari data."
    except Exception as e:
        print(f"Exception lain: {e}")
        traceback.print_exc()
        return "Terjadi kesalahan saat mencari data."

def cek_menit_kelipatan_15():
    sekarang = datetime.now()
    menit = sekarang.minute
    if menit % 15 == 0:
        print(f"Menit sekarang ({menit}) adalah kelipatan 15.")
        return True
    else:
        print(f"Menit sekarang ({menit}) bukan kelipatan 15.")
        return False

def cek_menit_kelipatan_16():
    sekarang = datetime.now()
    menit = sekarang.minute
    if menit % 15 ==9:
        print(f"Menit sekarang ({menit}) adalah kelipatan 15.")
        return True
    else:
        print(f"Menit sekarang ({menit}) bukan kelipatan 15.")
        return False
    

async def find_coin_gem_by_keyword_platform_and_timeframe(keyword, platform,update_platform=True):
    try:
        cursor = mysql_conn.get_cursor()
        time_40_minutes_ago = datetime.now() - timedelta(minutes=40)
        select_query = """
        SELECT ca_id FROM coin_gem WHERE keyword = %s AND platform = %s AND created_at >= %s;
        """
        cursor.execute(select_query, (keyword, platform, time_40_minutes_ago))
        result = cursor.fetchall()
        if result:
            if update_platform:
                update_query = """
                UPDATE coin_gem SET platform = 'pf' WHERE keyword = %s AND platform = %s AND created_at >= %s;
                """
                cursor.execute(update_query, (keyword, "pf" , time_40_minutes_ago))
                mysql_conn.commit()
                print("Platform updated to 'pf' for the matched records.")
                chat_id = -2391890259  # Ganti dengan ID chat yang diambil dari URL
                entity1 = await client.get_entity(PeerChannel(chat_id))
            formatted_message = "\n".join([f"{i + 1}. <code>{row[0]}</code> {await call_api(row[0])} alpha buyers: {await search_messages(entity1, row[0])} {get_wallet_signal_by_ca(row[0])} [<a href=https://bullx.io/terminal?chainId=1399811149&address={row[0]}>bullx</a>] " for i, row in enumerate(result)])
            return "▶️ List coin already list on ray: \n"+formatted_message
        else:
            return "There haven't been any viral coins listed on Raydium yet."

    except pymysql.MySQLError as e:
        print(f"Error saat mencari data: {e}")
        traceback.print_exc()
        return "Terjadi kesalahan saat mencari data."
    except Exception as e:
        print(f"Exception lain: {e}")
        traceback.print_exc()
        return "Terjadi kesalahan saat mencari data."
    


def find_full_link_by_link(link):
    try:
        cursor = mysql_conn.get_cursor()
        select_query ="""
        SELECT 1 
        FROM `twitter_info`
        WHERE `full_link` = %s
        AND `created_at` >= NOW() - INTERVAL 20 MINUTE;
        """
        cursor.execute(select_query, (link))
        result = cursor.fetchone()
        #print("POKWOPKWPOKWPOWKPOKWPOWKPWKWPOKWPOWKPKWPOWKPWOKPWOKWPKWPKWPWOKPWOKWPOKWPOKWPOKWPOWK")
        #print(result)
        return True if result else False
    except pymysql.MySQLError as e:
        print(f"Error saat mencari data: {e}")
        traceback.print_exc()
        return False
    except Exception as e:
        print(f"Exception lain: {e}")
        traceback.print_exc()
        return False

def find_latest_full_link_by_keyword(kata_kunci):
    try:
        cursor = mysql_conn.get_cursor()
        select_query = """
        SELECT full_link FROM twitter_info WHERE kata_kunci = %s ORDER BY created_at DESC LIMIT 1;
        """
        cursor.execute(select_query, (kata_kunci,))
        result = cursor.fetchone()
        if result:
            return result[0]
        else:
            return None
    except pymysql.MySQLError as e:
        print(f"Error saat mencari data: {e}")
        traceback.print_exc()
        return "Terjadi kesalahan saat mencari data."
    except Exception as e:
        print(f"Exception lain: {e}")
        traceback.print_exc()
        return "Terjadi kesalahan saat mencari data."
    
def is_ca_created_within_30_minutes(ca):
    try:
        cursor = mysql_conn.get_cursor()
        time_30_minutes_ago = datetime.now() - timedelta(minutes=30)
        select_query = """
        SELECT 1 FROM ray_list WHERE ca = %s AND created_at >= %s LIMIT 1;
        """
        cursor.execute(select_query, (ca, time_30_minutes_ago))
        result = cursor.fetchone()
        return True if result else False
    except pymysql.MySQLError as e:
        print(f"Error saat mencari data: {e}")
        traceback.print_exc()
        return False
    except Exception as e:
        print(f"Exception lain: {e}")
        traceback.print_exc()
        return False

def is_mcmoney(ca):
    try:
        cursor = mysql_conn.get_cursor()
        mcmoney_count = 0
        select_query = """
        SELECT 1 FROM ray_list WHERE ca = %s AND mcmoney > %s LIMIT 1;
        """
        cursor.execute(select_query, (ca, mcmoney_count))
        result = cursor.fetchone()
        return True if result else False
    except pymysql.MySQLError as e:
        print(f"Error saat mencari data: {e}")
        traceback.print_exc()
        return False
    except Exception as e:
        print(f"Exception lain: {e}")
        traceback.print_exc()
        return False
    

def is_ca_created_within_60_minutes(ca):
    try:
        cursor = mysql_conn.get_cursor()
        time_30_minutes_ago = datetime.now() - timedelta(minutes=60)
        select_query = """
        SELECT 1 FROM ray_list WHERE ca = %s AND created_at >= %s LIMIT 1;
        """
        cursor.execute(select_query, (ca, time_30_minutes_ago))
        result = cursor.fetchone()
        return True if result else False
    except pymysql.MySQLError as e:
        print(f"Error saat mencari data: {e}")
        traceback.print_exc()
        return False
    except Exception as e:
        print(f"Exception lain: {e}")
        traceback.print_exc()
        return False

def is_ca_created_within_10_minutes(ca):
    try:
        cursor = mysql_conn.get_cursor()
        time_30_minutes_ago = datetime.now() - timedelta(minutes=10)
        select_query = """
        SELECT 1 FROM ray_list WHERE ca = %s AND created_at >= %s LIMIT 1;
        """
        cursor.execute(select_query, (ca, time_30_minutes_ago))
        result = cursor.fetchone()
        return True if result else False
    except pymysql.MySQLError as e:
        print(f"Error saat mencari data: {e}")
        traceback.print_exc()
        return False
    except Exception as e:
        print(f"Exception lain: {e}")
        traceback.print_exc()
        return False

def is_wallet_signal_created_within_5_minutes(ca):
    try:
        cursor = mysql_conn.get_cursor()
        time_5_minutes_ago = datetime.now() - timedelta(minutes=15)
        select_query = """
        SELECT 1 FROM wallet_signal WHERE ca = %s AND created_at >= %s LIMIT 1;
        """
        cursor.execute(select_query, (ca, time_5_minutes_ago))
        result = cursor.fetchone()
        return True if result else False
    except pymysql.MySQLError as e:
        print(f"Error saat mencari data: {e}")
        traceback.print_exc()
        return False
    except Exception as e:
        print(f"Exception lain: {e}")
        traceback.print_exc()
        return False
    
def get_wallet_list_by_ca(ca):
    # Buat cursor untuk menjalankan query
    try:
        cursor = mysql_conn.get_cursor()
    
        # Query untuk mendapatkan data berdasarkan ca
        query = """
        SELECT whale1, whale2, ray_wallet, master, bot, momentum, smarter, is_sent 
        FROM wallet_signal 
        WHERE ca = %s
        """
        
        # Jalankan query dengan parameter ca
        cursor.execute(query, (ca,))
        
        # Ambil hasil query
        result = cursor.fetchone()
        
        # Tutup cursor
        cursor.close()
        
        # Jika data ditemukan, konversikan ke array integer; jika tidak, kembalikan array kosong
        return list(map(int, result)) if result else []
    except pymysql.MySQLError as e:
        print(f"Error saat mencari data: {e}")
        traceback.print_exc()
        return False
    except Exception as e:
        print(f"Exception lain: {e}")
        traceback.print_exc()
        return False

    
def upsert_wallet_signal(ca, whale1, whale2, ray_wallet, master, bot, momentum, smarter, is_sent=0):
    try:
        cursor = mysql_conn.get_cursor()
        # Check if ca already exists
        select_query = "SELECT 1 FROM wallet_signal WHERE ca = %s LIMIT 1;"
        cursor.execute(select_query, (ca,))
        result = cursor.fetchone()
        if result:
            # Update existing record with incremental values
            update_query = """
            UPDATE wallet_signal SET 
                whale1 = IFNULL(whale1, 0) + %s, 
                whale2 = IFNULL(whale2, 0) + %s, 
                ray_wallet = IFNULL(ray_wallet, 0) + %s, 
                master = IF(%s > master, %s, master), 
                bot = IF(%s > bot, %s, bot), 
                momentum = IF(%s > momentum, %s, momentum), 
                smarter = IF(%s > smarter, %s, smarter), 
                is_sent = %s
            WHERE ca = %s;
            """
            print(f"Alamat token up: {ca}")
            # Pass arguments matching the placeholders
            cursor.execute(update_query, (whale1, whale2, ray_wallet, master, master, bot, bot, momentum, momentum, smarter, smarter, is_sent, ca))
            print("Data berhasil diupdate di tabel wallet_signal!")
        else:
            # Insert new record
            insert_query = """
            INSERT INTO wallet_signal (ca, whale1, whale2, ray_wallet, master, bot, momentum, smarter, is_sent, created_at)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, NOW());
            """
            print(f"Alamat token in: {ca}")
            cursor.execute(insert_query, (ca, whale1, whale2, ray_wallet, master, bot, momentum, smarter, is_sent))
            print("Data berhasil diinsert ke tabel wallet_signal!"+ca)
        mysql_conn.commit()
    except pymysql.MySQLError as e:
        print(f"Error saat upsert data: {e}")
        traceback.print_exc()
    except Exception as e:
        print(f"Exception lain: {e}")
        traceback.print_exc()




async def add_to_queue(queue, code):
    timestamp = datetime.now().isoformat()
    queue.append((code, timestamp))

# Fungsi untuk memainkan suara alarm
def play_alarm():
    frequency = 2500  # Frekuensi suara
    duration = 10000  # Durasi suara dalam milidetik (1 detik)
    winsound.Beep(frequency, duration)

async def play_alarm_async():
    loop = asyncio.get_event_loop()
    with ThreadPoolExecutor() as pool:
        await loop.run_in_executor(pool, play_alarm)

async def forward_msg(message, file=None):
    receiver = InputPeerChat(user_id)
    await client.send_message(receiver, message, file=file, parse_mode='html')

async def forward_alert(message, file=None):
    #receiver = InputPeerChat(P00_alert)

    channel = await client.get_entity(P00_alert)
    
    # Creating an InputPeerChannel object
    receiver = InputPeerChannel(channel_id=channel.id, access_hash=channel.access_hash)

    await client.send_message(receiver, message, file=file, parse_mode='html')

async def forward_alert1(message, file=None):
    #receiver = InputPeerChat(P00_alert)

    channel = await client.get_entity(P00_alert)
    
    # Creating an InputPeerChannel object
    receiver = InputPeerChannel(channel_id=channel.id, access_hash=channel.access_hash)

    await client.send_message(receiver, message, file=file, parse_mode='markdown')


async def forward_mcap(message, file=None):
    #receiver = InputPeerChat(P00_alert)

    channel = await client.get_entity(cek_mcap)
    
    # Creating an InputPeerChannel object
    receiver = InputPeerChannel(channel_id=channel.id, access_hash=channel.access_hash)

    await client.send_message(receiver, message, file=file, parse_mode='markdown')

async def forward_coba(message, file=None):
    #receiver = InputPeerChat(P00_alert)
    receiver = InputPeerChat(cobaaan)
    await client.send_message(receiver, message, file=file, parse_mode='markdown')

async def forward_alert_template(message, file=None):
    #receiver = InputPeerChat(P00_alert)

    channel = await client.get_entity(P00_alert)
    
    # Creating an InputPeerChannel object
    last_message = await client.get_messages(channel, limit=1)
    if last_message:
        receiver = InputPeerChannel(channel_id=channel.id, access_hash=channel.access_hash)
        await client.send_message(receiver, message, file=file,  reply_to=last_message[0].id ,parse_mode='markdown')


async def forward_doge(message, file=None):
    receiver = doge_smart
    await client.send_message(receiver, message, file=file, parse_mode='html')

async def forward_alert_wallet(message, file=None):
    receiver = InputPeerChat(wallet_arlet)
    await client.send_message(receiver, message, file=file, parse_mode='markdown')

async def forward_alert_wallet1(message, file=None):
    receiver = InputPeerChat(wallet_arlet)
    await client.send_message(receiver, message, file=file, parse_mode='markdown')

async def forward_alert_err(message, file=None):
    receiver = InputPeerChat(ALERTERR)
    await client.send_message(receiver, message, file=file, parse_mode='markdown')

async def forward_gambler(message, file=None):
    receiver = InputPeerChat(gambler)
    await client.send_message(receiver, message, file=file, parse_mode='html')

async def forward_msg_trojan(message, file=None):
    receiver = userId_Prio2
    await client.send_message(receiver, message, file=file, parse_mode='html')

async def forward_msg_mcap_bot(message, file=None):
    receiver = userId_McapBot
    await client.send_message(receiver, message, file=file, parse_mode='html')

async def forward_msg_tw_bot(message, media):
    receiver = userId_TgBot
    if isinstance(media, telethon.tl.types.MessageMediaDocument) or isinstance(media, telethon.tl.types.MessageMediaPhoto):
        file = media.document if isinstance(media, telethon.tl.types.MessageMediaDocument) else media.photo
        await client.send_message(receiver, message, file=file, parse_mode='html')
    else:
        await client.send_message(receiver, message, parse_mode='html')

async def forward_rick_bot(message, file=None):
    # Replace 'channel_username_or_id' with the actual username or ID of the channel
    entity = await client.get_entity(4232182480)
    
    entity = await client.get_input_entity(user_tesrick)
    
    # Sending the message to the channel or user
    await client.send_message(entity, message, file=file, parse_mode='html')

async def forward_news(message, file=None):
    # Replace 'channel_username_or_id' with the actual username or ID of the channel
    channel = await client.get_entity(user_news)
    
    # Creating an InputPeerChannel object
    receiver = InputPeerChannel(channel_id=channel.id, access_hash=channel.access_hash)
    
    # Sending the message to the channel
    await client.send_message(receiver, message, file=file, parse_mode='html')

async def forward_check_x(message, file=None):
    # Replace 'channel_username_or_id' with the actual username or ID of the channel
    channel = await client.get_entity(user_check_x)
    
    # Creating an InputPeerChannel object
    receiver = InputPeerChannel(channel_id=channel.id, access_hash=channel.access_hash)
    
    # Sending the message to the channel
    await client.send_message(receiver, message, file=file, parse_mode='html')


async def forward_news_p0(message, file=None):
    # Replace 'channel_username_or_id' with the actual username or ID of the channel
    receiver = InputPeerChat(user_news_p0)
    await client.send_message(receiver, message, file=file, parse_mode='html')

async def forward_trend(message, file=None):
    # Replace 'channel_username_or_id' with the actual username or ID of the channel
    receiver = InputPeerChat(trend_list)
    await client.send_message(receiver, message, file=file, parse_mode='html')

async def getmaster():
    # Mendapatkan entitas grup/channel berdasarkan ID atau username
    chat_id = -2391890259  # Ganti dengan ID chat atau username grup
    entity = await client.get_entity(PeerChannel(chat_id))
    return entity


async def get_last_message():
    messages = await client.get_messages(cek_mcap, limit=1)
    last_message = messages[0]
    print("okee")
    print(last_message)
    if last_message.entities:
        return f"Teks ditemukan dalam entitas: {last_message.raw_text}"
    print(messages)
    return "Tidak ada pesan."


#Tools and Forward messages ================================================================================================================================================
@client.on(events.NewMessage(chats=["@bing_super_call"]))  # Ganti dengan nama grup Anda
async def handle_new_message(event):
    try:
        #print(event.message.text)
        #print("_PA_PA_PA_PA_PA_AP_AP_AP_A)A_)A_)A_PA_AP_AP_APA_PA_PA_PA_PA_AP_AP_APA_PA_AP_APA_PA_PA_PA_PA_PA_AP_AP_AP_AP_APA_PA_PA_AP_AP_APA_PA_AP_AP_AP_AP_APA_P_APA_PA_PA")
        pattern = r"`([a-zA-Z0-9]{32,})`"
        # Menggunakan regex untuk ekstraksi
        match = re.search(pattern, event.message.text)
        match2 = re.search(r'FDV NOW: \$([\d,]+)', event.message.text)
        word_before_parenthesis = event.message.text.split('(')[0]
        print(word_before_parenthesis)
        # Menampilkan hasil ekstraksi
        token_ca = match.group(1)
        if "500K+" in event.message.text or "boost:1500" in event.message.text :
            await forward_coba(f"""{event.message.text}   [ bullx ](https://bullx.io/terminal?chainId=1399811149&address={token_ca})""")
        if match and match2 and "jumped" in  event.message.text :
            await forward_alert_err(event.message.text)
            fdv_post_value = match2.group(1).replace(',', '')
            token_ca = match.group(1)
            print(f"Token CA: {token_ca}")
            #await forward_alert_err("▶️ coin from smart wallet: \n"+ token_ca)
            fdv = find_coin_gem_by_ca_id_and_platform_xmnt_fdv(token_ca, "dex", 60000)
            if fdv:
                kali_lipat = int(fdv_post_value) / fdv
                await forward_alert1(f"""🚀{word_before_parenthesis}🚀
🔹`{token_ca}`
🔹jumped {kali_lipat:.1f}X 
🔹Fdv post: {str(fdv)} 
🔹Fdv now: {fdv_post_value}  
🔹[bullx](https://bullx.io/terminal?chainId=1399811149&address={token_ca})""")

        else:
            print("Token CA tidak ditemukan.")
    except Exception as e:
        print(f"ErrorC: {e}")




@client.on(events.NewMessage(chats=[PeerChannel(user_check_x)]))  # Ganti dengan nama grup Anda
async def handle_new_message(event):
    global run_position
    try:
        #print(event.message.text)
        pattern = r'https://solscan\.io/token/([1-9A-HJ-NP-Za-km-z]+)'

        # Find the specific match
        cap = 0
        match = re.search(pattern, event.message.text)

        market_cap_pattern = r"Market Cap:\s\$(\d+)(\.\d+)?([kKmM])"
        # Find and convert the market cap value

        market_cap_match = re.search(market_cap_pattern, event.message.text)
        if market_cap_match:
            if match:
                token_address = match.group(1)
                amount = int(market_cap_match.group(1))  # Only take the integer part
                unit = market_cap_match.group(3).lower()

                # Convert 'k' or 'm' to numerical value
                if unit == 'k':
                    cap = amount * 1_000
                elif unit == 'm':
                    cap = amount * 1_000_000
                else:
                    cap = amount
                #print(cap)
            else:
                cap = 0
            print("################# "+ str(cap))

            if "Buy" in event.message.text and cap < 50000:
                ave_analitic = await call_api(token_address)
                await forward_doge(f"""
{token_address} 
{ave_analitic}
cekwall
""")  

        # Print the result if a match is found
        if match:
            token_address = match.group(1)
            if find_coin_gem_by_ca_id_and_platform_xmnt(token_address, "dex", 15):
                if token_address not in signal_list and "Buy" in event.message.text:
                    #await forward_alert_err(f"""{event.message.text}   [ bullx ](https://bullx.io/terminal?chainId=1399811149&address={token_address})""")
                    current_time = datetime.now()
                    # signal_list[token_address] = current_time
                await forward_alert_wallet1(f"""{event.message.text}   [ bullx ](https://bullx.io/terminal?chainId=1399811149&address={token_address})""")
            print("New message werfwereeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee: "+str(token_address))
            
            if (is_ca_created_within_30_minutes(token_address) or "Bonding curve progress" in event.message.text) and "Buy" in event.message.text :
                print(f"Alamat token ray: {token_address}")
                if "mcmoney" in event.message.text:
                    insert_data_ray_list(token_address, 0, 0, 0, 0, 0, 0, 0, 0 , 0 , 0 , 1)
                upsert_wallet_signal(token_address, 0, 0, 1, 0, 0, 0, 0, 0)
        elif "break" in event.message.text:
            run_position = False
        else:
            pattern = r'([1-9A-HJ-NP-Za-km-z]+)'
            match = re.search(pattern, event.message.text)

            # Print the result if a match is found
            if match:
                token_address = match.group(1)
                print(f"No match found in the message.")
                await chek_run_position(True,token_address)

    except Exception as e:
        print(f"ErrorC: {e}")
        tb = traceback.format_exc()
        print("An error occurred:\n", tb)
        print(f"Error55: {e}")

@client.on(events.NewMessage(chats=[PeerChannel(user_tesrick)]))  # Ganti dengan nama grup Anda
async def handle_new_message(event):
    try:
        message_data = {
            "token_address": None,
            "market_cap_value": 0,
            "smart_buyers_count": 0,
            "buyer_bot": 0
        }
     
        token_pattern = r"token/([a-zA-Z0-9]+)"
        # Pattern for the market cap with both uppercase and lowercase K/M within double asterisks
        market_cap_pattern = r"市值： \*\*\$(\d+(\.\d+)?)([kKmM])\*\*"
        #print( event.message.text)
        # Find token address
        token_match = re.search(token_pattern,  event.message.text)
        tittle= "Token Launch to Raydium"
        if "Pump内盘阶段" in event.message.text:
            tittle =  "Token Moving to Raydium"
        if token_match:
            message_data["token_address"] = token_match.group(1)
        
        pattern = r'\[(电报|推特|官网)\]\((.*?)\)'
        links = re.findall(pattern, event.message.text)
        # Mengonversi hasil ke dictionary

        # Find market cap and convert
        market_cap_pattern = r"市值：\s*\*\*\$(\d+(\.\d+)?)([kKmM])\*\*"
            # Find and convert the market cap value
        market_cap_match = re.search(market_cap_pattern,  event.message.text)
        if market_cap_match:
            amount =  int(market_cap_match.group(1).split('.')[0])
            unit = market_cap_match.group(3).lower()

            # Convert 'k' or 'm' to numerical value
            if unit == 'k':
                message_data["market_cap_value"] = amount * 1_000
            elif unit == 'm':
                message_data["market_cap_value"] = amount * 1_000_000
            else:
                message_data["market_cap_value"] = amount
            #print(message_data["market_cap_value"])
        else:
            message_data["market_cap_value"] = 0
            #print("## "+ event.message.text)
            #await forward_alert_wallet("## "+ event.message.text)
        # Extract "via Bot" count if it exists
        smarter = r"💡\s*(\d+)"
        bot_count = r"🚌\s*\*\*(\d+)"
        token_match1 = re.search(r'\[(.*?)\]\((https://solscan.io/token/[\w]+)\)', event.message.text)
        bot_count = re.search(bot_count,  event.message.text)
        smarter = re.search(smarter,  event.message.text)
        token_name =""
        jp_01 = ""
        if bot_count:
            message_data["buyer_bot"] = int(bot_count.group(1))
        if token_match1:
            token_name = token_match1.group(1)
        # Extract "Smart Buyers" count if it exists
        if smarter:
            message_data["smart_buyers_count"] = int(smarter.group(1))
        ave_analitic = await call_api(message_data['token_address'])
        message_jp = get_wallet_signal_by_ca_5params(message_data['token_address'])
        numbers = list(map(int, re.findall(r'\d+', ave_analitic)))
        sent = 0
        #print(event.message.text)
        #print("_PA_PA_PA_PA_PA_AP_AP_AP_A)A_)A_)A_PA_AP_AP_APA_PA_PA11111111111111111111111111111111111111111111111111111111111111")
        print(token_name)
        formatted_message = "".join(
            [f"[ LINK ]({link})" for name, link in links]
        ) + "🔗"        
        if is_mcmoney(message_data['token_address']) and message_data['token_address'] not in token_list:
            insert_data_coin_gem(message_data['token_address'], "dex", int(message_data['market_cap_value']), None, None, None, None)
            current_time = datetime.now()
            sent = 1
            token_list[message_data['token_address']] = current_time
            await forward_alert_err(f""" 
mcmoney💰 **{tittle}** 💰 
━━━━━━━━━━━━━━━
🔹 **Token:** {token_name}
🔹 `{message_data['token_address']}`
🔹 **Market Cap:** {message_data['market_cap_value']}
🔹 **Smart Buyers:** {message_data['smart_buyers_count']}
🔹 **Buyer Bot:** {message_data['buyer_bot']}

{message_jp} 
{ave_analitic}
{formatted_message}
━━━━━━━━━━━━━━━
📈 Stay updated for more insights!
[ pf ](https://pump.fun/{message_data['token_address']}) [ bullx ](https://bullx.io/terminal?chainId=1399811149&address={message_data['token_address']})
""")

            await forward_alert1(f""" 
💰 **{tittle}** 💰 
━━━━━━━━━━━━━━━
🔹 **Token:** {token_name}
🔹 `{message_data['token_address']}`
🔹 **Market Cap:** {message_data['market_cap_value']}
🔹 **Smart Buyers:** {message_data['smart_buyers_count']}
🔹 **Buyer Bot:** {message_data['buyer_bot']}
{ave_analitic}
{formatted_message}
━━━━━━━━━━━━━━━
📈 Stay updated for more insights!
[ pf ](https://pump.fun/{message_data['token_address']}) [ bullx ](https://bullx.io/terminal?chainId=1399811149&address={message_data['token_address']})
""")

            await forward_mcap(f""" 
💰 **{tittle}** 💰 
━━━━━━━━━━━━━━━
🔹 **Token:** {token_name}
🔹 `{message_data['token_address']}`
🔹 **Market Cap:** {message_data['market_cap_value']}
🔹 **Smart Buyers:** {message_data['smart_buyers_count']}
🔹 **Buyer Bot:** {message_data['buyer_bot']}

{message_jp} 
{ave_analitic}
{formatted_message}
━━━━━━━━━━━━━━━
📈 Stay updated for more insights!
[ pf ](https://pump.fun/{message_data['token_address']}) [ bullx ](https://bullx.io/terminal?chainId=1399811149&address={message_data['token_address']})
""")
        if is_wallet_sent_by_no(1) and message_data['token_address'] not in token_list:
            print(f""" {message_data['market_cap_value']}   {message_data['smart_buyers_count']}   {numbers[0]} """)
            if (message_data['market_cap_value'] > 100000 and message_data['smart_buyers_count'] >= 3) or message_data['smart_buyers_count'] >= 29:
                if (int(message_data['smart_buyers_count'] > 15) and int(int(numbers[0]) > 30)):
                    jp_01 = "🐓"
                current_time = datetime.now()
                sent = 1
                token_list[message_data['token_address']] = current_time
                insert_data_coin_gem(message_data['token_address'], "dex", int(message_data['market_cap_value']), None, None, None, None)
                formatted_message = "".join(
                    [f"[ LINK ]({link})" for name, link in links]
                ) + "🔗"
        # Append the data for this message to the list of data packages

                await forward_alert1(f""" 
{jp_01}💰 **{tittle}** 💰 
━━━━━━━━━━━━━━━
🔹 **Token:** {token_name}
🔹 `{message_data['token_address']}`
🔹 **Market Cap:** {message_data['market_cap_value']}
🔹 **Smart Buyers:** {message_data['smart_buyers_count']}
🔹 **Buyer Bot:** {message_data['buyer_bot']}
{ave_analitic}
{formatted_message}
━━━━━━━━━━━━━━━
📈 Stay updated for more insights!
[ pf ](https://pump.fun/{message_data['token_address']}) [ bullx ](https://bullx.io/terminal?chainId=1399811149&address={message_data['token_address']})
""")
                
                await forward_mcap(f""" 
{jp_01}💰 **{tittle}** 💰 
━━━━━━━━━━━━━━━
🔹 **Token:** {token_name}
🔹 `{message_data['token_address']}`
🔹 **Market Cap:** {message_data['market_cap_value']}
🔹 **Smart Buyers:** {message_data['smart_buyers_count']}
🔹 **Buyer Bot:** {message_data['buyer_bot']}

{message_jp} 
{ave_analitic}
{formatted_message}
━━━━━━━━━━━━━━━
📈 Stay updated for more insights!
[ pf ](https://pump.fun/{message_data['token_address']}) [ bullx ](https://bullx.io/terminal?chainId=1399811149&address={message_data['token_address']})
""")
        #print("sdhghsgdhsgdjhgsjhdgshjgdhjsgdjhgshjdghjsgdjhgshsgdjshgdjhgsj0000000000000000000000000000000000000000000000000000000000000000000000000")
        upsert_wallet_signal(message_data['token_address'], 0, 0, 0, int(message_data['smart_buyers_count']), int(message_data['buyer_bot']) , 0 ,int(numbers[0]), sent)

    except Exception as e:
        print(f"ErrorC: {e}")
        tb = traceback.format_exc()
        print("An error occurred:\n", tb)
        print(f"Error55: {e}")

# sinyal dj ===================================================================================================================
'''@client.on(events.NewMessage(chats=[PeerChannel(user_check_x)]))  # Ganti dengan nama grup Anda
async def handle_new_message(event):
    try:
        print(event.message.text)
        print("_OA_OA_O_PA___YQ_YQ_YQ_QY_QYQYQ_YQ_YQ_YQ_YQ_YQ_Q_QY_QY_Q_QY_YQ_YQ_YQYQQ_Y_Q_QYY_QY_Q_YQYQ_QY_Q_YQ_YQ_QY_YQ_QY_Q_YQ_Q_YQY_QYQ_QY")

    except Exception as e:
        print(f"ErrorLOP: {e}")



@client.on(events.NewMessage(chats=[PeerChannel(cek_mcap)]))  # Ganti dengan nama grup Anda
async def handle_new_message(event):
    try:
        await forward_alert1(f"""{event.message.text}""")

    except Exception as e:
        print(f"ErrorC: {e}")
        tb = traceback.format_exc()
        print("An error occurred:\n", tb)
        print(f"Error55: {e}")'''


@client.on(events.NewMessage(chats=["@SolanaWhaleTracker"]))  # Ganti dengan nama grup Anda
async def handle_new_message(event):
    try:
        #print(event.message.text)
        #print("_PA_PA_PA_PA_PA_AP_AP_AP_A)A_)A_)A_PA_AP_AP_APA_PA_PA_PA_PA_AP_AP_APA_PA_AP_APA_PA_PA_PA_PA_PA_AP_AP_AP_AP_APA_PA_PA_AP_AP_APA_PA_AP_AP_AP_AP_APA_P_APA_PA_PA")
        match = re.search(r"```([A-Za-z0-9]+)```", event.message.text)
        if match:
            pattern1 = r'Swapped (\d+(?:\.\d+)?) #SOL'
            # Find the matching number
            match1 = re.search(pattern1, event.message.text)
            contract_address = match.group(1)
            if match1:
                integer_part = match1.group(1).split('.')[0]  # Get only the integer part before the decimal
                if int(integer_part) >= 2 and find_coin_gem_by_ca_id_and_platform_60mnt(contract_address, "dex"):
                    await forward_alert_wallet1(f"""{event.message.text}  [ bullx ](https://bullx.io/terminal?chainId=1399811149&address={contract_address})""")
                print(f"Alamat tokenzz: {contract_address}  {integer_part}")
                if is_ca_created_within_30_minutes(contract_address):
                    upsert_wallet_signal(contract_address, 0, 1, 0,  0, 0, 0, 0, 0)
            else:
                print("No match found.")

        else:
            print("Alamat kontrak tidak ditemukan.")

    except Exception as e:
        print(f"ErrorC: {e}")
        tb = traceback.format_exc()
        print("An error occurred:\n", tb)
        print(f"Error55: {e}")



@client.on(events.NewMessage(chats=["@gmgnsignals"]))  # Ganti dengan nama grup Anda
async def handle_new_message(event):
    try:
        print(event.message.text)
        #print("_PA_PA_PA_PA_PA_AP_AP_AP_A)A_)A_)A_PA_AP_AP_APA_PA_PA_PA_PA_AP_AP_APA_PA_AP_APA_PA_PA_PA_PA_PA_AP_AP_AP_AP_APA_PA_PA_AP_AP_APA_PA_AP_AP_AP_AP_APA_P_APA_PA_PA")
        match = re.search(r"```([A-Za-z0-9]+)```", event.message.text)
        if match:
            pattern1 = r'Swapped (\d+(?:\.\d+)?) #SOL'
            # Find the matching number
            match1 = re.search(pattern1, event.message.text)
            contract_address = match.group(1)
            if match1:
              print(f"Alamat tokenzz: {contract_address} ")
      
            else:
                print("No match found.")

        else:
            print("Alamat kontrak tidak ditemukan.")

    except Exception as e:
        print(f"ErrorC: {e}")
        tb = traceback.format_exc()
        print("An error occurred:\n", tb)
        print(f"Error55: {e}")




@client.on(events.NewMessage(chats=["@signalsolanaby4am"]))  # Ganti dengan nama grup Anda
async def handle_new_message(event):
    try:
        print(event.message.text)
        print("_77777777777777777777PA_PA_PA_PA_PA_AP_AP_AP_A)A_)A_)A_PA_AP_AP_APA_PA_PA_PA_PA_AP_AP_APA_PA_AP_APA_PA_PA_PA_PA_PA_AP_AP_AP_AP_APA_PA_PA_AP_AP_APA_PA_AP_AP_AP_AP_APA_P_APA_PA_PA")
        #await forward_alert_wallet1(f"""{event.message.text}""")
        cap=0
        sm = 0
        match = re.search(r"(?<=\*\*CA:\*\*\s)[A-Za-z0-9]+", event.message.text)
        market_cap_pattern = r"Marketcap:\*\*\s*\$([\d,]+(\.\d+)?)([kKmM]?)"
            # Find and convert the market cap value
        market_cap_match = re.search(market_cap_pattern,  event.message.text)
        if market_cap_match:
            # Find and convert the market cap value
            amount = int(market_cap_match.group(1).replace(',', '').split('.')[0])
            unit = market_cap_match.group(3).lower()

            # Convert 'k' or 'm' to numerical value
            if unit == 'k':
                cap = amount * 1_000
            elif unit == 'm':
                cap = amount * 1_000_000
            else:
                cap = amount
            #print(message_data["market_cap_value"])
        else:
           cap = 0
        print(cap)
        if match:
            value = match.group(0)
            print("Value after CA:", value)
            jp_01 = ""
            message_jp = get_wallet_signal_by_ca_5params(value)
            sent = 0
            data = get_wallet_list_by_ca(value)
            ave_analitic = await call_api(value)
            numbers = list(map(int, re.findall(r'\d+', ave_analitic)))
            if numbers:
                sm = int(numbers[0])
            if data and not find_coin_gem_by_ca_id_and_platform_xmnt(value, "dex", 15) and is_wallet_signal_created_within_5_minutes(value) and value not in token_list:
                 if sm > 7 and cap > 200000 :
                    if (int(data[3]) > 15 and int(data[6]) > 30):
                        jp_01 = "🐓"
                    sent = 1
                    current_time = datetime.now()
                    token_list[value] = current_time
                    #gmgn_data = await fetch_gmgn(token_address)
                    input_text = hapus_teks(event.message.text)
            upsert_wallet_signal(value, 0, 0, 0, 0, 0, 0, 0, sent)
        #print("_77777777777777777777PA_PA_PA_PA_PA_AP_AP_AP_A)A_)A_)A_PA_AP_AP_APA_PA_PA_PA_PA_AP_AP_APA_PA_AP_APA_PA_PA_PA_PA_PA_AP_AP_AP_AP_APA_PA_PA_AP_AP_APA_PA_AP_AP_AP_AP_APA_P_APA_PA_PA")

    except Exception as e:
        print(f"ErrorC: {e}")
        tb = traceback.format_exc()
        print("An error occurred:\n", tb)
        print(f"Error55: {e}")


@client.on(events.NewMessage(chats=["@solana_whales_signal"]))  # Ganti dengan nama grup Anda
async def handle_new_message(event):
    try:
        #print(event.message.text)
        #print("_PA_PA_PA_PA_PA_AP_AP_AP_A)A_)A_)A_PA_AP_AP_APA_PA_PA_PA_PA_AP_AP_APA_PA_AP_APA_PA_PA_PA_PA_PA_AP_AP_AP_AP_APA_PA_PA_AP_AP_APA_PA_AP_AP_AP_AP_APA_P_APA_PA_PA")
        match = re.search(r"Token: `([A-Za-z0-9]+)`", event.message.text)

        if match:
            token_address = match.group(1)
            pattern1 =  r'Swapped \*\*(\d+(?:\.\d+)?)\*\* #SOL'
            # Find the matching number
            match1 = re.search(pattern1, event.message.text)
            if match1 and "#85% HIGH WINRATE" not in event.message.text  and "xiaomaogaoqian" not in event.message.text and "$TWC" not in event.message.text:
                integer_part = match1.group(1).split('.')[0]  # Get only the integer part before the decimal
                if int(integer_part) >= 2 and find_coin_gem_by_ca_id_and_platform_60mnt(token_address, "dex"):
                    if token_address not in signal_list:
                        current_time = datetime.now()
                        signal_list[token_address] = current_time
                        if int(integer_part) >= 7 and find_coin_gem_by_ca_id_and_platform_60mnt(token_address, "dex"):
                            await forward_coba(f"""
{event.message.text} 
━━━━━━━━━━━━━━━━━━
📈 Stay updated for more insights! [ bullx ](https://bullx.io/terminal?chainId=1399811149&address={token_address})
""")
                        await forward_alert_err(f"""
{event.message.text} 
━━━━━━━━━━━━━━━━━━
📈 Stay updated for more insights! [ bullx ](https://bullx.io/terminal?chainId=1399811149&address={token_address})
""")
                    await forward_alert_wallet1(f"""{event.message.text}   [ bullx ](https://bullx.io/terminal?chainId=1399811149&address={token_address})""")
                    
                print(f"Alamat tokenjj: {token_address} {integer_part}")
                if is_ca_created_within_30_minutes(token_address) or "#PumpFun" in event.message.text:
                    upsert_wallet_signal(token_address, 1, 0, 0,  0 , 0 , 0, 0, 0)
            else:
                print("No match found.")
            

        
    except Exception as e:
        print(f"ErrorC: {e}")
        tb = traceback.format_exc()
        print("An error occurred:\n", tb)
        print(f"Error55: {e}")

@client.on(events.NewMessage(chats=["@MomentumTrackerEN"]))  # Ganti dengan nama grup Anda
async def handle_new_message(event):
    try:
        #print(event.message.text)
        #print("_PA_PA_PA_PA_PA_AP_AP_AP_A)A_)A_)A_PA_AP_AP_APA_PA_PA11111111111111111111111111111111111111111111111111111111111111")
        token_match = re.search(r'\[(.*?)\]\((https://solscan.io/token/[\w]+)\) \((.*?)\)', event.message.text)
        contract_match = re.search(r'`([\w]+)`',  event.message.text)
        calls_match = re.search(r"CALLS - (\d+)", event.message.text)
        marketcap_match = re.search(r"Marketcap:\s\*\*\$(\d{1,3}(?:,\d{3})*(?:\.\d{1,2})?)\*\*", event.message.text)
        marketcap_value = 0
        twitter_pattern = r"🟢 \[Twitter\]\((.*?)\)"
        # Cari semua link Twitter dengan penanda tersebut
        twitter_links = ""
        twitter_links = re.findall(twitter_pattern, event.message.text)
        
        jp_01 = ""
        if marketcap_match:
            marketcap = marketcap_match.group(1)
            marketcap = marketcap.replace(",", "")  # Hapus koma dari angka
            marketcap_value = float(marketcap)  # Konversi ke float untuk perhitungan lebih lanjut
            print(f"Marketcap: ${marketcap_value}")
        if token_match:
            token_address = token_match.group(1)
            contract_address = contract_match.group(1)
            calls_count = calls_match.group(1)
            #print("_PA_PA_PA_PA_PA_AP_AP_AP_A)A_)A_)A_PA_AP_AP_APA_PA_PA11111111111111111111111111111111111111111111111111111111111111")
            print(f"Alamat token: {token_address}  Alamat kontrak: {contract_address}  Jumlah panggilan: {calls_count}")
            message_jp = get_wallet_signal_by_ca_5params(contract_address)
            match = re.search(r'ray_wallet: (\d+)', message_jp)
            ray_wallet_value = 0
            if match:
                ray_wallet_value = int(match.group(1))
                print(f"ray_wallet: {ray_wallet_value}")
            sent = 0
            data = get_wallet_list_by_ca(contract_address)
            print(data)
            print(is_wallet_signal_created_within_5_minutes(contract_address))
            if ray_wallet_value == 0 and data and int(marketcap_value) > 40000 and int(calls_count) > 2 and not find_coin_gem_by_ca_id_and_platform_xmnt(contract_address, "dex", 15) and is_wallet_signal_created_within_5_minutes(contract_address) and contract_address not in token_list: 
                if (int(data[3]) > 2 and int(data[6]) > 7) or (int(data[3]) > 8 and int(data[6]) > 2):
                    if (int(data[3]) > 15 and int(data[6]) > 30):
                        jp_01 = "🐓"
                    ave_analitic = await call_api(contract_address)
                    sent = 1
                    current_time = datetime.now()
                    token_list[contract_address] = current_time
                    #gmgn_data = await fetch_gmgn(token_address)
                    #insert_data_coin_gem(contract_address, "dex", int(marketcap_value), None, None, None, None)
                    await forward_alert(f"""
{jp_01}💰Token Information 
━━━━━━━━━━━━━━━
🔹 Token: {token_address}
🔹 <code>{contract_address}</code>
🔹 Market Cap: {marketcap_value}
🔹 Momentum calls: {calls_count}
🔹 Link X: {twitter_links}

{message_jp} 
{ave_analitic}
━━━━━━━━━━━━━━━
📈 Stay updated for more insights!
<a href="https://pump.fun/{contract_address}">pf</a> <a href="https://bullx.io/terminal?chainId=1399811149&address={contract_address}">bullx</a>
""")
            
            upsert_wallet_signal(contract_address, 0, 0, 0, 0, 0, int(calls_count), 0, sent)


        
        
    except Exception as e:
        print(f"ErrorC: {e}")
        tb = traceback.format_exc()
        print("An error occurred:\n", tb)
        print(f"Error55: {e}")
        


@client.on(events.NewMessage(chats=["@solana_alerts_dogeebot"]))  # Ganti dengan nama grup Anda
async def handle_new_message(event):
    try:
        #print(event.message.text)
        print("_PA_PA_PA_PA_PA_AP_AP_AP_A)A_)A_)A_PA_AP_AP_APA_PA_PA_PA_PA_AP_AP_APA_PA_AP_APA_PA_PA_PA_PA_PA_AP_AP_AP_AP_APA_PA_PA_AP_AP_APA_PA_AP_AP_AP_AP_APA_P_APA_PA_PA")
        converted_text = convert_text(event.message.text)
        #await forward_alert_err(converted_text)
    except Exception as e:
        print(f"ErrorC: {e}")

def hapus_teks(input_string):
    # Hapus teks "Copyright © 4AM"
    hasil_setelah_copyright = input_string.replace("Copyright © 4AM", "")
    
    # Hapus teks mulai dari 🎯 hingga ⌛️
    pola_1 = r"🎯.*"
    hasil_setelah_pola1 = re.sub(pola_1, "", hasil_setelah_copyright)
    
    # Hapus teks mulai dari 💹 hingga akhir teks
    pola_2 = r"💹.*"
    hasil_akhir = re.sub(pola_2, "", hasil_setelah_pola1)
    
    return hasil_akhir

import re

def hapus_teks_gmgn(input_string, pf):

    pola_1 = r"💰"
    input_string1 = re.sub(pola_1, pf, input_string)

    pola_11 = r"💊"
    input_string11 = re.sub(pola_11, pf, input_string1)

    pola_2 = r"^.*⚡️.*$"
    hasil_akhir2 = re.sub(pola_2, "", input_string11, flags=re.MULTILINE)

    pola_3 = r"^.*🌈.*$"
    hasil_akhir3 = re.sub(pola_3, "", hasil_akhir2, flags=re.MULTILINE)

    pola_4 = r"^.*📢.*$"
    hasil_akhir4 = re.sub(pola_4, "", hasil_akhir3, flags=re.MULTILINE)

    pola_5 = r"^.*💎.*$"
    hasil_akhir5 = re.sub(pola_5, "", hasil_akhir4, flags=re.MULTILINE)

    pola_6 = r"^.*backup bot:.*$"
    hasil_akhir6 = re.sub(pola_6, "", hasil_akhir5, flags=re.MULTILINE)

    pola_7 = r"^.*Backup BOT:.*$"
    hasil_akhir7 = re.sub(pola_7, "", hasil_akhir6, flags=re.MULTILINE)

    pola_8 = r"^.*NEW*"
    hasil_akhir8 = re.sub(pola_8, "", hasil_akhir7, flags=re.MULTILINE)

    pola_9 = r"^.*NEW*"
    hasil_akhir9 = re.sub(pola_9, "", hasil_akhir8, flags=re.MULTILINE)

    # Menghapus baris kosong yang mungkin tertinggal
    hasil_akhir9 = re.sub(r"^\s*\n", "", hasil_akhir9, flags=re.MULTILINE)

    return hasil_akhir9



def convert_text(text):
    # Mengubah bagian judul dan kontrak
    converted_text = "📈 **Token Launch on Raydium**\n\n"
    contract_address = ""
    # Menemukan token dan contract
    token_match = re.search(r'\[(.*?)\]\((https://solscan.io/token/[\w]+)\) \((.*?)\)', text)
    contract_match = re.search(r'`([\w]+)`', text)
    
    if token_match and contract_match:
        token_name = token_match.group(1)
        token_url = token_match.group(2)
        contract_address = contract_match.group(1)
        converted_text += f"**Token:** [{token_name}]({token_url}) \n**Contract:** `{contract_address}`\n\n"
    
    # Menangkap jumlah Smart Buyers dari teks
    smart_buyers_total_match = re.search(r'💡 (\d+) Smart Buyers 🔥', text)
    smart_buyers_total = smart_buyers_total_match.group(1) if smart_buyers_total_match else "Unknown"
    converted_text += f"**🔥 Smart Buyers ({smart_buyers_total})**\n"
    
    # Menambahkan informasi Smart Buyers
    for buyer_match in re.finditer(r'┣ \[(.*?)\]\((.*?)\) / Winrate: (.*?)% / BuyTX: (\d+) / PNL: \$(.*?) ', text):
        buyer_name = buyer_match.group(1)
        buyer_url = buyer_match.group(2)
        winrate = buyer_match.group(3)
        buy_tx = buyer_match.group(4)
        pnl = buyer_match.group(5)
        converted_text += f"┣ **[{buyer_name}]({buyer_url})**\n&emsp;**Winrate:** {winrate}% | **Buys:** {buy_tx} | **PNL:** ${pnl}K 🆕\n"
    
    # Menambahkan informasi Bot Buyers jika ada
    bot_buyers_total_match = re.search(r'\*\*(\d+)\*\* Buyers via Bot', text)
    bot_buyers_total = bot_buyers_total_match.group(1) if bot_buyers_total_match else "Unknown"
    converted_text += f"\n**Bot Buyers (Total: {bot_buyers_total})**\n"
    
    # Menambahkan detail Bot Buyers jika ada
    bot_buyers_match = re.search(r'├ Bonk: (\d+) / SolTBot: (\d+)\n├ Trojan: (\d+) / pepebot: (\d+)\n└ Bullx: (\d+) / Photon: (\d+)', text)
    if bot_buyers_match:
        bonk, soltb, trojan, pepe, bullx, photon = bot_buyers_match.groups()
        converted_text += f"├ Bonk: **{bonk}** | SolTBot: **{soltb}**\n├ Trojan: **{trojan}** | pepebot: **{pepe}**\n└ Bullx: **{bullx}** | Photon: **{photon}**\n"

    # Menambahkan token information
    token_info_match = re.search(r'Open Time: (.*?)\nMarket Cap: \$(.*?)K\nLiquidity: \$(.*?)K / SOL Pool: (.*?)\nPrice: \$(.*?)\nRenounced ✅ Burned ✅ Freeze ✅', text)
    if token_info_match:
        open_time, market_cap, liquidity, sol_pool, price = token_info_match.groups()
        converted_text += f"\n**Token Info**\n├ **Open:** {open_time}\n├ **Market Cap:** ${market_cap}K\n├ **Liquidity:** ${liquidity}K (SOL Pool: {sol_pool})\n└ **Price:** ${price}\n"

    # Menambahkan dev information
    dev_info_match = re.search(r'Dev Current Holding: (.*?)%\nDev Wallet Balance: (.*?) SOL\nTop 10 Holdings: (.*?)%', text)
    if dev_info_match:
        dev_holding, wallet_balance, top_holdings = dev_info_match.groups()
        converted_text += f"\n**Dev Info**\n├ **Dev Holding:** {dev_holding}%\n├ **Dev Wallet:** {wallet_balance} SOL\n└ **Top 10 Holdings:** {top_holdings}%\n"

    link_match = re.findall(r'\[(.*?)\]\((.*?)\)', text)
    for link_name, link_url in link_match:
        if link_name not in ['ENQLC', 'DC5BD', 'AAHBH']:  # skip buyer links already added above
            converted_text += f"🔗 [{link_name}]({link_url})"

    
    converted_text += f"[ bullx ](https://bullx.io/terminal?chainId=1399811149&address={contract_address}))"

    return converted_text

# sinyal prefer ==============================================================================================================
''''
@client.on(events.NewMessage(chats=["@preferrichroom"]))  # Ganti dengan nama grup Anda
async def handle_new_message(event):
    try:
        sender = await event.get_sender()
        sender_id = sender.id
        sender_username = sender.username
        if sender_username == "elroybandicoot" or sender_username == "elroysadrakh" or sender_username == "godstonk" or sender_username == "limehizel" or sender_username == "captainJedi" or sender_username == "vannightmare" or sender_username == "donRichX" or sender_username == "jojobmnn" or sender_username == "chenzeth" :   
            await forward_rick_bot(event.message.text+" sinyalprefer", event.message.media)
            #print(event.message.text)
            if "grup" in event.message.text or "cto" in event.message.text or "aped" in event.message.text or "play" in event.message.text or "$" in event.message.text or "chads" in event.message.text or "one" in event.message.text or "dj" in event.message.text or "Dj" in event.message.text:
                await forward_trend(event.message.text+"  #sinyalPreferGrup" + str(sender_username))
            if "buatin tg" in event.message.text or "setup tg" in event.message.text or "Buatin tg" in event.message.text:
                 await forward_msg(event.message.text+"  #sinyalCTOLuca" + str(sender_username))

    except Exception as e:
        print(f"ErrorL: {e}")
'''

# news all ============================================================================================================== 
async def fetch_news(session, url):
    try:
        async with session.get(url) as response:
            if response.status == 200:
                return await response.json()
            else:
                print(f"Request failed with status code {response.status}")
                return []
    except aiohttp.ClientOSError as e:
        print(f"ClientOSError: {e}")
    except asyncio.TimeoutError:
        print("Request timeout")
        
async def send_post_request_pos(session, endpoint, title, suggestions):
    coin=""
    for suggestion in suggestions:
        coin = suggestion.get('coin')
        if coin:
            a=""
        else:
            coin = ""
    payload = {
        "model": "llama3",
        "prompt": f"{title} , do you think the News will have a very huge positive price impact on the its {coin} crypto market? , please answer just with one word either Yes or No !",
        "stream": False
    }
    try:
        async with session.post(endpoint, json=payload) as response:
            if response.status == 200:
                response_data = await response.json()
                response_text = response_data.get('response', 'No response field found')
                print(f"Response from POST request POS: {response_text}")
                if response_text == "Yes":
                    print(f"Title: {title}")
                    print(f"Coin: {coin}")
                    await forward_news(title+" "+"Coin: "+coin+" POS")
            else:
                print(f"Failed to send POST request for title: {title} with status code {response.status}")
    except aiohttp.ClientOSError as e:
        print(f"ClientOSError: {e}")
    except asyncio.TimeoutError:
        print("Request timeout")

async def send_post_request_neg(session, endpoint, title, suggestions):
    coin=""
    for suggestion in suggestions:
        coin = suggestion.get('coin')
        if coin:
            a=""
        else:
            coin = ""
    payload = {
        "model": "llama3",
        "prompt": f"{title} , do you think the News will have a very huge negative price impact on the its {coin} crypto market? , please answer just with one word either Yes or No !",
        "stream": False
    }
    try:
        async with session.post(endpoint, json=payload) as response:
            if response.status == 200:
                response_data = await response.json()
                response_text = response_data.get('response', 'No response field found')
                #print(f"Response from POST request NEG: {response_text}")
                if response_text == "Yes":
                    #print(f"Title: {title}")
                    #print(f"Coin: {coin}")
                    await forward_news(title+" "+"Coin: "+coin+" NEG")
            else:
                print(f"Failed to send POST request for title: {title} with status code {response.status}")
    except aiohttp.ClientOSError as e:
        print(f"ClientOSError: {e}")
    except asyncio.TimeoutError:
        print("Request timeout")

async def fetch_and_post_news():
    fetch_url = "https://news.treeofalpha.com/api/news?limit=10"
    post_endpoint = "http://localhost:11434/api/generate"
    previous_ids = set()

    async with aiohttp.ClientSession() as session:
        while True:
            try:
                data = await fetch_news(session, fetch_url)
                if data is not None and len(data) > 0:
                    current_ids = {item['_id'] for item in data}

                    # Find new ids by subtracting previous_ids from current_ids

                    for item in data:
                        if item['_id'] not in previous_ids:
                            await send_post_request_pos(session, post_endpoint, item['title'], item.get('suggestions', []))
                            await send_post_request_neg(session, post_endpoint, item['title'], item.get('suggestions', []))

                    # Update previous_ids
                    previous_ids = current_ids

                    # Sleep for 1 second before the next request
                    await asyncio.sleep(15)
            except Exception as e:
                print(f"ErrorN: {e}")
# news all ============================================================================================================== 
def convert_to_int(value, unit):
    if unit == 'k':
        return int(value) * 1000
    elif unit == 'm':
        return int(value) * 1000000

async def search_messages(chat_id):
    global buyer_bot
    # Dapatkan waktu 40 menit yang lalu
    forty_minutes_ago = datetime.now() - timedelta(minutes=40)
    
    # Inisialisasi variabel untuk menyimpan pesan terbaru
    recent_message = None
    
    # Cari pesan yang mengandung kata kunci dalam waktu 40 menit terakhir
    async for message in client.iter_messages(chat_id, offset_date=forty_minutes_ago, limit=30):
        #print(message.text.lower())
        if  "heavy bought" in  message.text.lower():
            # 1. Regex untuk mendapatkan value dalam backtick
            pattern_backtick = r"`(.*?)`"
            matches_backtick = re.findall(pattern_backtick, message.text)
            time = False
            time_in_minutes =1000
            holder_value =0
            mcp_value = 0
            sm = 0

            pattern_holder = r"👥 holder: \*\*(\d+)\*\*"

            match_holder = re.search(pattern_holder,  message.text.lower())

            if match_holder:
                holder_value = int(match_holder.group(1))
                #print(f"Value holder: {holder_value}")

            pattern_mcp = r"mcp: \*\*\$(\d+)(?:\.\d+)?([km])\*\*"

            match_mcp = re.search(pattern_mcp, message.text.lower())

            if match_mcp:
                value, unit = match_mcp.groups()
                mcp_value = convert_to_int(value, unit)
                #print(f"Value mcp: {mcp_value}")
            else:
                print("Value mcp tidak ditemukan.")
            # 2. Regex untuk mencari waktu setelah 'open' (detik, menit, jam, hari)
            pattern_open_time = r"🕒 open: \*\*(\d+)([a-zA-Z]+)\*\*"
            match_open_time = re.search(pattern_open_time,message.text.lower())
            if match_open_time:
                value = int(match_open_time.group(1))  # Angka waktu
                unit = match_open_time.group(2)  # Satuan waktu (s, min, h, d)

                # Konversi ke menit
                if unit == "s":
                    time_in_minutes = value / 60
                elif unit == "min":
                    time_in_minutes = value
                elif unit == "h":
                    time_in_minutes = value * 60
                elif unit == "d":
                    time_in_minutes = value * 1440  # 1 hari = 1440 menit

                # Mengecek apakah kurang dari 15 menit
                if time_in_minutes < 15:
                    time = True
                    #print(f"Open time is less than 15 minutes ago: {time_in_minutes} minutes")
            else:
                print("Open time not found.")
            
            if matches_backtick and "EX3qFX3AYh6Hv3UDG6B2nnvgeWJUGRBSqi7g6QT5yE18" not in message.text and "D2vZhPW1mtZDcB1yxiErebPcsYBvsCKrieYGWkcSVxp6" not in message.text:
                ave_analitic = await call_api(matches_backtick[0])
                #print(f"Value dalam backtick: {matches_backtick}")
                if find_coin_gem_by_ca_id_and_platform_60mnt(matches_backtick[0], "dex") or find_coin_gem_by_ca_id_and_platform_xmnt(matches_backtick[0],"vol",30) and matches_backtick[0] in token_list:
                    if matches_backtick[0] not in signal_list:
                        current_time = datetime.now()
                        signal_list[matches_backtick[0]] = current_time
                        jp="💊"
                        if any(item in message.text for item in check_wallet):
                            jp="🐓"
                        input_text = hapus_teks_gmgn(message.text , f"""[ {jp} ](https://pump.fun/{matches_backtick[0]})""")
                        if time_in_minutes <= 7 and find_coin_gem_by_ca_id_and_platform_60mnt(matches_backtick[0], "dex"):
                            await forward_coba(f"""
{input_text} 
━━━━━━━━━━━━━━━━━━
{ave_analitic}

📈 Stay updated for more insights! [ bullx ](https://bullx.io/terminal?chainId=1399811149&address={matches_backtick[0]})
""")

                        await forward_alert_err(f"""
{input_text} 
━━━━━━━━━━━━━━━━━━
{ave_analitic}

📈 Stay updated for more insights! [ bullx ](https://bullx.io/terminal?chainId=1399811149&address={matches_backtick[0]})
""")
                if (time or find_coin_gem_by_ca_id_and_platform_xmnt(matches_backtick[0],"pf",15)) and not find_coin_gem_by_ca_id_and_platform(matches_backtick[0], "vol"):
                    ave_analitic = await call_api(matches_backtick[0])
                    numbers = list(map(int, re.findall(r'\d+', ave_analitic)))
                    if numbers:
                        sm = int(numbers[0])
                    jp=""
                    insert_data_coin_gem(matches_backtick[0], "vol", 100000, None, None, None, None)
                    insert_data_signal(matches_backtick[0],holder_value,sm,time_in_minutes,mcp_value)
                    #print(f"Value dalam backtick: {matches_backtick[0]}")
                    input_text = hapus_teks_gmgn(message.text , f"""[ 💊 ](https://pump.fun/{matches_backtick[0]})""")
                    if (holder_value >= 200 and sm >= 20 and time_in_minutes <=1 and mcp_value >= 150000) or (holder_value >= 150 and sm >= 5 and time_in_minutes <=2 and mcp_value <= 40000) or (holder_value >= 50 and sm >= 15 and time_in_minutes <=11 and mcp_value >= 1000000):
                        jp = "🐓"
                        await forward_alert1(f"""
{jp}{input_text} 
━━━━━━━━━━━━━━━━━━
{ave_analitic}

📈 Stay updated for more insights! [ bullx ](https://bullx.io/terminal?chainId=1399811149&address={matches_backtick[0]})
""")

                    
            else:
                print("Tidak ada nilai dalam backtick.")
        if  "kol buy" in  message.text.lower():
            time_in_minutes =1000
            mcp_value = 0
            pattern_backtick = r"`(.*?)`"
            matches_backtick = re.findall(pattern_backtick, message.text)
            pattern_before_kol_buy = r"(\d+)\s+kol\s+buy"
            value_before_kol_buy = 0
            match = re.search(pattern_before_kol_buy, message.text)

            if match:
                value_before_kol_buy = match.group(1)
                print(f"Value sebelum kol buy: {value_before_kol_buy}")
            else:
                print("Value sebelum kol buy tidak ditemukan.")
                
            if matches_backtick:
                print(f"Value dalam backtick: {matches_backtick}")
            if find_coin_gem_by_ca_id_and_platform_60mnt(matches_backtick[0], "dex") or find_coin_gem_by_ca_id_and_platform_60mnt(matches_backtick[0], "pf") or find_coin_gem_by_ca_id_and_platform_xmnt(matches_backtick[0],"vol",30):
                if matches_backtick[0] not in kol_buy:
                    kol_buy[matches_backtick[0]] = {}
                    await forward_alert_wallet1(f"""{message.text}  [ bullx ](https://bullx.io/terminal?chainId=1399811149&address={matches_backtick[0]})""")
                    await forward_alert_err(f"""{message.text}  [ bullx ](https://bullx.io/terminal?chainId=1399811149&address={matches_backtick[0]})""")
                    pattern_open_time = r"🕒 open: \*\*(\d+)([a-zA-Z]+)\*\*"
                    match_open_time = re.search(pattern_open_time,message.text.lower())
                    if match_open_time:
                        value = int(match_open_time.group(1))  # Angka waktu
                        unit = match_open_time.group(2)  # Satuan waktu (s, min, h, d)

                        # Konversi ke menit
                        if unit == "s":
                            time_in_minutes = value / 60
                        elif unit == "min":
                            time_in_minutes = value
                        elif unit == "h":
                            time_in_minutes = value * 60
                        elif unit == "d":
                            time_in_minutes = value * 1440  # 1 hari = 1440 menit

                        # Mengecek apakah kurang dari 15 menit
                        if time_in_minutes < 15:
                            time = True
                            #print(f"Open time is less than 15 minutes ago: {time_in_minutes} minutes")
                    else:
                        print("Open time not found.")
                    pattern_mcp = r"mcp: \*\*\$(\d+)(?:\.\d+)?([km])\*\*"

                    match_mcp = re.search(pattern_mcp, message.text.lower())

                    if match_mcp:
                        value, unit = match_mcp.groups()
                        mcp_value = convert_to_int(value, unit)
                        #print(f"Value mcp: {mcp_value}")
                    else:
                        print("Value mcp tidak ditemukan.")

                    if time_in_minutes <=5 and matches_backtick[0] not in token_list:
                        await forward_alert1(f"""{message.text}  [ bullx ](https://bullx.io/terminal?chainId=1399811149&address={matches_backtick[0]})""")
                        await forward_mcap(f"""{message.text}  [ bullx ](https://bullx.io/terminal?chainId=1399811149&address={matches_backtick[0]})""")
                        insert_data_coin_gem(matches_backtick[0], "dex", int(mcp_value), None, None, None, None)
                elif kol_buy[matches_backtick[0]]['kol_qty'] < value_before_kol_buy:
                    await forward_alert_wallet1(f"""{message.text}  [ bullx ](https://bullx.io/terminal?chainId=1399811149&address={matches_backtick[0]})""")
                kol_buy[matches_backtick[0]]['kol_qty'] = value_before_kol_buy

        

            
            
    # Jika ada pesan yang ditemukan, tampilkan dan kembalikan True
    '''if recent_message:
        bot_count = re.search(r"via Bot: (\d+)", recent_message.text)

        if bot_count:
            #print("Buyers via Bot:", int(bot_count.group(1))) 
            buyer_bot = int(bot_count.group(1))
        #print(f"Pesan terbaru: {recent_message.text}")
        match = re.search(r'💡 \*\*(\d+)\*\* Smart Buyers', recent_message.text)
        if match:
            smart_buyers_count = match.group(1)
        #await forward_alert_err("▶️ "+recent_message.text)'''
    return False



async def search_messages_all_5minutes(chat_id, keyword):
    # Set 40 minutes ago
    two_minutes_ago_wib = datetime.now(timezone(timedelta(hours=7))) - timedelta(minutes=2)
    # Initialize list to store each message's data package
    data_packages = []
    # Regex pattern for the token address as 39+ alphanumeric characters

    # Search for messages containing the keyword within the last 40 minutes
    async for message in client.iter_messages(chat_id, search=keyword, offset_date=two_minutes_ago_wib, limit=5):
        #print(message)
        if  keyword.lower() in message.text.lower():
            # Initialize a dictionary to store data for this message
            message_data = {
                "token_address": None,
                "market_cap_value": None,
                "smart_buyers_count": None,
                "buyer_bot": None
            }
            
            token_pattern = r"token/([a-zA-Z0-9]+)"
            # Pattern for the market cap with both uppercase and lowercase K/M within double asterisks
            market_cap_pattern = r"market cap: \*\*\$(\d+(\.\d+)?)([kKmM])\*\*"
            #print(message.text)
            # Find token address
            token_match = re.search(token_pattern, message.text)
            if token_match:
                message_data["token_address"] = token_match.group(1)

            # Find market cap and convert
            market_cap_pattern = r"[Mm]arket [Cc]ap:\s*\*\*\$(\d+(\.\d+)?)([kKmM])\*\*"
                # Find and convert the market cap value
            market_cap_match = re.search(market_cap_pattern, message.text)
            if market_cap_match:
                amount =  int(market_cap_match.group(1).split('.')[0])
                unit = market_cap_match.group(3).lower()

                # Convert 'k' or 'm' to numerical value
                if unit == 'k':
                    message_data["market_cap_value"] = amount * 1_000
                elif unit == 'm':
                    message_data["market_cap_value"] = amount * 1_000_000
                else:
                    message_data["market_cap_value"] = amount
                #print(message_data["market_cap_value"])
            else:
                message_data["market_cap_value"] = 67000
                #print("## "+message.text)
                #await forward_alert_wallet("## "+message.text)
            # Extract "via Bot" count if it exists
            bot_count = re.search(r"via Bot: (\d+)", message.text)
            if bot_count:
                message_data["buyer_bot"] = int(bot_count.group(1))
            
            # Extract "Smart Buyers" count if it exists
            match = re.search(r'💡 \*\*(\d+)\*\* Smart Buyers', message.text)
            if match:
                message_data["smart_buyers_count"] = int(match.group(1))

            # Append the data for this message to the list of data packages
            data_packages.append(message_data)

    # Return the list of data packages
    return data_packages


async def search_messages_whale1(keyword):
    # Replace with the actual username or chat ID
    chat_id = "@solana_whales_signal"  
    
    # Set the time threshold to 40 minutes ago
    forty_minutes_ago = datetime.now() - timedelta(minutes=40)
    
    # Initialize counter for the number of messages found
    message_count = 0
    
    # Search for messages containing the keyword within the last 40 minutes
    async for message in client.iter_messages(chat_id, search=keyword, offset_date=forty_minutes_ago):
        if keyword.lower() in message.text.lower():
            message_count += 1  # Increment the counter for each matching message
    
    # Return the total count of matching messages
    return message_count



async def search_messages_whale2(keyword):
    # Replace with the actual username or chat ID
    chat_id = "@SolanaWhaleTracker"  
    
    # Set the time threshold to 40 minutes ago
    forty_minutes_ago = datetime.now() - timedelta(minutes=40)
    
    # Initialize counter for the number of messages found
    message_count = 0
    
    # Search for messages containing the keyword within the last 40 minutes
    async for message in client.iter_messages(chat_id, search=keyword, offset_date=forty_minutes_ago):
        if keyword.lower() in message.text.lower():
            message_count += 1  # Increment the counter for each matching message
    
    # Return the total count of matching messages
    return message_count

async def search_messages_ray_wallet(keyword):
    # Replace with the actual chat ID
    chat_id = -2198583984  # This is the numeric chat ID
    
    # Set the time threshold to 40 minutes ago
    forty_minutes_ago = datetime.now() - timedelta(minutes=40)
    
    # Initialize counter for the number of messages found
    message_count = 0
    
    # Use PeerChannel if it's a channel, or PeerChat if it's a group chat
    # Here, we assume it's a channel; if it’s a group, use PeerChat
    async for message in client.iter_messages(PeerChannel(chat_id), search=keyword, offset_date=forty_minutes_ago):
        if keyword.lower() in message.text.lower():
            message_count += 1  # Increment the counter for each matching message
    
    # Return the total count of matching messages
    return message_count

# ricky 5 menit awal ============================================================================================================== 
def datetime_converter(o):
    if isinstance(o, datetime):
        return o.__str__()


async def chek_run_position(run ,token_address ):
    global run_position
    run_position = run
    while True:
        await asyncio.sleep(30)
        if run_position == False:
            await forward_alert_wallet("batas==========================================================================================================================================================")
            break
        try:
            ave_analitic = await call_api(token_address)
            message_jp = get_wallet_signal_by_ca(token_address)
            await forward_alert_wallet(f"""
/th {token_address}                                         
""")
            await forward_alert_wallet(f"""
{message_jp}
{ave_analitic}                                           
"""
            )

        except Exception as e:
            tb = traceback.format_exc()
            print("An error occurred:\n", tb)
            print(f"Error55: {e}")
    
async def chek_ten_minutes():
    while True:
        await asyncio.sleep(20)
        try:
            if cek_menit_kelipatan_15():
                current_time = datetime.now()
                date_time_hanya_menit = current_time.strftime("%Y-%m-%d %H:%M")
                if date_time_hanya_menit not in token_mcap:
                    token_mcap[date_time_hanya_menit] = current_time
                    await forward_mcap("/calls@Phanes_bot")
            '''if cek_menit_kelipatan_16():
                current_time = datetime.now()
                date_time_hanya_menit = current_time.strftime("%Y-%m-%d %H:%M")
                if date_time_hanya_menit not in token_mcap:
                    token_mcap[date_time_hanya_menit] = current_time
                    mess = await get_last_message()
                    #if "Tidak" not in mess:
                    #    await forward_alert1(f""" {mess} """)'''
            entity1 = "@gmgnsignals"
            await search_messages(entity1)
            '''
            recent_tokens = get_recent_wallet_signal_tokens()
            for token_address in recent_tokens:
                print("token cari1:" + token_address)
                if not find_coin_gem_by_ca_id_and_platform_60mnt(token_address, "dex"):
                    total_smart_alpha = await search_messages(entity1, token_address)
                    print(total_smart_alpha)
                    print("token cari:" + token_address)
                    if total_smart_alpha:
                        await forward_alert_wallet1(f"##Signal Heavy Bougth:  <code>{token_address}<code>\n  [ bullx ](https://bullx.io/terminal?chainId=1399811149&address={token_address}))")
                    #    upsert_wallet_signal(token_address, 0, 0, 0,  total_smart_alpha ,  0)'''
                
            #message_jp = get_wallet_signal_with_conditions()
            #if (message_jp):
            #    await forward_alert_wallet1("##Signal Wallet: \n"+message_jp)
            '''
            params_bulk1 = []
            params_bulktemp= ""
            count = 0
            count_t = 0
            for token in list(high_count_tokens.keys()):
                if (time.time() - high_count_tokens[token]['createdDelta']) <= 1200 and token not in high_count_tokens_correction:
                    count += 1
                    if count <= 7:
                        params_bulktemp += token+","
                        #print("sdoiusidusoi")
                        #print(len(high_count_tokens))
                        #print(count)
                        if count == 7:
                            params_bulk1.append(params_bulktemp)
                            params_bulktemp= ""
                    elif count <=14 :
                        params_bulktemp += token+","
                        if count == 14:
                            params_bulk1.append(params_bulktemp)
                            params_bulktemp= ""
                    elif count <=21 :
                        params_bulktemp += token+","
                        if count == 21:
                            params_bulk1.append(params_bulktemp)
                            params_bulktemp= ""
                    elif count <=28 :
                        params_bulktemp += token+","
                        if count == 28:
                            params_bulk1.append(params_bulktemp)
                            params_bulktemp= ""
                else:
                    count_t += 1

                if count + count_t == len(high_count_tokens.keys()) and count % 7 != 0:
                    params_bulk1.append(params_bulktemp)

            print(params_bulk1)

            for s in params_bulk1:
                if s != "":
                    url_dexscreener = f'https://api.dexscreener.com/latest/dex/tokens/'+s
                    headers_dexscreener = {}
                    dexscreener_data = await fetch_data_coin(url_dexscreener, headers_dexscreener)

                    if 'error' in dexscreener_data:
                        print("ASSSSSOOOOOy")
                        print(dexscreener_data['error'])
                    pairs = dexscreener_data.get('pairs', None)

                    if pairs:
                        for pair in dexscreener_data["pairs"]:
                            token_temp = pair.get('baseToken', {}).get('address', None)
                            if token_temp not in high_count_tokens_correction and pair["dexId"] == "raydium":
                                fdv_temp = 0
                                liq_temp = 0
                                if 'fdv' in pair:
                                    fdv_temp = pair["fdv"]
                                if 'liquidity' in pair:
                                    liq_temp = pair["liquidity"]["usd"]
                                websites = pair.get('info', {}).get('websites', [])
                                website_url = websites[0].get('url', None) if websites else None

                                socials = pair.get('info', {}).get('socials', [])
                                twitter_url = None
                                telegram_url = None

                                for social in socials:
                                    if social.get('type') == 'twitter':
                                        twitter_url = str(social.get('url'))
                                    elif social.get('type') == 'telegram':
                                        telegram_url = str(social.get('url'))

                                message_final = f"""
▶️ 💎 <b>{pair["baseToken"]["symbol"]}</b> #CTO #{pair["baseToken"]["name"]} [<a href="https://bullx.io/terminal?chainId=1399811149&address={token_temp}">bullx</a>] 

<code>{token_temp}</code>

MC: ${fdv_temp}   |       Liq: ${liq_temp}
Holders: 240      |       Top 10: 10.9%

<a href="https://dexscreener.com/solana/{token_temp}">Chart</a>  |  <a href="https://rugcheck.xyz/tokens/{token_temp}">Rugcheck</a>  |  <a href="https://solscan.io/token/{token_temp}">Solscan</a>
<a href="{telegram_url}">Telegram</a>  |  <a href="{website_url}">Website</a>  |  <a href="{twitter_url}">Twitter</a>

X Links: <a href="{twitter_url}">X</a>  |  <a href="https://twitter.com/search?q=${pair["baseToken"]["symbol"]}">Ticker</a>

🛒 <b><a href="https://t.me/BullxBetaBot?start=access_QDYDLGXD1U">Buy {pair["baseToken"]["symbol"]}</a></b> 💸
🔗 <b><a href="https://t.me/solana_trojanbot?startr-doremifas493385-{token_temp}">Trojan</a></b>
"""
                                if fdv_temp > 150000 and liq_temp >= 30000:
                                    high_count_tokens_correction[token_temp] = {'status': "moon", 'website_url': website_url, 'twitter_url': twitter_url , 'telegram_url' : telegram_url ,'createdDelta': high_count_tokens[token_temp]['createdDelta'] }
                                if (twitter_url and "cto" in twitter_url.lower()) or (telegram_url and "cto" in telegram_url.lower()):
                                    if token_temp in high_count_tokens_correction:
                                        if high_count_tokens_correction[token_temp]['status'] != "cto" :
                                            if token_temp in token_volume :
                                                if not find_coin_gem_by_ca_id_and_platform(token_temp, "dexcto"):
                                                    await forward_alert(message_final)
                                                    insert_data_coin_gem(token_temp, "dex", fdv_temp, None, None, None, None)  
                                            await forward_msg("https://dexscreener.com/solana/"+token_temp+" #CTO1 "+str(twitter_url)+" "+str(telegram_url))
                                            await forward_msg(str(token_temp)+" member_TG:  #CTO")
                                    elif token_temp not in high_count_tokens_correction:
                                            if not find_coin_gem_by_ca_id_and_platform(token_temp, "dexcto"):
                                                    await forward_alert(message_final)
                                                    insert_data_coin_gem(token_temp, "dexcto", fdv_temp, None, None, None, None)                                              
                                            await forward_msg("https://dexscreener.com/solana/"+token_temp+" #CTO2"+str(twitter_url)+" "+str(telegram_url))
                                    high_count_tokens_correction[token_temp] = {'status': "cto", 'website_url': website_url, 'twitter_url': twitter_url , 'telegram_url' : telegram_url ,'createdDelta': high_count_tokens[token_temp]['createdDelta'] }


            #tahap 2 cari koreksi
            params_bulk2 = []
            params_bulktemp= ""
            count = 0
            count_t = 0
            for token in list(high_count_tokens_correction.keys()):
                if (time.time() - high_count_tokens_correction[token]['createdDelta']) <= 7200 and (high_count_tokens_correction[token]['status'] == "moon" or high_count_tokens_correction[token]['status'] == "dip") :
                    count += 1
                    if count <= 7:
                        params_bulktemp += token+","
                        if count == 7:
                            params_bulk2.append(params_bulktemp)
                            params_bulktemp= ""
                    elif count <=14 :
                        params_bulktemp += token+","
                        if count == 14:
                            params_bulk2.append(params_bulktemp)
                            params_bulktemp= ""
                    elif count <=21 :
                        params_bulktemp += token+","
                        if count == 21:
                            params_bulk2.append(params_bulktemp)
                            params_bulktemp= ""
                    elif count <=28 :
                        params_bulktemp += token+","
                        if count == 28:
                            params_bulk2.append(params_bulktemp)
                            params_bulktemp= ""
                elif (time.time() - high_count_tokens_correction[token]['createdDelta']) > 9200:
                    del high_count_tokens_correction[token]   
                    count_t += 1
                else:
                    count_t += 1
                if count + count_t == len(high_count_tokens.keys()) and count % 7 != 0:
                    params_bulk1.append(params_bulktemp)

            for s in params_bulk2:         
                if s != "":
                    url_dexscreener2 = f'https://api.dexscreener.com/latest/dex/tokens/'+s
                    headers_dexscreener2 = headers_dexscreener = {}
                    dexscreener_data2 = await fetch_data_coin(url_dexscreener2, headers_dexscreener2)
                    
                    if 'error' in dexscreener_data2:
                        print("ASSSSSOOOOOy")
                        print(dexscreener_data2['error'])
                    pairs = dexscreener_data2.get('pairs', None)

                    if pairs:
                        for pair in dexscreener_data2["pairs"]:
                            token_temp = pair.get('baseToken', {}).get('address', None)
                            if token_temp in high_count_tokens_correction and pair["dexId"] == "raydium":
                                fdv_temp = 0
                                liq_temp = 0
                                if 'fdv' in pair:
                                    fdv_temp = pair["fdv"]
                                if 'liquidity' in pair:
                                    liq_temp = pair["liquidity"]["usd"]
                                websites = pair.get('info', {}).get('websites', [])
                                website_url = websites[0].get('url', None) if websites else None
                                socials = pair.get('info', {}).get('socials', [])
                                twitter_url = None
                                telegram_url = None
                                price_change_h24 = pair.get('priceChange', {}).get('h24', None)

                                for social in socials:
                                    if social.get('type') == 'twitter':
                                        twitter_url = str(social.get('url'))
                                    elif social.get('type') == 'telegram':
                                        telegram_url = str(social.get('url'))
                                message_final = f"""
▶️ 💎<b>{pair["baseToken"]["symbol"]}</b> #CTO #{pair["baseToken"]["name"]} [<a href="https://bullx.io/terminal?chainId=1399811149&address={token_temp}">bullx</a>] 

<code>{token_temp}</code>

MC: ${fdv_temp}   |       Liq: ${liq_temp}
Holders: 240      |       Top 10: 10.9%

<a href="https://dexscreener.com/solana/{token_temp}">Chart</a>  |  <a href="https://rugcheck.xyz/tokens/{token_temp}">Rugcheck</a>  |  <a href="https://solscan.io/token/{token_temp}">Solscan</a>
<a href="{telegram_url}">Telegram</a>  |  <a href="{website_url}">Website</a>  |  <a href="{twitter_url}">Twitter</a>

X Links: <a href="{twitter_url}">X</a>  |  <a href="https://twitter.com/search?q=${pair["baseToken"]["symbol"]}">Ticker</a>

🛒 <b><a href="https://t.me/BullxBetaBot?start=access_QDYDLGXD1U">Buy {pair["baseToken"]["symbol"]}</a></b> 💸
🔗 <b><a href="https://t.me/solana_trojanbot?start=r-godrekt-{token_temp}">Trojan</a></b>
"""
                                if (twitter_url and "cto" in twitter_url.lower()) or (telegram_url and "cto" in telegram_url.lower()) and high_count_tokens_correction[token_temp]['status'] != "cto" :
                                    if token_temp in token_volume :
                                        if not find_coin_gem_by_ca_id_and_platform(token_temp, "dexcto"):
                                            await forward_alert(message_final)
                                            insert_data_coin_gem(token_temp, "dexcto", fdv_temp, None, None, None, None)  
                                    await forward_msg("https://dexscreener.com/solana/"+token_temp+" #CTO3 "+str(twitter_url)+" "+str(telegram_url))
                                    await forward_msg(str(token_temp)+" member_TG:  #CTO")
                                    high_count_tokens_correction[token_temp]['status'] = "cto"                         
                                elif float(price_change_h24) < 20 and  high_count_tokens_correction[token_temp]['status'] != "dip" and high_count_tokens_correction[token_temp]['status'] != "cto":
                                    if token_temp in token_volume :
                                        if not find_coin_gem_by_ca_id_and_platform(token_temp, "dexcto"):
                                            await forward_alert(message_final)
                                            insert_data_coin_gem(token_temp, "dexcto", fdv_temp, None, None, None, None)  
                                    await forward_trend("https://dexscreener.com/solana/"+token_temp+" #dip "+str(twitter_url)+" "+str(telegram_url))
                                    await forward_trend(str(token_temp)+" #dip")
                                    high_count_tokens_correction[token_temp]['status'] = "dip"     '''  
   
        except Exception as e:
            tb = traceback.format_exc()
            print("An error occurred:\n", tb)
            print(f"Error55: {e}")
        

# ricky 5 menit awal ============================================================================================================== 

BASE_URL = "https://api.dryespah.com/v1api/v3/stats/alltags/totalholders?token_id={token}-solana"

# Headers (remains unchanged)
headersave = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-US,en;q=0.9,id;q=0.8,ms;q=0.7',
    'ave-udid': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36--1729941920835--2aab0369-b22d-4773-8cc5-5ebac34a5100',
    'lang': 'en',
    'origin': 'https://ave.ai',
    'priority': 'u=1, i',
    'referer': 'https://ave.ai/',
    'sec-ch-ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
    'x-auth': '8cc0085be7fb1a5975e7fd5f3007d62d1729941956122170608'
}

# Asynchronous function to call the API with a specified token
async def call_api(token):
    url = BASE_URL.format(token=token)  # Format the URL with the provided token
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(url, headers=headersave) as response:
                response.raise_for_status()  # Raise an error for bad responses
                json_response = await response.json()  # Parse JSON response
                
                # Extract and format the required data
                formatted_data = format_data(json_response['data'])
                print(formatted_data)  # Output the formatted data
                return formatted_data
        except Exception as e:
            print(f"Error calling API: {e}")
            #await forward_alert_err(f"Error calling API: {e}")
            print(f"Traceback: {traceback.format_exc()}")  # Print traceback for detailed error info

# Function to format the extracted data
def format_data(data):
    result = []
    for item in data:
        # Get the 'en' and 'total_address' fields
        en = item['en']
        total_address = item['total_address']
        result.append(f"{en}: {total_address}")

    # Join all entries with ' | ' for the final output
    return " | ".join(result)




async def fetch_gmgn(token_address):
    url = f'https://gmgn.ai/defi/quotation/v1/tokens/tag_wallet_count/sol/{token_address}'
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9,id;q=0.8,ms;q=0.7',
        'cookie': '_ga=GA1.1.1914834596.1729108225; __cf_bm=lfFRKDSUvh6JpWZOn3AaQHzTHll2vCVg3DQs_Kjs0sY-1730819406-1.0.1.1-LXaOZB13jYKQh5vpga.oevxZGZKlvGRLeYjA6OBodHzUQ_4LjxDKK3_QltOdbZjkHfxDxf7DTcvR1z62qoyGrQ; cf_clearance=1bF8UUL6PPP78qRdiYmvsVcARU0.l4Cj76ENeQNIqx8-1730819408-1.2.1.1-rNcjewnskqO2m4wHUdmYlW7Zqg6kpCfaco.g2U2Ad1_AIw2IMumb013YcHs8.zOSB4aLhKEaEjQnF2DNbMmK_KZqq.wI2N7bMDrHr5sUhoV7bN7n5_3MNnXl5tdPo7JJG0nfJbAg4qNpFUSjdPiB6yQBwy9b_xhLwJ2rCKeMfXd7NHwPFxcRlWvHs5PzOUPXLYNMnOEl0JDyhSjfG3H9vvmKZOER1xQ5Ni8PKvL8lmnGuMlhyY_Aw44j_aDjUPou9i.4KM_a5k6afd0u0kcyFR87i.UsSj7TAmY8.RvaDhYK_jQXh0OGZVa9rx82bzjWO5n9L4gFo4G1NBFJqgOjbQ51ywu9r218RFCTmQ3ZUzE84Dp0Rytw1XBYN4VMWwk6; _ga_0XM0LYXGC8=GS1.1.1730819405.25.1.1730819778.0.0.0',
        'if-none-match': 'W/"126-vVjkmH0NMCRdCEFC0v8eO8j1de8"',
        'priority': 'u=1, i',
        'referer': f'https://gmgn.ai/sol/token/{token_address}?tab=holders',
        'sec-ch-ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36'
    }

    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as response:
            if response.status == 200:
                data = await response.json()
                return format_response(data)
            else:
                return f"Error: {response.status}, {await response.text()}"

def format_response(data):
    if data["code"] != 0:
        return "Error: Gagal mengambil data."
    
    data_content = data["data"]
    formatted = (
        f"Smart: {data_content['smart_wallets']} | "
        f"Fresh: {data_content['fresh_wallets']} | "
        f"Renowned: {data_content['renowned_wallets']} | "
        f"Creator: {data_content['creator_wallets']} | "
        f"Sniper: {data_content['sniper_wallets']}\n"
        f"Rat: {data_content['rat_trader_wallets']} | "
        f"Following: {data_content['following_wallets']} | "
        f"Whale: {data_content['whale_wallets']} | "
        f"Top: {data_content['top_wallets']}"
    )
    return formatted


# get volume ============================================================================================================== 

params = {
    'address': 'BmanDqQELF7QY5uRPw8vg3eMjR74WZnszKmNbLJKkay3',
    'page_size': '100',
    'page': '1',
    'flow': 'out'
}
headers = {
    "accept": "application/json, text/plain, */*",
    "accept-language": "en-US,en;q=0.9,id;q=0.8,ms;q=0.7",
    "cookie": "_ga=GA1.1.1552685285.1703187686; amp_1adb3b=ewmgcpLztfynKaJxQoFPW3...1hpvuj7s3.1hpvuj7s3.c.0.c; cf_clearance=tyCvX3zNlrPsz1Da6R5cJkdMcrCWGuEbJlxY02LSJRI-1730723531-1.2.1.1-zICsa0Bp8XnbGTbzWDzbQpsdDH1r6dNfAchTRPKFOc2scJ.msK8a9iIbzNwmu1689DFWWndBuY74hEk_3YZUXTPLcwH2aclLit6nMV4qIwCsSWABjA7ZnpM1vvivWGVQT67wX0G7ziUNLEGZ9cCKJe4HAXlVilie8R9LNbeEdDx2y_I6AAQz6ltiiscxa81IJ5dU4t3v0qwPKsnKD.KSX6VdKucD1xC2ysacnLPKUXBrhcGbfVu2hlUmrzdLC7jxiERl3N5Qh0v5.ARlLVBeH0o5PntNEmxvGSNnAbTWgr9RDRnEqatfn_ATyA63OczC76aPeY4uyF9ICDkY5ETut9qtqq4aQOPBupE6OjKX1G_DLFUpkPpKq8EnwHZZ3vwR4i_.GFLkiqTPjiXb_4GSqcR.Dq6b9LxaFjLY_phGtGPsxDHHoryihyBUH_3WjQqT; _ga_PS3V7B7KV0=GS1.1.1730723082.374.1.1730723539.0.0.0",
    "if-none-match": 'W/"1912-+wYubRWfLhG9WgdV/nv7VwVE2hU"',
    "origin": "https://solscan.io",
    "priority": "u=1, i",
    "referer": "https://solscan.io/",
    "sec-ch-ua": '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "sol-aut": "YskAYUDB9dls0fKtx1G4hqoyjXrHb6iwuCvWHD9k",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"
}

kol_buy = {}

temp2_data = {}
# Penyimpanan token_address dan waktu terakhir diperbarui
token_store = {}
# Penyimpanan token_address dengan count > 10 dan waktu ditambahkannya
high_count_tokens = {}

high_count_tokens_correction = {}

token_store_pump = {}

high_count_tokens_5m = {} 

high_count_tokens_6m = {}

high_count_tokens_00 = {}

token_temps = {}

viral_token = {}

viral_name = {}

token_volume = {}

token_list = {}

signal_list = {}

viral_store = {}

token_mcap = {}


async def fetch_data(session, url , retries=1, timeout=10):
    """
    Fetch data from the given URL using aiohttp with error handling and retry logic.
    """
    # Mendapatkan peer/grup/channel
    timeout_obj = aiohttp.ClientTimeout(total=timeout)  # Set a total timeout for the request
    
    for attempt in range(retries):
        try:
            #response = requests.post('http://192.168.1.100:5000/solscan', json=params)
            async with session.get(url, headers=headers, params=params, timeout=timeout_obj) as response:
                if response.status == 200:
                    try:
                        data = await response.json()
                        return data
                    except ValueError as e:
                        #await forward_alert_err(f"#ALR Error decoding JSON 11: {e}")
                        print(f"Error decoding JSON: {e}")
                        print("Response content:", await response.text())
                        return {'error': 'Invalid JSON', 'details': str(e)}
                else:
                    #await forward_alert_err(f"#ALR Error decoding JSON 22 NEED RELOGIN !!!!!: {response.status}")
                    await asyncio.sleep(20)
                    return {'error': 'Request failed', 'status': response.status}
        
        except aiohttp.ClientConnectionError as e:
            #await forward_alert_err(f" #ALR Error decoding JSON 55: {e}")
            print(f"Connection error on attempt {attempt+1}. Retrying... Error: {e}")
            if attempt < retries - 1:  # Retry only if it's not the last attempt
                await asyncio.sleep(2)  # Wait before retrying
            else:
                print(f"Unexpected error121: {e}")
                return {'error': 'Connection failed after retries', 'details': str(e)}
        
        except asyncio.TimeoutError as e:
            print(f"Unexpected error454: {e}")
            #await forward_alert_err(f"#ALR Error decoding JSON 454!!!!!: {e}")
            await asyncio.sleep(20)
            return {'error': 'Request timed out', 'details454': str(e)}
        
        except Exception as e:
            #await forward_alert_err(f"#ALR Error decoding JSON 44: {e}")
            print(f"Unexpected error878: {e}")
            return {'error': 'An unexpected error occurred', 'details': str(e)}
    
    return {'error': 'Failed to fetch data after retries'}
                
async def fetch_data1(session, url , retries=1, timeout=10):
    """
    Fetch data from the given URL using aiohttp with error handling and retry logic.
    """
    # Mendapatkan peer/grup/channel
    timeout_obj = aiohttp.ClientTimeout(total=timeout)  # Set a total timeout for the request
    
    for attempt in range(retries):
        try:
            headers1 = {
                "Content-Type": "application/json"
            }
            params1 = {
                'address': 'BmanDqQELF7QY5uRPw8vg3eMjR74WZnszKmNbLJKkay3',
                'page_size': '100',
                'page': '1',
                'flow': 'out'
            }
            async with session.post("http://192.168.2.11:5000/solscan", headers=headers1, json=params1) as response:
            #response = requests.post("http://192.168.2.11:5000/solscan", headers=headers1, data=json.dumps(params1))
            #async with session.post(url, headers=headers, params=params, timeout=timeout_obj) as response:
                print(response)
                if response.status == 200:
                    print(response.json())
                    try:
                        data = await response.json()
                        return data
                    except ValueError as e:
                        #await forward_alert_err(f"#ALR Error decoding JSON 11: {e}")
                        print(f"Error decoding JSON: {e}")
                        print("Response content:", await response.text())
                        return {'error': 'Invalid JSON', 'details': str(e)}
                else:
                    #await forward_alert_err(f"#ALR Error decoding JSON 22 NEED RELOGIN !!!!!: ")
                    await asyncio.sleep(20)
                    return {'error'}
        
        except aiohttp.ClientConnectionError as e:
            #await forward_alert_err(f" #ALR Error decoding JSON 55: {e}")
            print(f"Connection error on attempt {attempt+1}. Retrying... Error: {e}")
            if attempt < retries - 1:  # Retry only if it's not the last attempt
                await asyncio.sleep(2)  # Wait before retrying
            else:
                print(f"Unexpected error121: {e}")
                return {'error': 'Connection failed after retries', 'details': str(e)}
        
        except asyncio.TimeoutError as e:
            print(f"Unexpected error454: {e}")
            #await forward_alert_err(f"#ALR Error decoding JSON 454!!!!!: {e}")
            await asyncio.sleep(20)
            return {'error': 'Request timed out', 'details454': str(e)}
        
        except Exception as e:
            #await forward_alert_err(f"#ALR Error decoding JSON 44: {e}")
            print(f"Unexpected error878: {e}")
            return {'error': 'An unexpected error occurred', 'details': str(e)}
    
    return {'error': 'Failed to fetch data after retries'}

    
async def fetch_data_dex(url, headers):
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as response:
            return await response.json()

async def get_volume():
    #connector = aiohttp.TCPConnector()
    global temp2_data
    global swicth
    global buyer_bot
    async with aiohttp.ClientSession() as session:
        while True:
            try:
                await asyncio.sleep(30)
                data = None
                time_difference_minutes = 0
                current_time = datetime.now()    
                # Fetch data from API
                if swicth:
                    url = "https://api-v2.solscan.io/v2/account/balance_change"
                    swicth = False
                    data = await fetch_data(session, url)
                else:
                    url = 'http://192.168.2.11:5000/solscan'
                    swicth = True
                    data = await fetch_data1(session, url)
                #print(data)
                if  'data' in data :
                    transactions = data['data']
                    #transactions = data['data']
                    new_tokens = set()
                    current_date = datetime.now()
                    temp_data = {}
                    for transaction in reversed(transactions):
                        #change = transaction.get('change', {})
                        token_address = transaction.get('token_address')
                        if token_address and token_address != 'So11111111111111111111111111111111111111112': #and str(change_amount).startswith('-'):
                            change_amount = int(transaction.get('amount', 0))
                            decimals = transaction.get('token_decimals', 0)
                            block_time = transaction.get('block_time')
                            if token_address in temp2_data:
                                if block_time> temp2_data[token_address]['block_time']: 
                                    if token_address not in temp_data :
                                        temp_data[token_address] = {'change_amount': [change_amount], 'decimals': [decimals], 'block_time': block_time, 'array_block' : [block_time] }
                                        new_tokens.add(token_address)
                                    elif token_address in temp_data and block_time > temp_data[token_address]['block_time']:
                                        temp_data[token_address]['change_amount'].append(change_amount)
                                        temp_data[token_address]['array_block'].append(block_time)
                                        temp_data[token_address]['decimals'].append(decimals)
                                        temp_data[token_address]['block_time']=block_time
                                        new_tokens.add(token_address)
                            elif token_address not in temp2_data:
                                if token_address not in temp_data:
                                    temp_data[token_address] = {'change_amount': [change_amount], 'decimals': [decimals], 'block_time': block_time, 'array_block' : [block_time] }
                                    new_tokens.add(token_address)
                                elif token_address in temp_data and block_time > temp_data[token_address]['block_time']:
                                    temp_data[token_address]['change_amount'].append(change_amount)
                                    temp_data[token_address]['array_block'].append(block_time)
                                    temp_data[token_address]['decimals'].append(decimals)
                                    temp_data[token_address]['block_time']=block_time
                                    new_tokens.add(token_address)                     
                    
                    temp2_data = temp_data

                    batch_size = []
                    if len(temp_data) <= 7:
                        batch_size.append(len(temp_data))
                    elif len(temp_data) <= 14:
                        batch_size = [7,len(temp_data)-7]
                    elif len(temp_data) <= 21:
                        batch_size = [7,7,len(temp_data)-14]
                    elif len(temp_data) <= 28:
                        batch_size = [7,7,7,len(temp_data)-21]
                    elif len(temp_data) <= 35:
                        batch_size = [7,7,7,7,len(temp_data)-28]
                    elif len(temp_data) <= 42:
                        batch_size = [7,7,7,7,7,len(temp_data)-35]
                    elif len(temp_data) <= 49:
                        batch_size = [7,7,7,7,7,7,len(temp_data)-42]
                    elif len(temp_data) <= 56:
                        batch_size = [7,7,7,7,7,7,7,len(temp_data)-49]

                    start = 0
                    for idx, size in enumerate(batch_size):
                        params_bulk = ""
                        end = start + size
                        data_batch = {k: temp_data[k] for k in list(temp_data)[start:end]}
                        start = end
                        #print(len(temp_data))
                        #print(f"Batch {idx + 1}:")
                        #print(f"len batc {len(data_batch)}:")
                        

                        for token_address in data_batch.keys():
                                params_bulk += token_address + ","

                        #print(params_bulk)
                        if params_bulk != "":
                            
                            url_dexscreener = f'https://api.dexscreener.com/latest/dex/tokens/{params_bulk}'
                            headers_dexscreener = headers_dexscreener = {}
                            dexscreener_data = await fetch_data_coin(url_dexscreener, headers_dexscreener)
                            fdv_temp = 100000
                            if 'error' in dexscreener_data:
                                print("ASSSSSOOOOOy")
                                print(dexscreener_data['error'])

                            pairs = dexscreener_data.get('pairs', None)
                            current_time = time.time()
                            #print(f"len pairs {len(pairs)}:")
                            #print(pairs) 
                            if pairs and len(pairs)>0:
                                for pair in dexscreener_data["pairs"]:
                                    token_address = pair.get('baseToken', {}).get('address', None)
                                    if token_address in temp_data and pair["dexId"] == "raydium":
                                        
                                        socials = pair.get('info', {}).get('socials', [])
                                        websites = pair.get('info', {}).get('websites', [])
                                        pair_created_at = pair.get('pairCreatedAt', None)
                                        pair_created_at = pair_created_at / 1000
                                        if pair_created_at:
                                            datetime_obj = datetime.fromtimestamp(pair_created_at, tz=pytz.UTC)

                                            # Convert to WIB (Waktu Indonesia Barat) timezone
                                            wib_timezone = pytz.timezone("Asia/Jakarta")
                                            datetime_wib = datetime_obj.astimezone(wib_timezone)

                                            #formatted date and time to a variable
                                            wib_time_str = datetime_wib.strftime('%Y-%m-%d %H:%M:%S %Z')
                                            current_time_wib = datetime.now(pytz.timezone('Asia/Jakarta'))

                                            # Hitung perbedaan waktu dalam menit
                                            time_difference_minutes = int((current_time_wib - datetime_wib).total_seconds() / 60)

                                            #print(f"Beda waktu: {time_difference_minutes} menit")

                                        
                                        twitter_url = None
                                        telegram_url = None
                                        web_url = None
                                        if 'fdv' in pair:
                                            fdv_temp = pair["fdv"]
                                        for social in socials:
                                            if social.get('type') == 'twitter':
                                                twitter_url = str(social.get('url'))
                                            elif social.get('type') == 'telegram':
                                                telegram_url = str(social.get('url'))
                                        for web in websites:
                                            if web.get('label') == 'Website':
                                                web_url = str(web.get('url'))
                                            #if not find_coin_gem_by_ca_id_and_platform(token_address, "sa"):
                                                #insert_data_coin_gem(token_address, "sa", 0, None, None, None, None)
                                        found_tokenss = None
                                        if twitter_url:
                                            found_tokenss = [token for token in viral_store if (token in twitter_url.lower() and token != "solana" and len(token)>1)]
                                        found_name = [token for token in viral_name if (token in pair["baseToken"]["symbol"].lower() and token != "solana" and len(token)>1)]
                                        viral_tw = "No"
                                        if found_tokenss or found_name or find_coin_gem_by_ca_id_and_platform(token_address, "pf"):
                                            viral_tw = "✅"

                                        message_final = f"""
<b>{pair["baseToken"]["symbol"]}</b> #{pair["baseToken"]["name"]} [<a href="https://pump.fun/{token_address}">pf</a>] [<a href="https://bullx.io/terminal?chainId=1399811149&address={token_address}">bullx</a>] [<a href="https://gmgn.ai/sol/token/{token_address}?tab=activity">gmgn</a>] [<a href="https://ave.ai/token/{token_address}-solana?from=Token">ave</a>]

<code>{token_address}</code>

MC: ${fdv_temp}   |       Liq: ${pair["liquidity"]["usd"]}
<a href="https://dexscreener.com/solana/{token_address}">Chart</a>  |  <a href="https://rugcheck.xyz/tokens/{token_address}">Rugcheck</a>  |  <a href="https://solscan.io/token/{token_address}">Solscan</a>
<a href="{telegram_url}">Telegram</a>  |  <a href="{web_url}">Website</a>  |  <a href="{twitter_url}">Twitter</a>

created_at: {wib_time_str} . {time_difference_minutes} minute ago
potential viral: {viral_tw} 
"""
                                        for index, block_time in enumerate(temp_data[token_address]['array_block']):
                                            #print(f"Index: {index}, Time: {block_time}")
                                            change_amount = temp_data[token_address]['change_amount'][index]
                                            decimals = temp_data[token_address]['decimals'][index]
                                            if token_address not in token_store:
                                                #print(pairs)
                                                result = {}
                                                pair_created_at = pair["pairCreatedAt"] / 1000  # convert to seconds
                                                created_at_datetime = datetime.fromtimestamp(pair_created_at, tz=timezone.utc)
                                                fdv_temp = 100000
                                                liq_temp = 160000
                                                if 'fdv' in pair:
                                                    fdv_temp = pair["fdv"]
                                                if 'liquidity' in pair:
                                                    liq_temp = pair["liquidity"]["usd"]
                                                
                                                token_store[token_address] = {'last_seen': current_date, 'count': 1, 'block_time': block_time, 'createdTime': pair_created_at, 'array_time' : [block_time] , 'telegram_url' : telegram_url , 'twitter_url' : twitter_url , 'fdv' : fdv_temp  }
                                                #print(current_time - pair_created_at)
                                                if pair_created_at > 0 :  # 5 minutes in seconds
                                                    result[pair["baseToken"]["symbol"]] = {
                                                    "pairCreatedAt": created_at_datetime.strftime('%Y-%m-%d %H:%M:%S'),
                                                    "priceChange_m5": pair["priceChange"]["m5"],
                                                    "volume_m5": pair["volume"]["m5"],
                                                    "txns_m5": pair["txns"]["m5"],
                                                    "fdv" : fdv_temp,
                                                    "liquidity" :liq_temp,
                                                    "price" : pair["priceUsd"],
                                                    "change_amount" : abs(change_amount),
                                                    "decimals" : decimals
                                                    }

                                                    print("Token Baruuuu:", token_address)
                                                    result_str = json.dumps(result)
                                                    temp_tx_sol = (abs(change_amount)/(10 ** decimals))*float(pair["priceUsd"])
                                                    if time_difference_minutes <= 30 and pair["priceChange"]["h1"] > 15 and temp_tx_sol > 1000 and token_address not in  high_count_tokens and liq_temp > 15000 :
                                                        if  token_address in token_volume:
                                                            if not find_coin_gem_by_ca_id_and_platform(token_address, "dex"):
                                                                ave_analitic = await call_api(token_address)
                                                                mcmoney_aler=""
                                                                match_sm = re.search(r"Smarters:\s*(\d+)", ave_analitic)
                                                                if match_sm:
                                                                    smarters_value = int(match_sm.group(1))
                                                                    if time_difference_minutes < 10 and smarters_value > 20:
                                                                        mcmoney_aler=" 💰 "
                                                                message_jp = get_wallet_signal_by_ca(token_address)
                                                                message_final += f"""
{message_jp}
{ave_analitic}

🛒 <b><a href="https://t.me/BullxBetaBot?start=access_QDYDLGXD1U">Buy {pair["baseToken"]["symbol"]}</a></b> 💸
🔗 <b><a href="https://t.me/solana_trojanbot?start=r-godrekt-{token_address}">Trojan</a></b>
                """                                             
                                                                await forward_doge(token_address)
                                                                await forward_alert("▶️"+mcmoney_aler+"💎 #volume "+message_final)
                                                                #insert_data_coin_gem(token_address, "dex", fdv_temp, None, None, None, None)
                                                        elif temp_tx_sol > 10000:
                                                            if not find_coin_gem_by_ca_id_and_platform(token_address, "dex"):
                                                                ave_analitic = await call_api(token_address)
                                                                mcmoney_aler=""
                                                                match_sm = re.search(r"Smarters:\s*(\d+)", ave_analitic)
                                                                if match_sm:
                                                                    smarters_value = int(match_sm.group(1))
                                                                    if time_difference_minutes < 10 and smarters_value > 20:
                                                                        mcmoney_aler=" 💰 "
                                                                message_jp = get_wallet_signal_by_ca(token_address)
                                                                message_final += f"""
{message_jp}
{ave_analitic}

🛒 <b><a href="https://t.me/BullxBetaBot?start=access_QDYDLGXD1U">Buy {pair["baseToken"]["symbol"]}</a></b> 💸
🔗 <b><a href="https://t.me/solana_trojanbot?start=r-godrekt-{token_address}">Trojan</a></b>
                """                                                                
                                                                await forward_doge(token_address)
                                                                await forward_alert("▶️"+mcmoney_aler+"💎 #volume "+message_final)
                                                                insert_data_coin_gem(token_address, "dex", fdv_temp, None, None, None, None)
                                                        elif twitter_url:
                                                            found_tokens = [token for token in viral_store if token in twitter_url.lower()]
                                                            if found_tokens:
                                                                if not find_coin_gem_by_ca_id_and_platform(token_address, "dex"):
                                                                    ave_analitic = await call_api(token_address)
                                                                    mcmoney_aler=""
                                                                    match_sm = re.search(r"Smarters:\s*(\d+)", ave_analitic)
                                                                    if match_sm:
                                                                        smarters_value = int(match_sm.group(1))
                                                                        if time_difference_minutes < 10 and smarters_value > 20:
                                                                            mcmoney_aler=" 💰 "
                                                                    message_jp = get_wallet_signal_by_ca(token_address)
                                                                    message_final += f"""
{message_jp}
{ave_analitic}

🛒 <b><a href="https://t.me/BullxBetaBot?start=access_QDYDLGXD1U">Buy {pair["baseToken"]["symbol"]}</a></b> 💸
🔗 <b><a href="https://t.me/solana_trojanbot?start=r-godrekt-{token_address}">Trojan</a></b>
                """                                                                
                                                                    await forward_doge(token_address)
                                                                    await forward_alert("▶️"+mcmoney_aler+"💎 #volume "+message_final)
                                                                    insert_data_coin_gem(token_address, "dex", fdv_temp, None, None, None, None)
                                                        print(token_address)
                                                        print("1113331111")
                                                        convic = 0
                                                        if token_address in high_count_tokens_6m:
                                                            convic += 1
                                                        if token_address in high_count_tokens_5m:
                                                            convic += 1
                                                        if token_address in high_count_tokens_00:
                                                            convic += 1
                                                        high_count_tokens[token_address] = {'block_time': block_time, 'post': False, 'count': 1 , 'createdDelta': pair_created_at }
                                                        counts = high_count_tokens[token_address]['count']
                                                        if (current_time - pair_created_at) <= 300:
                                                            if not find_coin_gem_by_ca_id_and_platform(token_address, "dex") and (find_coin_gem_by_ca_id_and_platform(token_address, "30k")  and find_coin_gem_by_ca_id_and_platform(token_address, "koth")  and find_coin_gem_by_ca_id_and_platform(token_address, "listray") ):                                                             
                                                                ave_analitic = await call_api(token_address)
                                                                mcmoney_aler=""
                                                                match_sm = re.search(r"Smarters:\s*(\d+)", ave_analitic)
                                                                if match_sm:
                                                                    smarters_value = int(match_sm.group(1))
                                                                    if time_difference_minutes < 10 and smarters_value > 20:
                                                                        mcmoney_aler=" 💰 "
                                                                message_jp = get_wallet_signal_by_ca(token_address)
                                                                message_final += f"""
{message_jp}
{ave_analitic}

🛒 <b><a href="https://t.me/BullxBetaBot?start=access_QDYDLGXD1U">Buy {pair["baseToken"]["symbol"]}</a></b> 💸
🔗 <b><a href="https://t.me/solana_trojanbot?start=r-godrekt-{token_address}">Trojan</a></b>
                """                                                                
                                                                await forward_doge(token_address)
                                                                await forward_alert("▶️"+mcmoney_aler+"💎 "+message_final)
                                                                insert_data_coin_gem(token_address, "dex", fdv_temp, None, None, None, None)
                                                                await forward_trend("https://dexscreener.com/solana/"+token_address+"?/= #DATA="+str(result_str)+" #PUMPFUN_1000USD #C:"+str(convic)+" Count:"+str(counts))
                                                            #await forward_trend("https://birdeye.so/find-trades/"+token_address+"?chain=solana")
                                                            if (twitter_url and "cto" in twitter_url.lower()) or (telegram_url and "cto" in telegram_url.lower()):
                                                                await forward_msg("https://dexscreener.com/solana/"+token_address+"?/= #DATA="+str(result_str)+" #PUMPFUN_1000USD #C:"+str(convic)+" Count:"+str(counts)+" #11CTOOO")
                                                                #await forward_msg("https://birdeye.so/find-trades/"+token_address+"?chain=solana Member_TG:"+str(member_count)+"#44CTOOO")
                                                            elif token_address in token_store_pump:
                                                                store_str = json.dumps(token_store_pump[token_address], default=datetime_converter)
                                                                if "cto" in  store_str.lower():
                                                                    await forward_msg("https://dexscreener.com/solana/"+token_address+"?/= #DATA="+str(result_str)+" #PUMPFUN_1000USD #C:"+str(convic)+" Count:"+str(counts)+" #11CTOOO")
                                                                    #await forward_msg("https://birdeye.so/find-trades/"+token_address+"?chain=solana Member_TG:"+str(member_count)+"#11CTOOO")
                                                    elif token_address in token_store_pump:
                                                        store_str = json.dumps(token_store_pump[token_address], default=datetime_converter)
                                                        if "cto" in  store_str.lower() or (twitter_url and "cto" in twitter_url.lower()) or (telegram_url and "cto" in telegram_url.lower()):
                                                            await forward_msg("https://dexscreener.com/solana/"+token_address+"?/= #DATA="+str(result_str)+" #PUMPFUN_1000USD #C:"+str(convic)+" Count:"+str(counts)+" #55CTOOO")
                                                            if token_address in token_volume :
                                                                if not find_coin_gem_by_ca_id_and_platform(token_address, "dex"):
                                                                    ave_analitic = await call_api(token_address)
                                                                    mcmoney_aler=""
                                                                    match_sm = re.search(r"Smarters:\s*(\d+)", ave_analitic)
                                                                    if match_sm:
                                                                        smarters_value = int(match_sm.group(1))
                                                                        if time_difference_minutes < 10 and smarters_value > 20:
                                                                            mcmoney_aler=" 💰 "
                                                                    message_final += f"""
{message_jp}
{ave_analitic}

🛒 <b><a href="https://t.me/BullxBetaBot?start=access_QDYDLGXD1U">Buy {pair["baseToken"]["symbol"]}</a></b> 💸
🔗 <b><a href="https://t.me/solana_trojanbot?start=r-godrekt-{token_address}">Trojan</a></b>
                """                                                                
                                                                    await forward_doge(token_address)
                                                                    #await forward_alert("▶️"+mcmoney_aler+"💎 "+message_final)
                                                                    insert_data_coin_gem(token_address, "dex", fdv_temp, None, None, None, None)
                                                            #await forward_msg("https://birdeye.so/find-trades/"+token_address+"?chain=solana Member_TG:"+str(member_count)+"#55CTOOO")   
                                                    elif (pair["priceChange"]["h24"] > 15  and 'fdv' in pair and liq_temp > 200000 and pair["fdv"] < 11000000) :
                                                        #print("owoowc")
                                                        #print(token_address)
                                                        #print("3333666633333")
                                                        if (current_time - pair_created_at) <= 300:
                                                            await forward_msg("https://dexscreener.com/solana/"+token_address+"?/= #DATA="+str(result_str)+" #3333666633333")
                                                            #await forward_msg("https://birdeye.so/find-trades/"+token_address+"?chain=solana")
                                                            #await #await forward_check_x(str(token_address))(token_address)
                                                    elif pair["priceChange"]["h24"] > 15 and liq_temp > 100000:
                                                        #print("AUUUww")
                                                        #print(token_address)
                                                        #print("55566665555")
                                                        await forward_trend("https://dexscreener.com/solana/"+token_address+"?/= #DATA="+str(result_str)+" #55566665555")
                                                        #await forward_trend("https://birdeye.so/find-trades/"+token_address+"?chain=solana")
                                                
                                            elif (token_address in token_store and block_time > token_store[token_address]['block_time']) or token_address in high_count_tokens :
                                                token_store[token_address]['last_seen'] = current_date
                                                token_store[token_address]['count']= 0
                                                token_store[token_address]['block_time'] = block_time
                                                if 'array_time' not in token_store[token_address]:
                                                    token_store[token_address]['array_time'] = []
                                                token_store[token_address]['array_time'].append(block_time)
                                                fdv_temp = 100000
                                                liq_temp = 99
                                                price = 0
                                                if 'fdv' in pair:
                                                    fdv_temp = pair["fdv"]
                                                if 'liquidity' in pair:
                                                    liq_temp = pair["liquidity"]["usd"]
                                                if 'priceUsd' in pair:
                                                    price = pair["priceUsd"]
                                                pair_created_at = pair["pairCreatedAt"] / 1000
                                                temp_tx_sol = (abs(change_amount)/(10 ** decimals))*float(price)
                                                if temp_tx_sol > 1000 and pair["priceChange"]["h1"] > 10 and liq_temp > 15000 and fdv_temp < 30000000 :
                                                    convic = 0
                                                    if token_address in high_count_tokens_6m:
                                                        convic += 1
                                                    if token_address in high_count_tokens_5m:
                                                        convic += 1
                                                    if token_address in high_count_tokens_00:
                                                        convic += 1

                                                    if token_address not in high_count_tokens:
                                                        print(token_address)
                                                        print("0002222000")
                                                        high_count_tokens[token_address] = {'block_time': block_time, 'post': False, 'count': 1 , 'createdDelta': pair_created_at}
                                                        counts =high_count_tokens[token_address]['count']
                                                        #await forward_trend("https://dexscreener.com/solana/"+token_address+"?/= #DATA= #PUMPFUN_1000USD #C:"+str(convic)+" Count:"+str(counts))
                                                        #await forward_trend("https://birdeye.so/find-trades/"+token_address+"?chain=solana")
                                                    elif token_address in high_count_tokens:
                                                        if block_time > high_count_tokens[token_address]['block_time']:
                                                            if temp_tx_sol > 10000 and (current_time - pair_created_at) <= 300:
                                                                if not find_coin_gem_by_ca_id_and_platform(token_address, "dex"):
                                                                    ave_analitic = await call_api(token_address)
                                                                    mcmoney_aler=""
                                                                    mcmoney = await search_messages_ray_wallet(token_address+" mcmoney")
                                                                    if mcmoney:
                                                                        mcmoney_aler="##"
                                                                    message_jp = get_wallet_signal_by_ca(token_address)
                                                                    message_final += f"""
{message_jp}
{ave_analitic}

🛒 <b><a href="https://t.me/BullxBetaBot?start=access_QDYDLGXD1U">Buy {pair["baseToken"]["symbol"]}</a></b> 💸
🔗 <b><a href="https://t.me/solana_trojanbot?start=r-godrekt-{token_address}">Trojan</a></b>
                """                                                                
                                                                    await forward_doge(token_address)
                                                                    await forward_alert("▶️"+mcmoney_aler+"💎 "+message_final)
                                                                    insert_data_coin_gem(token_address, "dex", fdv_temp, None, None, None, None)
                                                            #print(token_address)
                                                            #print(block_time)
                                                            #print("8822888")
                                                            #print( token_store[token_address]['block_time'])
                                                            if token_address not in high_count_tokens:
                                                                high_count_tokens[token_address] = {'block_time': block_time, 'post': False, 'count': 1, 'createdDelta': pair_created_at }
                                                            else:
                                                                high_count_tokens[token_address]['count'] += 1
                                                            counts =high_count_tokens[token_address]['count']
                                                            high_count_tokens[token_address]['block_time'] = block_time
                                                            #print("AUUUww5")
                                                            #await forward_trend("https://dexscreener.com/solana/"+token_address+"?/= #DATA= #PUMPFUN_1000USD #C:"+str(convic)+" Count:"+str(counts))
                                                            #await forward_trend("https://birdeye.so/find-trades/"+token_address+"?chain=solana")

                                         

                    cur_time = time.time()
                    current_date = datetime.now()  
                    print(current_date)
                    chat_id = -2391890259  # Ganti dengan ID chat yang diambil dari URL
                    entity1 = await client.get_entity(PeerChannel(chat_id))
                    for token in list(token_store.keys()):
                        if  'createdTime' in token_store[token] and 'fdv' in token_store[token] and token not in high_count_tokens_5m and token_store[token]['fdv'] < 7000000 and token_store[token]['count'] >= 5 and cur_time - token_store[token]['createdTime'] <= 500 and token_store[token]['liquidity'] > 20000:
                            convic = 0
                            counts = 0
                            if token in high_count_tokens:
                                convic += 1
                                counts = high_count_tokens[token]['count']
                            if token in high_count_tokens_6m:
                                convic += 1
                            if token in high_count_tokens_00:
                                convic += 1
                            if token not in high_count_tokens_5m:
                                print("AUUUww4")
                                #await forward_trend("https://dexscreener.com/solana/"+token+"?/=#trends5Menit #C:"+str(convic)+" Count:"+str(counts))
                                #await forward_trend("https://birdeye.so/find-trades/"+token+"?chain=solana #trends5Menit")
                            else:
                                print("AUUUww3")
                                #await forward_trend("https://dexscreener.com/solana/"+token+"?/=#trends5Menit #C:"+str(convic)+" Count:"+str(counts))
                                #await forward_trend("https://birdeye.so/find-trades/"+token+"?chain=solana #trends5Menit")
                            high_count_tokens_5m[token] = current_date
                      
                        # Periksa dan hapus data yang lebih dari 6 menit
                        six_minutes_ago = current_date - timedelta(minutes=5)
                        # Filter array_data untuk menghapus elemen yang lebih dari 6 menit
                        if 'array_time' in token_store[token]:
                            if len(token_store[token]['array_time']) > 0:
                                token_store[token]['array_time'] = [
                                    data for data in token_store[token]['array_time']
                                    if datetime.fromtimestamp(data) >= six_minutes_ago
                                ]
                        
                        if 'array_time' not in token_store[token]:
                                    token_store[token]['array_time'] = []

                    # Print dan simpan token_address yang count kemunculan lebih dari 10
                    for token in high_count_tokens:
                        if token in token_store_pump:
                            store_str = json.dumps(token_store_pump[token], default=datetime_converter) 
                        else:
                            store_str=""
                        if token in token_store:
                            dex_str = json.dumps(token_store[token], default=datetime_converter) 
                        else:
                            dex_str=""
                        params_cto=""
                        if "cto" in dex_str:
                            params_cto= "#3CTOOO"      
                            if token_store[token]['telegram_url']:
                                group_link = token_store[token]['telegram_url']
                        if high_count_tokens[token]['post'] == False and  high_count_tokens[token]['count'] > 0 and (time.time() - high_count_tokens[token]['createdDelta']) <= 600 :
                            convic = 0
                            if token_address in high_count_tokens_6m:
                                convic += 1
                            if token_address in high_count_tokens_5m:
                                convic += 1
                            if token_address in high_count_tokens_00:
                                convic += 1
                            if token in token_volume :
                                if not find_coin_gem_by_ca_id_and_platform(token, "dex"):
                                    message_final = await get_message_for_tg(token)
                                    if message_final:                          
                                        message_final += f"""
🛒 <b><a href="https://t.me/BullxBetaBot?start=access_QDYDLGXD1U">Buy {pair["baseToken"]["symbol"]}</a></b> 💸
🔗 <b><a href="https://t.me/solana_trojanbot?start=r-godrekt-{token}">Trojan</a></b>
                        """                                    
                                        await forward_doge(token)
                                        await forward_alert(message_final)
                                    insert_data_coin_gem(token, "dex", fdv_temp, None, None, None, None)              
                            #await forward_trend("https://dexscreener.com/solana/"+token+"?/=#trendsCount1000USD2 "+store_str+" #C:"+str(convic)+" #Count:"+str(high_count_tokens[token]['count'])+" "+params_cto)
                            #await forward_msg("https://birdeye.so/find-trades/"+token+"?chain=solana #trends "+params_cto+" member_TG:"+str(member_count))
                            high_count_tokens[token]['post'] = True
                        if high_count_tokens[token]['post'] == False and  high_count_tokens[token]['count'] > 1 and (time.time() - high_count_tokens[token]['createdDelta']) <= 2400 :
                            convic = 0
                            if token_address in high_count_tokens_6m:
                                convic += 1
                            if token_address in high_count_tokens_5m:
                                convic += 1
                            if token_address in high_count_tokens_00:
                                convic += 1


                            #if token in token_volume :
                            if not find_coin_gem_by_ca_id_and_platform(token, "dex"):
                                    chat_id = -2391890259  # Ganti dengan ID chat yang diambil dari URL
                                    entity1 = await client.get_entity(PeerChannel(chat_id))
                                    total_smart_alpha= await search_messages(entity1, token_address)
                                    if total_smart_alpha:
                                        message_final = await get_message_for_tg(token)
                                        if message_final:                          
                                            message_final += f"""
🛒 <b><a href="https://t.me/BullxBetaBot?start=access_QDYDLGXD1U">Buy {pair["baseToken"]["symbol"]}</a></b> 💸
🔗 <b><a href="https://t.me/solana_trojanbot?start=r-godrekt-{token}">Trojan</a></b>
                            """                                    
                                            await forward_doge(token)
                                            await forward_alert(message_final)
                                        insert_data_coin_gem(token, "dex", fdv_temp, None, None, None, None)                 
                            await forward_msg("https://dexscreener.com/solana/"+token+"?/=#trendsCount1000USD2 "+store_str+" #C:"+str(convic)+" #Count:"+str(high_count_tokens[token]['count'])+" "+params_cto)
                            #await forward_msg("https://birdeye.so/find-trades/"+token+"?chain=solana #trends "+params_cto+" member_TG:"+str(member_count))
                            high_count_tokens[token]['post'] = True
                        if high_count_tokens[token]['post'] == False and  high_count_tokens[token]['count'] > 2 and (time.time() - high_count_tokens[token]['createdDelta']) <= 1000 :
                            convic = 0
                            if token_address in high_count_tokens_6m:
                                convic += 1
                            if token_address in high_count_tokens_5m:
                                convic += 1
                            if token_address in high_count_tokens_00:
                                convic += 1
                            
                            if token in token_volume :
                                if not find_coin_gem_by_ca_id_and_platform(token, "dex"):
                                    message_final = await get_message_for_tg(token)
                                    if message_final:                          
                                        message_final += f"""
🛒 <b><a href="https://t.me/BullxBetaBot?start=access_QDYDLGXD1U">Buy {pair["baseToken"]["symbol"]}</a></b> 💸
🔗 <b><a href="https://t.me/solana_trojanbot?start=r-godrekt-{token}">Trojan</a></b>
                        """                                    
                                        await forward_doge(token)
                                        await forward_alert(message_final)
                                    insert_data_coin_gem(token, "dex", fdv_temp, None, None, None, None)           
                            await forward_trend("https://dexscreener.com/solana/"+token+"?/=#trendsCount1000USD3 "+store_str+" "+dex_str+" #C:"+str(convic)+" #Count:"+str(high_count_tokens[token]['count'])+" "+params_cto)
                            #await forward_msg("https://birdeye.so/find-trades/"+token+"?chain=solana #trends "+params_cto+" member_TG:"+str(member_count))
                            high_count_tokens[token]['post'] = True
                        elif high_count_tokens[token]['post'] == False and high_count_tokens[token]['count'] > 2:
                            convic = 0
                            if token_address in high_count_tokens_6m:
                                convic += 1
                            if token_address in high_count_tokens_5m:
                                convic += 1
                            if token_address in high_count_tokens_00:
                                convic += 1
                            if not find_coin_gem_by_ca_id_and_platform(token, "dex"):
                                message_final = await get_message_for_tg(token)  
                                if message_final:                          
                                    message_final += f"""
🛒 <b><a href="https://t.me/BullxBetaBot?start=access_QDYDLGXD1U">Buy {pair["baseToken"]["symbol"]}</a></b> 💸
🔗 <b><a href="https://t.me/solana_trojanbot?start=r-godrekt-{token}">Trojan</a></b>
                    """                                    
                                    await forward_doge(token)
                                    await forward_alert(message_final)
                                insert_data_coin_gem(token, "dex", fdv_temp, None, None, None, None)    
                            await forward_trend("https://dexscreener.com/solana/"+token+"?/=#trendsCount1000USD "+store_str+" "+dex_str+"  #C:"+str(convic)+" #Count:"+str(high_count_tokens[token]['count']))
                            await forward_trend("https://birdeye.so/find-trades/"+token+"?chain=solana #trends "+params_cto)
                            high_count_tokens[token]['post'] = True
                        
                    
                    # Hapus token dari penyimpanan setelah lebih dari satu jam
                    tokens_to_remove1 = [token for token, value in high_count_tokens.items() if current_date - datetime.fromtimestamp(value['block_time']) > timedelta(minutes=60)]
                    for token in tokens_to_remove1:
                        del high_count_tokens[token]
                    
                    tokens_to_remove2 = [token for token, time_added in high_count_tokens_5m.items() if current_date - time_added > timedelta(minutes=60)]
                    for token in tokens_to_remove2:
                        del high_count_tokens_5m[token]

                    tokens_to_remove3 = [token for token, time_added in high_count_tokens_6m.items() if current_date - time_added > timedelta(minutes=60)]
                    for token in tokens_to_remove3:
                        del high_count_tokens_6m[token]

                    tokens_to_remove4 = [token for token, time_added in token_volume.items() if current_date - time_added > timedelta(minutes=40)]
                    for token in tokens_to_remove4:
                        del token_volume[token]
                    #print("token_volume", token_volume)

                    tokens_to_remove5 = [token for token, time_added in viral_store.items() if current_date - time_added > timedelta(minutes=40)]
                    for token in tokens_to_remove5:
                        del viral_store[token]

                    tokens_to_remove6 = [token for token, time_added in token_list.items() if current_date - time_added > timedelta(minutes=120)]
                    for token in tokens_to_remove6:
                        del token_list[token]
                    
                    #print(high_count_tokens)

            except Exception as e:
                    tb = traceback.format_exc()
                    print("An error occurred:\n", tb)
                    #await asyncio.sleep(10)
                    #await forward_alert("Error11: ALERRTTT" + str(e))	
                    print(f"Error11: {e}")

#=================================================================================================================================

async def get_message_for_tg(token):
    global buyer_bot
    url_dexscreener = f'https://api.dexscreener.com/latest/dex/tokens/{token}'
    headers_dexscreener = headers_dexscreener = {}
    dexscreener_data = await fetch_data_coin(url_dexscreener, headers_dexscreener)

    if 'error' in dexscreener_data:
        print("ASSSSSOOOOOy")
        print(dexscreener_data['error'])

    pairs = dexscreener_data.get('pairs', None)
                            #print(pairs)
    print("AAA")
    if pairs:
        smart_wallet_alpha = "No"
        wib_time_str = None
        chat_id = -2391890259  # Ganti dengan ID chat yang diambil dari URL
        entity1 = await client.get_entity(PeerChannel(chat_id))
            #if not find_coin_gem_by_ca_id_and_platform(token, "sa"):
                #insert_data_coin_gem(token, "sa", 0, None, None, None, None)
        liq = 0
        fdv= 11000000
        pair = pairs[0]  # Ambil pasangan pertama
        price_change_h24 = pair.get('priceChange', {}).get('h1', None)
        liq = pair.get('liquidity', {}).get('usd', None)
        fdv = pair.get('fdv', None)
        pair_created_at = pair.get('pairCreatedAt', None)
        pair_created_at = pair_created_at / 1000
        if pair_created_at:
            datetime_obj = datetime.fromtimestamp(pair_created_at, tz=pytz.UTC)

            # Convert to WIB (Waktu Indonesia Barat) timezone
            wib_timezone = pytz.timezone("Asia/Jakarta")
            datetime_wib = datetime_obj.astimezone(wib_timezone)

            # Save the formatted date and time to a variable
            wib_time_str = datetime_wib.strftime('%Y-%m-%d %H:%M:%S %Z')
            current_time_wib = datetime.now(pytz.timezone('Asia/Jakarta'))

            # Hitung perbedaan waktu dalam menit
            time_difference_minutes = int((current_time_wib - datetime_wib).total_seconds() / 60)
            if time_difference_minutes > 30:
                return False
                

            #print(f"Beda waktu: {time_difference_minutes} menit")
        socials = pair.get('info', {}).get('socials', [])
        websites = pair.get('info', {}).get('websites', [])
        twitter_url = None
        telegram_url = None
        web_url = None
        for social in socials:
            if social.get('type') == 'twitter':
                twitter_url = str(social.get('url'))
            elif social.get('type') == 'telegram':
                telegram_url = str(social.get('url'))
        for web in websites:
            if web.get('label') == 'Website':
                web_url = str(web.get('url'))
        found_tokenss = None
        if twitter_url:
            found_tokenss = [token for token in viral_store if (token in twitter_url.lower() and token != "solana" and len(token)>1)]
        found_name = [token for token in viral_name if (token in pair["baseToken"]["symbol"].lower() and token != "solana" and len(token)>1)]
        viral_tw = "No"
        if found_tokenss or found_name or find_coin_gem_by_ca_id_and_platform(token, "pf"):
            viral_tw = "✅"
        
        ave_analitic = await call_api(token)
        message_jp = get_wallet_signal_by_ca(token)
        mcmoney_aler=""
        match_sm = re.search(r"Smarters:\s*(\d+)", ave_analitic)
        if match_sm:
            smarters_value = int(match_sm.group(1))
            if time_difference_minutes < 10 and smarters_value > 20:
                mcmoney_aler=" 💰 "


        message_final = f"""
📊{mcmoney_aler}💎<b>{pair["baseToken"]["symbol"]}</b> #{pair["baseToken"]["name"]} [<a href="https://pump.fun/{token}">pf</a>] [<a href="https://bullx.io/terminal?chainId=1399811149&address={token}">bullx</a>] [<a href="https://gmgn.ai/sol/token/{token}?tab=activity">gmgn</a>] [<a href="https://ave.ai/token/{token}-solana?from=Token">ave</a>]

<code>{token}</code>

MC: ${fdv}   |       Liq: ${liq}
<a href="https://dexscreener.com/solana/{token}">Chart</a>  |  <a href="https://rugcheck.xyz/tokens/{token}">Rugcheck</a>  |  <a href="https://solscan.io/token/{token}">Solscan</a>
<a href="{telegram_url}">Telegram</a>  |  <a href="{web_url}">Website</a>  |  <a href="{twitter_url}">Twitter</a>

potential viral: {viral_tw}
created_at: {wib_time_str} .   {time_difference_minutes} minute ago

{ave_analitic}
{message_jp}
"""
        return message_final
# waktu di pumpfun ===================================================================================================================

def is_sideways(prices, threshold=0.1, mean_threshold=6.141472506989746e-8):
    mean_price = statistics.mean(prices)
    if mean_price >= mean_threshold:
        return False
    for price in prices:
        if abs(price - mean_price) / mean_price > threshold:
            return False
    return True

def detect_spike(data, avg_volume, spike_threshold=2):
    for item in data:
        volume = item['volume']
        close = item['close']
        open_price = item['open']
        if volume > avg_volume * spike_threshold and close > open_price:
            return True
    return False

def check_token(token_address):
    url = "https://108.181.33.119/api/checkToken"
    params = {
        "tokenAddress": token_address,
        "__cpo": "aHR0cHM6Ly93d3cuY2hlY2tkZXgueHl6"
    }
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Accept-Language": "en-US,en;q=0.9,id;q=0.8,ms;q=0.7",
        "Cache-Control": "max-age=0",
        "Connection": "keep-alive",
        "Cookie": "__cpc=RXFOUlV0ZjFxdHg5L1VGd1ZrazRKZm5iR3ZOZ1ZobVlPVHpTcWRGdnJBa0VHU2RqVXhScWNjUXB1OFg5R3k1REdGQk56M2ZtbUc3bDg1UFhYcW9BMWFjZnpWLzh2VVlXd1JvTFNPZXNVK3ZDWWNYc1lCVHE5SW1oSE1SMkJJMEh2eHkzTDRjR2o2YTBXSUlyOE9uTDZoU2p5ckt3dmZiWkJ4WjRwUTlxVzdDc0dNb05DQ2l2eHNTenBJY2JDNXIrWEFQZkhLOHBwSFg2QTBrMzBGVXljTlM3b1F1T2MxMndDdXg5U2VJbEJnb1pERUNBNFkrVGpRWWh1ekI5S0kydDBVQjVaZTg4bkZEd0JUajhqZ0lKMmVpcXNrMzdpNkY4UGFHWDZiOXpOMVBsWkxXcC80SjhBMG5TdW1hWko1d0lDS0dka1V5NzZuL1h5UUd3TXBxa2J4Y1lrdUtVZ1g5WmFtbFhIR3dSbE9hNFhIUmpMcjRKSSs3WEpYTVdiQ0p6eUtTcWdRWk9JTHpYTndpR1ovZkt0R0NwZjdoUTUrMERTKzU4UkF1N0lpUWFqeGw2aGQ4VFpHLytCMm1ZUndvOTNyUkRnVUxqeVRYZHprakFKWWJ1U2c9PQ==",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "none",
        "Sec-Fetch-User": "?1",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
        "sec-ch-ua": '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"'
    }
   
    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        return response  # Assuming the response is JSON
    else:
        print(f"Request failed with status token paid code {response.status_code}")
        return None
    
def check_token2(token_address):
    url = 'https://185.16.38.230/api/checkToken'

    params = {
        'tokenAddress': token_address,
        '__cpo': 'aHR0cHM6Ly93d3cuY2hlY2tkZXgueHl6'
    }

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Language': 'en-US,en;q=0.9,id;q=0.8,ms;q=0.7',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Cookie': '__cpc=YjdMaGNkQXh5bjh2allsMWRlZXBnRklacHZTMkxxa09zK0d1K1BCazZPRnJ6eXVZQ280b25OcWkwQ01FKzZNS0w4aU94TzJqbWJPTnFvZ3p4MzdJMEZjYjBzajYvK1VwNjFCNGllczdWdUF1YzhuRGRXd2VUZnZtcElFbTZER1I=',
        'Referer': 'https://185.16.38.230/__cpi.php?s=YjdMaGNkQXh5bjh2allsMWRlZXBnRklacHZTMkxxa09zK0d1K1BCazZPRnJ6eXVZQ280b25OcWkwQ01FKzZNS0w4aU94TzJqbWJPTnFvZ3p4MzdJMEZjYjBzajYvK1VwNjFCNGllczdWdUF1YzhuRGRXd2VUZnZtcElFbTZER1I%3D&r=aHR0cHM6Ly93d3cuY2hlY2tkZXgueHl6L2FwaS9jaGVja1Rva2VuP3Rva2VuQWRkcmVzcz1BNWhDM2s0Z0dMM2p0ejdYN2RnWFhFQUx1NnA3SnNER0dkbnljc2hQcHVtcA%3D%3D&__cpo=1',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }
   
    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        return response  # Assuming the response is JSON
    else:
        print(f"Request failed with status token paid code {response.status_code}")
        return None
    
def check_price(token_address):
    url = f"https://frontend-api.pump.fun/candlesticks/{token_address}?offset=0&limit=1000&timeframe=1" 
    headers = {
        "accept": "*/*",
        "accept-language": "en-US,en;q=0.9,id;q=0.8,ms;q=0.7",
        "if-none-match": 'W/"93e-bo8+J78RPS0I6CapRtkE1lQcxKk"',
        "origin": "https://pump.fun",
        "priority": "u=1, i",
        "referer": "https://pump.fun/",
        "sec-ch-ua": '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
    } 
    params = {
        "tokenAddress": token_address
    }

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        return response  # Assuming the response is JSON
    else:
        print(f"Request failed with status price code {response.status_code}")
        return None
    
def check_tx(token_address):
    url = "https://frontend-api.pump.fun/trades/all/"+token_address    
    headers = {
        "accept": "*/*",
        "accept-language": "en-US,en;q=0.9,id;q=0.8,ms;q=0.7",
        "origin": "https://pump.fun",
        "referer": "https://pump.fun/",
        "Cookie": "__cf_bm=HmXY2EppDpCAi8a.dLEV_tVKDgZafnEFMr_Z6Lyu4eo-1726945869-1.0.1.1-3KWUgOzfJQ_5w8qlcoCr2vcm.qC5gEJHPwExOsS5rD7Wf8EznxVKoJBacZYJoIWJIVVdV01slDKzW7NK6_dqPQ"
    }

    offset = 0
    all_data_tx = []

    while True:
        params = {
            "limit": 200,
            "offset": offset,
            "minimumSize": 0
        }
        
        response = requests.get(url, headers=headers, params=params)
        
        if response.status_code == 200:
            data_tx = response.json()
            
            if len(data_tx) == 0:
                break
            
            all_data_tx.extend(data_tx)
            offset += 200
        else:
            print(f"Errorgugugu: {response.status_code}")
            break

    if all_data_tx:
        return all_data_tx  # Assuming the response is JSON
    else:
        print(f"Request failed with status tx code {response.status_code}")
        return None

def extract_segment(url):
    # Menghapus "https://" atau "http://"
    url = url.replace("https://", "").replace("http://", "")
    # Memisahkan domain dan sisa URL
    parts = url.split("/", 1)
    # Memeriksa apakah ada bagian setelah domain
    if len(parts) > 1:
        subparts = parts[1].split("/", 1)
        return subparts[0]
    return None

def format_twitter_link(twitter_status):
    # Mengekstrak URL dari format markdown link
    url_match = re.search(r'\((https?://[^\s]+)\)', twitter_status)
    if url_match:
        url = url_match.group(1)
        # Menggunakan regex untuk menghapus parameter tambahan di URL
        clean_url = re.sub(r'\?.*$', '', url)
        return clean_url
    return twitter_status

def hapus_setelah_tutup_kurung(text):
    if ']' in text:
        return text.split(']')[0]  # Mengambil bagian sebelum ']'
    return text  # Jika tidak ada ']', kembalikan teks aslinya

@client.on(events.NewMessage(chats=["@PumpFunNewPools"]))  # Ganti dengan nama grup Anda
async def handle_new_message(event):
    try:
        pattern = r"🔗 \*\*MINT CA\*\*\n`([^`]+)`"
        word_after_sol_of=""
        pattern_of = r"of\s+(\w+)"
        match_of = re.search(pattern_of, event.message.text)
        # Regex patterns
        pattern_website = r"Website\*\* :\s+(.*)"
        pattern_twitter = r"Twitter\*\* :\s+(.*)"
        pattern_telegram = r"Telegram\*\* :\s+(.*)"
        # Regex untuk menemukan alamat akun Solana dari URL

        # Search for patterns
        match_website = re.search(pattern_website, event.message.text)
        match_twitter = re.search(pattern_twitter, event.message.text)
        match_telegram = re.search(pattern_telegram, event.message.text)
        match = re.search(pattern, event.message.text)
        match_name = re.search(r'SOL of (\w{3})', event.message.text)

        

        if "NEW PUMP FUN POOL" in event.message.text and match and match_of and  match_website and match_twitter and match_telegram:
            token_address = match.group(1)
            website_status = match_website.group(1).strip()
            twitter_status = match_twitter.group(1).strip()
            telegram_status = match_telegram.group(1).strip()
            if match_name:
                word_after_sol_of = match_name.group(1)

            #print(first_address)
           
            #print(response)
            try:
                current_time = datetime.now()
                # Menghapus token yang sudah lebih dari 1 menit
                word_after_sol_of =word_after_sol_of.lower()
                #print(word_after_sol_of)
                #response_paid = check_token(token_address)
                token_temps[token_address] = current_time
                param_viral = False
                tokens_to_remove3 = [token for token, data in viral_token.items() if all(current_time - time_added > timedelta(minutes=1) for time_added in data['timestamps'])]
                for token in tokens_to_remove3:
                    del viral_token[token]
                
                tokens_to_remove4 = [token for token, data in viral_name.items() if all(current_time - time_added > timedelta(minutes=1) for time_added in data['timestamps'])]
                for token in tokens_to_remove4:
                    del viral_name[token]

                #print("_OA_OA_O_PA___YQ_YQ_YQ_QY_QYQYQ_YQ_YQ_YQ_YQ_YQ_Q_QY_QY_Q_QY_YQ_YQ_YQYQQ_Y_Q_QYY_QY_Q_YQYQ_QY_Q_YQ_YQ_QY_YQ_QY_Q_YQ_Q_YQY_QYQ_QY1")
                if "x.com" in twitter_status.lower():
                    if  "x.com" in website_status.lower() and "x.com" in telegram_status.lower():
                        param_viral = True
                    elif "available" in website_status.lower() and "available" in telegram_status.lower():
                        param_viral = True
                    elif "available" in website_status.lower() and "x.com" in telegram_status.lower():
                        param_viral = True

                    key_twitter = extract_segment(twitter_status.lower())
                    if key_twitter:
                        key_twitter = key_twitter.split(']')[0]
                        #print("_OA_OA_O_PA___YQ_YQ_YQ_QY_QYQYQ_YQ_YQ_YQ_YQ_YQ_Q_QY_QY_Q_QY_YQ_YQ_YQYQQ_Y_Q_QYY_QY_Q_YQYQ_QY_Q_YQ_YQ_QY_YQ_QY_Q_YQ_Q_YQY_QYQ_QY2")
                        #print(key_twitter)
                        #print(current_time)
                        # Mengecek apakah token sudah ada 2 kali dalam 10 menit terakhir
                        token_data = viral_token.get(key_twitter, {'timestamps': [], 'some_string': twitter_status.lower(), 'some_boolean': param_viral})
                        token_data['timestamps'] = [time for time in token_data['timestamps'] if current_time - time <= timedelta(minutes=1)]

                        if len(token_data['timestamps']) >= 2 and param_viral:
                            if  key_twitter not in viral_store:
                                #await forward_alert_err("viraak")
                                #print("_OA_OA_O_PA___YQ_YQ_YQ_QY_QYQYQ_YQ_YQ_YQ_YQ_YQ_Q_QY_QY_Q_QY_YQ_YQ_YQYQQ_Y_Q_QYY_QY_Q_YQYQ_QY_Q_YQ_YQ_QY_YQ_QY_Q_YQ_Q_YQY_QYQ_QY3")
                                key_twitter = re.sub(r"\).*$", "", key_twitter)
                                formatted_link = format_twitter_link(twitter_status.lower())
                                formatted_link = hapus_setelah_tutup_kurung(formatted_link)
                                key_twitter = key_twitter.split(']')[0]
                                messages =  await find_coin_gem_by_keyword_platform_and_timeframe(key_twitter, "movray", True)
                                #await forward_alert_err("💎-X Potential Viral-💎\n" + formatted_link +"\n " + messages)
                                if not find_full_link_by_link(formatted_link):
                                    await forward_alert("💎-X Potential Viral-💎\n" + formatted_link +"\n " + messages)
                                    insert_data_twitter(key_twitter , formatted_link, None, word_after_sol_of)
                            viral_store[key_twitter] = current_time
                            if word_after_sol_of not in viral_name:
                                viral_name[word_after_sol_of] = {'timestamps': []}

                            # Tambahkan timestamp ke dalam list 'timestamps'
                            viral_name[word_after_sol_of]['timestamps'].append(current_time)

                        # Menambahkan waktu saat ini ke dalam daftar waktu token
                        token_data['timestamps'].append(current_time)

                        # Menyimpan string dan boolean baru atau memperbarui yang ada
                        token_data['some_string'] = twitter_status.lower()
                        token_data['some_boolean'] = True

                        # Menyimpan kembali data token ke dalam viral_token
                        if param_viral:
                            viral_token[key_twitter] = token_data

            except Exception as e:
                tb = traceback.format_exc()
                print("An error occurred:\n", tb)
                print(f"Error00909: {e}")

    except Exception as e:
        tb = traceback.format_exc()
        print("An error occurred:\n", tb)
        print(f"ErrorQQ: {e}")


async def fetch_data_coin(url, headers, retries=3, timeout=30):
    """
    Fetch data from the given URL using aiohttp with error handling and retry logic.

    Parameters:
        url (str): The API endpoint to fetch data from.
        headers (dict): The headers to include in the request.
        retries (int): Number of times to retry the request in case of failure (default is 3).
        timeout (int): Timeout for the request in seconds (default is 30 seconds).

    Returns:
        dict: JSON data from the response if successful, or error information.
    """
    timeout = aiohttp.ClientTimeout(total=timeout)  # Set a total timeout for the request

    for attempt in range(retries):
        try:
            async with aiohttp.ClientSession(timeout=timeout) as session:
                async with session.get(url, headers=headers) as response:
                    if response.status == 200:
                        data = await response.json()
                        return data
                    else:
                        return {'error': 'Request failed', 'status': response.status}
        
        except aiohttp.ClientConnectionError as e:
            print(f"Connection error on attempt {attempt+1}. Retrying... Error: {e}")
            if attempt < retries - 1:  # If it's not the last attempt, wait before retrying
                await asyncio.sleep(2)  # Wait 2 seconds before retrying
            else:
                return {'error': 'Connection failed after retries', 'details': str(e)}
        
        except aiohttp.ClientPayloadError as e:
            return {'error': 'Payload error', 'details': str(e)}
        
        except asyncio.TimeoutError as e:
            return {'error': 'Request timed out', 'details': str(e)}
        
        except Exception as e:
            return {'error': 'An unexpected error occurred', 'details': str(e)}
    
    return {'error': 'Failed to fetch data after retries'}

def calculate_delta_minutes(created_timestamp, king_of_the_hill_timestamp):
    created_time = datetime.fromtimestamp(created_timestamp / 1000, tz=timezone.utc)
    king_of_the_hill_time = datetime.fromtimestamp(king_of_the_hill_timestamp / 1000, tz=timezone.utc)
    delta = king_of_the_hill_time - created_time
    return delta.total_seconds() / 60  # Kembali dalam menit

async def check_string_async(s):
    # Cek apakah 4 karakter awal adalah huruf dan tidak diakhiri dengan 'pump'
    if re.match(r'^[A-Za-z]{4}', s) and not s.endswith('pump'):
        return True
    return False

def check_symbol(mint_string, symbol):
    return mint_string[:3].upper() == symbol[:3].upper()

async def get_token_info(mint_string, retries=3, delay=2):
    async with aiohttp.ClientSession() as session:
        url = f"https://pumpportal.fun/api/data/token-info?ca={mint_string}"
        for attempt in range(retries):
            async with session.get(url) as response:
                if response.status == 200:
                    token_info = await response.json()
                    if 'data' in token_info:
                        return token_info['data']
                await asyncio.sleep(delay)
        return None

def extract_part_of_url_from_string(text):
    # Regular expression untuk mencari pola https://x.com/<kata>/
    match = re.search(r'https://x\.com/([^/]+)/', text)
    if match:
        return match.group(1)
    else:
        return None


@client.on(events.NewMessage(chats=["@PumpFunRaydium"]))  # Ganti dengan nama grup Anda
async def handle_new_message(event):
    try:
        pattern = r"`([a-zA-Z0-9]{32,})`"
        word_after_sol_of=""
        pattern_of = r"of\s+(\w+)"
        # Regex untuk menemukan alamat akun Solana dari URL
        #print(event.message.text)
        match = re.search(pattern, event.message.text)
        if "Token migration completed to Raydium" in event.message.text and match:
            token_address = match.group(1)
            print("okoktototoooto")
            print(token_address)
            insert_data_coin_gem(token_address, "pf", 60000, None, None, None, None)
            ave_analitic = await call_api(token_address)
            message_jp = get_wallet_signal_by_ca(token_address)
                #gmgn_data = await fetch_gmgn(token_address)
            await forward_rick_bot(token_address+"\n "+ ave_analitic  +"\n "+message_jp)
    
    except Exception as e:
        tb = traceback.format_exc()
        print("An error occurred:\n", tb)
        print(f"ErrorQQ: {e}")

# Fungsi untuk menangani pesan baru
@client.on(events.NewMessage(chats=[PeerChannel(plonk_bot)]))  # Ganti dengan nama grup Anda
async def handle_new_message(event):
    try:
        global buyer_bot
        token_address = ""
        ray_params = False
        symbol=""
        mcap = 0
        formatted_message = ""
        twitter_link = ""
        sm = 0
        if  "NEW RAYDIUM LAUNCH" in event.message.text and "Trending" not in event.message.text and not find_coin_gem_by_ca_id_and_platform(token_address, "pf"):
            #print(event.message.text)
            
            match = re.search(r'Mint:\s*`([\w]+)`', event.message.text)
            if match:
                token_address = match.group(1)
                print(token_address)
                insert_data_coin_gem(token_address, "pf", 60000, None, None, None, None)
                ave_analitic = await call_api(token_address)
                message_jp = get_wallet_signal_by_ca(token_address)
                #gmgn_data = await fetch_gmgn(token_address)
                await forward_rick_bot(token_address+"\n "+ ave_analitic  +"\n "+message_jp)

        if  "MOVING TO RAYDIUM" in event.message.text and "Trending" not in event.message.text :
            ray_params = True
        if (ray_params or "NEW KOTH" in event.message.text) and not any(substring in  event.message.text for substring in banned) and not any(substring in  event.message.text for substring in banned_wallet):
            match = re.search(r'\*\*Mint:\*\* `([\w]+)`', event.message.text)
            formatted_message = ""
            whale1 = ""
            whale2 = ""
            wallet_ray = ""
            mcmoney = ""
            if match:
                token_address = match.group(1)
            #print(event.message.text)
            if ray_params == False:
                print(f"CA KOTH: {token_address}")
                mcap = 30000
                # Regex untuk setiap bagian
                name_regex = r'\*\*Name:\*\* (.*?)\n'
                symbol_regex = r'\*\*Symbol:\*\* (.*?)\n'
                market_cap_regex = r'\*\*Market Cap:\*\* \$(.*?)\n'
                reply_count_regex = r'\*\*Reply Count:\*\* (.*?)\n'

                # Menggunakan regex untuk ekstrak nilai
                name_match = re.search(name_regex, event.message.text)
                symbol_match = re.search(symbol_regex, event.message.text)
                market_cap_match = re.search(market_cap_regex, event.message.text)
                reply_count_match = re.search(reply_count_regex, event.message.text)

                '''
                # Membentuk ulang pesan dengan hasil ekstraksi
                formatted_message = f"""
💊 💎 <b>{symbol_match.group(1)}</b> #{name_match.group(1)} [<a href="https://pump.fun/{token_address}">pumpfun</a>] 

<code>{token_address}</code>
<b>Name:</b> {name_match.group(1)}
<b>Symbol:</b> {symbol_match.group(1)}

<b>Market Cap:</b> ${market_cap_match.group(1)}
<b>Reply Count:</b> {reply_count_match.group(1)}

🛒 <b><a href="https://bullx.io/terminal?chainId=1399811149&address={token_address}">Buy {symbol_match.group(1)}</a></b> 💸
🔗 <b><a href="https://t.me/helenus_trojanbot?startr-doremifas493385">Trojan</a></b>
                """
            elif ray_params:
                current_time = datetime.now()
                #token_list[token_address] = current_time
                print(f"CA Ray: {token_address}")
                mcap = 60000
                #print(event.message.text)
                status_regex = r'✅ \*\*(.*?)\*\* ✅'
                name_regex = r'\*\*Name:\*\* (.*?)\n'
                symbol_regex = r'\*\*Symbol:\*\* (.*?)\n'
                top20_holding_regex = r'\*\*Top 20 Holding: (.*?)%\*\*'
                twitter_link = "~~"
                viral_parameter = "_X_"
                smart_wallet_alpha = "No"
                # Menggunakan regex untuk ekstrak nilai
                status_match = re.search(status_regex, event.message.text)
                name_match = re.search(r"\*\*Name:\*\*\s*([^\n]+)", event.message.text)
                symbol_match = re.search(r"\*\*Symbol:\*\*\s*([^\n]+)", event.message.text)
                symbol = symbol_match.group(1)
                top20_holding_match = re.search(top20_holding_regex, event.message.text)
                # Membentuk ulang pesan dengan hasil ekstraksi
                total_smart_alpha= 0
                whale1 = 0
                whale2 =0
                wallet_ray = 0
                #ave_analitic = await call_api(token_address)
                message_jp = get_wallet_signal_by_ca(token_address)
                #gmgn_data = await fetch_gmgn(token_address)
                #await forward_rick_bot(token_address+"\n "+ ave_analitic  +"\n "+message_jp)
                numbers = list(map(int, re.findall(r'\d+', ave_analitic)))
                if numbers:
                    sm = int(numbers[0])
                    #insert_data_ray_list(token_address, total_smart_alpha, buyer_bot, numbers[0], numbers[1], numbers[2], numbers[3], numbers[4], (whale1) , (whale2) , (wallet_ray) , (0))

                formatted_message = f"""
💊 💎<b>{symbol_match.group(1)}</b> #{name_match.group(1)} [<a href="https://pump.fun/{token_address}">pumpfun</a>] [<a href="https://gmgn.ai/sol/token/{token_address}?tab=activity">gmgn</a>] [<a href="https://ave.ai/token/{token_address}-solana?from=Token">ave</a>]

✅ <b>{status_match.group(1)}</b> ✅

<code>{token_address}</code>

<b>Name:</b> {name_match.group(1)}
<b>Symbol:</b> {symbol_match.group(1)}
<b>X:</b> {twitter_link}
<b>Viral:</b> {viral_parameter}
<b>Top 20 Holding:</b> {top20_holding_match.group(1)}%
whale1: {whale1} | whale2: {whale2} | wallet_ray: {wallet_ray}
{message_jp}
                """

        if token_address != "":
            waktu_sekarang = datetime.now()
            all_data_tx =check_tx(token_address)
            response = check_price(token_address)
            #response_paid = check_token(token_address)
            
               
            if all_data_tx and response and response.status_code == 200:

                print("token adres PF "+token_address)
                paid = False
                # Panjang array utama
                array_length = len(all_data_tx)
    
                # Menghitung jumlah buy dan sell
                total_buy = sum(1 for trade in all_data_tx if trade['is_buy'])
                total_sell = sum(1 for trade in all_data_tx if not trade['is_buy'])
                
                # Menghitung jumlah buy dan sell dengan sol_amount lebih dari 1.000.000.000
                high_value_buy = sum(1 for trade in all_data_tx if trade['is_buy'] and trade['sol_amount'] > 1_000_000_000)
                high_value_sell = sum(1 for trade in all_data_tx if not trade['is_buy'] and trade['sol_amount'] > 1_000_000_000)
                
                # Menghitung jumlah buy dengan sol_amount lebih dari 5.000.000.000
                high_value_buy_5b = sum(1 for trade in all_data_tx if trade['is_buy'] and trade['sol_amount'] > 5_000_000_000)
                
                # Menghitung jumlah data dengan timestamp yang sama
                timestamps = [trade['timestamp'] for trade in all_data_tx]
                timestamp_counts = Counter(timestamps)
                duplicate_timestamps = {timestamp for timestamp, count in timestamp_counts.items() if count > 1}
                filtered_users = [trade for trade in all_data_tx if trade['is_buy'] and trade['sol_amount'] >= 500000000 and trade['timestamp'] in duplicate_timestamps]
                
                # Mendapatkan sol_amount tertinggi ketika is_buy
                max_sol_amount_buy = max((trade['sol_amount'] for trade in all_data_tx if trade['is_buy']), default=None)
                
                # Menghitung total sol_amount untuk setiap user yang is_buy = true
                user_sol_amounts = defaultdict(int)
                user_timestamps = defaultdict(list)
                user_transactions = defaultdict(list)
                for trade in all_data_tx:
                    if trade['is_buy']:
                        user_sol_amounts[trade['user']] += trade['sol_amount']
                        user_timestamps[trade['user']].append(trade['timestamp'])
                        user_transactions[trade['user']].append(trade['sol_amount'])
                
                # Mengambil 5 user dengan sol_amount tertinggi
                top_users = sorted(user_sol_amounts.items(), key=lambda x: x[1], reverse=True)[:5]

                # Memeriksa kesamaan timestamp antara top 5 users
                timestamp_matches = defaultdict(set)
                for user, _ in top_users:
                    timestamps = user_timestamps[user]
                    for timestamp in timestamps:
                        for other_user, _ in top_users:
                            if other_user != user and timestamp in user_timestamps[other_user]:
                                timestamp_matches[user].add(timestamp)
                                timestamp_matches[other_user].add(timestamp)

                    # Menentukan apakah ada user yang memiliki kesamaan timestamp lebih dari sekali
                has_multiple_matches = {user: len(matches) > 1 for user, matches in timestamp_matches.items()}
                
                # Mencari user dengan signature yang sama di filtered_users
                signature_counts = defaultdict(int)
                sol_amounts_per_signature = defaultdict(int)
                
                for trade in filtered_users:
                    signature = trade['signature']
                    signature_counts[signature] += 1
                    sol_amounts_per_signature[signature] += trade['sol_amount']
                
                # Mengambil jumlah user dengan signature yang sama dan total sol_amount
                same_signature_users = [(signature, count, sol_amount) for signature, count, sol_amount in zip(signature_counts.keys(), signature_counts.values(), sol_amounts_per_signature.values()) if count > 1]

                # Menghitung total sol_amount dari grup user yang memiliki kesamaan signature dengan minimal 2 atau lebih
                total_sol_amount_grouped = sum(sol_amount for _, _, sol_amount in same_signature_users)


                user_token_amounts = defaultdict(int)
                for trade in all_data_tx:
                    if trade['is_buy']:
                        user_token_amounts[trade['user']] += trade['token_amount']
                    else:
                        user_token_amounts[trade['user']] -= trade['token_amount']
                
                # Mengambil 5 user dengan token_amount tertinggi
                top_token_holders = sorted(user_token_amounts.items(), key=lambda x: x[1], reverse=True)[:5]

                if "**Tool**" in event.message.text:
                    text_temp= event.message.text.split("**Tool**")[0]
                else:
                    text_temp= event.message.text.split("**AD**")[0]
                    
                # Hasil yang akan ditampilkan
                result = (
                    f": {text_temp}\n"
                    f"Panjang array utama: {array_length}\n"
                    f"Jumlah total buy: {total_buy}\n"
                    f"Jumlah total sell: {total_sell}\n"
                    f"Jumlah data dengan timestamp yang sama: {len(duplicate_timestamps)}\n"
                    f"sol_amount tertinggi ketika is_buy: {max_sol_amount_buy / 1_000_000_000:.2f} SOL\n"
                    f"Total sol_amount untuk 5 users tertinggi dengan is_buy=True:\n"
                )
                
                top_user_flag = True
                count_i = 1
                for user, total_sol in top_users:
                    count_x=1
                    total_sol_billion = total_sol / 1_000_000_000
                    if total_sol_billion > 15:
                        top_user_flag = False
                    result += f"{count_i}: {user}\n"
                    result += f"   Total: {total_sol_billion:.2f} SOL\n"
                    for sol_amount in user_transactions[user]:
                        result += f"  {count_x}: {sol_amount / 1_000_000_000:.2f}  SOL\n"
                        count_x +=1
                    count_i+=1
                
                result += "Jumlah user dengan signature yang sama dan total sol_amount:\n"
                for signature, count, total_sol in same_signature_users:
                    total_sol_billion = total_sol / 1_000_000_000
                    result += f"Jumlah user: {count}, Total sol_amount: {total_sol_billion:.2f} SOL\n"
                    if count > 1:
                        top_user_flag = False
                
                                                                    # Menambahkan hasil pemeriksaan kesamaan timestamp
                result += "\nKesamaan timestamp antara top 5 users:\n"
                for user, has_match in has_multiple_matches.items():
                    if has_match:
                        result += f"{user}: {has_match}\n"
                        top_user_flag = False

                result += "\nTop 5 token holders:\n"
                for user, total_token in top_token_holders:
                    nilai_2 = 1000000000000000
                    # Menghitung persentase
                    persentase = (total_token / nilai_2) * 100
                    if user in banned_wallet or persentase > 12:
                        top_user_flag = False

                
                sent = False
                ray= ""
                if ray_params:
                    ray= "RAYYY LIST Deploy"
                else:
                    ray= "KOTH"

                current_time = datetime.now()
                viral_param = False
                text_messages =event.message.text
                insert_data_coin_gem(token_address, "pf", mcap, None, None, None, None)
                found_tokens = [token for token in viral_store if (token in text_messages.lower() and token != "solana" and len(token)>1)]
                found_name = [token for token in viral_name if (token in symbol.lower() and token != "solana" and len(token)>1)]
                new_twitter_link = ""
                if  (found_tokens or found_name):
                    if found_tokens:
                        new_twitter_link = find_latest_full_link_by_keyword(found_tokens[0])
                        formatted_message = formatted_message.replace(twitter_link, new_twitter_link)    
                    viral_param = True
                if sm > 8 and ray_params and viral_param and (not find_coin_gem_by_ca_id_and_platform(token_address, "pf")) and viral_param:
                    new_twitter_link = ""
                    if viral_param:
                        formatted_message = formatted_message.replace(viral_parameter, "✅")
                    formatted_message += f"""
🛒 <b><a href="https://bullx.io/terminal?chainId=1399811149&address={token_address}">Buy {symbol}</a></b> 💸
🔗 <b><a href="https://t.me/helenus_trojanbot?startr-doremifas493385-{token_address}">Trojan</a></b>
                """
                    await forward_doge(token_address)     
                    await forward_alert(formatted_message)
                    if smart_wallet_alpha == "✅" and (not find_coin_gem_by_ca_id_and_platform(token_address, "sa")):
                        insert_data_coin_gem(token_address, "sa", mcap, None, None, None, None)
                    
                    # Cari data berdasarkan ca_id dan platform

                if total_sol_amount_grouped / 1_000_000_000 < 1 and max_sol_amount_buy / 1_000_000_000 < 15 and top_user_flag:
                    if token_address in token_temps:
                        waktu_simpan=token_temps[token_address]
                        selisih_waktu = waktu_sekarang - waktu_simpan
                        if selisih_waktu < timedelta(minutes=5):
                            token_volume[token_address] = current_time
                            if viral_param:
                                if not find_coin_gem_by_ca_id_and_platform(token_address, "pf"):
                                    if ray_params:
                                        #await forward_alert(formatted_message)
                                        insert_data_coin_gem(token_address, "pf", mcap, None, None, None, None)
                                    else:
                                        insert_data_coin_gem(token_address, "viralkoth", mcap, None, None, None, None)
                            await forward_msg("https://pump.fun/"+str(token_address)+" "+result+"  SinyalFASTLISTING "+ ray)
                            #await #await forward_check_x(str(token_address))(str(token_address))

                    data = response.json()

                    if sent == False and paid:
                        print("Datsinyall paid 1")
                        print(paid)
                        sent = True
                        token_volume[token_address] = current_time
                        if viral_param:
                            if not find_coin_gem_by_ca_id_and_platform(token_address, "pf"):
                                if ray_params:
                                    #await forward_alert(formatted_message)
                                    insert_data_coin_gem(token_address, "pf", mcap, None, None, None, None)
                        insert_data_coin_gem(token_address, "koth", mcap, None, None, None, None)
                        await forward_msg("https://pump.fun/"+str(token_address)+" "+result+"  Viral Param PF "+ray)
                        #await #await forward_check_x(str(token_address))(str(token_address))
                    if sent == False and len(data) == 2 and data[0]['volume'] > 40203042087 and data[1]['volume'] > 40203042087 and  data[0]['close'] > data[0]['open'] and  data[1]['close'] > data[1]['open']:
                        print("Datsinyall 1")
                        sent = True
                        token_volume[token_address] = current_time
                        if not find_coin_gem_by_ca_id_and_platform(token_address, "pf"):
                            if viral_param:
                                if ray_params:
                                    #await forward_alert(formatted_message)
                                    insert_data_coin_gem(token_address, "pf", mcap, None, None, None, None)
                                else:
                                    insert_data_coin_gem(token_address, "koth", mcap, None, None, None, None)
                            elif ray_params:
                                insert_data_coin_gem(token_address, "listray", mcap, None, None, None, None)
                            
                        await forward_msg("https://pump.fun/"+str(token_address)+" "+result+"  SinyalvolumePump1 "+ray)
                        #await #await forward_check_x(str(token_address))(str(token_address))
                    if  sent == False and len(data) > 3 and data[-1]['volume'] > 20203042087 and data[-1]['close'] > data[-1]['open'] and data[-2]['close'] > data[-2]['open'] and data[-3]['close'] > data[-3]['open']:
                        print("Datsinyall 2")
                        sent = True
                        token_volume[token_address] = current_time
                        if not find_coin_gem_by_ca_id_and_platform(token_address, "pf"):
                            if viral_param:
                                if ray_params:
                                    #await forward_alert(formatted_message)
                                    insert_data_coin_gem(token_address, "pf", mcap, None, None, None, None)
                                else:
                                    insert_data_coin_gem(token_address, "koth", mcap, None, None, None, None)
                            elif ray_params:
                                insert_data_coin_gem(token_address, "listray", mcap, None, None, None, None)
                        await forward_msg("https://pump.fun/"+str(token_address)+" "+result+"  SinyalvolumePump2 "+ray)
                        #await #await forward_check_x(str(token_address))(str(token_address))
                    if sent == False and len(data) <= 4 and len(data) > 2 and  data[0]['volume'] > 10203042087 and data[1]['volume'] > 12203042087 and data[2]['volume'] > 14203042087 :
                        print("Datsinyall 3")
                        sent = True
                        token_volume[token_address] = current_time
                        if not find_coin_gem_by_ca_id_and_platform(token_address, "pf"):
                            if viral_param:
                                if ray_params:
                                    #await forward_alert(formatted_message)
                                    insert_data_coin_gem(token_address, "pf", mcap, None, None, None, None)
                                else:
                                    insert_data_coin_gem(token_address, "koth", mcap, None, None, None, None)
                            elif ray_params:
                                insert_data_coin_gem(token_address, "listray", mcap, None, None, None, None)
                        await forward_msg("https://pump.fun/"+str(token_address)+" "+result+"  SinyalvolumePump3 "+ray)
                        #await #await forward_check_x(str(token_address))(str(token_address))
                    if sent == False and len(data) >= 5 and data[-1]['volume'] > 15203042087 and data[-2]['volume'] > 7203042087 and data[-1]['close'] > data[-1]['open'] and  data[-2]['close'] > data[-2]['open']  and  data[-3]['close'] > data[-3]['open'] and  data[-4]['close'] > data[-4]['open'] and  data[-5]['close'] > data[-5]['open'] :
                        print("SinyalvolumePump4 ")
                        sent = True
                        token_volume[token_address] = current_time
                        if not find_coin_gem_by_ca_id_and_platform(token_address, "pf"):
                            if viral_param:
                                if ray_params:
                                    #await forward_alert(formatted_message)
                                    insert_data_coin_gem(token_address, "pf", mcap, None, None, None, None)
                                else:
                                    insert_data_coin_gem(token_address, "koth", mcap, None, None, None, None)
                            elif ray_params:
                                insert_data_coin_gem(token_address, "listray", mcap, None, None, None, None)
                        await forward_msg("https://pump.fun/"+str(token_address)+" "+result+"  SinyalvolumePump4 "+ray)
                        #await #await forward_check_x(str(token_address))(str(token_address))
                    if sent == False and len(data) >= 14:  # Perlu setidaknya 14 data (10 untuk sideways + 4 untuk spike)
                        # Mengambil harga penutupan (close) dan volume
                        closes = [item['close'] for item in data]
                        volumes = [item['volume'] for item in data]

                        # Analisis kondisi sideways pada 10 data terakhir tanpa 4 data paling akhir
                        sideways_detected = is_sideways(closes[-10:-4])  # Cek kondisi sideways pada data ke-5 sampai ke-14 dari belakang

                        if sideways_detected:
                            print("Kondisi sideways terdeteksi.")
                            avg_volume = statistics.mean(volumes[-10:-4])
                            # Deteksi spike volume pada 4 data paling akhir
                            if detect_spike(data[-4:], avg_volume, spike_threshold=3):  # Cek spike pada 4 data paling akhir
                                print("Spike volume terdeteksi pada 4 data paling akhir.")
                                sent = True
                                token_volume[token_address] = current_time
                                if not find_coin_gem_by_ca_id_and_platform(token_address, "pf"):
                                    if viral_param:
                                        if ray_params:
                                            #await forward_alert(formatted_message)
                                            insert_data_coin_gem(token_address, "pf", mcap, None, None, None, None)
                                        else:
                                            insert_data_coin_gem(token_address, "koth", mcap, None, None, None, None)
                                    elif ray_params:
                                        insert_data_coin_gem(token_address, "listray", mcap, None, None, None, None)
                                await forward_msg("https://pump.fun/"+str(token_address)+" "+result+"  Sinyalspike1 "+ray)
                                #await #await forward_check_x(str(token_address))(str(token_address))
                            else:
                                print("Tidak ada spike volume pada 4 data paling akhir.")
                        else:
                            print("Kondisi sideways tidak terdeteksi.")
                    if sent == False and len(data) >= 14 and ray_params:
                        if data[-1]['close'] > data[-2]['close'] and data[-2]['close'] > data[-3]['close'] and data[-1]['volume'] > 12203042087 and data[-2]['volume'] > 12203042087:
                            print("Spike volume terdeteksi pada 4 data paling akhir.")
                            await forward_msg("https://pump.fun/"+str(token_address)+" "+result+"  Sinyalspike2 "+ray)
                            sent = True
                            token_volume[token_address] = current_time
                            if not find_coin_gem_by_ca_id_and_platform(token_address, "pf"):
                                if viral_param:
                                    if ray_params:
                                        #await forward_alert(formatted_message)
                                        insert_data_coin_gem(token_address, "pf", mcap, None, None, None, None)
                            #await #await forward_check_x(str(token_address))(str(token_address))
                        else:
                            print("Tidak ada spike volume pada 4 data paling akhir.")
                    if sent == False and len(data) < 14 and len(data) > 2:  # Perlu setidaknya 14 data (10 untuk sideways + 4 untuk spike)
                        # Mengambil harga penutupan (close) dan volume
                        closes = [item['close'] for item in data]
                        volumes = [item['volume'] for item in data]

                        # Analisis kondisi sideways pada 10 data terakhir tanpa 4 data paling akhir
                        sideways_detected = is_sideways(closes[:-2])  # Cek kondisi sideways pada data ke-5 sampai ke-14 dari belakang

                        if sideways_detected:
                            print("Kondisi sideways terdeteksi.")
                            avg_volume = statistics.mean(volumes[:-2])
                            # Deteksi spike volume pada 4 data paling akhir
                            if detect_spike(data[-2:], avg_volume, spike_threshold=3):  # Cek spike pada 4 data paling akhir
                                print("Spike volume terdeteksi pada 4 data paling akhir.")
                                await forward_msg("https://pump.fun/"+str(token_address)+" "+result+"  Sinyalspike2 "+ray)
                                sent = True
                                token_volume[token_address] = current_time
                                if viral_param:
                                    if not find_coin_gem_by_ca_id_and_platform(token_address, "pf"):
                                        if ray_params:
                                            #await forward_alert(formatted_message)
                                            insert_data_coin_gem(token_address, "pf", mcap, None, None, None, None)
                                #await #await forward_check_x(str(token_address))(str(token_address))
                            else:
                                print("Tidak ada spike volume pada 4 data paling akhir.")
                        else:
                            print("Kondisi sideways tidak terdeteksi.")
                    else:
                        # Mengecek jika volume terbanyak bukan pada array paling awal
                        max_volume = max(data, key=lambda x: x['volume'])
                        if max_volume != data[0]:
                            print("Volume terbanyak bukan pada array paling awal.")
                            # Mengecek jika array paling akhir memiliki close lebih besar dari nilai close array sebelumnya
                            if data[-1]['close'] > data[-2]['close']:
                                token_volume[token_address] = current_time
                                print("Array paling akhir memiliki nilai close lebih besar dari nilai close array sebelumnya.")
                                await forward_trend("https://pump.fun/"+str(token_address)+"  SinyalvolumePump")
                                sent = True
                            else:
                                print("Array paling akhir tidak memiliki nilai close lebih besar dari nilai close array sebelumnya.")
                        else:
                            print("Volume gagal")
            else:
                print(f"Permintaan gagal dengan status kode {response.status_code}")

            if ray_params:
                result = extract_part_of_url_from_string(event.message.text)
                if result is not None:
                    result = re.sub(r"\).*$", "", result)
                    insert_data_coin_gem(token_address, "movray", mcap, None , result.lower() , None, None)
                else:
                    result = ""
                if not find_coin_gem_by_ca_id_and_platform(token_address, "pf"):
                    found_tokens = [token for token in viral_store if (token in result and token != "solana" and len(token)>1)]
                    if found_tokens:
                        #await forward_alert(formatted_message)
                        insert_data_coin_gem(token_address, "pf", mcap, None , result.lower() , None, None)
            
            if ray_params:
                token_to_delete = []
                for token_address, waktu_simpan in token_temps.items():
                    selisih_waktu = datetime.now() - waktu_simpan
                    if selisih_waktu > timedelta(minutes=30):
                        token_to_delete.append(token_address)
                for token_address in token_to_delete:
                    del token_temps[token_address]
    
                url_coin = f'https://frontend-api.pump.fun/coins/{token_address}'
                headers_coin = {
                    'accept-language': 'en-US,en;q=0.9,id;q=0.8,ms;q=0.7',
                    'origin': 'https://pump.fun',
                    'referer': 'https://pump.fun/'
                }
                coin_data = await fetch_data_coin(url_coin, headers_coin)
                
                if 'error' in coin_data:
                    print(coin_data['error'])
                    return

                creator = coin_data.get('creator', None)
                symbol = coin_data.get('symbol', None)
                king_of_the_hill_timestamp = coin_data.get('king_of_the_hill_timestamp', None)
                twitter = coin_data.get('twitter', None)
                telegram = coin_data.get('telegram', None)
                website = coin_data.get('website', None)
                created_timestamp = coin_data.get('created_timestamp', None)
                
                if created_timestamp and king_of_the_hill_timestamp:
                    delta_minutes = calculate_delta_minutes(created_timestamp, king_of_the_hill_timestamp)
                else:
                    delta_minutes = None
                
                if (twitter and "cto" in twitter.lower()) or (telegram and "cto" in telegram.lower()) and delta_minutes and delta_minutes < 4:
                    await forward_msg("https://pump.fun/"+str(token_address) +"  HIGH CONVICTION!!!!")
                
                result = {
                    'creator': creator,
                    'symbol': symbol,
                    'king_of_the_hill_timestamp': king_of_the_hill_timestamp,
                    'twitter': twitter,
                    'telegram': telegram,
                    'website': website,
                    'delta_minutes': delta_minutes,
                    'signal': False,
                    'time' : datetime.now()
                }
                print(result['delta_minutes'])
                if   result['delta_minutes'] and result['delta_minutes'] > 0:
                    url_balances = f'https://frontend-api.pump.fun/balances/{creator}?limit=50&offset=0'
                    headers_balances = {
                        'accept': '*/*',
                        'accept-language': 'en-US,en;q=0.9,id;q=0.8,ms;q=0.7',
                        'origin': 'https://pump.fun',
                        'referer': 'https://pump.fun/'
                    }
                    
                    balances_data = await fetch_data_coin(url_balances, headers_balances)
                    
                    if 'error' in balances_data:
                        print(balances_data['error'])
                        return
                    
                    # Cari nilai value dari symbol yang didapat dari endpoint pertama
                    value = None
                    for item in balances_data:
                        if item['symbol'] == symbol:
                            value = item['value']
                            break
                    result['value'] = value
                    #print(result) 
                    if value and int(value) < 500:
                        token_store_pump[token_address] = result
                print("String tidak sssssssssssssssssssssssssssssss kata 'asas'")
                current_time = datetime.now()  
                for token in list(token_store_pump.keys()):
                    if token_store_pump[token]['time']:
                        if current_time - token_store_pump[token]['time'] > timedelta(minutes=120):
                            del token_store_pump[token]
                    else:
                        del token_store_pump[token]'''

    except Exception as e:
        tb = traceback.format_exc()
        print("An error occurred:\n", tb)
        print(f"Error00: {e}")
# waktu di pumpfun ===================================================================================================================

'''
@client.on(events.NewMessage(chats=["@PumpFun15K"]))  # Ganti dengan nama grup Anda
async def handle_new_message(event):
    try:
        #print(event.message.text)
        pattern = r'Market cap\s*\n\s*`([A-Za-z0-9]+)`'
        match = re.search(pattern, event.message.text)
        if ("Market cap" in event.message.text) and match and not any(substring in  event.message.text for substring in banned) and not any(substring in  event.message.text for substring in banned_wallet):
            token_address = match.group(1)
            print(f"CA 15K: {token_address}")

            waktu_sekarang = datetime.now()
            all_data_tx =check_tx(token_address)
            response = check_price(token_address)
            #response_paid = check_token(token_address)
            token_temps[token_address] = waktu_sekarang

            name_link_regex = r'🪙 \[\*\*(.*?)\*\* \| \*\*(.*?)\]\((.*?)\)'
            created_at_regex = r'🕒 \*\*Created at\*\* : (.*?)\n'
            creator_regex = r'🎨 \*\*Creator\*\* : \[(.*?)\]\((.*?)\)'
            marketcap_regex = r'💰 \*\*Marketcap\*\* : \$ __(.*?)__'
            trades_regex = r'📊 \*\*Trades\*\* : __(.*?)__ txs \| ⬆️ __(.*?)__ ⬇️ __(.*?)__'
            replies_regex = r'💬 \*\*Replies\*\* : __(.*?)__'
            king_regex = r'👑 \*\*KING\*\* : __(.*?)__'
            top10_holders_regex = r'🏦 \*\*HOLDERS\*\* » \*\*TOP 10\*\* : `(.*?)%`'
            holder_details_regex = r'├ \[(.*?)\]\((.*?)\) » `(.*?)%`'
            website_regex = r'🌐 \*\*Website\*\* : __(.*?)__'
            twitter_regex = r'🐦 \*\*Twitter\*\* : \[(.*?)\]\((.*?)\)'
            telegram_regex = r'📱 \*\*Telegram\*\* : __(.*?)__'
            pump_fun_regex = r'💊 \*\*Pump Fun\*\* : \[\*\*(.*?)\*\* \| \*\*(.*?)\]\((.*?)\)'

            # Menggunakan regex untuk ekstrak nilai
            name_match = re.search(name_link_regex, event.message.text)
            created_at_match = re.search(created_at_regex, event.message.text)
            creator_match = re.search(creator_regex, event.message.text)
            marketcap_match = re.search(marketcap_regex, event.message.text)
            trades_match = re.search(trades_regex, event.message.text)
            replies_match = re.search(replies_regex, event.message.text)
            king_match = re.search(king_regex, event.message.text)
            top10_holders_match = re.search(top10_holders_regex, event.message.text)
            holders_match = re.findall(holder_details_regex, event.message.text)
            website_match = re.search(website_regex, event.message.text)
            twitter_match = re.search(twitter_regex, event.message.text)
            telegram_match = re.search(telegram_regex, event.message.text)
            pump_fun_match = re.search(pump_fun_regex, event.message.text)

            # Membentuk ulang pesan dengan hasil ekstraksi
            formatted_message = f"""
💊 💎 <b>{name_match.group(1)}</b> #{name_match.group(1)} [<a href="https://pump.fun/{token_address}">pumpfun</a>] 

<code>{token_address}</code>
🪙 <b><a href="{name_match.group(3)}">{name_match.group(1)} | {name_match.group(2)}</a></b>
├ 🕒 <b>Created at</b> : {created_at_match.group(1)}
├ 🎨 <b>Creator</b> : <a href="{creator_match.group(2)}">{creator_match.group(1)}</a>
├ 💰 <b>Marketcap</b> : $ {marketcap_match.group(1)}
└ 💬 <b>Replies</b> : {replies_match.group(1)}

🏦 <b>HOLDERS</b> » <b>TOP 10</b> : <code>{top10_holders_match.group(1)}%</code>
            """
            formatted_message += f"""
🛒 <b><a href="https://bullx.io/terminal?chainId=1399811149&address={token_address}">Buy {name_match.group(1)}</a></b> 💸
🔗 <b><a href="https://t.me/helenus_trojanbot?startr-doremifas493385-{token_address}">Trojan</a></b>
            """
               
            if all_data_tx and response and response.status_code == 200:

                print("token adres PF "+token_address)
                paid = False
                # Panjang array utama
                array_length = len(all_data_tx)
    
                # Menghitung jumlah buy dan sell
                total_buy = sum(1 for trade in all_data_tx if trade['is_buy'])
                total_sell = sum(1 for trade in all_data_tx if not trade['is_buy'])
                
                # Menghitung jumlah buy dan sell dengan sol_amount lebih dari 1.000.000.000
                high_value_buy = sum(1 for trade in all_data_tx if trade['is_buy'] and trade['sol_amount'] > 1_000_000_000)
                high_value_sell = sum(1 for trade in all_data_tx if not trade['is_buy'] and trade['sol_amount'] > 1_000_000_000)
                
                # Menghitung jumlah buy dengan sol_amount lebih dari 5.000.000.000
                high_value_buy_5b = sum(1 for trade in all_data_tx if trade['is_buy'] and trade['sol_amount'] > 5_000_000_000)
                
                # Menghitung jumlah data dengan timestamp yang sama
                timestamps = [trade['timestamp'] for trade in all_data_tx]
                timestamp_counts = Counter(timestamps)
                duplicate_timestamps = {timestamp for timestamp, count in timestamp_counts.items() if count > 1}
                filtered_users = [trade for trade in all_data_tx if trade['is_buy'] and trade['sol_amount'] >= 500000000 and trade['timestamp'] in duplicate_timestamps]
                
                # Mendapatkan sol_amount tertinggi ketika is_buy
                max_sol_amount_buy = max((trade['sol_amount'] for trade in all_data_tx if trade['is_buy']), default=None)
                
                # Menghitung total sol_amount untuk setiap user yang is_buy = true
                user_sol_amounts = defaultdict(int)
                user_timestamps = defaultdict(list)
                user_transactions = defaultdict(list)
                for trade in all_data_tx:
                    if trade['is_buy']:
                        user_sol_amounts[trade['user']] += trade['sol_amount']
                        user_timestamps[trade['user']].append(trade['timestamp'])
                        user_transactions[trade['user']].append(trade['sol_amount'])
                
                # Mengambil 5 user dengan sol_amount tertinggi
                top_users = sorted(user_sol_amounts.items(), key=lambda x: x[1], reverse=True)[:5]

                # Memeriksa kesamaan timestamp antara top 5 users
                timestamp_matches = defaultdict(set)
                for user, _ in top_users:
                    timestamps = user_timestamps[user]
                    for timestamp in timestamps:
                        for other_user, _ in top_users:
                            if other_user != user and timestamp in user_timestamps[other_user]:
                                timestamp_matches[user].add(timestamp)
                                timestamp_matches[other_user].add(timestamp)

                    # Menentukan apakah ada user yang memiliki kesamaan timestamp lebih dari sekali
                has_multiple_matches = {user: len(matches) > 1 for user, matches in timestamp_matches.items()}

                # Memeriksa kesamaan timestamp antara top 5 users
                timestamp_matches = defaultdict(set)
                for user, _ in top_users:
                    timestamps = user_timestamps[user]
                    for timestamp in timestamps:
                        for other_user, _ in top_users:
                            if other_user != user and timestamp in user_timestamps[other_user]:
                                timestamp_matches[user].add(timestamp)
                                timestamp_matches[other_user].add(timestamp)
                
                # Mencari user dengan signature yang sama di filtered_users
                signature_counts = defaultdict(int)
                sol_amounts_per_signature = defaultdict(int)
                
                for trade in filtered_users:
                    signature = trade['signature']
                    signature_counts[signature] += 1
                    sol_amounts_per_signature[signature] += trade['sol_amount']
                
                # Mengambil jumlah user dengan signature yang sama dan total sol_amount
                same_signature_users = [(signature, count, sol_amount) for signature, count, sol_amount in zip(signature_counts.keys(), signature_counts.values(), sol_amounts_per_signature.values()) if count > 1]

                # Menghitung total sol_amount dari grup user yang memiliki kesamaan signature dengan minimal 2 atau lebih
                total_sol_amount_grouped = sum(sol_amount for _, _, sol_amount in same_signature_users)

                user_token_amounts = defaultdict(int)
                for trade in all_data_tx:
                    if trade['is_buy']:
                        user_token_amounts[trade['user']] += trade['token_amount']
                    else:
                        user_token_amounts[trade['user']] -= trade['token_amount']
                
                # Mengambil 5 user dengan token_amount tertinggi
                top_token_holders = sorted(user_token_amounts.items(), key=lambda x: x[1], reverse=True)[:5]

                if "**Tool**" in event.message.text:
                    text_temp= event.message.text.split("**Tool**")[0]
                else:
                    text_temp= event.message.text.split("**AD**")[0]
                # Hasil yang akan ditampilkan
                result = (
                    f": {text_temp}\n"
                    f"Panjang array utama: {array_length}\n"
                    f"Jumlah total buy: {total_buy}\n"
                    f"Jumlah data dengan timestamp yang sama: {len(duplicate_timestamps)}\n"
                    f"sol_amount tertinggi ketika is_buy: {max_sol_amount_buy / 1_000_000_000:.2f} SOL\n"
                    f"Total sol_amount untuk 5 users tertinggi dengan is_buy=True:\n"
                )
                
                top_user_flag = True
                count_i = 1
                for user, total_sol in top_users:
                    count_x=1
                    total_sol_billion = total_sol / 1_000_000_000
                    if total_sol_billion > 15:
                        top_user_flag = False
                    result += f"{count_i}: {user}\n"
                    result += f"   Total: {total_sol_billion:.2f} SOL\n"
                    for sol_amount in user_transactions[user]:
                        result += f"  {count_x}: {sol_amount / 1_000_000_000:.2f}  SOL\n"
                        count_x +=1
                    count_i+=1
                     

                        
                
                result += "Jumlah user dengan signature yang sama dan total sol_amount:\n"
                for signature, count, total_sol in same_signature_users:
                    total_sol_billion = total_sol / 1_000_000_000
                    result += f"Jumlah user: {count}, Total sol_amount: {total_sol_billion:.2f} SOL\n"
                    if count > 1:
                        top_user_flag = False


                                                    # Menambahkan hasil pemeriksaan kesamaan timestamp
                result += "\nKesamaan timestamp antara top 5 users:\n"
                for user, has_match in has_multiple_matches.items():
                    if has_match:
                        result += f"{user}: {has_match}\n"
                        top_user_flag = False

                result += "\nTop 5 token holders:\n"
                for user, total_token in top_token_holders:
                    nilai_2 = 1000000000000000
                    # Menghitung persentase
                    persentase = (total_token / nilai_2) * 100
                    if user in banned_wallet or persentase > 12:
                        top_user_flag = False

                sent = False
                ray= "15K"

                current_time = datetime.now()
                viral_param = False
                text_messages =event.message.text
                found_tokens = [token for token in viral_store if (token in text_messages.lower() and token != "solana" and len(token)>1)]
                if found_tokens:
                    viral_param = True

                if total_sol_amount_grouped / 1_000_000_000 < 1 and max_sol_amount_buy / 1_000_000_000 < 15 and top_user_flag:
                    data = response.json()

                    text_messages =event.message.text
                    
                    if found_tokens:
                        if not find_coin_gem_by_ca_id_and_platform(token_address, "pf"):
                            #await forward_alert(formatted_message)
                            insert_data_coin_gem(token_address, "15k", marketcap_match.group(1), None, None, None, None)
                    if sent == False and paid:
                        print("Datsinyall paid 1")
                        print(paid)
                        sent = True
                        token_volume[token_address] = current_time
                        if viral_param:
                            if not find_coin_gem_by_ca_id_and_platform(token_address, "pf"):
                                if not find_coin_gem_by_ca_id_and_platform(token_address, "tgroup"):
                                    insert_data_coin_gem(token_address, "15k", marketcap_match.group(1), None, None, None, None)
                                else:
                                    #await forward_alert(formatted_message)
                                    insert_data_coin_gem(token_address, "15k", marketcap_match.group(1), None, None, None, None)
                            await forward_trend("https://pump.fun/"+str(token_address)+" "+result+"  Viral Param PF "+ray)
                        #await #await forward_check_x(str(token_address))(str(token_address))
                    if sent == False and len(data) == 2 and data[0]['volume'] > 50203042087 and data[1]['volume'] > 50203042087 and  data[0]['close'] > data[0]['open'] and  data[1]['close'] > data[1]['open']:
                        print("Datsinyall 1")
                        sent = True
                        token_volume[token_address] = current_time
                        if not find_coin_gem_by_ca_id_and_platform(token_address, "pf"):
                            if not find_coin_gem_by_ca_id_and_platform(token_address, "tgroup"):
                                insert_data_coin_gem(token_address, "15k", marketcap_match.group(1), None, None, None, None)
                            else:
                                #await forward_alert(formatted_message)
                                insert_data_coin_gem(token_address, "15k", marketcap_match.group(1), None, None, None, None)
                        await forward_trend("https://pump.fun/"+str(token_address)+" "+result+"  SinyalvolumePump1 "+ray)
                        #await #await forward_check_x(str(token_address))(str(token_address))
                    if  sent == False and len(data) > 3 and data[-1]['volume'] > 20203042087 and data[-1]['close'] > data[-1]['open'] and data[-2]['close'] > data[-2]['open'] and data[-3]['close'] > data[-3]['open']:
                        print("Datsinyall 2")
                        sent = True
                        token_volume[token_address] = current_time
                        if not find_coin_gem_by_ca_id_and_platform(token_address, "pf"):
                            if not find_coin_gem_by_ca_id_and_platform(token_address, "tgroup"):
                                insert_data_coin_gem(token_address, "15k", marketcap_match.group(1), None, None, None, None)
                            else:
                                #await forward_alert(formatted_message)
                                insert_data_coin_gem(token_address, "15k", marketcap_match.group(1), None, None, None, None)
                        await forward_trend("https://pump.fun/"+str(token_address)+" "+result+"  SinyalvolumePump2 "+ray)
                        #await #await forward_check_x(str(token_address))(str(token_address))
                    if sent == False and len(data) <= 4 and len(data) > 2 and  data[0]['volume'] > 10203042087 and data[1]['volume'] > 12203042087 and data[2]['volume'] > 14203042087 :
                        print("Datsinyall 3")
                        sent = True
                        token_volume[token_address] = current_time
                        if not find_coin_gem_by_ca_id_and_platform(token_address, "pf"):
                            if not find_coin_gem_by_ca_id_and_platform(token_address, "tgroup"):
                                insert_data_coin_gem(token_address, "15k", marketcap_match.group(1), None, None, None, None)
                            else:
                                #await forward_alert(formatted_message)
                                insert_data_coin_gem(token_address, "15k", marketcap_match.group(1), None, None, None, None)
                        await forward_trend("https://pump.fun/"+str(token_address)+" "+result+"  SinyalvolumePump3 "+ray)
                        #await #await forward_check_x(str(token_address))(str(token_address))
                    if sent == False and len(data) >= 5 and data[-1]['volume'] > 15203042087 and data[-2]['volume'] > 7203042087 and data[-1]['close'] > data[-1]['open'] and  data[-2]['close'] > data[-2]['open']  and  data[-3]['close'] > data[-3]['open'] and  data[-4]['close'] > data[-4]['open'] and  data[-5]['close'] > data[-5]['open'] :
                        print("SinyalvolumePump4 ")
                        sent = True
                        token_volume[token_address] = current_time
                        if not find_coin_gem_by_ca_id_and_platform(token_address, "pf"):
                            if not find_coin_gem_by_ca_id_and_platform(token_address, "tgroup"):
                                insert_data_coin_gem(token_address, "15k", marketcap_match.group(1), None, None, None, None)
                            else:
                                #await forward_alert(formatted_message)
                                insert_data_coin_gem(token_address, "15k", marketcap_match.group(1), None, None, None, None)
                        await forward_trend("https://pump.fun/"+str(token_address)+" "+result+"  SinyalvolumePump4 "+ray)
                        #await #await forward_check_x(str(token_address))(str(token_address))
                    if sent == False and len(data) >= 14:  # Perlu setidaknya 14 data (10 untuk sideways + 4 untuk spike)
                        # Mengambil harga penutupan (close) dan volume
                        closes = [item['close'] for item in data]
                        volumes = [item['volume'] for item in data]

                        # Analisis kondisi sideways pada 10 data terakhir tanpa 4 data paling akhir
                        sideways_detected = is_sideways(closes[-10:-4])  # Cek kondisi sideways pada data ke-5 sampai ke-14 dari belakang

                        if sideways_detected:
                            print("Kondisi sideways terdeteksi.")
                            avg_volume = statistics.mean(volumes[-10:-4])
                            # Deteksi spike volume pada 4 data paling akhir
                            if detect_spike(data[-4:], avg_volume, spike_threshold=3):  # Cek spike pada 4 data paling akhir
                                print("Spike volume terdeteksi pada 4 data paling akhir.")
                                sent = True
                                token_volume[token_address] = current_time
                                if not find_coin_gem_by_ca_id_and_platform(token_address, "pf"):
                                    if not find_coin_gem_by_ca_id_and_platform(token_address, "tgroup"):
                                        insert_data_coin_gem(token_address, "15k", marketcap_match.group(1), None, None, None, None)
                                    else:
                                        #await forward_alert(formatted_message)
                                        insert_data_coin_gem(token_address, "15k", marketcap_match.group(1), None, None, None, None)
                                await forward_trend("https://pump.fun/"+str(token_address)+" "+result+"  Sinyalspike1 "+ray)
                                #await #await forward_check_x(str(token_address))(str(token_address))
                            else:
                                print("Tidak ada spike volume pada 4 data paling akhir.")
                        else:
                            print("Kondisi sideways tidak terdeteksi.")
                    if sent == False and len(data) < 14 and len(data) > 2:  # Perlu setidaknya 14 data (10 untuk sideways + 4 untuk spike)
                        # Mengambil harga penutupan (close) dan volume
                        closes = [item['close'] for item in data]
                        volumes = [item['volume'] for item in data]

                        # Analisis kondisi sideways pada 10 data terakhir tanpa 4 data paling akhir
                        sideways_detected = is_sideways(closes[:-2])  # Cek kondisi sideways pada data ke-5 sampai ke-14 dari belakang

                        if sideways_detected:
                            print("Kondisi sideways terdeteksi.")
                            avg_volume = statistics.mean(volumes[:-2])
                            # Deteksi spike volume pada 4 data paling akhir
                            if detect_spike(data[-2:], avg_volume, spike_threshold=3):  # Cek spike pada 4 data paling akhir
                                print("Spike volume terdeteksi pada 4 data paling akhir.")
                                await forward_trend("https://pump.fun/"+str(token_address)+" "+result+"  Sinyalspike2 "+ray)
                                sent = True
                            else:
                                print("Tidak ada spike volume pada 4 data paling akhir.")
                        else:
                            print("Kondisi sideways tidak terdeteksi.")
            else:
                print(f"Permintaan gagal dengan status kode {response.status_code}")
            
    except Exception as e:
        tb = traceback.format_exc()
        print("An error occurred:\n", tb)
        print(f"Error00: {e}")'''
# waktu di pumpfun ===================================================================================================================


'''@client.on(events.NewMessage(chats=["@PumpFun30K"]))  # Ganti dengan nama grup Anda
async def handle_new_message(event):
    try:
        #print(event.message.text)
        pattern = r'Market cap\s*\n\s*`([A-Za-z0-9]+)`'
        match = re.search(pattern, event.message.text)
        if ("Market cap" in event.message.text) and match and not any(substring in  event.message.text for substring in banned) and not any(substring in  event.message.text for substring in banned_wallet):
            token_address = match.group(1)
            print(f"CA 35K: {token_address}")

            waktu_sekarang = datetime.now()
            all_data_tx =check_tx(token_address)
            response = check_price(token_address)
            #response_paid = check_token(token_address)
            token_temps[token_address] = waktu_sekarang


            name_link_regex = r'🪙 \[\*\*(.*?)\*\* \| \*\*(.*?)\]\((.*?)\)'
            created_at_regex = r'🕒 \*\*Created at\*\* : (.*?)\n'
            creator_regex = r'🎨 \*\*Creator\*\* : \[(.*?)\]\((.*?)\)'
            marketcap_regex = r'💰 \*\*Marketcap\*\* : \$ __(.*?)__'
            trades_regex = r'📊 \*\*Trades\*\* : __(.*?)__ txs \| ⬆️ __(.*?)__ ⬇️ __(.*?)__'
            replies_regex = r'💬 \*\*Replies\*\* : __(.*?)__'
            king_regex = r'👑 \*\*KING\*\* : __(.*?)__'
            top10_holders_regex = r'🏦 \*\*HOLDERS\*\* » \*\*TOP 10\*\* : `(.*?)%`'
            holder_details_regex = r'├ \[(.*?)\]\((.*?)\) » `(.*?)%`'
            website_regex = r'🌐 \*\*Website\*\* : __(.*?)__'
            twitter_regex = r'🐦 \*\*Twitter\*\* : \[(.*?)\]\((.*?)\)'
            telegram_regex = r'📱 \*\*Telegram\*\* : __(.*?)__'
            pump_fun_regex = r'💊 \*\*Pump Fun\*\* : \[\*\*(.*?)\*\* \| \*\*(.*?)\]\((.*?)\)'

            # Menggunakan regex untuk ekstrak nilai
            name_match = re.search(name_link_regex, event.message.text)
            created_at_match = re.search(created_at_regex, event.message.text)
            creator_match = re.search(creator_regex, event.message.text)
            marketcap_match = re.search(marketcap_regex, event.message.text)
            trades_match = re.search(trades_regex, event.message.text)
            replies_match = re.search(replies_regex, event.message.text)
            king_match = re.search(king_regex, event.message.text)
            top10_holders_match = re.search(top10_holders_regex, event.message.text)
            holders_match = re.findall(holder_details_regex, event.message.text)
            website_match = re.search(website_regex, event.message.text)
            twitter_match = re.search(twitter_regex, event.message.text)
            telegram_match = re.search(telegram_regex, event.message.text)
            pump_fun_match = re.search(pump_fun_regex, event.message.text)

            # Membentuk ulang pesan dengan hasil ekstraksi
            formatted_message = f"""
💊 💎 <b>{name_match.group(1)}</b> #{name_match.group(1)} [<a href="https://pump.fun/{token_address}">pumpfun</a>] 

<code>{token_address}</code>
🪙 <b><a href="{name_match.group(3)}">{name_match.group(1)} | {name_match.group(2)}</a></b>
├ 🕒 <b>Created at</b> : {created_at_match.group(1)}
├ 🎨 <b>Creator</b> : <a href="{creator_match.group(2)}">{creator_match.group(1)}</a>
├ 💰 <b>Marketcap</b> : $ {marketcap_match.group(1)}
└ 💬 <b>Replies</b> : {replies_match.group(1)}

🏦 <b>HOLDERS</b> » <b>TOP 10</b> : <code>{top10_holders_match.group(1)}%</code>
            """
            formatted_message += f"""
🛒 <b><a href="https://bullx.io/terminal?chainId=1399811149&address={token_address}">Buy {name_match.group(1)}</a></b> 💸
🔗 <b><a href="https://t.me/helenus_trojanbot?startr-doremifas493385-{token_address}">Trojan</a></b>
            """

            if all_data_tx and response  and response.status_code == 200:

                #data_paid = response_paid.json()
                #print(data_paid)
                #paid = data_paid.get('paid', 'Unknown')
                print("token adres PF "+token_address)
                paid = False
                # Panjang array utama
                array_length = len(all_data_tx)
    
                # Menghitung jumlah buy dan sell
                total_buy = sum(1 for trade in all_data_tx if trade['is_buy'])
                total_sell = sum(1 for trade in all_data_tx if not trade['is_buy'])
                
                # Menghitung jumlah buy dan sell dengan sol_amount lebih dari 1.000.000.000
                high_value_buy = sum(1 for trade in all_data_tx if trade['is_buy'] and trade['sol_amount'] > 1_000_000_000)
                high_value_sell = sum(1 for trade in all_data_tx if not trade['is_buy'] and trade['sol_amount'] > 1_000_000_000)
                
                # Menghitung jumlah buy dengan sol_amount lebih dari 5.000.000.000
                high_value_buy_5b = sum(1 for trade in all_data_tx if trade['is_buy'] and trade['sol_amount'] > 5_000_000_000)
                
                # Menghitung jumlah data dengan timestamp yang sama
                timestamps = [trade['timestamp'] for trade in all_data_tx]
                timestamp_counts = Counter(timestamps)
                duplicate_timestamps = {timestamp for timestamp, count in timestamp_counts.items() if count > 1}
                filtered_users = [trade for trade in all_data_tx if trade['is_buy'] and trade['sol_amount'] >= 500000000 and trade['timestamp'] in duplicate_timestamps]
                
                # Mendapatkan sol_amount tertinggi ketika is_buy
                max_sol_amount_buy = max((trade['sol_amount'] for trade in all_data_tx if trade['is_buy']), default=None)
                
                # Menghitung total sol_amount untuk setiap user yang is_buy = true
                user_sol_amounts = defaultdict(int)
                user_timestamps = defaultdict(list)
                user_transactions = defaultdict(list)
                for trade in all_data_tx:
                    if trade['is_buy']:
                        user_sol_amounts[trade['user']] += trade['sol_amount']
                        user_timestamps[trade['user']].append(trade['timestamp'])
                        user_transactions[trade['user']].append(trade['sol_amount'])
                
                # Mengambil 5 user dengan sol_amount tertinggi
                top_users = sorted(user_sol_amounts.items(), key=lambda x: x[1], reverse=True)[:5]

                # Memeriksa kesamaan timestamp antara top 5 users
                timestamp_matches = defaultdict(set)
                for user, _ in top_users:
                    timestamps = user_timestamps[user]
                    for timestamp in timestamps:
                        for other_user, _ in top_users:
                            if other_user != user and timestamp in user_timestamps[other_user]:
                                timestamp_matches[user].add(timestamp)
                                timestamp_matches[other_user].add(timestamp)

                    # Menentukan apakah ada user yang memiliki kesamaan timestamp lebih dari sekali
                has_multiple_matches = {user: len(matches) > 1 for user, matches in timestamp_matches.items()}
                
                # Mencari user dengan signature yang sama di filtered_users
                signature_counts = defaultdict(int)
                sol_amounts_per_signature = defaultdict(int)
                
                for trade in filtered_users:
                    signature = trade['signature']
                    signature_counts[signature] += 1
                    sol_amounts_per_signature[signature] += trade['sol_amount']
                
                # Mengambil jumlah user dengan signature yang sama dan total sol_amount
                same_signature_users = [(signature, count, sol_amount) for signature, count, sol_amount in zip(signature_counts.keys(), signature_counts.values(), sol_amounts_per_signature.values()) if count > 1]

                # Menghitung total sol_amount dari grup user yang memiliki kesamaan signature dengan minimal 2 atau lebih
                total_sol_amount_grouped = sum(sol_amount for _, _, sol_amount in same_signature_users)

                user_token_amounts = defaultdict(int)
                for trade in all_data_tx:
                    if trade['is_buy']:
                        user_token_amounts[trade['user']] += trade['token_amount']
                    else:
                        user_token_amounts[trade['user']] -= trade['token_amount']
                
                # Mengambil 5 user dengan token_amount tertinggi
                top_token_holders = sorted(user_token_amounts.items(), key=lambda x: x[1], reverse=True)[:5]

                if "**Tool**" in event.message.text:
                    text_temp= event.message.text.split("**Tool**")[0]
                else:
                    text_temp= event.message.text.split("**AD**")[0]
                # Hasil yang akan ditampilkan
                result = (
                    f"https://bullx.io/terminal?chainId=1399811149&address={token_address}\n"
                    f": {text_temp}\n"
                    f"Panjang array utama: {array_length}\n"
                    f"Jumlah total buy: {total_buy}\n"
                    f"Jumlah data dengan timestamp yang sama: {len(duplicate_timestamps)}\n"
                    f"sol_amount tertinggi ketika is_buy: {max_sol_amount_buy / 1_000_000_000:.2f} SOL\n"
                    f"Total sol_amount untuk 5 users tertinggi dengan is_buy=True:\n"
                )
                
                top_user_flag = True
                count_i = 1
                for user, total_sol in top_users:
                    count_x=1
                    total_sol_billion = total_sol / 1_000_000_000
                    if total_sol_billion > 15:
                        top_user_flag = False
                    result += f"{count_i}: {user}\n"
                    result += f"   Total: {total_sol_billion:.2f} SOL\n"
                    for sol_amount in user_transactions[user]:
                        result += f"  {count_x}: {sol_amount / 1_000_000_000:.2f}  SOL\n"
                        count_x +=1
                    count_i+=1
                     
                    count_i+=1

                result += "Jumlah user dengan signature yang sama dan total sol_amount:\n"
                for signature, count, total_sol in same_signature_users:
                    total_sol_billion = total_sol / 1_000_000_000
                    result += f"Jumlah user: {count}, Total sol_amount: {total_sol_billion:.2f} SOL\n"
                    if count > 1:
                        top_user_flag = False
                

                                    # Menambahkan hasil pemeriksaan kesamaan timestamp
                result += "\nKesamaan timestamp antara top 5 users:\n"
                for user, has_match in has_multiple_matches.items():
                    if has_match:
                        result += f"{user}: {has_match}\n"
                        top_user_flag = False

                result += "\nTop 5 token holders:\n"
                for user, total_token in top_token_holders:
                    nilai_2 = 1000000000000000
                    # Menghitung persentase
                    persentase = (total_token / nilai_2) * 100
                    if user in banned_wallet or persentase > 12:
                        top_user_flag = False               

                sent = False
                ray= "30K "

                current_time = datetime.now()
                viral_param = False
                text_messages =event.message.text
                found_tokens = [token for token in viral_store if token in text_messages.lower()]
                if found_tokens:
                    viral_param = True

                if total_sol_amount_grouped / 1_000_000_000 < 1 and max_sol_amount_buy / 1_000_000_000 < 15 and top_user_flag:
                    data = response.json()
                    if sent == False and paid:
                        print("Datsinyall paid 1")
                        print(paid)
                        sent = True
                        token_volume[token_address] = current_time
                        if viral_param:
                            if not find_coin_gem_by_ca_id_and_platform(token_address, "pf"):
                                if not find_coin_gem_by_ca_id_and_platform(token_address, "tgroup"):
                                    insert_data_coin_gem(token_address, "30k", marketcap_match.group(1), None, None, None, None)
                                else:
                                    #await forward_alert
                                    insert_data_coin_gem(token_address, "30k", marketcap_match.group(1), None, None, None, None)
                            await forward_msg("https://pump.fun/"+str(token_address)+" "+result+"  Viral Param PF "+ray)
                        #await #await forward_check_x(str(token_address))(str(token_address))
                    if sent == False and len(data) == 2 and data[0]['volume'] > 40203042087 and data[1]['volume'] > 40203042087 and  data[0]['close'] > data[0]['open'] and  data[1]['close'] > data[1]['open']:
                        print("Datsinyall 1")
                        sent = True
                        token_volume[token_address] = current_time
                        if not find_coin_gem_by_ca_id_and_platform(token_address, "pf"):
                            if not find_coin_gem_by_ca_id_and_platform(token_address, "tgroup"):
                                insert_data_coin_gem(token_address, "30k", marketcap_match.group(1), None, None, None, None)
                            else:
                                #await forward_alert
                                insert_data_coin_gem(token_address, "30k", marketcap_match.group(1), None, None, None, None)
                        await forward_msg("https://pump.fun/"+str(token_address)+" "+result+"  SinyalvolumePump1 "+ray)
                        #await forward_check_x(str(token_address)) forward_check_x(str(token_address))(str(token_address))
                    if  sent == False and len(data) > 3 and data[-1]['volume'] > 20203042087 and data[-1]['close'] > data[-1]['open'] and data[-2]['close'] > data[-2]['open'] and data[-3]['close'] > data[-3]['open']:
                        print("Datsinyall 2")
                        sent = True
                        token_volume[token_address] = current_time
                        if not find_coin_gem_by_ca_id_and_platform(token_address, "pf"):
                            if not find_coin_gem_by_ca_id_and_platform(token_address, "tgroup"):
                                insert_data_coin_gem(token_address, "30k", marketcap_match.group(1), None, None, None, None)
                            else:
                                #await forward_alert
                                insert_data_coin_gem(token_address, "30k", marketcap_match.group(1), None, None, None, None)
                        await forward_msg("https://pump.fun/"+str(token_address)+" "+result+"  SinyalvolumePump2 "+ray)
                        #await forward_check_x(str(token_address)) forward_check_x(str(token_address))(str(token_address))
                    if sent == False and len(data) <= 4 and len(data) > 2 and  data[0]['volume'] > 10203042087 and data[1]['volume'] > 12203042087 and data[2]['volume'] > 14203042087 :
                        print("Datsinyall 3")
                        sent = True
                        token_volume[token_address] = current_time
                        if not find_coin_gem_by_ca_id_and_platform(token_address, "pf"):
                            if not find_coin_gem_by_ca_id_and_platform(token_address, "tgroup"):
                                insert_data_coin_gem(token_address, "30k", marketcap_match.group(1), None, None, None, None)
                            else:
                                #await forward_alert
                                insert_data_coin_gem(token_address, "30k", marketcap_match.group(1), None, None, None, None)
                        await forward_msg("https://pump.fun/"+str(token_address)+" "+result+"  SinyalvolumePump3 "+ray)
                        #await forward_check_x(str(token_address)) forward_check_x(str(token_address))(str(token_address))
                    if sent == False and len(data) >= 5 and data[-1]['volume'] > 15203042087 and data[-2]['volume'] > 7203042087 and data[-1]['close'] > data[-1]['open'] and  data[-2]['close'] > data[-2]['open']  and  data[-3]['close'] > data[-3]['open'] and  data[-4]['close'] > data[-4]['open'] and  data[-5]['close'] > data[-5]['open'] :
                        print("SinyalvolumePump4 ")
                        sent = True
                        token_volume[token_address] = current_time
                        if not find_coin_gem_by_ca_id_and_platform(token_address, "pf"):
                            if not find_coin_gem_by_ca_id_and_platform(token_address, "tgroup"):
                                insert_data_coin_gem(token_address, "30k", marketcap_match.group(1), None, None, None, None)
                            else:
                                #await forward_alert
                                insert_data_coin_gem(token_address, "30k", marketcap_match.group(1), None, None, None, None)
                        await forward_msg("https://pump.fun/"+str(token_address)+" "+result+"  SinyalvolumePump4 "+ray)
                        #await forward_check_x(str(token_address)) forward_check_x(str(token_address))(str(token_address))
                    if sent == False and len(data) >= 14:  # Perlu setidaknya 14 data (10 untuk sideways + 4 untuk spike)
                        # Mengambil harga penutupan (close) dan volume
                        closes = [item['close'] for item in data]
                        volumes = [item['volume'] for item in data]

                        # Analisis kondisi sideways pada 10 data terakhir tanpa 4 data paling akhir
                        sideways_detected = is_sideways(closes[-10:-4])  # Cek kondisi sideways pada data ke-5 sampai ke-14 dari belakang

                        if sideways_detected:
                            print("Kondisi sideways terdeteksi.")
                            avg_volume = statistics.mean(volumes[-10:-4])
                            # Deteksi spike volume pada 4 data paling akhir
                            if detect_spike(data[-4:], avg_volume, spike_threshold=3):  # Cek spike pada 4 data paling akhir
                                print("Spike volume terdeteksi pada 4 data paling akhir.")
                                sent = True
                                token_volume[token_address] = current_time
                                if not find_coin_gem_by_ca_id_and_platform(token_address, "pf"):
                                    if not find_coin_gem_by_ca_id_and_platform(token_address, "tgroup"):
                                        insert_data_coin_gem(token_address, "30k", marketcap_match.group(1), None, None, None, None)
                                    else:
                                        #await forward_alert
                                        insert_data_coin_gem(token_address, "30k", marketcap_match.group(1), None, None, None, None)
                                await forward_msg("https://pump.fun/"+str(token_address)+" "+result+"  Sinyalspike1 "+ray)
                                #await forward_check_x(str(token_address)) forward_check_x(str(token_address))(str(token_address))
                            else:
                                print("Tidak ada spike volume pada 4 data paling akhir.")
                        else:
                            print("Kondisi sideways tidak terdeteksi.")
                    if sent == False and len(data) < 14 and len(data) > 2:  # Perlu setidaknya 14 data (10 untuk sideways + 4 untuk spike)
                        # Mengambil harga penutupan (close) dan volume
                        closes = [item['close'] for item in data]
                        volumes = [item['volume'] for item in data]

                        # Analisis kondisi sideways pada 10 data terakhir tanpa 4 data paling akhir
                        sideways_detected = is_sideways(closes[:-2])  # Cek kondisi sideways pada data ke-5 sampai ke-14 dari belakang

                        if sideways_detected:
                            print("Kondisi sideways terdeteksi.")
                            avg_volume = statistics.mean(volumes[:-2])
                            # Deteksi spike volume pada 4 data paling akhir
                            if detect_spike(data[-2:], avg_volume, spike_threshold=3):  # Cek spike pada 4 data paling akhir
                                print("Spike volume terdeteksi pada 4 data paling akhir.")
                                await forward_msg("https://pump.fun/"+str(token_address)+" "+result+"  Sinyalspike2 "+ray)
                                sent = True
                                token_volume[token_address] = current_time
                                if viral_param:
                                    if not find_coin_gem_by_ca_id_and_platform(token_address, "pf"):
                                        if not find_coin_gem_by_ca_id_and_platform(token_address, "tgroup"):
                                            insert_data_coin_gem(token_address, "30k", marketcap_match.group(1), None, None, None, None)
                                        else:
                                            #await forward_alert
                                            insert_data_coin_gem(token_address, "30k", marketcap_match.group(1), None, None, None, None)
                                #await #await forward_check_x(str(token_address))(str(token_address))
                            else:
                                print("Tidak ada spike volume pada 4 data paling akhir.")
                        else:
                            print("Kondisi sideways tidak terdeteksi.")
            else:
                print(f"Permintaan gagal dengan status kode {response.status_code}")
            
    except Exception as e:
        tb = traceback.format_exc()
        print("An error occurred:\n", tb)
        print(f"Error00: {e}")
# waktu di pumpfun ==================================================================================================================='''


async def main():
    global entity1
    await client.start()
    chat_id = -2391890259
    entity1 = await client.get_entity(PeerChannel(chat_id))
    print("Client started")
    await asyncio.gather(
        chek_ten_minutes(),
        #get_volume(),
        #fetch_and_post_news(),
        client.run_until_disconnected()
    )


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())