import os
import approot
class Saver:
    def save_to_xlsx(df_data, _path = os.path.join(approot.get_root(),'data'), _file_name = 'file'):
        df_data.to_excel(os.path.join(_path, _file_name))

    def save_to_mysql(df):
        pass




