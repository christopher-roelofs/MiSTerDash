import sqlite3

db_file = "openvgdb.sqlite"

def get_rom_by_hash(hash):
    db_connection = sqlite3.connect(db_file)
    cur = db_connection.cursor()
    cur.execute(f"SELECT * FROM ROMS WHERE romHashSHA1=?", (hash,))
    rows = cur.fetchall()
    db_connection.close()
    if len(rows) > 0:
        return rows[0]
    else:
        return ("","","","","","","","","","","","","","","")

def get_release_by_rom_id(id):
    db_connection = sqlite3.connect(db_file)
    cur = db_connection.cursor()
    cur.execute(f"SELECT * FROM RELEASES WHERE romID=? ", (id,))
    rows = cur.fetchall()
    db_connection.close()
    if len(rows) > 0:
        return rows[0]
    else:
        return ("","","","","","","","","","","","","","","","","","")

def get_rom_by_name_or_hash(name,hash):
    db_connection = sqlite3.connect(db_file)
    cur = db_connection.cursor()
    cur.execute(f"SELECT * FROM ROMS WHERE romHashSHA1=? OR romFileName like ?", (hash,'%'+name+'%',))
    rows = cur.fetchall()
    db_connection.close()
    if len(rows) > 0:
        return rows[0]
    else:
        return ("","","","","","","","","","","","","","","")



if __name__ == "__main__":
    #print(get_rom_by_hash("56FE858D1035DCE4B68520F457A0858BAE7BB16D"))
    print(get_release_by_rom_id("1"))