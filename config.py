import os
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox


username = os.getlogin()


def get_source_dir():
    global source_dir    source_dir = filedialog.askdirectory()
    source_entry.delete(0, tk.END)
    source_entry.insert(0, source_dir)


def get_backup_dir():
    global backup_dir    backup_dir = filedialog.askdirectory()
    backup_entry.delete(0, tk.END)
    backup_entry.insert(0, backup_dir)


def get_save():
    try:
        os.mkdir(f'C:\\Users\\{username}\\BACKUP')
    except FileExistsError:
        pass    finally:
        with open(f'C:\\Users\\{username}\\BACKUP\\config.txt', 'w',encoding='utf-8') as file:
            file.write(f'source_dir = {source_dir}\n')
            file.write(f'backup_dir = {backup_dir}\n')
            show_alert()


def show_alert():
    messagebox.showinfo("저장됨", "파일이 저장되었습니다.")


root = tk.Tk()
root.title("매일 매일 백업")
root.geometry("250x200")
root.resizable(False, False)

source_label = tk.Label(root, text="백업 대상 폴더 주소")
source_label.pack()
source_entry = tk.Entry(root, width=30)
source_entry.pack()

source_button = tk.Button(root, text="폴더 선택", command=get_source_dir)
source_button.pack()

backup_label = tk.Label(root, text="백업 되는 곳")
backup_label.pack()

backup_entry = tk.Entry(root, width=30)
backup_entry.pack()

backup_button = tk.Button(root, text="폴더 선택", command=get_backup_dir)
backup_button.pack()

tk.Label(root, text="").pack()

backup_button = tk.Button(root, text="설정 저장", command=get_save)
backup_button.pack()

root.mainloop()
