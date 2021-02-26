__author__      = "Juvyoung"
__copyright__   = "Copyright 2018"
__version__     = "0.0.1"
__email__       = ""
__status__      = "Prototype"
__date__        = "2021-02-26"

#import 
import os
import shutil
import hashlib

#import win32con
#import win32api
# ======================================  Library =================================================

# ======================================  Data types   ============================================

# ==================================   Public functions   =========================================
'''@package
       Function description
       
   Note: Hidden source code
------------------------------------''' 
#def src_code_hidden( folder ):
#    
#    file = folder + '\\' + "U_disc_backup.py"
#    attr = win32api.GetFileAttributes(file)
#    print(attr)
#    
#    return None


def file_extention( filename ):
    """
    file path format extract
    ----------
    filename : file format
        e.g. file1.txt; 
             file2.c;
             file3.h;

    Returns
    -------
    name : file name
    extension : file extension
        e.g. .c, .h, .txt....

    """
    (filepath, tempfilename) = os.path.split(filename)
    (name, extension) = os.path.splitext(tempfilename)
    # print( 'file name is: {0}\nExtension is: {1}.'.center(20).format(name,extension))
    return ( name, extension )


def md5check(fname):
    """
    file content md5 checksum generation
    Note: use 4 bytes of content in file then generate md5 checksum
    """
    m = hashlib.md5()
    with open(fname, mode = 'r', encoding = 'utf-8', errors = 'ignore' ) as fileobj:
#    with open(fname, encoding = 'utf-8') as fileobj:
        while True:
            dat = fileobj.read(1024)

            if not dat:
                break
            else:        
                m.update(dat.encode('utf-8') )
#                print(dat)
            
    return m.hexdigest()


def file_copy( file, bckf ):
    """
    files copy to destination folder
    ----------
    file : TYPE
        DESCRIPTION.
    bckf : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    """
    # IF file already existed, check md5 content update or not
    if os.path.isfile(bckf):
        old_md5 = md5check( file )
        new_md5 = md5check( bckf )
           
        if new_md5 != old_md5:
            print( " old md5 checksum: {0} \n new md5 checksum: {1} "
                  .format(old_md5, new_md5) )  
            shutil.copy(file, bckf)
            print( file  + ' copy to ' + bckf )
     
    # IF Target file not existed
    else: 
        dir_bckf = os.path.dirname( bckf )
        if os.path.exists(dir_bckf):
            shutil.copy(file, bckf)
            print( file  + ' copy to ' + bckf )
        else:
            try: 
                os.makedirs( dir_bckf )
                shutil.copy(file, bckf)
                print( file  + ' copy to ' + bckf )
            except WindowsError:
                print( "create backup folder FAILED ")


def lsdir( folder, backup ):
    """
    Folder & Subfolder iterative copy
    ----------
    folder : source folder path
        
    backup : Target (Copy) folder path

    Returns
    -------
    None.

    Examples: 
    >>>lsdir( current folder where .py script located,
              Target folder path, just copy )
    
    """    
    FILE_EXTENTION_ALLOWED = ['.txt','.py','.dbc','.c','.h']
    
    path = os.listdir(folder) #file list
    print( "elements list in folder ---> || {0} || \n{1}\n".format(folder,path) )
    
    for line in path:
        line = folder + '\\' + line
 
        #    IF file: generate md5 checksum
        if os.path.isfile(line):
            (str_file_name, str_file_type) = file_extention(line)
#            print( "file name is: {0}\nfile type is: {1}".format( str_file_name, str_file_type ) )
            if( os.path.splitext(os.path.basename(__file__))[0] != str_file_name ) and \
              ( True == (str_file_type in FILE_EXTENTION_ALLOWED ) ):
                  bk_file = line.replace(folder, backup)
                  file_copy( line, bk_file )             # Copy to des folder 

        #    IF folder: iterative 
        elif os.path.isdir(line):
            bk_file = line.replace(folder, backup)
            bk_sub_folder = line.replace(line, bk_file)

            lsdir(line, bk_sub_folder)
            
        else:
            print("====== exception =======")

# =====================   Application Zone   ==================================
'''------------------------------------------
           First Edition

            by: Juvyoung
--------------------------------------------'''
print ("\n".rjust(40, '=') +       
       "  File backup script ".center(30) +
       "\n".ljust(40, '=') ) 
# ----------------------------------
#         MAIN FUNCTION
# ----------------------------------
def main():    
#    des_folder   = 'C:\\Users\\cn40335\\Documents\\Pyth\\FileSystem\\backup'
    try: 
        raw_input          # Python 2
    except NameError: 
        raw_input = input  # Python 3
        
    src_folder = os.getcwd()
    des_folder = raw_input("Please enter backup folder --> ")
    print('Source folder is: {0}'.format(src_folder))
    print('Backup folder is: {0} \n'.format(des_folder))
    lsdir( src_folder, des_folder )
    
    print("------ THE END -------- \n  ")


'''
%%%%%%%%   START  %%%%%%%%%%%%
'''
if __name__ == "__main__":
    main()


# END OF FILE
    
'''
    src_code_hidden( old_path )
    src_code_hidden( new_bk )
    print(os.path.splitext(os.path.basename(__file__))[0])
'''    