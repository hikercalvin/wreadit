
def move_file(dectect_name, folder_name):
    '''
    dectect_name:
        
    folder_name:
        
    '''    
    # 抓出為【正常模型】的所有檔案名稱
    import os 
    save = []
    for i in os.listdir():
        if dectect_name in i:
            save.append(i)
    
    # save=[i for i in os.listdir() if plot_name2 in i]
    
    # make folder
    ff = [i for i in save if not '.' in i ]
    ff = [i for i in ff if  '（' in i ]
    
    
            
    try:
        os.makedirs(folder_name)
        folder_namenew= folder_name
    
    except:
        
        try:
            os.makedirs(folder_name + '（' +str(0)+'）')
            folder_namenew= folder_name + '（' +str(0)+'）'
        except: 
            
            for i in range(0, 10):
                iinn = [j for j in ff if folder_name + '（' +str(i)+'）'  in j]
                if len(iinn) == 0:
                    os.makedirs(folder_name + '（' +str(i)+'）')
                    folder_namenew =folder_name + '（' +str(i)+'）'
                    break
                
                # break
        
    
    
    # move files to that created folder
    import shutil
    save = [i for i in save if '.' in i ]
    for m in save:
        shutil.move(m, folder_namenew)
        
def move_file_plus(dectect_name, folder_name):
    '''
    dectect_name:
        
    folder_name:
        
    '''    
    # 抓出為【正常模型】的所有檔案名稱
    import os 
    save = []
    for i in os.listdir():
        if dectect_name in i:
            save.append(i)
    
    # save=[i for i in os.listdir() if plot_name2 in i]
    
    # make folder
    
            
    try:
        os.makedirs(folder_name)
        folder_namenew= folder_name
    
    except:
        
        try:
            os.makedirs(folder_name + '（' +str(0)+'）')
            folder_namenew= folder_name + '（' +str(0)+'）'
        except: 
            
            for i in range(0, 10):
                iinn = [j for j in save if folder_name + '（' +str(i)+'）'  in j]
                if len(iinn) == 0:
                    os.makedirs(folder_name + '（' +str(i)+'）')
                    folder_namenew =folder_name + '（' +str(i)+'）'
                    break
                
                # break
        
    
    
    # move files to that created folder
    import shutil
    save = [i for i in save]
    for m in save:
        shutil.move(m, folder_namenew)
