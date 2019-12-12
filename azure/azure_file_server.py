from azure.storage.file import FileService


file_service = FileService(
    account_name="account_name",
    account_key="account_key"
)

# ファイル一覧表示
generator = file_service.list_directories_and_files('my-file')
for file_or_dir in generator:
    print(file_or_dir.name)


# ローカルのtest.txtをAzure Storageへアップロード
from azure.storage.file import ContentSettings
file_service.create_file_from_path(
    'my-file',
    None,
    'test.txt',
    'test.txt',
    content_settings=ContentSettings(content_type='text/plain'))