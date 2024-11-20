import sqlite3

conn = sqlite3.connect('youtube_videos.db')
cursor = conn.cursor()

cursor.execute(''' 
    CREATE TABLE IF NOT EXISTS videos(
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        time TEXT NOT NULL
    )
 ''')
def list_videos():
    cursor.execute("SELECT * FROM videos")
    for row in cursor.fetchall():
        print(row)

def add_videos(name,time):
    cursor.execute("INSERT INTO videos (name,time) VALUES (?,?)", (name,time))
    conn.commit()

def update_videos(video_ID,new_name,new_time):
    cursor.execute("UPDATE videos SET name = ?, time = ? WHERE id = ?", (new_name,new_time,video_ID))
    conn.commit()

    
def delete_videos(video_ID):
    cursor.execute("DELETE FROM videos WHERE id = ?", (video_ID,))
    conn.commit()

def main():
    while True:
        print("\n Youtube Manager app with DB")
        print("1.List videos")
        print("2.Add videos")
        print("3. Update videos")
        print("4. Delete videos")
        print("5. Exit the app")
        choice = input("Enter your choice: ")

        if choice == "1":
            list_videos()
            # Have to add a feature where if list is empty is should print an empty list
        elif choice == "2":
            name = input("Enter your video name: ")
            time = input("Enter your video time: ")
            add_videos(name,time)
        elif choice == "3":
            videos_ID = input("Enter your video ID: ")
            new_name = input("Enter your video name: ")
            new_time = input("Enter your video time: ")
            update_videos(videos_ID,new_name,new_time)
        elif choice == "4":
            videos_ID = input("Enter your video ID to delete: ")
            delete_videos(videos_ID)
        elif choice == "5":
            break
        else:
            print("Invalid Index")

    conn.close()
if __name__ == "__main__":
    main()