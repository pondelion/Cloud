from azure.storage.file import FileService


# アカウント名、アカウントキーからファイルサービスを作成する
def get_file_service(account_name, account_key):
    return FileService(account_name=accout_name, account_key=account_key)


# Azureストレージファイル一覧の表示する
def get_azure_storage_filelist(file_service, fileshare_name)
    files = []
    try:
        generator = file_service.list_directories_and_files(fileshare_name)
        for file_or_dir in generator:
            files.append(file_or_dir.name)
    except Exception as e:
        print('Failed to get Azure storage file list')
        print(e)
    return files


# filenameのファイルをダウンロードしout_filenameで保存する
def donwload_file(file_service, fileshare_name, filename, out_filename):
    try:
        file_service.get_file_to_path(
            fileshare_name,
            None,
            file,
            file
        )
    except Exception as e:
        print('Failed to download file : {}'.format(filename))
        print(e)
