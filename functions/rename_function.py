def rename_func(match_table,old_name_col,new_name_co,path=".",file_name_incl_ext=False,add_extension=False):
    """
    path = the file path where the files reside, defaults to the currect directory
    old_name_col : col name of old file in match table
    new_name_col : col name of new name in the match table
    match_table = the table to match the old to new file name (shoul be a data frame)
    file_name_incl_ext : if the file name includes the extension in the match table,defaults to false
    add_extension : add file extension to the new name or not, defaults no extension
    """
    import pathlib,os
    path = pathlib.Path(path)
    if file_name_incl_ext:
        "if the old file name in the match table include file extension"  
        if add_extension:
            "if new name does not include the file enxtension"
            for file in path.iterdir():
                if file.name in match_table[old_name_col]:
                    file_old_name = file.name
                    extension = os.path.splitext(file.name)[1]
                    file_new_name = (match_table[match_table[old_name_col]==file_old_name][new_name_col]).values[0]+extension
                    file.rename(path/file_new_name)
        else:
            "if new name includes the file enxtension"
            for file in path.iterdir():
                if file.name in match_table[old_name_col]:
                    file_old_name = file.name
                    extension = os.path.splitext(file.name)[1]
                    file_new_name = (match_table[match_table[old_name_col]==file_old_name][new_name_col]).values[0]
                    file.rename(path/file_new_name)

    else:
        "if the old file name in the match table does not include file extension"
        for file in path.iterdir():
            file_split = os.path.splitext(file.name)
            extension = file_split[1]
            file_old_name = file_split[0]

            if file_old_name in match_table[old_name_col]:
                file_new_name = (match_table[match_table[old_name_col]==file_old_name][new_name_col]).values[0]+extension
                file.rename(path/file_new_name)
