import streamlit as st
from pathlib import Path
import os
import shutil

st.set_page_config(page_title="CRUD File Manager", layout="centered")

st.title("📁 CRUD File Manager")

# ---------------- FUNCTIONS ---------------- #

def readfileandfolder():
    p = Path('')
    items = list(p.rglob('*'))
    return items


def create_file(file_name, content):
    p = Path(file_name)

    if p.exists():
        return "FILE ALREADY EXISTS!"

    with open(file_name, 'w') as file:
        file.write(content)

    return "FILE CREATED!"


def read_file(file_name):
    p = Path(file_name)

    if p.exists():
        with open(file_name, 'r') as file:
            return file.read()

    return "FILE NOT FOUND!"


def update_file(file_name, content, mode):
    p = Path(file_name)

    if p.exists():
        with open(file_name, mode) as file:
            file.write(content)

        return "FILE UPDATED!"

    return "FILE NOT FOUND!"


def delete_file(file_name):
    p = Path(file_name)

    if p.exists():
        os.remove(p)
        return "FILE DELETED!"

    return "FILE NOT FOUND!"


def rename_file(file_name, new_name):
    p = Path(file_name)

    if p.exists():
        p.rename(new_name)
        return "FILE RENAMED!"

    return "FILE NOT FOUND!"


def create_folder(folder_name):
    p = Path(folder_name)

    if p.exists():
        return "FOLDER ALREADY EXISTS!"

    p.mkdir()
    return "FOLDER CREATED!"


def delete_folder(folder_name):
    p = Path(folder_name)

    if p.exists():
        shutil.rmtree(folder_name)
        return "FOLDER DELETED!"

    return "FOLDER NOT FOUND!"


# ---------------- SIDEBAR ---------------- #

option = st.sidebar.selectbox(
    "Choose Operation",
    [
        "Create File",
        "Read File",
        "Update File",
        "Delete File",
        "Rename File",
        "Create Folder",
        "Delete Folder",
        "View Files/Folders"
    ]
)

# ---------------- UI ---------------- #

if option == "View Files/Folders":
    st.subheader("📂 Files & Folders")

    items = readfileandfolder()

    for item in items:
        st.write(item)

elif option == "Create File":
    st.subheader("📄 Create File")

    file_name = st.text_input("Enter File Name")
    content = st.text_area("Enter Content")

    if st.button("Create"):
        msg = create_file(file_name, content)
        st.success(msg)

elif option == "Read File":
    st.subheader("📖 Read File")

    file_name = st.text_input("Enter File Name")

    if st.button("Read"):
        content = read_file(file_name)
        st.text_area("Content", content, height=300)

elif option == "Update File":
    st.subheader("✏️ Update File")

    file_name = st.text_input("Enter File Name")

    mode = st.radio(
        "Select Update Mode",
        ["Overwrite", "Append"]
    )

    content = st.text_area("Enter Content")

    if st.button("Update"):

        file_mode = 'w' if mode == "Overwrite" else 'a'

        msg = update_file(file_name, content, file_mode)

        st.success(msg)

elif option == "Delete File":
    st.subheader("🗑️ Delete File")

    file_name = st.text_input("Enter File Name")

    if st.button("Delete"):
        msg = delete_file(file_name)
        st.success(msg)

elif option == "Rename File":
    st.subheader("🔄 Rename File")

    file_name = st.text_input("Current File Name")
    new_name = st.text_input("New File Name")

    if st.button("Rename"):
        msg = rename_file(file_name, new_name)
        st.success(msg)

elif option == "Create Folder":
    st.subheader("📁 Create Folder")

    folder_name = st.text_input("Enter Folder Name")

    if st.button("Create Folder"):
        msg = create_folder(folder_name)
        st.success(msg)

elif option == "Delete Folder":
    st.subheader("❌ Delete Folder")

    folder_name = st.text_input("Enter Folder Name")

    if st.button("Delete Folder"):
        msg = delete_folder(folder_name)
        st.success(msg)