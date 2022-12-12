from PyQt5 import QtWidgets
import sys

from timetable import Ui_Tables
from add_timetable import Ui_add_tables
from student import Ui_students
from add_student import Ui_add_student
from classroom import Ui_classroom
from add_classroom import Ui_add_classroom
from update_classroom import Ui_update_classroom
from update_student import Ui_update_student
from update_timetable import Ui_update_tables

from db_file import get_table
from db_file import add_student_in_table
from db_file import add_classroom_in_table
from db_file import add_timetable_in_table
from db_file import del_timetable_from_table
from db_file import del_student_from_table
from db_file import del_classroom_from_table
from db_file import sql_procedure_timetable
from db_file import sql_function_conc
from db_file import update_student
from db_file import update_classroom

# from db_file import


KEY_WORD_DICT = {
    "timetable": "",
    "add_timetable__classroom": "",
    "add_timetable__subject": "",
    "add_timetable__worker": "",
    "add_timetable__group": "",
    "add_timetable__class_type": "",
    "student": "",
    "add_student__group": "",
    "classroom": "",
    "add_classroom__corpus": "",
    "find_worker": "",
    "find_classroom": ""
}


def start():
    timetable_w.comboBox.clear()
    timetable_info = get_table("timetable")
    timetable_w.comboBox.addItem("")
    for elem in timetable_info:
        timetable_w.comboBox.addItem(elem["title"])

    timetable_w.comboBox_2.clear()
    worker_info = get_table("worker")
    timetable_w.comboBox_2.addItem("")
    for elem in worker_info:
        timetable_w.comboBox_2.addItem(elem["worker_name"])

    timetable_w.comboBox_3.clear()
    classroom_info = get_table("classroom")
    timetable_w.comboBox_3.addItem("")
    for elem in classroom_info:
        timetable_w.comboBox_3.addItem(elem["number"])

    timetable_window.show()


def timetable__add_timetable():
    add_timetable_w.comboBox_5.clear()
    timetable_info = get_table("stud_group")
    add_timetable_w.comboBox_5.addItem("")
    for elem in timetable_info:
        add_timetable_w.comboBox_5.addItem(elem["group_name"])

    add_timetable_w.comboBox_2.clear()
    subjects_info = get_table("subjects")
    add_timetable_w.comboBox_2.addItem("")
    for elem in subjects_info:
        add_timetable_w.comboBox_2.addItem(elem["subjects_name"])

    add_timetable_w.comboBox_3.clear()
    worker_info = get_table("worker")
    add_timetable_w.comboBox_3.addItem("")
    for elem in worker_info:
        add_timetable_w.comboBox_3.addItem(elem["worker_name"])

    add_timetable_w.comboBox_4.clear()
    class_type_info = get_table("class_type")
    add_timetable_w.comboBox_4.addItem("")
    for elem in class_type_info:
        add_timetable_w.comboBox_4.addItem(elem["title"])

    add_timetable_w.comboBox.clear()
    classroom_info = get_table("classroom")
    add_timetable_w.comboBox.addItem("")
    for elem in classroom_info:
        add_timetable_w.comboBox.addItem(elem["number"])

    timetable_window.close()
    add_timetable_window.show()


def add_timetable__timetable():
    group_info = get_table("stud_group")
    *group_info, = filter(lambda x: x["group_name"] == KEY_WORD_DICT["add_timetable__group"], group_info)
    id_group_code = group_info[0]["id_group_code"]

    classroom_info = get_table("classroom")
    *classroom_info, = filter(lambda x: x["number"] == KEY_WORD_DICT["add_timetable__classroom"], classroom_info)
    id_classroom_code = classroom_info[0]["id_classroom_code"]

    subject_info = get_table("subjects")
    *subject_info, = filter(lambda x: x["subjects_name"] == KEY_WORD_DICT["add_timetable__subject"], subject_info)
    id_subjects_code = subject_info[0]["id_subjects_code"]

    worker_info = get_table("worker")
    *worker_info, = filter(lambda x: x["worker_name"] == KEY_WORD_DICT["add_timetable__worker"], worker_info)
    id_worker_code = worker_info[0]["id_worker_code"]

    class_type_info = get_table("class_type")
    *class_type_info, = filter(lambda x: x["title"] == KEY_WORD_DICT["add_timetable__class_type"], class_type_info)
    id_class_type_code = class_type_info[0]["id_class_type_code"]

    title = add_timetable_w.lineEdit.text()

    # print(id_group_code)
    # print(id_classroom_code)
    # print(id_subjects_code)
    # print(id_worker_code)
    # print(id_class_type_code)

    result = add_timetable_in_table(id_group_code,
                                    id_classroom_code,
                                    id_subjects_code,
                                    id_worker_code,
                                    id_class_type_code,
                                    title)
    print(result)

    KEY_WORD_DICT["add_timetable__classroom"] = ""
    KEY_WORD_DICT["add_timetable__subject"] = ""
    KEY_WORD_DICT["add_timetable__worker"] = ""
    KEY_WORD_DICT["add_timetable__group"] = ""
    KEY_WORD_DICT["add_timetable__class_type"] = ""

    timetable_w.comboBox.clear()
    timetable_info = get_table("timetable")
    timetable_w.comboBox.addItem("")
    for elem in timetable_info:
        timetable_w.comboBox.addItem(elem["title"])
    add_timetable_window.close()
    timetable_window.show()


def add_timetable__timetable__cancel():
    KEY_WORD_DICT["add_timetable__classroom"] = ""
    KEY_WORD_DICT["add_timetable__subject"] = ""
    KEY_WORD_DICT["add_timetable__worker"] = ""
    KEY_WORD_DICT["add_timetable__group"] = ""
    KEY_WORD_DICT["add_timetable__class_type"] = ""
    add_timetable_window.close()
    timetable_window.show()


def timetable__student():
    student_w.comboBox.clear()
    timetable_info = get_table("student")
    student_w.comboBox.addItem("")
    for elem in timetable_info:
        student_w.comboBox.addItem(elem["student_ticket_number"])
    timetable_window.close()
    student_window.show()


def student__timetable():
    timetable_w.comboBox.clear()
    timetable_info = get_table("timetable")
    timetable_w.comboBox.addItem("")
    for elem in timetable_info:
        timetable_w.comboBox.addItem(elem["title"])
    student_window.close()
    timetable_window.show()


def student__classroom():
    classroom_w.comboBox.clear()
    timetable_info = get_table("classroom")
    classroom_w.comboBox.addItem("")
    for elem in timetable_info:
        classroom_w.comboBox.addItem(elem["number"])

    classroom_total = 0
    count_classroom_info = get_table("count_classroom")
    for elem in count_classroom_info:
        classroom_total += elem["count"]

    text = sql_function_conc("Количество классов:", str(classroom_total))
    classroom_w.label_3.setText(text)

    student_window.close()
    classroom_window.show()


def student__add_student():
    add_student_w.comboBox.clear()
    stud_group_info = get_table("stud_group")
    add_student_w.comboBox.addItem("")
    for elem in stud_group_info:
        add_student_w.comboBox.addItem(elem["group_name"])

    student_window.close()
    add_student_window.show()


def add_student__student():
    group_name = KEY_WORD_DICT["add_student__group"]
    name = add_student_w.lineEdit.text()
    code = add_student_w.lineEdit_2.text()

    stud_group_info = get_table("stud_group")
    *stud_group_info, = filter(lambda x: x["group_name"] == group_name, stud_group_info)
    id_stud_group = stud_group_info[0]["id_group_code"]
    result = add_student_in_table(id_stud_group, name, code)
    print(result)

    student_w.comboBox.clear()
    timetable_info = get_table("student")
    student_w.comboBox.addItem("")
    for elem in timetable_info:
        student_w.comboBox.addItem(elem["student_ticket_number"])

    KEY_WORD_DICT["add_student__group"] = ""

    add_student_window.close()
    student_window.show()


def add_student__student__cancel():
    student_w.comboBox.clear()
    timetable_info = get_table("student")
    student_w.comboBox.addItem("")
    for elem in timetable_info:
        student_w.comboBox.addItem(elem["student_ticket_number"])

    KEY_WORD_DICT["add_student__group"] = ""
    add_student_window.close()
    student_window.show()


def timetable__classroom():
    classroom_w.comboBox.clear()
    timetable_info = get_table("classroom")
    classroom_w.comboBox.addItem("")
    for elem in timetable_info:
        classroom_w.comboBox.addItem(elem["number"])

    classroom_total = 0
    count_classroom_info = get_table("count_classroom")
    for elem in count_classroom_info:
        classroom_total += elem["count"]

    text = sql_function_conc("Количество классов:", str(classroom_total))
    classroom_w.label_3.setText(text)

    timetable_window.close()
    classroom_window.show()


def classroom__timetable():
    timetable_w.comboBox.clear()
    timetable_info = get_table("timetable")
    timetable_w.comboBox.addItem("")
    for elem in timetable_info:
        timetable_w.comboBox.addItem(elem["title"])
    classroom_window.close()
    timetable_window.show()


def classroom__student():
    student_w.comboBox.clear()
    timetable_info = get_table("student")
    student_w.comboBox.addItem("")
    for elem in timetable_info:
        student_w.comboBox.addItem(elem["student_ticket_number"])
    classroom_window.close()
    student_window.show()


def classroom__add_classroom():
    add_classroom_w.comboBox.clear()
    corpus_info = get_table("corpus")
    add_classroom_w.comboBox.addItem("")
    for elem in corpus_info:
        add_classroom_w.comboBox.addItem(elem["corpus_name"])

    classroom_window.close()
    add_classroom_window.show()


def add_classroom__classroom():
    corpus_name = KEY_WORD_DICT["add_classroom__corpus"]
    number = add_classroom_w.lineEdit.text()

    corpus_info = get_table("corpus")
    *corpus_info, = filter(lambda x: x["corpus_name"] == corpus_name, corpus_info)
    id_corpus = corpus_info[0]["id_corpus"]
    result = add_classroom_in_table(id_corpus, number)
    print(result)

    classroom_w.comboBox.clear()
    timetable_info = get_table("classroom")
    classroom_w.comboBox.addItem("")
    for elem in timetable_info:
        classroom_w.comboBox.addItem(elem["number"])

    classroom_total = 0
    count_classroom_info = get_table("count_classroom")
    for elem in count_classroom_info:
        classroom_total += elem["count"]

    text = sql_function_conc("Количество классов:", classroom_total)
    classroom_w.label_3.setText(text)

    KEY_WORD_DICT["add_classroom__corpus"] = ""

    add_classroom_window.close()
    classroom_window.show()


def add_classroom__classroom__cancel():
    classroom_w.comboBox.clear()
    timetable_info = get_table("classroom")
    classroom_w.comboBox.addItem("")
    for elem in timetable_info:
        classroom_w.comboBox.addItem(elem["number"])

    classroom_total = 0
    count_classroom_info = get_table("count_classroom")
    for elem in count_classroom_info:
        classroom_total += elem["count"]

    text = sql_function_conc("Количество классов:", str(classroom_total))
    classroom_w.label_3.setText(text)

    KEY_WORD_DICT["add_classroom__corpus"] = ""

    add_classroom_window.close()
    classroom_window.show()


# UPDATE

def classroom_to_update():
    if KEY_WORD_DICT["classroom"]:

        classroom_info = get_table("classroom")
        *classroom_info, = filter(lambda x: x["number"] == KEY_WORD_DICT["classroom"], classroom_info)
        id_corpus = classroom_info[0]["id_corpus"]
        number = classroom_info[0]["number"]

        update_classroom_w.lineEdit.setText(number)

        update_classroom_w.comboBox.clear()
        worker_info = get_table("corpus")
        update_classroom_w.comboBox.addItem("")
        for elem in worker_info:
            update_classroom_w.comboBox.addItem(elem["corpus_name"])
            if elem["id_corpus"] == id_corpus:
                KEY_WORD_DICT["add_classroom__corpus"] = elem["corpus_name"]

        index = update_classroom_w.comboBox.findText(KEY_WORD_DICT["add_classroom__corpus"])
        update_classroom_w.comboBox.setCurrentIndex(index)

        classroom_window.close()
        update_classroom_window.show()


def classroom_from_update():
    corpus_info = get_table("corpus")
    *corpus_info, = filter(lambda x: x["corpus_name"] == KEY_WORD_DICT["add_classroom__corpus"], corpus_info)
    id_corpus_code = corpus_info[0]["id_corpus"]

    classroom_info = get_table("classroom")
    *classroom_info, = filter(lambda x: x["number"] == KEY_WORD_DICT["classroom"], classroom_info)
    id_classroom_code = classroom_info[0]["id_classroom_code"]

    number = update_classroom_w.lineEdit.text()

    result = update_classroom(number, id_corpus_code, id_classroom_code)
    print(result)

    KEY_WORD_DICT["add_classroom__corpus"] = ""

    classroom_w.textBrowser.setText("")
    update_classroom_window.close()
    classroom_window.show()


def classroom_from_update_cancel():

    KEY_WORD_DICT["add_classroom__corpus"] = ""
    update_classroom_window.close()
    classroom_window.show()


def student_to_update():
    if KEY_WORD_DICT["student"]:
        student_info = get_table("student")
        *student_info, = filter(lambda x: x["student_ticket_number"] == KEY_WORD_DICT["student"], student_info)
        id_group_code = student_info[0]["id_group_code"]
        stud_name = student_info[0]["stud_name"]
        student_ticket_number = student_info[0]["student_ticket_number"]

        update_student_w.lineEdit.setText(stud_name)
        update_student_w.lineEdit_2.setText(student_ticket_number)

        update_student_w.comboBox.clear()
        worker_info = get_table("stud_group")
        update_student_w.comboBox.addItem("")
        for elem in worker_info:
            update_student_w.comboBox.addItem(elem["group_name"])
            if elem["id_group_code"] == id_group_code:
                KEY_WORD_DICT["add_student__group"] = elem["group_name"]

        index = update_student_w.comboBox.findText(KEY_WORD_DICT["add_student__group"])
        update_student_w.comboBox.setCurrentIndex(index)

        student_window.close()
        update_student_window.show()


def student_from_update():
    group_info = get_table("stud_group")
    *group_info, = filter(lambda x: x["group_name"] == KEY_WORD_DICT["add_student__group"], group_info)
    id_group_code = group_info[0]["id_group_code"]

    student_info = get_table("student")
    *student_info, = filter(lambda x: x["student_ticket_number"] == KEY_WORD_DICT["student"], student_info)
    id_student_code = student_info[0]["id_student_code"]

    stud_name = update_student_w.lineEdit.text()
    student_ticket_number = update_student_w.lineEdit_2.text()

    result = update_student(stud_name, student_ticket_number, id_group_code, id_student_code)
    print(result)

    KEY_WORD_DICT["add_student__group"] = ""

    student_w.textBrowser.setText("")

    update_student_window.close()
    student_window.show()


def student_from_update_cancel():
    KEY_WORD_DICT["add_student__group"] = ""
    update_student_window.close()
    student_window.show()


def timetable_to_update():
    if KEY_WORD_DICT["timetable"]:

        timetable = sql_procedure_timetable(KEY_WORD_DICT["timetable"])

        id_group_code = timetable["id_group_code"]
        id_classroom_code = timetable["id_classroom_code"]
        id_subjects_code = timetable["id_subjects_code"]
        id_worker_code = timetable["id_worker_code"]
        id_class_type_code = timetable["id_class_type_code"]

        update_timetable_w.comboBox_5.clear()
        timetable_info = get_table("stud_group")
        update_timetable_w.comboBox_5.addItem("")
        for elem in timetable_info:
            update_timetable_w.comboBox_5.addItem(elem["group_name"])
            if elem["id_group_code"] == id_group_code:
                KEY_WORD_DICT["add_timetable__group"] = elem["group_name"]

        update_timetable_w.comboBox_2.clear()
        subjects_info = get_table("subjects")
        update_timetable_w.comboBox_2.addItem("")
        for elem in subjects_info:
            update_timetable_w.comboBox_2.addItem(elem["subjects_name"])
            if elem["id_subjects_code"] == id_subjects_code:
                KEY_WORD_DICT["add_timetable__subject"] = elem["subjects_name"]

        update_timetable_w.comboBox_3.clear()
        worker_info = get_table("worker")
        update_timetable_w.comboBox_3.addItem("")
        for elem in worker_info:
            update_timetable_w.comboBox_3.addItem(elem["worker_name"])
            if elem["id_worker_code"] == id_worker_code:
                KEY_WORD_DICT["add_timetable__worker"] = elem["worker_name"]

        update_timetable_w.comboBox_4.clear()
        class_type_info = get_table("class_type")
        update_timetable_w.comboBox_4.addItem("")
        for elem in class_type_info:
            update_timetable_w.comboBox_4.addItem(elem["title"])
            if elem["id_class_type_code"] == id_class_type_code:
                KEY_WORD_DICT["add_timetable__class_type"] = elem["title"]

        update_timetable_w.comboBox.clear()
        classroom_info = get_table("classroom")
        update_timetable_w.comboBox.addItem("")
        for elem in classroom_info:
            update_timetable_w.comboBox.addItem(elem["number"])
            if elem["id_classroom_code"] == id_classroom_code:
                KEY_WORD_DICT["add_timetable__classroom"] = elem["number"]

        index = update_timetable_w.comboBox.findText(KEY_WORD_DICT["add_timetable__classroom"])
        update_timetable_w.comboBox.setCurrentIndex(index)

        index = update_timetable_w.comboBox_2.findText(KEY_WORD_DICT["add_timetable__subject"])
        update_timetable_w.comboBox_2.setCurrentIndex(index)

        index = update_timetable_w.comboBox_3.findText(KEY_WORD_DICT["add_timetable__worker"])
        update_timetable_w.comboBox_3.setCurrentIndex(index)

        index = update_timetable_w.comboBox_4.findText(KEY_WORD_DICT["add_timetable__class_type"])
        update_timetable_w.comboBox_4.setCurrentIndex(index)

        index = update_timetable_w.comboBox_5.findText(KEY_WORD_DICT["add_timetable__group"])
        update_timetable_w.comboBox_5.setCurrentIndex(index)

        timetable_window.close()
        update_timetable_window.show()


def timetable_from_update():
    group_info = get_table("stud_group")
    *group_info, = filter(lambda x: x["group_name"] == KEY_WORD_DICT["add_timetable__group"], group_info)
    id_group_code = group_info[0]["id_group_code"]

    classroom_info = get_table("classroom")
    *classroom_info, = filter(lambda x: x["number"] == KEY_WORD_DICT["add_timetable__classroom"], classroom_info)
    id_classroom_code = classroom_info[0]["id_classroom_code"]

    subject_info = get_table("subjects")
    *subject_info, = filter(lambda x: x["subjects_name"] == KEY_WORD_DICT["add_timetable__subject"], subject_info)
    id_subjects_code = subject_info[0]["id_subjects_code"]

    worker_info = get_table("worker")
    *worker_info, = filter(lambda x: x["worker_name"] == KEY_WORD_DICT["add_timetable__worker"], worker_info)
    id_worker_code = worker_info[0]["id_worker_code"]

    class_type_info = get_table("class_type")
    *class_type_info, = filter(lambda x: x["title"] == KEY_WORD_DICT["add_timetable__class_type"], class_type_info)
    id_class_type_code = class_type_info[0]["id_class_type_code"]

    title = update_timetable_w.lineEdit.text()

    # print(id_group_code)
    # print(id_classroom_code)
    # print(id_subjects_code)
    # print(id_worker_code)
    # print(id_class_type_code)

    result = del_timetable_from_table(title)
    print(result)

    result = add_timetable_in_table(id_group_code,
                                    id_classroom_code,
                                    id_subjects_code,
                                    id_worker_code,
                                    id_class_type_code,
                                    title)
    print(result)

    timetable_w.comboBox.clear()
    timetable_info = get_table("timetable")
    timetable_w.comboBox.addItem("")
    for elem in timetable_info:
        timetable_w.comboBox.addItem(elem["title"])
    KEY_WORD_DICT["add_timetable__classroom"] = ""
    KEY_WORD_DICT["add_timetable__subject"] = ""
    KEY_WORD_DICT["add_timetable__worker"] = ""
    KEY_WORD_DICT["add_timetable__group"] = ""
    KEY_WORD_DICT["add_timetable__class_type"] = ""

    timetable_w.textBrowser.setText("")
    update_timetable_window.close()
    timetable_window.show()


def timetable_from_update_cancel():

    KEY_WORD_DICT["add_timetable__classroom"] = ""
    KEY_WORD_DICT["add_timetable__subject"] = ""
    KEY_WORD_DICT["add_timetable__worker"] = ""
    KEY_WORD_DICT["add_timetable__group"] = ""
    KEY_WORD_DICT["add_timetable__class_type"] = ""

    update_timetable_window.close()
    timetable_window.show()


# DELETE BUTTON

def delete_timetable():
    title = KEY_WORD_DICT["timetable"]
    result = del_timetable_from_table(title)
    print(result)

    timetable_w.comboBox.clear()
    timetable_info = get_table("timetable")
    timetable_w.comboBox.addItem("")
    for elem in timetable_info:
        timetable_w.comboBox.addItem(elem["title"])


def delete_student():
    code = KEY_WORD_DICT["student"]
    result = del_student_from_table(code)
    print(result)

    student_w.comboBox.clear()
    timetable_info = get_table("student")
    student_w.comboBox.addItem("")
    for elem in timetable_info:
        student_w.comboBox.addItem(elem["student_ticket_number"])


def delete_classroom():
    number = KEY_WORD_DICT["classroom"]
    result = del_classroom_from_table(number)
    print(result)

    classroom_w.comboBox.clear()
    timetable_info = get_table("classroom")
    classroom_w.comboBox.addItem("")
    for elem in timetable_info:
        classroom_w.comboBox.addItem(elem["number"])

    classroom_total = 0
    count_classroom_info = get_table("count_classroom")
    for elem in count_classroom_info:
        classroom_total += elem["count"]

    text = f"Количество классов: {classroom_total}"
    classroom_w.label_3.setText(text)


# COMBOBOX


def timetable__box(text):
    KEY_WORD_DICT["timetable"] = text
    if KEY_WORD_DICT["timetable"]:
        timetable_info = get_table("timetable")
        *timetable_info, = filter(lambda x: x["title"] == KEY_WORD_DICT["timetable"], timetable_info)
        id_group_code = timetable_info[0]["id_group_code"]
        id_subjects_code = timetable_info[0]["id_subjects_code"]
        id_worker_code = timetable_info[0]["id_worker_code"]
        id_class_type_code = timetable_info[0]["id_class_type_code"]
        id_classroom_code = timetable_info[0]["id_classroom_code"]

        group_info = get_table("stud_group")
        *group_info, = filter(lambda x: x["id_group_code"] == id_group_code, group_info)
        group_name = group_info[0]["group_name"]

        subjects_info = get_table("subjects")
        *subjects, = filter(lambda x: x["id_subjects_code"] == id_subjects_code, subjects_info)
        subjects_name = subjects[0]["subjects_name"]

        worker_info = get_table("worker")
        *worker, = filter(lambda x: x["id_worker_code"] == id_worker_code, worker_info)
        worker_name = worker[0]["worker_name"]

        class_type_info = get_table("class_type")
        *class_type, = filter(lambda x: x["id_class_type_code"] == id_class_type_code, class_type_info)
        title = class_type[0]["title"]

        classroom_info = get_table("classroom")
        *classroom, = filter(lambda x: x["id_classroom_code"] == id_classroom_code, classroom_info)
        number = classroom[0]["number"]

        text = f"Таблица: {text}\n\nНазвание группы: {group_name}\nПредмет: {subjects_name}\n" \
               f"Сотрудник: {worker_name}\nТип класса: {title}\n" \
               f"Аудитория: {number}\n"
        timetable_w.textBrowser.setText(text)


def add_timetable__classroom_box(text):
    KEY_WORD_DICT["add_timetable__classroom"] = text


def add_timetable__subject_box(text):
    KEY_WORD_DICT["add_timetable__subject"] = text


def add_timetable__worker_box(text):
    KEY_WORD_DICT["add_timetable__worker"] = text


def add_timetable__group_box(text):
    KEY_WORD_DICT["add_timetable__group"] = text


def add_timetable__class_type_box(text):
    KEY_WORD_DICT["add_timetable__class_type"] = text


def student__box(text):
    KEY_WORD_DICT["student"] = text
    if KEY_WORD_DICT["student"]:

        student_info = get_table("student")
        *student, = filter(lambda x: x["student_ticket_number"] == text, student_info)
        id_group_code = student[0]["id_group_code"]
        stud_name = student[0]["stud_name"]

        stud_group_info = get_table("stud_group")
        *stud_group, = filter(lambda x: x["id_group_code"] == id_group_code, stud_group_info)
        id_course_code = stud_group[0]["id_course_code"]
        group_name = stud_group[0]["group_name"]

        course_info = get_table("course")
        *course, = filter(lambda x: x["id_course_code"] == id_course_code, course_info)
        course_number = course[0]["course_number"]

        text = f"Студент: {stud_name}\n\nШифр: {text}\nГруппа: {group_name}\nКуср: {course_number}\n"
        student_w.textBrowser.setText(text)


def add_student__group_box(text):
    KEY_WORD_DICT["add_student__group"] = text


def classroom__box(text):
    KEY_WORD_DICT["classroom"] = text
    if KEY_WORD_DICT["classroom"]:
        classroom_info = get_table("classroom")
        *classroom, = filter(lambda x: x["number"] == text, classroom_info)
        id_corpus = classroom[0]["id_corpus"]

        corpus_info = get_table("corpus")
        *corpus, = filter(lambda x: x["id_corpus"] == id_corpus, corpus_info)
        corpus_name = corpus[0]["corpus_name"]

        text = f"Аудитория - {text}\n\nКорпус: {corpus_name}"

        classroom_w.textBrowser.setText(text)


def add_classroom__corpus_box(text):
    KEY_WORD_DICT["add_classroom__corpus"] = text


def find_timeteble_for_worker(text):
    KEY_WORD_DICT["find_worker"] = text


def find_timeteble_for_classroom(text):
    KEY_WORD_DICT["find_classroom"] = text


def find():
    classroom = KEY_WORD_DICT["find_classroom"]
    worker = KEY_WORD_DICT["find_worker"]

    def search_for_worker():
        worker_info = get_table("worker")
        *worker_info, = filter(lambda x: x["worker_name"] == worker, worker_info)
        id_worker_code = worker_info[0]["id_worker_code"]

        timetable_list = list()

        timetable_info = get_table("timetable")
        *timetable_info, = filter(lambda x: x["id_worker_code"] == id_worker_code, timetable_info)
        for elem in timetable_info:
            timetable_list.append(elem["title"])

        return timetable_list

    def search_for_classroom():
        classroom_info = get_table("classroom")
        *classroom_info, = filter(lambda x: x["number"] == classroom, classroom_info)
        id_classroom_code = classroom_info[0]["id_classroom_code"]

        timetable_list = list()

        timetable_info = get_table("timetable")
        *timetable_info, = filter(lambda x: x["id_classroom_code"] == id_classroom_code, timetable_info)
        for elem in timetable_info:
            timetable_list.append(elem["title"])

        return timetable_list

    if classroom and worker:
        timetable_list_worker = search_for_worker()
        timetable_list_classroom = search_for_classroom()
        timetable_list = list(set(timetable_list_worker) & set(timetable_list_classroom))

    elif classroom:
        timetable_list = search_for_classroom()

    elif worker:
        timetable_list = search_for_worker()

    else:
        return

    timetable = get_table("timetable")
    timetable_w.comboBox.clear()
    timetable_w.comboBox.addItem("")
    for elem in timetable:
        if elem["title"] in timetable_list:
            timetable_w.comboBox.addItem(str(elem["title"]))

    timetable_w.textBrowser.setText("")


app = QtWidgets.QApplication(sys.argv)

timetable_window = QtWidgets.QMainWindow()
timetable_w = Ui_Tables()
timetable_w.setupUi(timetable_window)
timetable_w.pushButton.clicked.connect(timetable__student)
timetable_w.pushButton_2.clicked.connect(timetable__classroom)
timetable_w.pushButton_3.clicked.connect(timetable__add_timetable)
timetable_w.pushButton_4.clicked.connect(delete_timetable)
timetable_w.pushButton_5.clicked.connect(find)
timetable_w.pushButton_6.clicked.connect(timetable_to_update)
timetable_w.comboBox.activated[str].connect(timetable__box)
timetable_w.comboBox_2.activated[str].connect(find_timeteble_for_worker)
timetable_w.comboBox_3.activated[str].connect(find_timeteble_for_classroom)

start()

add_timetable_window = QtWidgets.QDialog()
add_timetable_w = Ui_add_tables()
add_timetable_w.setupUi(add_timetable_window)
add_timetable_w.pushButton.clicked.connect(add_timetable__timetable)
add_timetable_w.pushButton_2.clicked.connect(add_timetable__timetable__cancel)
add_timetable_w.comboBox.activated[str].connect(add_timetable__classroom_box)
add_timetable_w.comboBox_2.activated[str].connect(add_timetable__subject_box)
add_timetable_w.comboBox_3.activated[str].connect(add_timetable__worker_box)
add_timetable_w.comboBox_4.activated[str].connect(add_timetable__class_type_box)
add_timetable_w.comboBox_5.activated[str].connect(add_timetable__group_box)


student_window = QtWidgets.QDialog()
student_w = Ui_students()
student_w.setupUi(student_window)
student_w.pushButton.clicked.connect(student__timetable)
student_w.pushButton_2.clicked.connect(student__classroom)
student_w.pushButton_3.clicked.connect(student__add_student)
student_w.pushButton_4.clicked.connect(delete_student)
student_w.pushButton_6.clicked.connect(student_to_update)
student_w.comboBox.activated[str].connect(student__box)

add_student_window = QtWidgets.QDialog()
add_student_w = Ui_add_student()
add_student_w.setupUi(add_student_window)
add_student_w.pushButton.clicked.connect(add_student__student)
add_student_w.pushButton_2.clicked.connect(add_student__student__cancel)
add_student_w.comboBox.activated[str].connect(add_student__group_box)


classroom_window = QtWidgets.QDialog()
classroom_w = Ui_classroom()
classroom_w.setupUi(classroom_window)
classroom_w.pushButton.clicked.connect(classroom__student)
classroom_w.pushButton_2.clicked.connect(classroom__timetable)
classroom_w.pushButton_3.clicked.connect(classroom__add_classroom)
classroom_w.pushButton_4.clicked.connect(delete_classroom)
classroom_w.pushButton_6.clicked.connect(classroom_to_update)
classroom_w.comboBox.activated[str].connect(classroom__box)

add_classroom_window = QtWidgets.QDialog()
add_classroom_w = Ui_add_classroom()
add_classroom_w.setupUi(add_classroom_window)
add_classroom_w.pushButton.clicked.connect(add_classroom__classroom)
add_classroom_w.pushButton_2.clicked.connect(add_classroom__classroom__cancel)
add_classroom_w.comboBox.activated[str].connect(add_classroom__corpus_box)


update_timetable_window = QtWidgets.QDialog()
update_timetable_w = Ui_update_tables()
update_timetable_w.setupUi(update_timetable_window)
update_timetable_w.pushButton.clicked.connect(timetable_from_update)
update_timetable_w.pushButton_2.clicked.connect(timetable_from_update_cancel)
update_timetable_w.comboBox.activated[str].connect(add_timetable__classroom_box)
update_timetable_w.comboBox_2.activated[str].connect(add_timetable__subject_box)
update_timetable_w.comboBox_3.activated[str].connect(add_timetable__worker_box)
update_timetable_w.comboBox_4.activated[str].connect(add_timetable__class_type_box)
update_timetable_w.comboBox_5.activated[str].connect(add_timetable__group_box)

update_student_window = QtWidgets.QDialog()
update_student_w = Ui_update_student()
update_student_w.setupUi(update_student_window)
update_student_w.pushButton.clicked.connect(student_from_update)
update_student_w.pushButton_2.clicked.connect(student_from_update_cancel)
update_student_w.comboBox.activated[str].connect(add_student__group_box)

update_classroom_window = QtWidgets.QDialog()
update_classroom_w = Ui_update_classroom()
update_classroom_w.setupUi(update_classroom_window)
update_classroom_w.pushButton.clicked.connect(classroom_from_update)
update_classroom_w.pushButton_2.clicked.connect(classroom_from_update_cancel)
update_classroom_w.comboBox.activated[str].connect(add_classroom__corpus_box)


##################

sys.exit(app.exec_())
