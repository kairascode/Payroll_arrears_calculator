import tkinter as tk

import tksheet

top = tk.Tk()

sheet = tksheet.Sheet(top)

sheet.grid()

sheet.set_sheet_data([["{ri+cj}" for cj in range(6)] for ri in range(9)])

# table enable choices listed below:

sheet.enable_bindings(("single_select",

                       "row_select",

                       "column_width_resize",

                       "arrowkeys",

                       "right_click_popup_menu",

                       "rc_select",

                       "rc_insert_row",

                       "rc_delete_row",

                       "copy",

                       "cut",

                       "paste",

                       "delete",

                       "undo",

                       "edit_cell"))

top.mainloop()